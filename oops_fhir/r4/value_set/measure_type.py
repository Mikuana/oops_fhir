from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.measure_type import MeasureType as MeasureType_


__all__ = ["MeasureType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MeasureType(MeasureType_):
    """
    MeasureType

    The type of measure (includes codes from 2.16.840.1.113883.1.11.20368).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/measure-type
    """

    class Meta:
        resource = _resource
