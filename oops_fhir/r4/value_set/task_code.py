from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.task_code import TaskCode as TaskCode_


__all__ = ["TaskCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TaskCode(TaskCode_):
    """
    Task Codes

    Codes indicating the type of action that is expected to be performed

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/task-code
    """

    class Meta:
        resource = _resource
