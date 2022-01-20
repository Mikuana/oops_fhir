from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["SpecimenCollection"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SpecimenCollection(ValueSet):
    """
    Specimen collection methods

    Actions that can be taken for the collection of specimen from a subject.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/specimen-collection
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
