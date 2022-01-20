from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_role_link_status import (
    v3RoleLinkStatus as v3RoleLinkStatus_,
)


__all__ = ["v3RoleLinkStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3RoleLinkStatus(v3RoleLinkStatus_):
    """
    v3 Code System RoleLinkStatus

      Description:  Codes representing possible states of a RoleLink, as
defined by the RoleLink class state machine.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-RoleLinkStatus
    """

    class Meta:
        resource = _resource
