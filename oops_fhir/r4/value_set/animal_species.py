from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["AnimalSpecies"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AnimalSpecies(ValueSet):
    """
    Animal species

    This example value set defines a set of codes that can be used to
indicate species of animal patients.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/animal-species
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
