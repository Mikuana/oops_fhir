from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["RequestPriority"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class RequestPriority:
    """
    RequestPriority

    Identifies the level of importance to be assigned to actioning the
request.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/request-priority
    """

    routine = CodeSystemConcept(
        {
            "code": "routine",
            "definition": "The request has normal priority.",
            "display": "Routine",
        }
    )
    """
    Routine

    The request has normal priority.
    """

    urgent = CodeSystemConcept(
        {
            "code": "urgent",
            "definition": "The request should be actioned promptly - higher priority than routine.",
            "display": "Urgent",
        }
    )
    """
    Urgent

    The request should be actioned promptly - higher priority than routine.
    """

    asap = CodeSystemConcept(
        {
            "code": "asap",
            "definition": "The request should be actioned as soon as possible - higher priority than urgent.",
            "display": "ASAP",
        }
    )
    """
    ASAP

    The request should be actioned as soon as possible - higher priority than urgent.
    """

    stat = CodeSystemConcept(
        {
            "code": "stat",
            "definition": "The request should be actioned immediately - highest possible priority.  E.g. an emergency.",
            "display": "STAT",
        }
    )
    """
    STAT

    The request should be actioned immediately - highest possible priority.  E.g. an emergency.
    """

    class Meta:
        resource = _resource
