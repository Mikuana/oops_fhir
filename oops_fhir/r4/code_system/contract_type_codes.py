from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContractTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContractTypeCodes:
    """
    Contract Type Codes

    This value set includes sample Contract Type codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/contract-type
    """

    privacy = CodeSystemConcept(
        {"code": "privacy", "definition": "Privacy policy.", "display": "Privacy"}
    )
    """
    Privacy

    Privacy policy.
    """

    disclosure = CodeSystemConcept(
        {
            "code": "disclosure",
            "definition": "Information disclosure policy.",
            "display": "Disclosure",
        }
    )
    """
    Disclosure

    Information disclosure policy.
    """

    healthinsurance = CodeSystemConcept(
        {
            "code": "healthinsurance",
            "definition": "Health Insurance policy.",
            "display": "Health Insurance",
        }
    )
    """
    Health Insurance

    Health Insurance policy.
    """

    supply = CodeSystemConcept(
        {
            "code": "supply",
            "definition": "Contract to supply goods or services.",
            "display": "Supply Contract",
        }
    )
    """
    Supply Contract

    Contract to supply goods or services.
    """

    consent = CodeSystemConcept(
        {"code": "consent", "definition": "Consent Directive.", "display": "Consent"}
    )
    """
    Consent

    Consent Directive.
    """

    class Meta:
        resource = _resource
