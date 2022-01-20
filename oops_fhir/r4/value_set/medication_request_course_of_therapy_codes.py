from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.medication_request_course_of_therapy_codes import (
    medicationRequestCourseofTherapyCodes as medicationRequestCourseofTherapyCodes_,
)


__all__ = ["medicationRequestCourseofTherapyCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class medicationRequestCourseofTherapyCodes(medicationRequestCourseofTherapyCodes_):
    """
    Medication request  course of  therapy  codes

    MedicationRequest Course of Therapy Codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/medicationrequest-course-of-therapy
    """

    class Meta:
        resource = _resource
