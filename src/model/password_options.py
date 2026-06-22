from dataclasses import dataclass

@dataclass
class PasswordOptions:
    length: int
    include_upper: bool
    include_lower: bool
    include_digits: bool
    include_symbols: bool
    exclude_ambiguous: bool