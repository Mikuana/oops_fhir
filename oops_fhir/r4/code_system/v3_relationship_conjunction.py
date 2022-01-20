from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3RelationshipConjunction"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3RelationshipConjunction:
    """
    v3 Code System RelationshipConjunction

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-RelationshipConjunction
    """

    and_ = CodeSystemConcept(
        {"code": "AND", "definition": "This condition must be true.", "display": "and"}
    )
    """
    and

    This condition must be true.
    """

    or_ = CodeSystemConcept(
        {
            "code": "OR",
            "definition": "At least one of the condition among all OR conditions must be true.",
            "display": "or",
        }
    )
    """
    or

    At least one of the condition among all OR conditions must be true.
    """

    xor = CodeSystemConcept(
        {
            "code": "XOR",
            "definition": "One and only one of the XOR conditions must be true.",
            "display": "exclusive or",
        }
    )
    """
    exclusive or

    One and only one of the XOR conditions must be true.
    """

    class Meta:
        resource = _resource
