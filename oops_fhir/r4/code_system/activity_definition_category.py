from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ActivityDefinitionCategory"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ActivityDefinitionCategory:
    """
    ActivityDefinitionCategory

    High-level categorization of the type of activity.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/activity-definition-category
    """

    treatment = CodeSystemConcept(
        {
            "code": "treatment",
            "definition": "The activity is intended to provide or is related to treatment of the patient.",
            "display": "Treatment",
        }
    )
    """
    Treatment

    The activity is intended to provide or is related to treatment of the patient.
    """

    education = CodeSystemConcept(
        {
            "code": "education",
            "definition": "The activity is intended to provide or is related to education of the patient.",
            "display": "Education",
        }
    )
    """
    Education

    The activity is intended to provide or is related to education of the patient.
    """

    assessment = CodeSystemConcept(
        {
            "code": "assessment",
            "definition": "The activity is intended to perform or is related to assessment of the patient.",
            "display": "Assessment",
        }
    )
    """
    Assessment

    The activity is intended to perform or is related to assessment of the patient.
    """

    class Meta:
        resource = _resource
