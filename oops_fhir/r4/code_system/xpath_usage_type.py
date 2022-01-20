from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["XPathUsageType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class XPathUsageType:
    """
    XPathUsageType

    How a search parameter relates to the set of elements returned by
evaluating its xpath query.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/search-xpath-usage
    """

    normal = CodeSystemConcept(
        {
            "code": "normal",
            "definition": "The search parameter is derived directly from the selected nodes based on the type definitions.",
            "display": "Normal",
        }
    )
    """
    Normal

    The search parameter is derived directly from the selected nodes based on the type definitions.
    """

    phonetic = CodeSystemConcept(
        {
            "code": "phonetic",
            "definition": "The search parameter is derived by a phonetic transform from the selected nodes.",
            "display": "Phonetic",
        }
    )
    """
    Phonetic

    The search parameter is derived by a phonetic transform from the selected nodes.
    """

    nearby = CodeSystemConcept(
        {
            "code": "nearby",
            "definition": "The search parameter is based on a spatial transform of the selected nodes.",
            "display": "Nearby",
        }
    )
    """
    Nearby

    The search parameter is based on a spatial transform of the selected nodes.
    """

    distance = CodeSystemConcept(
        {
            "code": "distance",
            "definition": "The search parameter is based on a spatial transform of the selected nodes, using physical distance from the middle.",
            "display": "Distance",
        }
    )
    """
    Distance

    The search parameter is based on a spatial transform of the selected nodes, using physical distance from the middle.
    """

    other = CodeSystemConcept(
        {
            "code": "other",
            "definition": "The interpretation of the xpath statement is unknown (and can't be automated).",
            "display": "Other",
        }
    )
    """
    Other

    The interpretation of the xpath statement is unknown (and can't be automated).
    """

    class Meta:
        resource = _resource
