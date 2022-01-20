from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MediaType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MediaType:
    """
    Media Type

    Codes for high level media categories.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/media-type
    """

    image = CodeSystemConcept(
        {
            "code": "image",
            "definition": "The media consists of one or more unmoving images, including photographs, computer-generated graphs and charts, and scanned documents",
            "display": "Image",
        }
    )
    """
    Image

    The media consists of one or more unmoving images, including photographs, computer-generated graphs and charts, and scanned documents
    """

    video = CodeSystemConcept(
        {
            "code": "video",
            "definition": "The media consists of a series of frames that capture a moving image",
            "display": "Video",
        }
    )
    """
    Video

    The media consists of a series of frames that capture a moving image
    """

    audio = CodeSystemConcept(
        {
            "code": "audio",
            "definition": "The media consists of a sound recording",
            "display": "Audio",
        }
    )
    """
    Audio

    The media consists of a sound recording
    """

    class Meta:
        resource = _resource
