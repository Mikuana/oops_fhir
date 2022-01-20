from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_route_of_administration import (
    v3RouteOfAdministration as v3RouteOfAdministration_,
)


__all__ = ["v3RouteOfAdministration"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3RouteOfAdministration(v3RouteOfAdministration_):
    """
    v3 Code System RouteOfAdministration

     The path the administered medication takes to get into the body or into
contact with the body.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-RouteOfAdministration
    """

    class Meta:
        resource = _resource
