from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.alternative_code_kind import (
    AlternativeCodeKind as AlternativeCodeKind_,
)


__all__ = ["AlternativeCodeKind"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AlternativeCodeKind(AlternativeCodeKind_):
    """
    AlternativeCodeKind

    Indicates the type of use for which the code is defined.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/codesystem-altcode-kind
    """

    class Meta:
        resource = _resource
