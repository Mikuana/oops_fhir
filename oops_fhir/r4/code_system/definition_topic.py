from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DefinitionTopic"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DefinitionTopic:
    """
    DefinitionTopic

    High-level categorization of the definition, used for searching,
sorting, and filtering.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/definition-topic
    """

    treatment = CodeSystemConcept(
        {
            "code": "treatment",
            "definition": "The definition is related to treatment of the patient.",
            "display": "Treatment",
        }
    )
    """
    Treatment

    The definition is related to treatment of the patient.
    """

    education = CodeSystemConcept(
        {
            "code": "education",
            "definition": "The definition is related to education of the patient.",
            "display": "Education",
        }
    )
    """
    Education

    The definition is related to education of the patient.
    """

    assessment = CodeSystemConcept(
        {
            "code": "assessment",
            "definition": "The definition is related to assessment of the patient.",
            "display": "Assessment",
        }
    )
    """
    Assessment

    The definition is related to assessment of the patient.
    """

    class Meta:
        resource = _resource
