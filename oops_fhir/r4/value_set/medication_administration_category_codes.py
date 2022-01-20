from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.medication_administration_category_codes import (
    MedicationAdministrationCategoryCodes as MedicationAdministrationCategoryCodes_,
)


__all__ = ["MedicationAdministrationCategoryCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MedicationAdministrationCategoryCodes(MedicationAdministrationCategoryCodes_):
    """
    Medication administration  category  codes

    MedicationAdministration Category Codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/medication-admin-category
    """

    class Meta:
        resource = _resource
