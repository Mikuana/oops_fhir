from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DocumentReferenceStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DocumentReferenceStatus:
    """
    DocumentReferenceStatus

    The status of the document reference.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/document-reference-status
    """

    current = CodeSystemConcept(
        {
            "code": "current",
            "definition": "This is the current reference for this document.",
            "display": "Current",
        }
    )
    """
    Current

    This is the current reference for this document.
    """

    superseded = CodeSystemConcept(
        {
            "code": "superseded",
            "definition": "This reference has been superseded by another reference.",
            "display": "Superseded",
        }
    )
    """
    Superseded

    This reference has been superseded by another reference.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "This reference was created in error.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    This reference was created in error.
    """

    class Meta:
        resource = _resource
