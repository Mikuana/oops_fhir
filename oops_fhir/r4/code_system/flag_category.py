from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["FlagCategory"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class FlagCategory:
    """
    Flag Category

    Example list of general categories for flagged issues. (Not complete or
necessarily appropriate.)

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/flag-category
    """

    diet = CodeSystemConcept(
        {
            "code": "diet",
            "definition": "Flags related to the subject's dietary needs.",
            "display": "Diet",
        }
    )
    """
    Diet

    Flags related to the subject's dietary needs.
    """

    drug = CodeSystemConcept(
        {
            "code": "drug",
            "definition": "Flags related to the subject's medications.",
            "display": "Drug",
        }
    )
    """
    Drug

    Flags related to the subject's medications.
    """

    lab = CodeSystemConcept(
        {
            "code": "lab",
            "definition": "Flags related to performing laboratory tests and related processes (e.g. phlebotomy).",
            "display": "Lab",
        }
    )
    """
    Lab

    Flags related to performing laboratory tests and related processes (e.g. phlebotomy).
    """

    admin = CodeSystemConcept(
        {
            "code": "admin",
            "definition": "Flags related to administrative and financial processes.",
            "display": "Administrative",
        }
    )
    """
    Administrative

    Flags related to administrative and financial processes.
    """

    contact = CodeSystemConcept(
        {
            "code": "contact",
            "definition": "Flags related to coming into contact with the patient.",
            "display": "Subject Contact",
        }
    )
    """
    Subject Contact

    Flags related to coming into contact with the patient.
    """

    clinical = CodeSystemConcept(
        {
            "code": "clinical",
            "definition": "Flags related to the subject's clinical data.",
            "display": "Clinical",
        }
    )
    """
    Clinical

    Flags related to the subject's clinical data.
    """

    behavioral = CodeSystemConcept(
        {
            "code": "behavioral",
            "definition": "Flags related to behavior.",
            "display": "Behavioral",
        }
    )
    """
    Behavioral

    Flags related to behavior.
    """

    research = CodeSystemConcept(
        {
            "code": "research",
            "definition": "Flags related to research.",
            "display": "Research",
        }
    )
    """
    Research

    Flags related to research.
    """

    advance_directive = CodeSystemConcept(
        {
            "code": "advance-directive",
            "definition": "Flags related to subject's advance directives.",
            "display": "Advance Directive",
        }
    )
    """
    Advance Directive

    Flags related to subject's advance directives.
    """

    safety = CodeSystemConcept(
        {
            "code": "safety",
            "definition": "Flags related to safety precautions.",
            "display": "Safety",
        }
    )
    """
    Safety

    Flags related to safety precautions.
    """

    class Meta:
        resource = _resource
