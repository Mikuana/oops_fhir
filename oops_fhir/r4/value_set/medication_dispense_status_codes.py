from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.medication_dispense_status_codes import (
    MedicationDispenseStatusCodes as MedicationDispenseStatusCodes_,
)


__all__ = ["MedicationDispenseStatusCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MedicationDispenseStatusCodes(MedicationDispenseStatusCodes_):
    """
    Medication dispense  status  codes

    MedicationDispense Status Codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/medicationdispense-status
    """

    class Meta:
        resource = _resource
