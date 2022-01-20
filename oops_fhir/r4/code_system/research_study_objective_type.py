from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ResearchStudyObjectiveType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ResearchStudyObjectiveType:
    """
    ResearchStudyObjectiveType

    Codes for the kind of study objective.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/research-study-objective-type
    """

    primary = CodeSystemConcept(
        {
            "code": "primary",
            "definition": "The main question to be answered, and the one that drives any statistical planning for the study—e.g., calculation of the sample size to provide the appropriate power for statistical testing.",
            "display": "Primary",
        }
    )
    """
    Primary

    The main question to be answered, and the one that drives any statistical planning for the study—e.g., calculation of the sample size to provide the appropriate power for statistical testing.
    """

    secondary = CodeSystemConcept(
        {
            "code": "secondary",
            "definition": "Question to be answered in the study that is of lesser importance than the primary objective.",
            "display": "Secondary",
        }
    )
    """
    Secondary

    Question to be answered in the study that is of lesser importance than the primary objective.
    """

    exploratory = CodeSystemConcept(
        {
            "code": "exploratory",
            "definition": "Exploratory questions to be answered in the study.",
            "display": "Exploratory",
        }
    )
    """
    Exploratory

    Exploratory questions to be answered in the study.
    """

    class Meta:
        resource = _resource
