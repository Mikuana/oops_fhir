from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["TriggerType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class TriggerType:
    """
    TriggerType

    The type of trigger.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/trigger-type
    """

    named_event = CodeSystemConcept(
        {
            "code": "named-event",
            "definition": "The trigger occurs in response to a specific named event, and no other information about the trigger is specified. Named events are completely pre-coordinated, and the formal semantics of the trigger are not provided.",
            "display": "Named Event",
        }
    )
    """
    Named Event

    The trigger occurs in response to a specific named event, and no other information about the trigger is specified. Named events are completely pre-coordinated, and the formal semantics of the trigger are not provided.
    """

    periodic = CodeSystemConcept(
        {
            "code": "periodic",
            "definition": "The trigger occurs at a specific time or periodically as described by a timing or schedule. A periodic event cannot have any data elements, but may have a name assigned as a shorthand for the event.",
            "display": "Periodic",
        }
    )
    """
    Periodic

    The trigger occurs at a specific time or periodically as described by a timing or schedule. A periodic event cannot have any data elements, but may have a name assigned as a shorthand for the event.
    """

    data_changed = CodeSystemConcept(
        {
            "code": "data-changed",
            "concept": [
                {
                    "code": "data-added",
                    "definition": "The trigger occurs whenever data of a particular type is added.",
                    "display": "Data Added",
                },
                {
                    "code": "data-modified",
                    "definition": "The trigger occurs whenever data of a particular type is modified.",
                    "display": "Data Updated",
                },
                {
                    "code": "data-removed",
                    "definition": "The trigger occurs whenever data of a particular type is removed.",
                    "display": "Data Removed",
                },
            ],
            "definition": "The trigger occurs whenever data of a particular type is changed in any way, either added, modified, or removed.",
            "display": "Data Changed",
        }
    )
    """
    Data Changed

    The trigger occurs whenever data of a particular type is changed in any way, either added, modified, or removed.
    """

    data_accessed = CodeSystemConcept(
        {
            "code": "data-accessed",
            "definition": "The trigger occurs whenever data of a particular type is accessed.",
            "display": "Data Accessed",
        }
    )
    """
    Data Accessed

    The trigger occurs whenever data of a particular type is accessed.
    """

    data_access_ended = CodeSystemConcept(
        {
            "code": "data-access-ended",
            "definition": "The trigger occurs whenever access to data of a particular type is completed.",
            "display": "Data Access Ended",
        }
    )
    """
    Data Access Ended

    The trigger occurs whenever access to data of a particular type is completed.
    """

    class Meta:
        resource = _resource
