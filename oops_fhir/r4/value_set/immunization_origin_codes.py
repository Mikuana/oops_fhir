from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ImmunizationOriginCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationOriginCodes(ValueSet):
    """
    Immunization Origin Codes

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the source of the data when the report of
the immunization event is not based on information from the person,
entity or organization who administered the vaccine. This value set is
provided as a suggestive example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/immunization-origin
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
