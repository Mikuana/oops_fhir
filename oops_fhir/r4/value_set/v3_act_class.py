from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_class import v3ActClass as v3ActClass_


__all__ = ["v3ActClass"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActClass(v3ActClass_):
    """
    v3 Code System ActClass

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ActClass
    """

    class Meta:
        resource = _resource
