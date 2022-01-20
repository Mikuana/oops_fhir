from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.example_vision_prescription_product_codes import (
    ExampleVisionPrescriptionProductCodes as ExampleVisionPrescriptionProductCodes_,
)


__all__ = ["ExampleVisionPrescriptionProductCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExampleVisionPrescriptionProductCodes(ExampleVisionPrescriptionProductCodes_):
    """
    Example Vision Prescription Product Codes

    This value set includes a smattering of Prescription Product codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/vision-product
    """

    class Meta:
        resource = _resource
