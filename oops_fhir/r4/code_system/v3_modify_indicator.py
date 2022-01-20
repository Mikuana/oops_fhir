from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ModifyIndicator"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ModifyIndicator:
    """
    v3 Code System ModifyIndicator

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ModifyIndicator
    """

    m = CodeSystemConcept(
        {
            "code": "M",
            "definition": "Modified subscription to a query server.",
            "display": "Modified subscription",
        }
    )
    """
    Modified subscription

    Modified subscription to a query server.
    """

    n = CodeSystemConcept(
        {
            "code": "N",
            "definition": "New subscription to a query server.",
            "display": "New subscription",
        }
    )
    """
    New subscription

    New subscription to a query server.
    """

    class Meta:
        resource = _resource
