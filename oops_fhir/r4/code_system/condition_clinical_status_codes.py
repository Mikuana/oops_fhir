from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ConditionClinicalStatusCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ConditionClinicalStatusCodes:
    """
    Condition Clinical Status Codes

    Preferred value set for Condition Clinical Status.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/condition-clinical
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "concept": [
                {
                    "code": "recurrence",
                    "definition": "The subject is experiencing a re-occurence or repeating of a previously resolved condition, e.g. urinary tract infection, pancreatitis, cholangitis, conjunctivitis.",
                    "display": "Recurrence",
                },
                {
                    "code": "relapse",
                    "definition": "The subject is experiencing a return of a condition, or signs and symptoms after a period of improvement or remission, e.g. relapse of cancer, multiple sclerosis, rheumatoid arthritis, systemic lupus erythematosus, bipolar disorder, [psychotic relapse of] schizophrenia, etc.",
                    "display": "Relapse",
                },
            ],
            "definition": "The subject is currently experiencing the symptoms of the condition or there is evidence of the condition.",
            "display": "Active",
        }
    )
    """
    Active

    The subject is currently experiencing the symptoms of the condition or there is evidence of the condition.
    """

    inactive = CodeSystemConcept(
        {
            "code": "inactive",
            "concept": [
                {
                    "code": "remission",
                    "definition": "The subject is no longer experiencing the symptoms of the condition, but there is a risk of the symptoms returning.",
                    "display": "Remission",
                },
                {
                    "code": "resolved",
                    "definition": "The subject is no longer experiencing the symptoms of the condition and there is a negligible perceived risk of the symptoms returning.",
                    "display": "Resolved",
                },
            ],
            "definition": "The subject is no longer experiencing the symptoms of the condition or there is no longer evidence of the condition.",
            "display": "Inactive",
        }
    )
    """
    Inactive

    The subject is no longer experiencing the symptoms of the condition or there is no longer evidence of the condition.
    """

    class Meta:
        resource = _resource
