from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.unit_type_codes import UnitTypeCodes as UnitTypeCodes_


__all__ = ["UnitTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class UnitTypeCodes(UnitTypeCodes_):
    """
    Unit Type Codes

    This value set includes a smattering of Unit type codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/benefit-unit
    """

    class Meta:
        resource = _resource
