from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.identity_assurance_level import (
    IdentityAssuranceLevel as IdentityAssuranceLevel_,
)


__all__ = ["IdentityAssuranceLevel"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class IdentityAssuranceLevel(IdentityAssuranceLevel_):
    """
    IdentityAssuranceLevel

    The level of confidence that this link represents the same actual
person, based on NIST Authentication Levels.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/identity-assuranceLevel
    """

    class Meta:
        resource = _resource
