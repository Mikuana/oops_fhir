from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_entity_code import v3EntityCode as v3EntityCode_


__all__ = ["v3EntityCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityCode(v3EntityCode_):
    """
    v3 Code System EntityCode

      OpenIssue:  Missing description.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-EntityCode
    """

    class Meta:
        resource = _resource
