from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.udicodes import UDICodes as UDICodes_


__all__ = ["UDICodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class UDICodes(UDICodes_):
    """
    UDI Codes

    This value set includes sample UDI codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/udi
    """

    class Meta:
        resource = _resource
