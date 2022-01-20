from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ClaimTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ClaimTypeCodes:
    """
    Claim Type Codes

    This value set includes Claim Type codes.

    Status: draft - Version: 4.0.1

    Copyright HL7 Inc.

    http://terminology.hl7.org/CodeSystem/claim-type
    """

    institutional = CodeSystemConcept(
        {
            "code": "institutional",
            "definition": "Hospital, clinic and typically inpatient claims.",
            "display": "Institutional",
        }
    )
    """
    Institutional

    Hospital, clinic and typically inpatient claims.
    """

    oral = CodeSystemConcept(
        {
            "code": "oral",
            "definition": "Dental, Denture and Hygiene claims.",
            "display": "Oral",
        }
    )
    """
    Oral

    Dental, Denture and Hygiene claims.
    """

    pharmacy = CodeSystemConcept(
        {
            "code": "pharmacy",
            "definition": "Pharmacy claims for goods and services.",
            "display": "Pharmacy",
        }
    )
    """
    Pharmacy

    Pharmacy claims for goods and services.
    """

    professional = CodeSystemConcept(
        {
            "code": "professional",
            "definition": "Typically, outpatient claims from Physician, Psychological, Chiropractor, Physiotherapy, Speech Pathology, rehabilitative, consulting.",
            "display": "Professional",
        }
    )
    """
    Professional

    Typically, outpatient claims from Physician, Psychological, Chiropractor, Physiotherapy, Speech Pathology, rehabilitative, consulting.
    """

    vision = CodeSystemConcept(
        {
            "code": "vision",
            "definition": "Vision claims for professional services and products such as glasses and contact lenses.",
            "display": "Vision",
        }
    )
    """
    Vision

    Vision claims for professional services and products such as glasses and contact lenses.
    """

    class Meta:
        resource = _resource
