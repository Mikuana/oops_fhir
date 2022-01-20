from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["PerformerRoleCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class PerformerRoleCodes:
    """
    Performer Role Codes

    This value set includes sample Performer Role codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://hl7.org/fhir/consentperformer
    """

    consenter = CodeSystemConcept(
        {
            "code": "consenter",
            "definition": "An entity or an entity's delegatee who is the grantee in an agreement such as a consent for services, advanced directive, or a privacy consent directive in accordance with jurisdictional, organizational, or patient policy.",
            "display": "Consenter",
        }
    )
    """
    Consenter

    An entity or an entity's delegatee who is the grantee in an agreement such as a consent for services, advanced directive, or a privacy consent directive in accordance with jurisdictional, organizational, or patient policy.
    """

    grantee = CodeSystemConcept(
        {
            "code": "grantee",
            "definition": "An entity which accepts certain rights or authority from a grantor.",
            "display": "Grantee",
        }
    )
    """
    Grantee

    An entity which accepts certain rights or authority from a grantor.
    """

    grantor = CodeSystemConcept(
        {
            "code": "grantor",
            "definition": "An entity which agrees to confer certain rights or authority to a grantee.",
            "display": "Grantor",
        }
    )
    """
    Grantor

    An entity which agrees to confer certain rights or authority to a grantee.
    """

    delegatee = CodeSystemConcept(
        {
            "code": "delegatee",
            "definition": "A party to whom some right or authority is granted by a delegator.",
            "display": "Delegatee",
        }
    )
    """
    Delegatee

    A party to whom some right or authority is granted by a delegator.
    """

    delegator = CodeSystemConcept(
        {
            "code": "delegator",
            "definition": "A party that grants all or some portion its right or authority to another party.",
            "display": "Delegator",
        }
    )
    """
    Delegator

    A party that grants all or some portion its right or authority to another party.
    """

    class Meta:
        resource = _resource
