from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.immunization_funding_source import (
    ImmunizationFundingSource as ImmunizationFundingSource_,
)


__all__ = ["ImmunizationFundingSource"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationFundingSource(ImmunizationFundingSource_):
    """
    Immunization Funding Source

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the source of the vaccine administered.
This value set is provided as a suggestive example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/immunization-funding-source
    """

    class Meta:
        resource = _resource
