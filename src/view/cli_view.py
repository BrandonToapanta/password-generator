class PasswordGeneratorUI:
    @staticmethod
    def prompt_options() -> tuple[int, dict]:
        print("\n--- CONFIGURACIÓN DEL GENERADOR SEGURO ---")
        length = int(input("Ingrese longitud de la contraseña: "))
        opts = {
            "include_upper": input("¿Incluir mayúsculas? (s/n): ").lower() == 's',
            "include_lower": input("¿Incluir minúsculas? (s/n): ").lower() == 's',
            "include_digits": input("¿Incluir números? (s/n): ").lower() == 's',
            "include_symbols": input("¿Incluir símbolos? (s/n): ").lower() == 's',
            "exclude_ambiguous": input("¿Excluir caracteres ambiguos (O, 0, l, 1)? (s/n): ").lower() == 's'
        }
        return length, opts

    @staticmethod
    def show_result(password: str, is_valid: bool, entropy: float, errors: list):
        print("\n--- RESULTADO DE GENERACIÓN ---")
        print(f"Contraseña Generada: {password}")
        print(f"Entropía Matemática: {entropy:.2f} bits")
        if is_valid:
            print("Estado de la política: ¡CUMPLE CON TODAS LAS REGLAS DE SEGURIDAD!")
        else:
            print("Estado de la política: RECHAZADA POR LA POLÍTICA")
            for err in errors:
                print(f" - Error: {err}")