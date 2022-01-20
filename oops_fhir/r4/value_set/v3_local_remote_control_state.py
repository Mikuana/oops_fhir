from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_local_remote_control_state import (
    v3LocalRemoteControlState as v3LocalRemoteControlState_,
)


__all__ = ["v3LocalRemoteControlState"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3LocalRemoteControlState(v3LocalRemoteControlState_):
    """
    v3 Code System LocalRemoteControlState

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-LocalRemoteControlState
    """

    class Meta:
        resource = _resource
