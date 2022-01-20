from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["CarePlanActivityOutcome"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CarePlanActivityOutcome(SNOMEDCT):
    """
    Care Plan Activity Outcome

    Example codes indicating the outcome of a care plan activity. Note that
these are in no way complete and might not even be appropriate for some
uses.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/care-plan-activity-outcome
    """

    class Meta:
        resource = _resource
