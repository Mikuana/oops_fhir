from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.medication_request_status_reason_codes import (
    medicationRequestStatusReasonCodes as medicationRequestStatusReasonCodes_,
)


__all__ = ["medicationRequestStatusReasonCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class medicationRequestStatusReasonCodes(medicationRequestStatusReasonCodes_):
    """
    Medication request  status  reason  codes

    MedicationRequest Status Reason Codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/medicationrequest-status-reason
    """

    class Meta:
        resource = _resource
