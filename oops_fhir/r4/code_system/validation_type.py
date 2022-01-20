from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["validationtype"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class validationtype:
    """
    Validation-type

    What the target is validated against

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/validation-type
    """

    nothing = CodeSystemConcept({"code": "nothing", "display": "Nothing"})
    """
    Nothing

    
    """

    primary = CodeSystemConcept({"code": "primary", "display": "Primary Source"})
    """
    Primary Source

    
    """

    multiple = CodeSystemConcept({"code": "multiple", "display": "Multiple Sources"})
    """
    Multiple Sources

    
    """

    class Meta:
        resource = _resource
