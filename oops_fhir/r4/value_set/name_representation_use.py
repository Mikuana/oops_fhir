from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["NameRepresentationUse"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class NameRepresentationUse(ValueSet):
    """
    NameRepresentationUse

    A set of codes for each different representation of a name.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/name-v3-representation
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
