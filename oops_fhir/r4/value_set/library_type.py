from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.library_type import LibraryType as LibraryType_


__all__ = ["LibraryType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class LibraryType(LibraryType_):
    """
    LibraryType

    The type of knowledge asset this library contains.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/library-type
    """

    class Meta:
        resource = _resource
