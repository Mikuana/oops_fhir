from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_status import v3ActStatus as v3ActStatus_


__all__ = ["v3ActStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActStatus(v3ActStatus_):
    """
    v3 Code System ActStatus

     Codes representing the defined possible states of an Act, as defined by
the Act class state machine.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ActStatus
    """

    class Meta:
        resource = _resource
