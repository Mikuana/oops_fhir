from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AdverseEventOutcome"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AdverseEventOutcome:
    """
    AdverseEventOutcome

    TODO (and should this be required?).

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/adverse-event-outcome
    """

    resolved = CodeSystemConcept({"code": "resolved", "display": "Resolved"})
    """
    Resolved

    
    """

    recovering = CodeSystemConcept({"code": "recovering", "display": "Recovering"})
    """
    Recovering

    
    """

    ongoing = CodeSystemConcept({"code": "ongoing", "display": "Ongoing"})
    """
    Ongoing

    
    """

    resolved_with_sequelae = CodeSystemConcept(
        {"code": "resolvedWithSequelae", "display": "Resolved with Sequelae"}
    )
    """
    Resolved with Sequelae

    
    """

    fatal = CodeSystemConcept({"code": "fatal", "display": "Fatal"})
    """
    Fatal

    
    """

    unknown = CodeSystemConcept({"code": "unknown", "display": "Unknown"})
    """
    Unknown

    
    """

    class Meta:
        resource = _resource
