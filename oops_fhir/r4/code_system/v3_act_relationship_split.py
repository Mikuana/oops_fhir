from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ActRelationshipSplit"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ActRelationshipSplit:
    """
    v3 Code System ActRelationshipSplit

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ActRelationshipSplit
    """

    e1 = CodeSystemConcept(
        {
            "code": "E1",
            "definition": 'The pre-condition associated with the branch is evaluated once and if true the branch may be entered. All other exclusive branches compete with each other and only one will be selected. This implements a COND, IF and CASE conditionals, or "XOR-split." The order in which the branches are considered may be specified in the priorityNumber attribute.',
            "display": "exclusive try once",
        }
    )
    """
    exclusive try once

    The pre-condition associated with the branch is evaluated once and if true the branch may be entered. All other exclusive branches compete with each other and only one will be selected. This implements a COND, IF and CASE conditionals, or "XOR-split." The order in which the branches are considered may be specified in the priorityNumber attribute.
    """

    ew = CodeSystemConcept(
        {
            "code": "EW",
            "definition": "A branch is selected as soon as the pre-condition associated with the branch evaluates to true.  If the condition is false, the branch may be entered later, when the condition turns true.  All other exclusive branches compete with each other and only one will be selected.  Each waiting branch executes in parallel with the default join code wait  (see below). The order in which the branches are considered may be specified in the Service_relationship.priority_nmb.",
            "display": "exclusive wait",
        }
    )
    """
    exclusive wait

    A branch is selected as soon as the pre-condition associated with the branch evaluates to true.  If the condition is false, the branch may be entered later, when the condition turns true.  All other exclusive branches compete with each other and only one will be selected.  Each waiting branch executes in parallel with the default join code wait  (see below). The order in which the branches are considered may be specified in the Service_relationship.priority_nmb.
    """

    i1 = CodeSystemConcept(
        {
            "code": "I1",
            "definition": "A branch is executed if its associated preconditions permit. If associated preconditions do not permit, the branch is dropped.  Inclusive branches are not suppressed and do not suppress other branches.",
            "display": "inclusive try once",
        }
    )
    """
    inclusive try once

    A branch is executed if its associated preconditions permit. If associated preconditions do not permit, the branch is dropped.  Inclusive branches are not suppressed and do not suppress other branches.
    """

    iw = CodeSystemConcept(
        {
            "code": "IW",
            "definition": "A branch is executed as soon as its associated conditions permit.  If the condition is false, the branch may be entered later, when the condition turns true.  Inclusive branches are not suppressed and do not suppress other branches.  Each waiting branch executes in parallel with the default join code wait  (see below).",
            "display": "inclusive wait",
        }
    )
    """
    inclusive wait

    A branch is executed as soon as its associated conditions permit.  If the condition is false, the branch may be entered later, when the condition turns true.  Inclusive branches are not suppressed and do not suppress other branches.  Each waiting branch executes in parallel with the default join code wait  (see below).
    """

    class Meta:
        resource = _resource
