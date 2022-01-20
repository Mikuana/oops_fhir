from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ImmunizationReasonCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationReasonCodes(ValueSet):
    """
    Immunization Reason Codes

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the reason why a dose of vaccine was
administered. This value set is provided as a suggestive example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/immunization-reason
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
