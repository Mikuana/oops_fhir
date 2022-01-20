from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.family_history_status import (
    FamilyHistoryStatus as FamilyHistoryStatus_,
)


__all__ = ["FamilyHistoryStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FamilyHistoryStatus(FamilyHistoryStatus_):
    """
    FamilyHistoryStatus

    A code that identifies the status of the family history record.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/history-status
    """

    class Meta:
        resource = _resource
