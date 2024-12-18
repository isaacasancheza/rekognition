from typing import TYPE_CHECKING, cast, overload

from boto3 import client

from . import L1, L2, L3
from .label import RekognitionLabel

if TYPE_CHECKING:
    from mypy_boto3_rekognition import RekognitionClient


rekognition = client('rekognition')


def get_label_from_name(
    name: str,
    /,
) -> RekognitionLabel:
    for module in [L1, L2, L3]:
        for attribute in dir(module):
            if attribute.startswith('_'):
                continue
            label = getattr(module, attribute)
            label = cast(RekognitionLabel, label)
            if label.name == name:
                return label
    raise ValueError('Label not found')


@overload
def moderate_and_detect_labels(
    *,
    key: str,
    bucket: str,
    labels: list[RekognitionLabel],
    rekognition_client: 'RekognitionClient' = rekognition,
) -> tuple[bool, list[RekognitionLabel]]:
    pass


@overload
def moderate_and_detect_labels(
    *,
    bytes: bytes,
    labels: list[RekognitionLabel],
    rekognition_client: 'RekognitionClient' = rekognition,
) -> tuple[bool, list[RekognitionLabel]]:
    pass


def moderate_and_detect_labels(
    *,
    key: str | None = None,
    bytes: bytes | None = None,
    bucket: str | None = None,
    labels: list[RekognitionLabel],
    rekognition_client: 'RekognitionClient' = rekognition,
) -> tuple[bool, list[RekognitionLabel]]:
    """
    Returns detected labels and whether the image is safe.
    https://docs.aws.amazon.com/rekognition/latest/dg/moderation-api.html
    """

    if bytes is not None:
        response = rekognition_client.detect_moderation_labels(
            Image={
                'Bytes': bytes,
            },
        )

    if bucket is not None and key is not None:
        response = rekognition_client.detect_moderation_labels(
            Image={
                'S3Object': {
                    'Bucket': bucket,
                    'Name': key,
                },
            },
        )

    is_safe = True
    detected_labels = []
    for label in response['ModerationLabels']:
        assert 'Name' in label
        label = get_label_from_name(label['Name'])
        if label in labels:
            is_safe = False
        detected_labels.append(label)
    return is_safe, detected_labels
