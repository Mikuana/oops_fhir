from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["canpushupdates"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class canpushupdates:
    """
    Can-push-updates

    Ability of the primary source to push updates/alerts

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/can-push-updates
    """

    yes = CodeSystemConcept({"code": "yes", "display": "Yes"})
    """
    Yes

    
    """

    no = CodeSystemConcept({"code": "no", "display": "No"})
    """
    No

    
    """

    undetermined = CodeSystemConcept(
        {"code": "undetermined", "display": "Undetermined"}
    )
    """
    Undetermined

    
    """

    class Meta:
        resource = _resource
