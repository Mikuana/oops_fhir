from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.data_type import DataType

from oops_fhir.r4.code_system.resource_type import ResourceType


__all__ = ["FHIRDefinedType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FHIRDefinedType(ValueSet):
    """
    FHIRDefinedType

    A list of all the concrete types defined in this version of the FHIR
specification - Data Types and Resource Types.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/defined-types
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
