from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["MediaCollectionViewProjection"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MediaCollectionViewProjection(SNOMEDCT):
    """
    Media Collection View/Projection

    Codes defined in SNOMED CT that can be used to record Media Recording
views.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/media-view
    """

    class Meta:
        resource = _resource
