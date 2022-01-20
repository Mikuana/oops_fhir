from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["IdentifierTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class IdentifierTypeCodes(ValueSet):
    """
    IdentifierType

    A coded type for an identifier that can be used to determine which
identifier to use for a specific purpose.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/identifier-type
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
