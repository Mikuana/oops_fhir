from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.code_search_support import (
    CodeSearchSupport as CodeSearchSupport_,
)


__all__ = ["CodeSearchSupport"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CodeSearchSupport(CodeSearchSupport_):
    """
    CodeSearchSupport

    The degree to which the server supports the code search parameter on
ValueSet, if it is supported.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/code-search-support
    """

    class Meta:
        resource = _resource
