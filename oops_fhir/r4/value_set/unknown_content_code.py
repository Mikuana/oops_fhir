from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.unknown_content_code import (
    UnknownContentCode as UnknownContentCode_,
)


__all__ = ["UnknownContentCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class UnknownContentCode(UnknownContentCode_):
    """
    UnknownContentCode

    A code that indicates whether an application accepts unknown elements or
extensions when reading resources.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/unknown-content-code
    """

    class Meta:
        resource = _resource
