from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContractActionCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContractActionCodes:
    """
    Contract Action Codes

    This value set includes sample Contract Action codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/contractaction
    """

    action_a = CodeSystemConcept(
        {
            "code": "action-a",
            "definition": "Definition for Action A",
            "display": "Action A",
        }
    )
    """
    Action A

    Definition for Action A
    """

    action_b = CodeSystemConcept(
        {
            "code": "action-b",
            "definition": "Definition for Action B",
            "display": "Action B",
        }
    )
    """
    Action B

    Definition for Action B
    """

    class Meta:
        resource = _resource
