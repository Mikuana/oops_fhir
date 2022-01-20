from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_role_code import v3RoleCode as v3RoleCode_


__all__ = ["v3RoleCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3RoleCode(v3RoleCode_):
    """
    v3 Code System RoleCode

     A set of codes further specifying the kind of Role; specific
classification codes for further qualifying RoleClass codes.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-RoleCode
    """

    class Meta:
        resource = _resource
