from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["NoteType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class NoteType:
    """
    NoteType

    The presentation types of notes.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/note-type
    """

    display = CodeSystemConcept(
        {"code": "display", "definition": "Display the note.", "display": "Display"}
    )
    """
    Display

    Display the note.
    """

    print_ = CodeSystemConcept(
        {
            "code": "print",
            "definition": "Print the note on the form.",
            "display": "Print (Form)",
        }
    )
    """
    Print (Form)

    Print the note on the form.
    """

    printoper = CodeSystemConcept(
        {
            "code": "printoper",
            "definition": "Print the note for the operator.",
            "display": "Print (Operator)",
        }
    )
    """
    Print (Operator)

    Print the note for the operator.
    """

    class Meta:
        resource = _resource
