from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContractResourceActionStatusCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceActionStatusCodes:
    """
    Contract Resource Action Status codes

    This value set contract specific codes for action status.

    Status: draft - Version: 4.0.1

    Copyright HL7 International.

    http://hl7.org/fhir/contract-action-status
    """

    complete = CodeSystemConcept(
        {"code": "complete", "definition": "To be completed", "display": "Complete"}
    )
    """
    Complete

    To be completed
    """

    class Meta:
        resource = _resource
