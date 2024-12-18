from . import L1 as _L1
from .label import RekognitionLabel as _Label

_TAXONOMY_LEVEL = 2

ExplicitNudity = _Label(
    name='Explicit Nudity',
    parent=_L1.Explicit,
    taxonomy_level=_TAXONOMY_LEVEL,
)

ExplicitSexualActivity = _Label(
    name='Explicit Sexual Activity',
    parent=_L1.Explicit,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Depiction of actual or simulated sexual acts which encompasses human sexual intercourse, oral sex, as well as male genital stimulation and female genital stimulation by other body parts and objects. The term also includes ejaculation or vaginal fluids on body parts and erotic practices or roleplaying involving bondage, discipline, dominance and submission, and sadomasochism.
"""

SexToys = _Label(
    name='Sex Toys',
    parent=_L1.Explicit,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Objects or devices used for sexual stimulation or pleasure, e.g., dildo, vibrator, butt plug, beats, etc.
"""

NonExplicitNudity = _Label(
    name='Non-Explicit Nudity',
    parent=_L1.NonExplicitNudityOfIntimatePartsAndKissing,
    taxonomy_level=_TAXONOMY_LEVEL,
)

ObstructedIntimateParts = _Label(
    name='Obstructed Intimate Parts',
    parent=_L1.NonExplicitNudityOfIntimatePartsAndKissing,
    taxonomy_level=_TAXONOMY_LEVEL,
)

KissingOnTheLips = _Label(
    name='Kissing on the Lips',
    parent=_L1.NonExplicitNudityOfIntimatePartsAndKissing,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Depiction of one person's lips making contact with another person's lips.
"""

FemaleSwimwearOrUnderwear = _Label(
    name='Female Swimwear or Underwear',
    parent=_L1.SwimwearOrUnderwear,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Human clothing for female swimwear (e.g., one-piece swimsuits, bikinis, tankinis, etc.) and female underwear (e.g., bras, panties, briefs, lingerie, thongs, etc.)
"""

MaleSwimwearOrUnderwear = _Label(
    name='Male Swimwear or Underwear',
    parent=_L1.SwimwearOrUnderwear,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Human clothing for male swimwear (e.g., swim trunks, boardshorts, swim briefs, etc.) and male underwear (e.g., briefs, boxers, etc.)
"""

Weapons = _Label(
    name='Weapons',
    parent=_L1.Violence,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Instruments or devices used to cause harm or damage to living beings, structures, or systems. This includes firearms (e.g., guns, rifles, machine gunes, etc.), sharp weapons (e.g., swords, knives, etc.), explosives and ammunition (e.g., missile, bombs, bullets, etc.).
"""

GraphicViolence = _Label(
    name='Graphic Violence',
    parent=_L1.Violence,
    taxonomy_level=_TAXONOMY_LEVEL,
)

DeathAndEmaciation = _Label(
    name='Death and Emaciation',
    parent=_L1.VisuallyDisturbing,
    taxonomy_level=_TAXONOMY_LEVEL,
)

Crashes = _Label(
    name='Crashes',
    parent=_L1.VisuallyDisturbing,
    taxonomy_level=_TAXONOMY_LEVEL,
)

Products = _Label(
    name='Products',
    parent=_L1.DrugsAndTobacco,
    taxonomy_level=_TAXONOMY_LEVEL,
)

DrugsAndTobaccoParaphernaliaAndUse = _Label(
    name='Drugs & Tobacco Paraphernalia & Use',
    parent=_L1.DrugsAndTobacco,
    taxonomy_level=_TAXONOMY_LEVEL,
)

AlcoholUse = _Label(
    name='Alcohol Use',
    parent=_L1.Alcohol,
    taxonomy_level=_TAXONOMY_LEVEL,
)

AlcoholicBeverages = _Label(
    name='Alcoholic Beverages',
    parent=_L1.Alcohol,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Close up of one or multiple bottles of alcohol or liquor, glasses or mugs with alcohol or liquor, and glasses or mugs with alcohol or liquor held by an individual. This term does not apply to an individual drinking from bottles or glasses of alcohol or liquor.
"""

MiddleFinger = _Label(
    name='Middle Finger',
    parent=_L1.RudeGestures,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Visual depiction of a hand gesture with middle finger is extended upward while the other fingers are folded down.
"""

NaziParty = _Label(
    name='Nazi Party',
    parent=_L1.HateSymbols,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Visual depiction of symbols, flags, or gestures associated with Nazi Party.
"""

WhiteSupremacy = _Label(
    name='White Supremacy',
    parent=_L1.HateSymbols,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Visual depiction of symbols or clothings associated with Ku Klux Klan (KKK) and images with confederate flags.
"""

Extremist = _Label(
    name='Extremist',
    parent=_L1.HateSymbols,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Images containing extremist and terrorist group flags.
"""
