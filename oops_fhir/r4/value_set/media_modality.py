from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.media_modality import MediaModality as MediaModality_


__all__ = ["MediaModality"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MediaModality(MediaModality_):
    """
    Media Modality

    Detailed information about the type of the image - its kind, purpose, or
the kind of equipment used to generate it.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/media-modality
    """

    class Meta:
        resource = _resource
