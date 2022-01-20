from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ActRelationshipJoin"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ActRelationshipJoin:
    """
    v3 Code System ActRelationshipJoin

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ActRelationshipJoin
    """

    d = CodeSystemConcept(
        {
            "code": "D",
            "definition": "Detach this branch from the other branches so it will not be resynchronized with the other branches.",
            "display": "detached",
        }
    )
    """
    detached

    Detach this branch from the other branches so it will not be resynchronized with the other branches.
    """

    k = CodeSystemConcept(
        {
            "code": "K",
            "definition": "When all other concurrent branches are terminated, interrupt and discontinue this branch.",
            "display": "kill",
        }
    )
    """
    kill

    When all other concurrent branches are terminated, interrupt and discontinue this branch.
    """

    w = CodeSystemConcept(
        {
            "code": "W",
            "definition": "Wait for this branch to terminate.",
            "display": "wait",
        }
    )
    """
    wait

    Wait for this branch to terminate.
    """

    x = CodeSystemConcept(
        {
            "code": "X",
            "definition": "Wait for any one of the branches in the set of exclusive wait branches to terminate, then discontinue all the other exclusive wait branches.",
            "display": "exclusive wait",
        }
    )
    """
    exclusive wait

    Wait for any one of the branches in the set of exclusive wait branches to terminate, then discontinue all the other exclusive wait branches.
    """

    class Meta:
        resource = _resource
