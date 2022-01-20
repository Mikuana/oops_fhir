from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["GoalStartEvent"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class GoalStartEvent(ValueSet):
    """
    Goal start event

    Identifies types of events that might trigger the start of a goal.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/goal-start-event
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
