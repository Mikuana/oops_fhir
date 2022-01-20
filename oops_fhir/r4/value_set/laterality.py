from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["Laterality"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class Laterality(ValueSet):
    """
    Laterality

    Laterality: SNOMED-CT concepts for 'left', 'right', and 'bilateral'

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/bodysite-laterality
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
