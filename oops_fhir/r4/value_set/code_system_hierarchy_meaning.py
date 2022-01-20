from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.code_system_hierarchy_meaning import (
    CodeSystemHierarchyMeaning as CodeSystemHierarchyMeaning_,
)


__all__ = ["CodeSystemHierarchyMeaning"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CodeSystemHierarchyMeaning(CodeSystemHierarchyMeaning_):
    """
    CodeSystemHierarchyMeaning

    The meaning of the hierarchy of concepts in a code system.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/codesystem-hierarchy-meaning
    """

    class Meta:
        resource = _resource
