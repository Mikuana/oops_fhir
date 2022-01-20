from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CodeSystemHierarchyMeaning"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CodeSystemHierarchyMeaning:
    """
    CodeSystemHierarchyMeaning

    The meaning of the hierarchy of concepts in a code system.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/codesystem-hierarchy-meaning
    """

    grouped_by = CodeSystemConcept(
        {
            "code": "grouped-by",
            "definition": "No particular relationship between the concepts can be assumed, except what can be determined by inspection of the definitions of the elements (possible reasons to use this: importing from a source where this is not defined, or where various parts of the hierarchy have different meanings).",
            "display": "Grouped By",
        }
    )
    """
    Grouped By

    No particular relationship between the concepts can be assumed, except what can be determined by inspection of the definitions of the elements (possible reasons to use this: importing from a source where this is not defined, or where various parts of the hierarchy have different meanings).
    """

    is_a = CodeSystemConcept(
        {
            "code": "is-a",
            "definition": "A hierarchy where the child concepts have an IS-A relationship with the parents - that is, all the properties of the parent are also true for its child concepts. Not that is-a is a property of the concepts, so additional subsumption relationships may be defined using properties or the [subsumes](extension-codesystem-subsumes.html) extension.",
            "display": "Is-A",
        }
    )
    """
    Is-A

    A hierarchy where the child concepts have an IS-A relationship with the parents - that is, all the properties of the parent are also true for its child concepts. Not that is-a is a property of the concepts, so additional subsumption relationships may be defined using properties or the [subsumes](extension-codesystem-subsumes.html) extension.
    """

    part_of = CodeSystemConcept(
        {
            "code": "part-of",
            "definition": "Child elements list the individual parts of a composite whole (e.g. body site).",
            "display": "Part Of",
        }
    )
    """
    Part Of

    Child elements list the individual parts of a composite whole (e.g. body site).
    """

    classified_with = CodeSystemConcept(
        {
            "code": "classified-with",
            "definition": 'Child concepts in the hierarchy may have only one parent, and there is a presumption that the code system is a "closed world" meaning all things must be in the hierarchy. This results in concepts such as "not otherwise classified.".',
            "display": "Classified With",
        }
    )
    """
    Classified With

    Child concepts in the hierarchy may have only one parent, and there is a presumption that the code system is a "closed world" meaning all things must be in the hierarchy. This results in concepts such as "not otherwise classified.".
    """

    class Meta:
        resource = _resource
