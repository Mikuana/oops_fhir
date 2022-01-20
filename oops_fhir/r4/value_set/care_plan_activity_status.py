from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.care_plan_activity_status import (
    CarePlanActivityStatus as CarePlanActivityStatus_,
)


__all__ = ["CarePlanActivityStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CarePlanActivityStatus(CarePlanActivityStatus_):
    """
    CarePlanActivityStatus

    Codes that reflect the current state of a care plan activity within its
overall life cycle.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/care-plan-activity-status
    """

    class Meta:
        resource = _resource
