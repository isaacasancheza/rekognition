from pathlib import Path

from rekognition import L1, L2, RekognitionLabel, moderate_and_detect_labels

L1s = [
    L1.Explicit,
    L1.NonExplicitNudityOfIntimatePartsAndKissing,
    L1.SwimwearOrUnderwear,
    L1.Violence,
    L1.VisuallyDisturbing,
    L1.DrugsAndTobacco,
    L1.Alcohol,
    L1.RudeGestures,
    L1.Gambling,
]
IMAGES_DIR = Path(__file__).parent / 'images'


def moderate_image(
    path: Path,
    labels: list[RekognitionLabel],
    is_safe: bool,
    /,
):
    with open(path, 'rb') as f:
        f_is_safe, labels = moderate_and_detect_labels(
            bytes=f.read(),
            labels=labels,
        )
        assert is_safe == f_is_safe


def test_animated_beach():
    moderate_image(
        IMAGES_DIR / 'animated_beach.jpg',
        L1s,
        True,
    )


def test_family_picnic():
    moderate_image(
        IMAGES_DIR / 'family_picnic.jpg',
        L1s,
        True,
    )


def test_illustrated_surfer():
    moderate_image(
        IMAGES_DIR / 'illustrated_surfer.jpg',
        L1s,
        True,
    )


def test_yoga_swimwear():
    moderate_image(
        IMAGES_DIR / 'yoga_swimwear.jpg',
        [
            L2.NonExplicitNudity,
        ],
        False,
    )
