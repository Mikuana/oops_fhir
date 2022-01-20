from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CommonTags"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CommonTags:
    """
    Common Tags

    Common Tag Codes defined by FHIR project

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/common-tags
    """

    actionable = CodeSystemConcept(
        {
            "code": "actionable",
            "definition": "This request is intended to be acted upon, not merely stored",
            "display": "Actionable",
        }
    )
    """
    Actionable

    This request is intended to be acted upon, not merely stored
    """

    class Meta:
        resource = _resource
