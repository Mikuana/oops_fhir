from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.medication_request_intent import (
    medicationRequestIntent as medicationRequestIntent_,
)


__all__ = ["medicationRequestIntent"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class medicationRequestIntent(medicationRequestIntent_):
    """
    Medication request  intent

    MedicationRequest Intent Codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/medicationrequest-intent
    """

    class Meta:
        resource = _resource
