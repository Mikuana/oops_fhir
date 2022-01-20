from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AdverseEventSeverity"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AdverseEventSeverity:
    """
    AdverseEventSeverity

    The severity of the adverse event itself, in direct relation to the
subject.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/adverse-event-severity
    """

    mild = CodeSystemConcept({"code": "mild", "display": "Mild"})
    """
    Mild

    
    """

    moderate = CodeSystemConcept({"code": "moderate", "display": "Moderate"})
    """
    Moderate

    
    """

    severe = CodeSystemConcept({"code": "severe", "display": "Severe"})
    """
    Severe

    
    """

    class Meta:
        resource = _resource
