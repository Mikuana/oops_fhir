from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ImmunizationEvaluationDoseStatusCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationEvaluationDoseStatusCodes:
    """
    Immunization Evaluation Dose Status codes

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the validity of a dose relative to a
particular recommended schedule. This value set is provided as a
suggestive example.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status
    """

    valid = CodeSystemConcept(
        {
            "code": "valid",
            "definition": "The dose counts toward fulfilling a path to immunity for a patient, providing protection against the target disease.",
            "display": "Valid",
        }
    )
    """
    Valid

    The dose counts toward fulfilling a path to immunity for a patient, providing protection against the target disease.
    """

    notvalid = CodeSystemConcept(
        {
            "code": "notvalid",
            "definition": "The dose does not count toward fulfilling a path to immunity for a patient.",
            "display": "Not valid",
        }
    )
    """
    Not valid

    The dose does not count toward fulfilling a path to immunity for a patient.
    """

    class Meta:
        resource = _resource
