from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3SubstitutionCondition"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3SubstitutionCondition:
    """
    v3 Code System SubstitutionCondition

     Identifies what sort of change is permitted or has occurred between the
item that was ordered/requested and the one that was/will be provided.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-SubstitutionCondition
    """

    underscore_conditional = CodeSystemConcept(
        {
            "code": "_Conditional",
            "concept": [
                {
                    "code": "CONFIRM",
                    "definition": "Confirmation with Contact Person prior to making any substitutions has or will occur.",
                    "display": "Confirm first",
                },
                {
                    "code": "NOTIFY",
                    "definition": "Notification to the Contact Person, prior to substitution and through normal institutional procedures, has or will be made.",
                    "display": "Notify first",
                },
            ],
            "definition": "Some conditions may be attached to an allowable substitution.  An allowable substitution is based on a match to any other attributes that may be specified.",
            "display": "Conditional",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Conditional

    Some conditions may be attached to an allowable substitution.  An allowable substitution is based on a match to any other attributes that may be specified.
    """

    nosub = CodeSystemConcept(
        {
            "code": "NOSUB",
            "definition": "Substitution is not permitted.",
            "display": "No substitution",
        }
    )
    """
    No substitution

    Substitution is not permitted.
    """

    uncond = CodeSystemConcept(
        {
            "code": "UNCOND",
            "definition": "No conditions are required.",
            "display": "Unconditional",
        }
    )
    """
    Unconditional

    No conditions are required.
    """

    class Meta:
        resource = _resource
