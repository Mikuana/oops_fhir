from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.specimen_contained_preference import (
    SpecimenContainedPreference as SpecimenContainedPreference_,
)


__all__ = ["SpecimenContainedPreference"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SpecimenContainedPreference(SpecimenContainedPreference_):
    """
    SpecimenContainedPreference

    Degree of preference of a type of conditioned specimen.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/specimen-contained-preference
    """

    class Meta:
        resource = _resource
