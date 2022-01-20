from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ActRelationshipCheckpoint"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ActRelationshipCheckpoint:
    """
    v3 Code System ActRelationshipCheckpoint

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ActRelationshipCheckpoint
    """

    b = CodeSystemConcept(
        {
            "code": "B",
            "definition": "Condition is tested every time before execution of the service (WHILE condition DO service).",
            "display": "beginning",
        }
    )
    """
    beginning

    Condition is tested every time before execution of the service (WHILE condition DO service).
    """

    e = CodeSystemConcept(
        {
            "code": "E",
            "definition": "Condition is tested at the end of a repeated service execution.  The service is repeated only if the condition is true (DO service WHILE condition).",
            "display": "end",
        }
    )
    """
    end

    Condition is tested at the end of a repeated service execution.  The service is repeated only if the condition is true (DO service WHILE condition).
    """

    s = CodeSystemConcept(
        {
            "code": "S",
            "definition": "Condition is tested once before the service is executed (IF condition THEN service).",
            "display": "entry",
        }
    )
    """
    entry

    Condition is tested once before the service is executed (IF condition THEN service).
    """

    t = CodeSystemConcept(
        {
            "code": "T",
            "definition": "Condition must be true throughout the execution and the service is interrupted (asynchronously) as soon as the condition turns false (asynchronous WHILE loop).  The service must be interruptible.",
            "display": "through",
        }
    )
    """
    through

    Condition must be true throughout the execution and the service is interrupted (asynchronously) as soon as the condition turns false (asynchronous WHILE loop).  The service must be interruptible.
    """

    x = CodeSystemConcept(
        {
            "code": "X",
            "definition": "Condition is a loop checkpoint, i.e. it is a step of an activity plan and, if negative causes the containing loop to exit.",
            "display": "exit",
        }
    )
    """
    exit

    Condition is a loop checkpoint, i.e. it is a step of an activity plan and, if negative causes the containing loop to exit.
    """

    class Meta:
        resource = _resource
