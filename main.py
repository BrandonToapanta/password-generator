from src.view.cli_view import PasswordGeneratorUI
from src.model.password_options import PasswordOptions
from src.model.password_policy import PasswordPolicy
from src.controller.password_controller import PasswordGenerator, EntropyCalculator, PasswordValidator
from src.model.character_set import CharacterSetBuilder


def main():
    view = PasswordGeneratorUI()
    generator = PasswordGenerator()
    policy = PasswordPolicy()

    length, opts_dict = view.prompt_options()

    options = PasswordOptions(length=length, **opts_dict)

    try:
        charset = CharacterSetBuilder.build(options)
        password = generator.generate(length, options)

        entropy = EntropyCalculator.calculate(length, charset.size())
        result = PasswordValidator.validate(password, policy, entropy)

        view.show_result(password, result.is_valid, result.entropy_bits, result.errors)

    except ValueError as e:
        print(f"Error de configuración: {e}")


if __name__ == "__main__":
    main()