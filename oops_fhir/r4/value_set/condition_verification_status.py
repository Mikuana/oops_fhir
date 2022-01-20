from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.condition_verification_status import (
    ConditionVerificationStatus as ConditionVerificationStatus_,
)


__all__ = ["ConditionVerificationStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConditionVerificationStatus(ConditionVerificationStatus_):
    """
    ConditionVerificationStatus

    The verification status to support or decline the clinical status of the
condition or diagnosis.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/condition-ver-status
    """

    class Meta:
        resource = _resource
