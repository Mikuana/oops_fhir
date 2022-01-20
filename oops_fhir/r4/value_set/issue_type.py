from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.issue_type import IssueType as IssueType_


__all__ = ["IssueType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class IssueType(IssueType_):
    """
    IssueType

    A code that describes the type of issue.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/issue-type
    """

    class Meta:
        resource = _resource
