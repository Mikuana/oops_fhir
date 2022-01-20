from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DefinitionStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DefinitionStatus:
    """
    DefinitionStatus

    Codes identifying the lifecycle stage of a definition.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/definition-status
    """

    draft = CodeSystemConcept(
        {
            "code": "draft",
            "definition": 'The definition is in the design stage and is not yet considered to be "ready for use".',
            "display": "Draft",
        }
    )
    """
    Draft

    The definition is in the design stage and is not yet considered to be "ready for use".
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "The definition is considered ready for use.",
            "display": "Active",
        }
    )
    """
    Active

    The definition is considered ready for use.
    """

    withdrawn = CodeSystemConcept(
        {
            "code": "withdrawn",
            "definition": "The definition should no longer be used.",
            "display": "Withdrawn",
        }
    )
    """
    Withdrawn

    The definition should no longer be used.
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": 'The authoring/source system does not know which of the status values currently applies for this resource.  Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply,  but the authoring/source system does not know which.',
            "display": "Unknown",
        }
    )
    """
    Unknown

    The authoring/source system does not know which of the status values currently applies for this resource.  Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply,  but the authoring/source system does not know which.
    """

    class Meta:
        resource = _resource
