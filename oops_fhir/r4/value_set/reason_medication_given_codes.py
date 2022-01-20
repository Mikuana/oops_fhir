from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.reason_medication_given_codes import (
    ReasonMedicationGivenCodes as ReasonMedicationGivenCodes_,
)


__all__ = ["ReasonMedicationGivenCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ReasonMedicationGivenCodes(ReasonMedicationGivenCodes_):
    """
    Reason Medication Given Codes

    This value set is provided as an example. The value set to instantiate
this attribute should be drawn from a robust terminology code system
that consists of or contains concepts to support the medication process.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/reason-medication-given-codes
    """

    class Meta:
        resource = _resource
