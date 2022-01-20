from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ImmunizationFundingSource"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationFundingSource:
    """
    Immunization Funding Source

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the source of the vaccine administered.
This value set is provided as a suggestive example.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/immunization-funding-source
    """

    private = CodeSystemConcept(
        {
            "code": "private",
            "definition": "The vaccine was purchased with private funds.",
            "display": "Private",
        }
    )
    """
    Private

    The vaccine was purchased with private funds.
    """

    public = CodeSystemConcept(
        {
            "code": "public",
            "definition": "The vaccine was purchased with public funds.",
            "display": "Public",
        }
    )
    """
    Public

    The vaccine was purchased with public funds.
    """

    class Meta:
        resource = _resource
