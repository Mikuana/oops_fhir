from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ProcessPriorityCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ProcessPriorityCodes:
    """
    Process Priority Codes

    This value set includes the financial processing priority codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/processpriority
    """

    stat = CodeSystemConcept(
        {
            "code": "stat",
            "definition": "Immediately in real time.",
            "display": "Immediate",
        }
    )
    """
    Immediate

    Immediately in real time.
    """

    normal = CodeSystemConcept(
        {"code": "normal", "definition": "With best effort.", "display": "Normal"}
    )
    """
    Normal

    With best effort.
    """

    deferred = CodeSystemConcept(
        {
            "code": "deferred",
            "definition": "Later, when possible.",
            "display": "Deferred",
        }
    )
    """
    Deferred

    Later, when possible.
    """

    class Meta:
        resource = _resource
