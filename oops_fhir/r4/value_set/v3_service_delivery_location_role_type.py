from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_role_code import v3RoleCode


__all__ = ["v3ServiceDeliveryLocationRoleType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ServiceDeliveryLocationRoleType(v3RoleCode):
    """
    V3 Value SetServiceDeliveryLocationRoleType

     A role of a place that further classifies the setting (e.g., accident
site, road side, work site, community location) in which services are
delivered.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ServiceDeliveryLocationRoleType
    """

    class Meta:
        resource = _resource
