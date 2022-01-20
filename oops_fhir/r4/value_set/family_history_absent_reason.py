from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.family_history_absent_reason import (
    FamilyHistoryAbsentReason as FamilyHistoryAbsentReason_,
)


__all__ = ["FamilyHistoryAbsentReason"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FamilyHistoryAbsentReason(FamilyHistoryAbsentReason_):
    """
    FamilyHistoryAbsentReason

    Codes describing the reason why a family member's history is not
available.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/history-absent-reason
    """

    class Meta:
        resource = _resource
