from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["FMConditionCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class FMConditionCodes:
    """
    FM Condition Codes

    This value set includes sample Conditions codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://hl7.org/fhir/fm-conditions
    """

    one23987 = CodeSystemConcept(
        {"code": "123987", "definition": "Headache", "display": "Headache"}
    )
    """
    Headache

    Headache
    """

    class Meta:
        resource = _resource
