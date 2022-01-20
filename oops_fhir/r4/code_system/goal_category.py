from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["GoalCategory"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class GoalCategory:
    """
    Goal category

    Example codes for grouping goals to use for filtering or presentation.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/goal-category
    """

    dietary = CodeSystemConcept(
        {
            "code": "dietary",
            "definition": "Goals related to the consumption of food and/or beverages.",
            "display": "Dietary",
        }
    )
    """
    Dietary

    Goals related to the consumption of food and/or beverages.
    """

    safety = CodeSystemConcept(
        {
            "code": "safety",
            "definition": "Goals related to the personal protection of the subject.",
            "display": "Safety",
        }
    )
    """
    Safety

    Goals related to the personal protection of the subject.
    """

    behavioral = CodeSystemConcept(
        {
            "code": "behavioral",
            "definition": "Goals related to the manner in which the subject acts.",
            "display": "Behavioral",
        }
    )
    """
    Behavioral

    Goals related to the manner in which the subject acts.
    """

    nursing = CodeSystemConcept(
        {
            "code": "nursing",
            "definition": "Goals related to the practice of nursing or established by nurses.",
            "display": "Nursing",
        }
    )
    """
    Nursing

    Goals related to the practice of nursing or established by nurses.
    """

    physiotherapy = CodeSystemConcept(
        {
            "code": "physiotherapy",
            "definition": "Goals related to the mobility and/or motor capability of the subject.",
            "display": "Physiotherapy",
        }
    )
    """
    Physiotherapy

    Goals related to the mobility and/or motor capability of the subject.
    """

    class Meta:
        resource = _resource
