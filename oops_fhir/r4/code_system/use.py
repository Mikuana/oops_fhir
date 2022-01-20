from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["Use"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class Use:
    """
    Use

    The purpose of the Claim: predetermination, preauthorization, claim.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/claim-use
    """

    claim = CodeSystemConcept(
        {
            "code": "claim",
            "definition": "The treatment is complete and this represents a Claim for the services.",
            "display": "Claim",
        }
    )
    """
    Claim

    The treatment is complete and this represents a Claim for the services.
    """

    preauthorization = CodeSystemConcept(
        {
            "code": "preauthorization",
            "definition": "The treatment is proposed and this represents a Pre-authorization for the services.",
            "display": "Preauthorization",
        }
    )
    """
    Preauthorization

    The treatment is proposed and this represents a Pre-authorization for the services.
    """

    predetermination = CodeSystemConcept(
        {
            "code": "predetermination",
            "definition": "The treatment is proposed and this represents a Pre-determination for the services.",
            "display": "Predetermination",
        }
    )
    """
    Predetermination

    The treatment is proposed and this represents a Pre-determination for the services.
    """

    class Meta:
        resource = _resource
