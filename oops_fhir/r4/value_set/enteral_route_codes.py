from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["EnteralRouteCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EnteralRouteCodes(ValueSet):
    """
    Enteral Route Codes

    EnteralRouteOfAdministration: Codes specifying the route of
administration of enteral formula.  This value set is composed of HL7 V3
codes and is provided as a suggestive example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/enteral-route
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
