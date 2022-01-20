from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.rejection_criterion import (
    RejectionCriterion as RejectionCriterion_,
)


__all__ = ["RejectionCriterion"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class RejectionCriterion(RejectionCriterion_):
    """
    RejectionCriterion

    Criterion for rejection of the specimen by laboratory.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/rejection-criteria
    """

    class Meta:
        resource = _resource
