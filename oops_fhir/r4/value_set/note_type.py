from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.note_type import NoteType as NoteType_


__all__ = ["NoteType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class NoteType(NoteType_):
    """
    NoteType

    The presentation types of notes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/note-type
    """

    class Meta:
        resource = _resource
