from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.udientry_type import UDIEntryType as UDIEntryType_


__all__ = ["UDIEntryType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class UDIEntryType(UDIEntryType_):
    """
    UDIEntryType

    Codes to identify how UDI data was entered.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/udi-entry-type
    """

    class Meta:
        resource = _resource
