from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.immunization_subpotent_reason import (
    ImmunizationSubpotentReason as ImmunizationSubpotentReason_,
)


__all__ = ["ImmunizationSubpotentReason"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationSubpotentReason(ImmunizationSubpotentReason_):
    """
    Immunization Subpotent Reason

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the reason why a dose is considered to be
subpotent. This value set is provided as a suggestive example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/immunization-subpotent-reason
    """

    class Meta:
        resource = _resource
