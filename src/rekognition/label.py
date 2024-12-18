from dataclasses import dataclass
from typing import Literal


@dataclass
class RekognitionLabel:
    name: str
    parent: 'RekognitionLabel | None'
    taxonomy_level: Literal[1, 2, 3]
