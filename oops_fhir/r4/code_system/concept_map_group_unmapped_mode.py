from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ConceptMapGroupUnmappedMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ConceptMapGroupUnmappedMode:
    """
    ConceptMapGroupUnmappedMode

    Defines which action to take if there is no match in the group.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/conceptmap-unmapped-mode
    """

    provided = CodeSystemConcept(
        {
            "code": "provided",
            "definition": "Use the code as provided in the $translate request.",
            "display": "Provided Code",
        }
    )
    """
    Provided Code

    Use the code as provided in the $translate request.
    """

    fixed = CodeSystemConcept(
        {
            "code": "fixed",
            "definition": "Use the code explicitly provided in the group.unmapped.",
            "display": "Fixed Code",
        }
    )
    """
    Fixed Code

    Use the code explicitly provided in the group.unmapped.
    """

    other_map = CodeSystemConcept(
        {
            "code": "other-map",
            "definition": "Use the map identified by the canonical URL in the url element.",
            "display": "Other Map",
        }
    )
    """
    Other Map

    Use the map identified by the canonical URL in the url element.
    """

    class Meta:
        resource = _resource
