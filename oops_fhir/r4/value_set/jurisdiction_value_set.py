from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["JurisdictionValueSet"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class JurisdictionValueSet(ValueSet):
    """
    Jurisdiction

    This value set defines a base set of codes for country, country
subdivision and region    for indicating where a resource is intended to
be used.             Note: The codes for countries and country
subdivisions are taken from    [ISO
3166](https://www.iso.org/iso-3166-country-codes.html)    while the
codes for "supra-national" regions are from    [UN Standard country or
area codes for statistical use
(M49)](http://unstats.un.org/unsd/methods/m49/m49.htm).

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/jurisdiction
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
