from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["failureaction"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class failureaction:
    """
    Failure-action

    The result if validation fails

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/failure-action
    """

    fatal = CodeSystemConcept({"code": "fatal", "display": "Fatal"})
    """
    Fatal

    
    """

    warn = CodeSystemConcept({"code": "warn", "display": "Warning"})
    """
    Warning

    
    """

    rec_only = CodeSystemConcept({"code": "rec-only", "display": "Record only"})
    """
    Record only

    
    """

    none = CodeSystemConcept({"code": "none", "display": "None"})
    """
    None

    
    """

    class Meta:
        resource = _resource
