from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["validationstatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class validationstatus:
    """
    Validation-status

    Status of the validation of the target against the primary source

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/validation-status
    """

    successful = CodeSystemConcept({"code": "successful", "display": "Successful"})
    """
    Successful

    
    """

    failed = CodeSystemConcept({"code": "failed", "display": "Failed"})
    """
    Failed

    
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": "The validations status has not been determined yet",
            "display": "Unknown",
        }
    )
    """
    Unknown

    The validations status has not been determined yet
    """

    class Meta:
        resource = _resource
