from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["CarePlanIntent"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CarePlanIntent(ValueSet):
    """
    Care Plan Intent

    Codes indicating the degree of authority/intentionality associated with
a care plan.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/care-plan-intent
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
