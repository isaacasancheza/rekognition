"""
https://docs.aws.amazon.com/rekognition/latest/dg/moderation-api.html#moderation-api-categories
"""

from . import L2 as _L2
from .label import RekognitionLabel as _Label

_TAXONOMY_LEVEL = 3

ExposedMaleGenitalia = _Label(
    name='Exposed Male Genitalia',
    parent=_L2.ExplicitNudity,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Human male genitalia, including the penis (whether erect or flaccid), the scrotum, and any discernible pubic hair. This term is applicable in contexts involving sexual activity or any visual content where male genitals are displayed either completely or partially.
"""

ExposedFemaleGenitalia = _Label(
    name='Exposed Female Genitalia',
    parent=_L2.ExplicitNudity,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
External parts of the female reproductive system, encompassing the vulva, vagina, and any observable pubic hair. This term is applicable in scenarios involving sexual activity or any visual content where these aspects of female anatomy are displayed either completely or partially.
"""

ExposedButtocksOrAnus = _Label(
    name='Exposed Buttocks or Anus',
    parent=_L2.ExplicitNudity,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Human buttocks or anus, including instances where the buttocks are nude or when they are discernible through sheer clothing. The definition specifically applies to situations where the buttocks or anus are directly and completely visible, excluding scenarios where any form of underwear or clothing provides complete or partial coverage.
"""

ExposedFemaleNipple = _Label(
    name='Exposed Female Nipple',
    parent=_L2.ExplicitNudity,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Human female nipples, including fully visible and partially visible aerola (area surrounding the nipples) and nipples.
"""

BareBack = _Label(
    name='Bare Back',
    parent=_L2.NonExplicitNudity,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Human posterior part where the majority of the skin is visible from the neck to the end of the spine. This term does not apply when the individual's back is partially or fully occluded.
"""

ExposedMaleNipple = _Label(
    name='Exposed Male Nipple',
    parent=_L2.NonExplicitNudity,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Human male nipples, including partially visible nipples.
"""

PartiallyExposedButtocks = _Label(
    name='Partially Exposed Buttocks',
    parent=_L2.NonExplicitNudity,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Partially exposed human buttocks. This term includes a partially visible region of the buttocks or butt cheeks due to short clothes, or partially visible top portion of the anal cleft. The term does not apply to cases where the buttocks is fully nude.
"""

PartiallyExposedFemaleBreast = _Label(
    name='Partially Exposed Female Breast',
    parent=_L2.NonExplicitNudity,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Partially exposed human female breast where one a portion of the female's breast is visible or uncovered while not revealing the entire breast. This term applies when the region of the inner breast fold is visible or when the lower breast crease is visible with nipple fully covered or occluded.
"""

ImpliedNudity = _Label(
    name='Implied Nudity',
    parent=_L2.NonExplicitNudity,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
An individual who is nude, either topless or bottomless, but with intimate parts such as buttocks, nipples, or genitalia covered, occluded, or not fully visible.
"""

ObstructedFemaleNipple = _Label(
    name='Obstructed Female Nipple',
    parent=_L2.ObstructedIntimateParts,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Visual depiction of a situation in which a female's nipples is covered by opaque clothing or coverings, but their shapes are clearly visible.
"""

ObstructedMaleGenitalia = _Label(
    name='Obstructed Male Genitalia',
    parent=_L2.ObstructedIntimateParts,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Visual depiction of a situation in which a male's genitalia or penis is covered by opaque clothing or coverings, but its shape is clearly visible. This term applies when the obstructed genitalia in the image is in close-up.
"""

WeaponViolence = _Label(
    name='Weapon Violence',
    parent=_L2.GraphicViolence,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
The use of weapons to cause harm, damage, injury, or death to oneself, other individuals, or properties.
"""

PhysicalViolence = _Label(
    name='Physical Violence',
    parent=_L2.GraphicViolence,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
The act of causing harm to other individuals or property (e.g., hitting, fighting, pulling hair, etc.) or other act of violence involving crowd or multiple individuals.
"""

SelfHarm = _Label(
    name='Self-Harm',
    parent=_L2.GraphicViolence,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
The act of causing harm to oneself, often by cutting body parts such as arms or legs, where cuts are typically visible.
"""

BloodAndGore = _Label(
    name='Blood & Gore',
    parent=_L2.GraphicViolence,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Visual representation of violence on a person, a group of individuals, or animals, involving open wounds, bloodshed, and mutilated body parts.
"""

ExplosionsAndBlasts = _Label(
    name='Explosions and Blasts',
    parent=_L2.GraphicViolence,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Depiction of a violent and destructive burst of intense flames with thick smoke or dust and smoke erupting from the ground.
"""

EmaciatedBodies = _Label(
    name='Emaciated Bodies',
    parent=_L2.DeathAndEmaciation,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Human bodies that are extremely thin and undernourished with severe physical wasting and depletion of muscle and fat tissue.
"""

Corpses = _Label(
    name='Corpses',
    parent=_L2.DeathAndEmaciation,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Human corpses in the form of mutilated bodies, hanging corpses, or skeletons.
"""

AirCrash = _Label(
    name='Air Crash',
    parent=_L2.Crashes,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Incidents of air vehicles, such as airplanes, helicopters, or other flying vehicles, resulting in damage, injury, or death. This term applies when parts of the air vehicles are visible.
"""

Pills = _Label(
    name='Pills',
    parent=_L2.Products,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
Small, solid, often round or oval-shaped tables or capsules. This term applies to pills presented as standalones, in a bottle, or a transparent packet and does not apply to a visual depiction of a person taking pills.
"""

Smoking = _Label(
    name='Smoking',
    parent=_L2.DrugsAndTobaccoParaphernaliaAndUse,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
The act of inhaling, exhaling, and lighting up burning substances including cigarettes, cigars, e-cigarettes, hookah, or joint.
"""

Drinking = _Label(
    name='Drinking',
    parent=_L2.AlcoholUse,
    taxonomy_level=_TAXONOMY_LEVEL,
)
"""
The act of drinking alcoholic beverages from bottles or glasses of alcohol or liquor.
"""
