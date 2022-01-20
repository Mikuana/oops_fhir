from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExamplePaymentTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExamplePaymentTypeCodes:
    """
    Example Payment Type Codes

    This value set includes example Payment Type codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/ex-paymenttype
    """

    complete = CodeSystemConcept(
        {
            "code": "complete",
            "definition": "Complete (final) payment of the benefit under the Claim less any adjustments.",
            "display": "Complete",
        }
    )
    """
    Complete

    Complete (final) payment of the benefit under the Claim less any adjustments.
    """

    partial = CodeSystemConcept(
        {
            "code": "partial",
            "definition": "Partial payment of the benefit under the Claim less any adjustments.",
            "display": "Partial",
        }
    )
    """
    Partial

    Partial payment of the benefit under the Claim less any adjustments.
    """

    class Meta:
        resource = _resource
