from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["CodesForImmunizationSiteOfAdministration"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CodesForImmunizationSiteOfAdministration(ValueSet):
    """
    Codes for Immunization Site of Administration

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the body site where the vaccination
occurred. This value set is provided as a suggestive example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/immunization-site
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
