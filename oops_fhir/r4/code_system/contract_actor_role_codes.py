from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContractActorRoleCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContractActorRoleCodes:
    """
    Contract Actor Role Codes

    This value set includes sample Contract Actor Role codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/contractactorrole
    """

    practitioner = CodeSystemConcept(
        {
            "code": "practitioner",
            "definition": "Someone who provides health care related services to people or animals including both clinical and support services.",
            "display": "Practitioner",
        }
    )
    """
    Practitioner

    Someone who provides health care related services to people or animals including both clinical and support services.
    """

    patient = CodeSystemConcept(
        {
            "code": "patient",
            "definition": "A receiver, human or animal, of health care related goods and services.",
            "display": "Patient",
        }
    )
    """
    Patient

    A receiver, human or animal, of health care related goods and services.
    """

    class Meta:
        resource = _resource
