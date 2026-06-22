import secrets

class SecureRandomProvider:
    """Encapsula el uso de CSPRNG para evitar la predictibilidad de índices."""

    def next_int(self, max_exclusive: int) -> int:
        return secrets.randbelow(max_exclusive)


class CharacterSet:
    def __init__(self, characters: str):
        self._characters = characters

    def size(self) -> int:
        return len(self._characters)

    def get(self, index: int) -> str:
        return self._characters[index]


class CharacterSetBuilder:
    @staticmethod
    def build(options: PasswordOptions) -> CharacterSet:
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        digits = "0123456789"
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

        # Eliminación de caracteres ambiguos (O/0, l/1, I) si está activo
        if options.exclude_ambiguous:
            upper = upper.replace("O", "").replace("I", "")
            lower = lower.replace("l", "")
            digits = digits.replace("0", "").replace("1", "")
            symbols = symbols.replace("|", "")

        pool = ""
        if options.include_upper: pool += upper
        if options.include_lower: pool += lower
        if options.include_digits: pool += digits
        if options.include_symbols: pool += symbols

        if not pool:
            raise ValueError("Debe seleccionar al menos una categoría de caracteres.")

        return CharacterSet(pool)