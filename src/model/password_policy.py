from dataclasses import dataclass, field
from typing import List

@dataclass
class PasswordPolicy:
    min_length: int = 12
    min_upper: int = 1
    min_lower: int = 1
    min_digits: int = 1
    min_symbols: int = 1
    min_entropy_bits: float = 60.0
    forbidden_patterns: List[str] = field(default_factory=lambda: ["123", "password", "qwerty"])