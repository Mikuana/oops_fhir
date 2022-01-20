from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.patient_medicine_change_types import (
    PatientMedicineChangeTypes as PatientMedicineChangeTypes_,
)


__all__ = ["PatientMedicineChangeTypes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class PatientMedicineChangeTypes(PatientMedicineChangeTypes_):
    """
    Patient Medicine Change Types

    Example Item Flags for the List Resource. In this case, these are the
kind of flags that would be used on a medication list at the end of a
consultation.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/list-item-flag
    """

    class Meta:
        resource = _resource
