from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.medicationrequest_status import (
    medicationrequestStatus as medicationrequestStatus_,
)


__all__ = ["medicationrequestStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class medicationrequestStatus(medicationrequestStatus_):
    """
    Medicationrequest  status

    MedicationRequest Status Codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/medicationrequest-status
    """

    class Meta:
        resource = _resource
