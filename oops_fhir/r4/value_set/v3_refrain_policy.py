from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_code import v3ActCode


__all__ = ["v3RefrainPolicy"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3RefrainPolicy(v3ActCode):
    """
    V3 Value SetRefrainPolicy

     Conveys prohibited actions which an information custodian, receiver, or
user is not permitted to perform unless otherwise authorized or
permitted under specified circumstances.  Examples:    prohibit
redisclosure without consent directive

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-RefrainPolicy
    """

    class Meta:
        resource = _resource
