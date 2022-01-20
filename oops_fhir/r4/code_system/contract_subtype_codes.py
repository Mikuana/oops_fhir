from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContractSubtypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContractSubtypeCodes:
    """
    Contract Subtype Codes

    This value set includes sample Contract Subtype codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/contractsubtypecodes
    """

    disclosure_ca = CodeSystemConcept(
        {
            "code": "disclosure-ca",
            "definition": "Canadian health information disclosure policy.",
            "display": "Disclosure-CA",
        }
    )
    """
    Disclosure-CA

    Canadian health information disclosure policy.
    """

    disclosure_us = CodeSystemConcept(
        {
            "code": "disclosure-us",
            "definition": "United States health information disclosure policy.",
            "display": "Disclosure-US",
        }
    )
    """
    Disclosure-US

    United States health information disclosure policy.
    """

    class Meta:
        resource = _resource
