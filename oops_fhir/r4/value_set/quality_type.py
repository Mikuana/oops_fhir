from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.quality_type import qualityType as qualityType_


__all__ = ["qualityType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class qualityType(qualityType_):
    """
    qualityType

    Type for quality report.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/quality-type
    """

    class Meta:
        resource = _resource
