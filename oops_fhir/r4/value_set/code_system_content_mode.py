from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.code_system_content_mode import (
    CodeSystemContentMode as CodeSystemContentMode_,
)


__all__ = ["CodeSystemContentMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CodeSystemContentMode(CodeSystemContentMode_):
    """
    CodeSystemContentMode

    The extent of the content of the code system (the concepts and codes it
defines) are represented in a code system resource.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/codesystem-content-mode
    """

    class Meta:
        resource = _resource
