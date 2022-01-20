from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContractResourceDefinitionSubtypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceDefinitionSubtypeCodes:
    """
    Contract Resource Definition Subtype codes

    This value set contract specific codes for status.

    Status: draft - Version: 4.0.1

    Copyright HL7 International.

    http://hl7.org/fhir/contract-definition-subtype
    """

    temp = CodeSystemConcept(
        {"code": "temp", "definition": "To be completed", "display": "Temporary Value"}
    )
    """
    Temporary Value

    To be completed
    """

    class Meta:
        resource = _resource
