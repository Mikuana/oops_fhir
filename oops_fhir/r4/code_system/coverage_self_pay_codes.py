from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CoverageSelfPayCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CoverageSelfPayCodes:
    """
    Coverage SelfPay Codes

    This value set includes Coverage SelfPay codes.

    Status: draft - Version: 4.0.1

    Copyright HL7 International.

    http://terminology.hl7.org/CodeSystem/coverage-selfpay
    """

    pay = CodeSystemConcept(
        {
            "code": "pay",
            "definition": "An individual or organization is paying directly for goods and services.",
            "display": "Pay",
        }
    )
    """
    Pay

    An individual or organization is paying directly for goods and services.
    """

    class Meta:
        resource = _resource
