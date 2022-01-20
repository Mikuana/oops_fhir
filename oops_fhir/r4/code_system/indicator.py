from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["Indicator"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class Indicator:
    """
    None

    This value set captures the set of indicator codes defined by the CDS
Hooks specification.

    Status: draft - Version: 4.0.1

    Copyright None

    http://cds-hooks.hl7.org/CodeSystem/indicator
    """

    info = CodeSystemConcept(
        {"code": "info", "display": "The response is informational"}
    )
    """
    The response is informational

    
    """

    warning = CodeSystemConcept(
        {"code": "warning", "display": "The response is a warning"}
    )
    """
    The response is a warning

    
    """

    critical = CodeSystemConcept(
        {
            "code": "critical",
            "display": "The response is critical and indicates the workflow should not be allowed to proceed",
        }
    )
    """
    The response is critical and indicates the workflow should not be allowed to proceed

    
    """

    class Meta:
        resource = _resource
