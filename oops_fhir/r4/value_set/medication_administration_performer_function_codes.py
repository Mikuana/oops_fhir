from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.medication_administration_performer_function_codes import (
    MedicationAdministrationPerformerFunctionCodes as MedicationAdministrationPerformerFunctionCodes_,
)


__all__ = ["MedicationAdministrationPerformerFunctionCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MedicationAdministrationPerformerFunctionCodes(
    MedicationAdministrationPerformerFunctionCodes_
):
    """
    Medication administration  performer  function  codes

    MedicationAdministration Performer Function Codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/med-admin-perform-function
    """

    class Meta:
        resource = _resource
