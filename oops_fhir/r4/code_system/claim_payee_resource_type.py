from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ClaimPayeeResourceType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ClaimPayeeResourceType:
    """
    ClaimPayeeResourceType

    The type of Claim payee Resource.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/ex-payee-resource-type
    """

    organization = CodeSystemConcept(
        {
            "code": "organization",
            "definition": "Organization resource.",
            "display": "Organization",
        }
    )
    """
    Organization

    Organization resource.
    """

    patient = CodeSystemConcept(
        {"code": "patient", "definition": "Patient resource.", "display": "Patient"}
    )
    """
    Patient

    Patient resource.
    """

    practitioner = CodeSystemConcept(
        {
            "code": "practitioner",
            "definition": "Practitioner resource.",
            "display": "Practitioner",
        }
    )
    """
    Practitioner

    Practitioner resource.
    """

    relatedperson = CodeSystemConcept(
        {
            "code": "relatedperson",
            "definition": "RelatedPerson resource.",
            "display": "RelatedPerson",
        }
    )
    """
    RelatedPerson

    RelatedPerson resource.
    """

    class Meta:
        resource = _resource
