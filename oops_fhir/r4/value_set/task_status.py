from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.task_status import TaskStatus as TaskStatus_


__all__ = ["TaskStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TaskStatus(TaskStatus_):
    """
    TaskStatus

    The current status of the task.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/task-status
    """

    class Meta:
        resource = _resource
