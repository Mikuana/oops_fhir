from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_role_link_type import v3RoleLinkType as v3RoleLinkType_


__all__ = ["v3RoleLinkType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3RoleLinkType(v3RoleLinkType_):
    """
    v3 Code System RoleLinkType

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-RoleLinkType
    """

    class Meta:
        resource = _resource
