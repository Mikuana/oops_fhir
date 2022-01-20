from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_role_status import v3RoleStatus as v3RoleStatus_


__all__ = ["v3RoleStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3RoleStatus(v3RoleStatus_):
    """
    v3 Code System RoleStatus

     Codes representing the defined possible states of an Role, as defined
by the Role class state machine.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-RoleStatus
    """

    class Meta:
        resource = _resource
