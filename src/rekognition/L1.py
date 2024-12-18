"""
https://docs.aws.amazon.com/rekognition/latest/dg/moderation-api.html#moderation-api-categories
"""

from .label import RekognitionLabel as _Label

_TAXONOMY_LEVEL = 1

Explicit = _Label(
    'Explicit',
    None,
    _TAXONOMY_LEVEL,
)

NonExplicitNudityOfIntimatePartsAndKissing = _Label(
    'Non-Explicit Nudity of Intimate parts and Kissing',
    None,
    _TAXONOMY_LEVEL,
)

SwimwearOrUnderwear = _Label(
    'Swimwear or Underwear',
    None,
    _TAXONOMY_LEVEL,
)

Violence = _Label(
    'Violence',
    None,
    _TAXONOMY_LEVEL,
)

VisuallyDisturbing = _Label(
    'Visually Disturbing',
    None,
    _TAXONOMY_LEVEL,
)

DrugsAndTobacco = _Label(
    'Drugs & Tobacco',
    None,
    _TAXONOMY_LEVEL,
)

Alcohol = _Label(
    'Alcohol',
    None,
    _TAXONOMY_LEVEL,
)

RudeGestures = _Label(
    'Rude Gestures',
    None,
    _TAXONOMY_LEVEL,
)

Gambling = _Label(
    name='Gambling',
    parent=None,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
The act of participating in games of chance for a chance to win a prize in casinos, e.g., playing cards, blackjacks, roulette, slot machines at casinos, etc.
"""

HateSymbols = _Label(
    name='Hate Symbols',
    parent=None,
    taxonomy_level=_TAXONOMY_LEVEL,
)
