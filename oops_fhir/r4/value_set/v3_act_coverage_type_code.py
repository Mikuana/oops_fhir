from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_code import v3ActCode


__all__ = ["v3ActCoverageTypeCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActCoverageTypeCode(v3ActCode):
    """
    V3 Value SetActCoverageTypeCode

      Definition:  Set of codes indicating the type of insurance policy or
program that pays for the cost of benefits provided to covered parties.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ActCoverageTypeCode
    """

    class Meta:
        resource = _resource
