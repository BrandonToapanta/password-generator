import math
import secrets
from src.model.password_options import PasswordOptions
from src.model.password_policy import PasswordPolicy
from src.model.validation_result import ValidationResult
from src.model.character_set import CharacterSetBuilder, SecureRandomProvider


class EntropyCalculator:
    @staticmethod
    def calculate(length: int, charset_size: int) -> float:
        if charset_size <= 0 or length <= 0:
            return 0.0
        # Fórmula matemática estándar: E = L * log2(N)
        return float(length * math.log2(charset_size))


class PasswordValidator:
    @staticmethod
    def validate(password: str, policy: PasswordPolicy, entropy: float) -> ValidationResult:
        errors = []

        # Estructuras condicionales de validación basadas en la política
        if len(password) < policy.min_length:
            errors.append(f"La longitud es menor a {policy.min_length} caracteres.")

        if sum(1 for c in password if c.isupper()) < policy.min_upper:
            errors.append("Faltan caracteres en mayúscula.")

        if sum(1 for c in password if c.islower()) < policy.min_lower:
            errors.append("Faltan caracteres en minúscula.")

        if sum(1 for c in password if c.isdigit()) < policy.min_digits:
            errors.append("Faltan dígitos numéricos.")

        if sum(1 for c in password if c.isprintable() and not c.isalnum()) < policy.min_symbols:
            errors.append("Faltan caracteres especiales o símbolos.")

        if entropy < policy.min_entropy_bits:
            errors.append(
                f"Entropía insuficiente ({entropy:.2f} bits). Mínimo requerido: {policy.min_entropy_bits} bits.")

        for pattern in policy.forbidden_patterns:
            if pattern in password.lower():
                errors.append(f"Contiene un patrón prohibido: '{pattern}'.")

        return ValidationResult(is_valid=len(errors) == 0, errors=errors, entropy_bits=entropy)


class PasswordGenerator:
    def __init__(self):
        self.random_provider = SecureRandomProvider()

    def generate(self, length: int, options: PasswordOptions) -> str:
        charset = CharacterSetBuilder.build(options)
        password_chars = []

        """
        Garantizamos el uso de almenos uno de los caracteres, en el caso de seleccionar 
        ambiguo se le coloca otro cadena de seleccion emitiendo los caracteres considerados ambiguos                    
        """

        if options.include_upper: password_chars.append(secrets.choice(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if not options.exclude_ambiguous else "ABCDEFGHJKLMNOPQRSTUVWXYZ"))
        if options.include_lower: password_chars.append(secrets.choice(
            "abcdefghijklmnopqrstuvwxyz" if not options.exclude_ambiguous else "abcdefghijkmnopqrstuvwxyz"))
        if options.include_digits: password_chars.append(
            secrets.choice("0123456789" if not options.exclude_ambiguous else "23456789"))
        if options.include_symbols: password_chars.append(secrets.choice(
            "!@#$%^&*()_+-=[]{}|;:,.<>?" if not options.exclude_ambiguous else "!@#$%^&*()_+-=[]{}:,.<>?"))

        # Estructura repetitiva para rellenar la longitud restante solicitada
        remaining_length = length - len(password_chars)
        for _ in range(remaining_length):
            random_index = self.random_provider.next_int(charset.size())
            password_chars.append(charset.get(random_index))

        # Barajado criptográfico final para romper posiciones fijas predecibles
        secrets.SystemRandom().shuffle(password_chars)
        return "".join(password_chars)