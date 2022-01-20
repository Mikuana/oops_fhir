from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContractTermSubtypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContractTermSubtypeCodes:
    """
    Contract Term Subtype Codes

    This value set includes sample Contract Term SubType codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/contracttermsubtypecodes
    """

    condition = CodeSystemConcept(
        {
            "code": "condition",
            "definition": "Terms that go to the very root of a contract.",
            "display": "Condition",
        }
    )
    """
    Condition

    Terms that go to the very root of a contract.
    """

    warranty = CodeSystemConcept(
        {
            "code": "warranty",
            "definition": "Less imperative than a condition, so the contract will survive a breach",
            "display": "Warranty",
        }
    )
    """
    Warranty

    Less imperative than a condition, so the contract will survive a breach
    """

    innominate = CodeSystemConcept(
        {
            "code": "innominate",
            "definition": "Breach of which might or might not go to the root of the contract depending upon the nature of the breach",
            "display": "Innominate",
        }
    )
    """
    Innominate

    Breach of which might or might not go to the root of the contract depending upon the nature of the breach
    """

    class Meta:
        resource = _resource
