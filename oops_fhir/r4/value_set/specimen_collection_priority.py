from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["SpecimenCollectionPriority"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SpecimenCollectionPriority(ValueSet):
    """
    Specimen collection priority

     This example value set defines a set of codes that can be used to
indicate the priority of collection of a specimen.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/specimen-collection-priority
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
