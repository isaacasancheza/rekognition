"""
https://docs.aws.amazon.com/rekognition/latest/dg/moderation-api.html#moderation-api-categories
"""

from . import L1, L2, L3
from .label import RekognitionLabel
from .utils import moderate_and_detect_labels
