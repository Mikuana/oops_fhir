from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.task_intent import TaskIntent as TaskIntent_


__all__ = ["TaskIntent"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TaskIntent(ValueSet):
    """
    TaskIntent

    Distinguishes whether the task is a proposal, plan or full order.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/task-intent
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
