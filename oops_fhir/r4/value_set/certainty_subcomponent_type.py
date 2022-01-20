from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.certainty_subcomponent_type import (
    CertaintySubcomponentType as CertaintySubcomponentType_,
)


__all__ = ["CertaintySubcomponentType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CertaintySubcomponentType(CertaintySubcomponentType_):
    """
    CertaintySubcomponentType

    The subcomponent classification of quality of evidence rating systems.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/certainty-subcomponent-type
    """

    class Meta:
        resource = _resource
