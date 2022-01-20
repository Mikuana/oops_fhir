from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.media_type import MediaType as MediaType_


__all__ = ["MediaType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MediaType(MediaType_):
    """
    Media Type

    Codes for high level media categories.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/media-type
    """

    class Meta:
        resource = _resource
