from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["CarePlanActivityKind"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CarePlanActivityKind(ValueSet):
    """
    Care Plan Activity Kind

    Resource types defined as part of FHIR that can be represented as in-
line definitions of a care plan activity.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/care-plan-activity-kind
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
