from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_mood import v3ActMood


__all__ = ["v3ActMoodPredicate"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActMoodPredicate(v3ActMood):
    """
    V3 Value SetActMoodPredicate

     Any of the above service moods (e.g., event, intent, or goal) can be
turned into a predicate used as a criterion to express conditionals (or
queries.)  However, currently we allow only criteria on service events.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ActMoodPredicate
    """

    class Meta:
        resource = _resource
