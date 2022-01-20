from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.medication_dispense_performer_function_codes import (
    MedicationDispensePerformerFunctionCodes as MedicationDispensePerformerFunctionCodes_,
)


__all__ = ["MedicationDispensePerformerFunctionCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MedicationDispensePerformerFunctionCodes(
    MedicationDispensePerformerFunctionCodes_
):
    """
    Medication dispense  performer  function  codes

    MedicationDispense Performer Function Codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/medicationdispense-performer-function
    """

    class Meta:
        resource = _resource
