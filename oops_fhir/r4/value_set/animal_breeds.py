from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["AnimalBreeds"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AnimalBreeds(ValueSet):
    """
    Animal breeds

    This example value set defines a set of codes that can be used to
indicate breeds of species.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/animal-breeds
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
