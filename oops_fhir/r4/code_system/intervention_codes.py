from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["InterventionCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class InterventionCodes:
    """
    Intervention Codes

    This value set includes sample Intervention codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://hl7.org/fhir/intervention
    """

    unknown = CodeSystemConcept(
        {"code": "unknown", "definition": "Unknown", "display": "Unknown"}
    )
    """
    Unknown

    Unknown
    """

    other = CodeSystemConcept(
        {"code": "other", "definition": "Other", "display": "Other"}
    )
    """
    Other

    Other
    """

    class Meta:
        resource = _resource
