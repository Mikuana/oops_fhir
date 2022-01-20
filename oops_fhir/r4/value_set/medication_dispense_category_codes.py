from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.medication_dispense_category_codes import (
    MedicationDispenseCategoryCodes as MedicationDispenseCategoryCodes_,
)


__all__ = ["MedicationDispenseCategoryCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MedicationDispenseCategoryCodes(MedicationDispenseCategoryCodes_):
    """
    Medication dispense  category  codes

    MedicationDispense Category Codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/medicationdispense-category
    """

    class Meta:
        resource = _resource
