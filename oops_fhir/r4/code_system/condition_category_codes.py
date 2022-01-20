from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ConditionCategoryCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ConditionCategoryCodes:
    """
    Condition Category Codes

    Preferred value set for Condition Categories.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/condition-category
    """

    problem_list_item = CodeSystemConcept(
        {
            "code": "problem-list-item",
            "definition": "An item on a problem list that can be managed over time and can be expressed by a practitioner (e.g. physician, nurse), patient, or related person.",
            "display": "Problem List Item",
        }
    )
    """
    Problem List Item

    An item on a problem list that can be managed over time and can be expressed by a practitioner (e.g. physician, nurse), patient, or related person.
    """

    encounter_diagnosis = CodeSystemConcept(
        {
            "code": "encounter-diagnosis",
            "definition": "A point in time diagnosis (e.g. from a physician or nurse) in context of an encounter.",
            "display": "Encounter Diagnosis",
        }
    )
    """
    Encounter Diagnosis

    A point in time diagnosis (e.g. from a physician or nurse) in context of an encounter.
    """

    class Meta:
        resource = _resource
