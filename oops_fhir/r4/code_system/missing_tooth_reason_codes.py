from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MissingToothReasonCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MissingToothReasonCodes:
    """
    Missing Tooth Reason Codes

    This value set includes sample Missing Tooth Reason codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/missingtoothreason
    """

    e = CodeSystemConcept({"code": "e", "definition": "Extraction", "display": "E"})
    """
    E

    Extraction
    """

    c = CodeSystemConcept({"code": "c", "definition": "Congenital", "display": "C"})
    """
    C

    Congenital
    """

    u = CodeSystemConcept({"code": "u", "definition": "Unknown", "display": "U"})
    """
    U

    Unknown
    """

    o = CodeSystemConcept({"code": "o", "definition": "Other", "display": "O"})
    """
    O

    Other
    """

    class Meta:
        resource = _resource
