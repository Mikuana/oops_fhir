from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExampleVisionPrescriptionProductCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExampleVisionPrescriptionProductCodes:
    """
    Example Vision Prescription Product Codes

    This value set includes a smattering of Prescription Product codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct
    """

    lens = CodeSystemConcept(
        {
            "code": "lens",
            "definition": "A lens to be fitted to a frame to comprise a pair of glasses.",
            "display": "Lens",
        }
    )
    """
    Lens

    A lens to be fitted to a frame to comprise a pair of glasses.
    """

    contact = CodeSystemConcept(
        {
            "code": "contact",
            "definition": "A lens to be fitted for wearing directly on an eye.",
            "display": "Contact Lens",
        }
    )
    """
    Contact Lens

    A lens to be fitted for wearing directly on an eye.
    """

    class Meta:
        resource = _resource
