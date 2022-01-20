from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContributorType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContributorType:
    """
    ContributorType

    The type of contributor.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/contributor-type
    """

    author = CodeSystemConcept(
        {
            "code": "author",
            "definition": "An author of the content of the module.",
            "display": "Author",
        }
    )
    """
    Author

    An author of the content of the module.
    """

    editor = CodeSystemConcept(
        {
            "code": "editor",
            "definition": "An editor of the content of the module.",
            "display": "Editor",
        }
    )
    """
    Editor

    An editor of the content of the module.
    """

    reviewer = CodeSystemConcept(
        {
            "code": "reviewer",
            "definition": "A reviewer of the content of the module.",
            "display": "Reviewer",
        }
    )
    """
    Reviewer

    A reviewer of the content of the module.
    """

    endorser = CodeSystemConcept(
        {
            "code": "endorser",
            "definition": "An endorser of the content of the module.",
            "display": "Endorser",
        }
    )
    """
    Endorser

    An endorser of the content of the module.
    """

    class Meta:
        resource = _resource
