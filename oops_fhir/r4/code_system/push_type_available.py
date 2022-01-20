from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["pushtypeavailable"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class pushtypeavailable:
    """
    Push-type-available

    Type of alerts/updates the primary source can send

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/push-type-available
    """

    specific = CodeSystemConcept(
        {"code": "specific", "display": "Specific requested changes"}
    )
    """
    Specific requested changes

    
    """

    any_ = CodeSystemConcept({"code": "any", "display": "Any changes"})
    """
    Any changes

    
    """

    source = CodeSystemConcept({"code": "source", "display": "As defined by source"})
    """
    As defined by source

    
    """

    class Meta:
        resource = _resource
