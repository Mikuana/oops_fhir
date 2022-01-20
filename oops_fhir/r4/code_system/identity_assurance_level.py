from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["IdentityAssuranceLevel"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class IdentityAssuranceLevel:
    """
    IdentityAssuranceLevel

    The level of confidence that this link represents the same actual
person, based on NIST Authentication Levels.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/identity-assuranceLevel
    """

    level1 = CodeSystemConcept(
        {
            "code": "level1",
            "definition": "Little or no confidence in the asserted identity's accuracy.",
            "display": "Level 1",
        }
    )
    """
    Level 1

    Little or no confidence in the asserted identity's accuracy.
    """

    level2 = CodeSystemConcept(
        {
            "code": "level2",
            "definition": "Some confidence in the asserted identity's accuracy.",
            "display": "Level 2",
        }
    )
    """
    Level 2

    Some confidence in the asserted identity's accuracy.
    """

    level3 = CodeSystemConcept(
        {
            "code": "level3",
            "definition": "High confidence in the asserted identity's accuracy.",
            "display": "Level 3",
        }
    )
    """
    Level 3

    High confidence in the asserted identity's accuracy.
    """

    level4 = CodeSystemConcept(
        {
            "code": "level4",
            "definition": "Very high confidence in the asserted identity's accuracy.",
            "display": "Level 4",
        }
    )
    """
    Level 4

    Very high confidence in the asserted identity's accuracy.
    """

    class Meta:
        resource = _resource
