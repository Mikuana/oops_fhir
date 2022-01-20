from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.data_type import DataType as DataType_


__all__ = ["DataType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DataType(DataType_):
    """
    DataType

    A version specific list of the data types defined by the FHIR
specification for use as an element  type (any of the FHIR defined data
types).

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/data-types
    """

    class Meta:
        resource = _resource
