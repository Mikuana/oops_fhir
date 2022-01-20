from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3MessageWaitingPriority"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3MessageWaitingPriority:
    """
    v3 Code System MessageWaitingPriority

     Indicates that the receiver has messages for the sender  OpenIssue:
Description does not make sense relative to name of coding system.  Must
be reviewed and improved.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-MessageWaitingPriority
    """

    h = CodeSystemConcept(
        {
            "code": "H",
            "definition": "High priority messages are available",
            "display": "High",
        }
    )
    """
    High

    High priority messages are available
    """

    l = CodeSystemConcept(
        {
            "code": "L",
            "definition": "Low priority messages are available",
            "display": "Low",
        }
    )
    """
    Low

    Low priority messages are available
    """

    m = CodeSystemConcept(
        {
            "code": "M",
            "definition": "Medium priority messages are available",
            "display": "Medium",
        }
    )
    """
    Medium

    Medium priority messages are available
    """

    class Meta:
        resource = _resource
