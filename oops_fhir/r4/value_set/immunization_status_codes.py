from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ImmunizationStatusCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationStatusCodes(ValueSet):
    """
    Immunization Status Codes

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the current status of the administered
dose of vaccine.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/immunization-status
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
