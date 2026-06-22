from dataclasses import dataclass, field
from typing import List

@dataclass
class ValidationResult:
    is_valid: bool
    errors: List[str] = field(default_factory=list)
    entropy_bits: float = 0.0