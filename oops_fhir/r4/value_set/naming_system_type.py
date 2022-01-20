from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.naming_system_type import (
    NamingSystemType as NamingSystemType_,
)


__all__ = ["NamingSystemType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class NamingSystemType(NamingSystemType_):
    """
    NamingSystemType

    Identifies the purpose of the naming system.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/namingsystem-type
    """

    class Meta:
        resource = _resource
