from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_mood import v3ActMood


__all__ = ["v3ActMoodIntent"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActMoodIntent(v3ActMood):
    """
    V3 Value SetActMoodIntent

     An intention or plan to perform a service. Historical note: in previous
RIM versions, the intent mood was captured as a separate class
hierarchy, called Service_intent_or_order.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ActMoodIntent
    """

    class Meta:
        resource = _resource
