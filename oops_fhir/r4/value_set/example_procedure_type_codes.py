from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.example_procedure_type_codes import (
    ExampleProcedureTypeCodes as ExampleProcedureTypeCodes_,
)


__all__ = ["ExampleProcedureTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExampleProcedureTypeCodes(ExampleProcedureTypeCodes_):
    """
    Example Procedure Type Codes

    This value set includes example Procedure Type codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/ex-procedure-type
    """

    class Meta:
        resource = _resource
