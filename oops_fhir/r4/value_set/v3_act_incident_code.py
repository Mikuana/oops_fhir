from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_code import v3ActCode


__all__ = ["v3ActIncidentCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActIncidentCode(v3ActCode):
    """
    V3 Value SetActIncidentCode

     Set of codes indicating the type of incident or accident.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ActIncidentCode
    """

    class Meta:
        resource = _resource
