from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.medication_administration_status_codes import (
    MedicationAdministrationStatusCodes as MedicationAdministrationStatusCodes_,
)


__all__ = ["MedicationAdministrationStatusCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MedicationAdministrationStatusCodes(MedicationAdministrationStatusCodes_):
    """
    Medication administration  status  codes

    MedicationAdministration Status Codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/medication-admin-status
    """

    class Meta:
        resource = _resource
