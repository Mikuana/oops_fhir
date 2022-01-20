from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.medication_status_codes import (
    MedicationStatusCodes as MedicationStatusCodes_,
)


__all__ = ["MedicationStatusCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MedicationStatusCodes(MedicationStatusCodes_):
    """
    Medication  status  codes

    Medication Status Codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/medication-status
    """

    class Meta:
        resource = _resource
