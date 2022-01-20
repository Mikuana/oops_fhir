from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.example_program_reason_codes import (
    ExampleProgramReasonCodes as ExampleProgramReasonCodes_,
)


__all__ = ["ExampleProgramReasonCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExampleProgramReasonCodes(ExampleProgramReasonCodes_):
    """
    Example Program Reason Codes

    This value set includes sample Program Reason Span codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/ex-program-code
    """

    class Meta:
        resource = _resource
