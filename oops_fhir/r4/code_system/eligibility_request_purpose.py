from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["EligibilityRequestPurpose"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class EligibilityRequestPurpose:
    """
    EligibilityRequestPurpose

    A code specifying the types of information being requested.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/eligibilityrequest-purpose
    """

    auth_requirements = CodeSystemConcept(
        {
            "code": "auth-requirements",
            "definition": "The prior authorization requirements for the listed, or discovered if specified, converages for the categories of service and/or specifed biling codes are requested.",
            "display": "Coverage auth-requirements",
        }
    )
    """
    Coverage auth-requirements

    The prior authorization requirements for the listed, or discovered if specified, converages for the categories of service and/or specifed biling codes are requested.
    """

    benefits = CodeSystemConcept(
        {
            "code": "benefits",
            "definition": "The plan benefits and optionally benefits consumed  for the listed, or discovered if specified, converages are requested.",
            "display": "Coverage benefits",
        }
    )
    """
    Coverage benefits

    The plan benefits and optionally benefits consumed  for the listed, or discovered if specified, converages are requested.
    """

    discovery = CodeSystemConcept(
        {
            "code": "discovery",
            "definition": "The insurer is requested to report on any coverages which they are aware of in addition to any specifed.",
            "display": "Coverage Discovery",
        }
    )
    """
    Coverage Discovery

    The insurer is requested to report on any coverages which they are aware of in addition to any specifed.
    """

    validation = CodeSystemConcept(
        {
            "code": "validation",
            "definition": "A check that the specified coverages are in-force is requested.",
            "display": "Coverage Validation",
        }
    )
    """
    Coverage Validation

    A check that the specified coverages are in-force is requested.
    """

    class Meta:
        resource = _resource
