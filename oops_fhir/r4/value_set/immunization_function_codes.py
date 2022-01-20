from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ImmunizationFunctionCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationFunctionCodes(ValueSet):
    """
    Immunization Function Codes

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the function a practitioner or
organization may play in the immunization event. This value set is
provided as a suggestive example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/immunization-function
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
