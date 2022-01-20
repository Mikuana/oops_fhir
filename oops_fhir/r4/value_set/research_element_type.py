from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.research_element_type import (
    ResearchElementType as ResearchElementType_,
)


__all__ = ["ResearchElementType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ResearchElementType(ResearchElementType_):
    """
    ResearchElementType

    The possible types of research elements (E.g. Population, Exposure,
Outcome).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/research-element-type
    """

    class Meta:
        resource = _resource
