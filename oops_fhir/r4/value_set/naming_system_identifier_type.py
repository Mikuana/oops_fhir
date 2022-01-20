from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.naming_system_identifier_type import (
    NamingSystemIdentifierType as NamingSystemIdentifierType_,
)


__all__ = ["NamingSystemIdentifierType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class NamingSystemIdentifierType(NamingSystemIdentifierType_):
    """
    NamingSystemIdentifierType

    Identifies the style of unique identifier used to identify a namespace.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/namingsystem-identifier-type
    """

    class Meta:
        resource = _resource
