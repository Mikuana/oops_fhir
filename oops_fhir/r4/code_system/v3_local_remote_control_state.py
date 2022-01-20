from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3LocalRemoteControlState"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3LocalRemoteControlState:
    """
    v3 Code System LocalRemoteControlState

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-LocalRemoteControlState
    """

    l = CodeSystemConcept(
        {
            "code": "L",
            "definition": "An equipment can either work autonomously ('Local' control state).",
            "display": "Local",
        }
    )
    """
    Local

    An equipment can either work autonomously ('Local' control state).
    """

    r = CodeSystemConcept(
        {
            "code": "R",
            "definition": "An equipment can be controlled by another system, e.g., LAS computer ('Remote' control state).",
            "display": "Remote",
        }
    )
    """
    Remote

    An equipment can be controlled by another system, e.g., LAS computer ('Remote' control state).
    """

    class Meta:
        resource = _resource
