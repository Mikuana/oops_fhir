from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["TaskIntent"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class TaskIntent:
    """
    TaskIntent

    Distinguishes whether the task is a proposal, plan or full order.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/task-intent
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": "The intent is not known.  When dealing with Task, it's not always known (or relevant) how the task was initiated - i.e. whether it was proposed, planned, ordered or just done spontaneously.",
            "display": "Unknown",
        }
    )
    """
    Unknown

    The intent is not known.  When dealing with Task, it's not always known (or relevant) how the task was initiated - i.e. whether it was proposed, planned, ordered or just done spontaneously.
    """

    class Meta:
        resource = _resource
