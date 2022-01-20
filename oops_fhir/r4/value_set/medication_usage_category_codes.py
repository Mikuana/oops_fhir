from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.medication_usage_category_codes import (
    Medicationusagecategorycodes as Medicationusagecategorycodes_,
)


__all__ = ["Medicationusagecategorycodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class Medicationusagecategorycodes(Medicationusagecategorycodes_):
    """
    Medication usage category codes

    Medication Status Codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/medication-statement-category
    """

    class Meta:
        resource = _resource
