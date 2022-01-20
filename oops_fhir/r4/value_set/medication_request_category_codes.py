from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.medication_request_category_codes import (
    medicationRequestCategoryCodes as medicationRequestCategoryCodes_,
)


__all__ = ["medicationRequestCategoryCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class medicationRequestCategoryCodes(medicationRequestCategoryCodes_):
    """
    Medication request  category  codes

    MedicationRequest Category Codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/medicationrequest-category
    """

    class Meta:
        resource = _resource
