from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CatalogEntryRelationType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CatalogEntryRelationType:
    """
    CatalogEntryRelationType

    The type of relations between entries.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/relation-type
    """

    triggers = CodeSystemConcept(
        {
            "code": "triggers",
            "definition": "the related entry represents an activity that may be triggered by the current item.",
            "display": "Triggers",
        }
    )
    """
    Triggers

    the related entry represents an activity that may be triggered by the current item.
    """

    is_replaced_by = CodeSystemConcept(
        {
            "code": "is-replaced-by",
            "definition": "the related entry represents an item that replaces the current retired item.",
            "display": "Replaced By",
        }
    )
    """
    Replaced By

    the related entry represents an item that replaces the current retired item.
    """

    class Meta:
        resource = _resource
