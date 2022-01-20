from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.practitioner_role import (
    PractitionerRole as PractitionerRole_,
)

from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["PractitionerRole"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class PractitionerRole(ValueSet):
    """
    Practitioner role

    This example value set defines a set of codes that can be used to
indicate the role of a Practitioner.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/practitioner-role
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
