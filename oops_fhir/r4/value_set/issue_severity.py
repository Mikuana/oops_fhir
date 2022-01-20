from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.issue_severity import IssueSeverity as IssueSeverity_


__all__ = ["IssueSeverity"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class IssueSeverity(IssueSeverity_):
    """
    IssueSeverity

    How the issue affects the success of the action.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/issue-severity
    """

    class Meta:
        resource = _resource
