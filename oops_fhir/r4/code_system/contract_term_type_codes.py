from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContractTermTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContractTermTypeCodes:
    """
    Contract Term Type Codes

    This value set includes sample Contract Term Type codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/contracttermtypecodes
    """

    statutory = CodeSystemConcept(
        {
            "code": "statutory",
            "definition": "Based on specialized statutes that deal with particular subjects.",
            "display": "Statutory",
        }
    )
    """
    Statutory

    Based on specialized statutes that deal with particular subjects.
    """

    subject_to = CodeSystemConcept(
        {
            "code": "subject-to",
            "definition": "Execution of the term in the contract is conditional on the execution of other actions.",
            "display": "Subject To",
        }
    )
    """
    Subject To

    Execution of the term in the contract is conditional on the execution of other actions.
    """

    class Meta:
        resource = _resource
