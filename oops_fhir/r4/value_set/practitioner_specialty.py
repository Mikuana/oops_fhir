from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.practitioner_specialty import (
    PractitionerSpecialty as PractitionerSpecialty_,
)


__all__ = ["PractitionerSpecialty"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class PractitionerSpecialty(PractitionerSpecialty_):
    """
    Practitioner specialty

    This example value set defines a set of codes that can be used to
indicate the specialty of a Practitioner.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/practitioner-specialty
    """

    class Meta:
        resource = _resource
