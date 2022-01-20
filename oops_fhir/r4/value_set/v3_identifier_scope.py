from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_identifier_scope import (
    v3IdentifierScope as v3IdentifierScope_,
)


__all__ = ["v3IdentifierScope"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3IdentifierScope(v3IdentifierScope_):
    """
    v3 Code System IdentifierScope

      Description:  Codes to specify the scope in which the identifier
applies to the object with which it is associated, and used in the
datatype property II.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-IdentifierScope
    """

    class Meta:
        resource = _resource
