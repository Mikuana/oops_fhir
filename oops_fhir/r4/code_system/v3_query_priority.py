from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3QueryPriority"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3QueryPriority:
    """
    v3 Code System QueryPriority

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-QueryPriority
    """

    d = CodeSystemConcept(
        {
            "code": "D",
            "definition": "Query response is deferred.",
            "display": "Deferred",
        }
    )
    """
    Deferred

    Query response is deferred.
    """

    i = CodeSystemConcept(
        {
            "code": "I",
            "definition": "Query response is immediate.",
            "display": "Immediate",
        }
    )
    """
    Immediate

    Query response is immediate.
    """

    class Meta:
        resource = _resource
