from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["UnitTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class UnitTypeCodes:
    """
    Unit Type Codes

    This value set includes a smattering of Unit type codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/benefit-unit
    """

    individual = CodeSystemConcept(
        {
            "code": "individual",
            "definition": "A single individual",
            "display": "Individual",
        }
    )
    """
    Individual

    A single individual
    """

    family = CodeSystemConcept(
        {
            "code": "family",
            "definition": "A family, typically includes self, spouse(s) and children to a defined age",
            "display": "Family",
        }
    )
    """
    Family

    A family, typically includes self, spouse(s) and children to a defined age
    """

    class Meta:
        resource = _resource
