from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.example_onset_type_reason_codes import (
    ExampleOnsetTypeReasonCodes as ExampleOnsetTypeReasonCodes_,
)


__all__ = ["ExampleOnsetTypeReasonCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExampleOnsetTypeReasonCodes(ExampleOnsetTypeReasonCodes_):
    """
    Example Onset Type (Reason) Codes

    This value set includes sample Service Modifier codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/ex-onsettype
    """

    class Meta:
        resource = _resource
