from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["medicationRequestCourseofTherapyCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class medicationRequestCourseofTherapyCodes:
    """
    Medication request  course of  therapy  codes

    MedicationRequest Course of Therapy Codes

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/medicationrequest-course-of-therapy
    """

    continuous = CodeSystemConcept(
        {
            "code": "continuous",
            "definition": "A medication which is expected to be continued beyond the present order and which the patient should be assumed to be taking unless explicitly stopped.",
            "display": "Continuous long term therapy",
        }
    )
    """
    Continuous long term therapy

    A medication which is expected to be continued beyond the present order and which the patient should be assumed to be taking unless explicitly stopped.
    """

    acute = CodeSystemConcept(
        {
            "code": "acute",
            "definition": "A medication which the patient is only expected to consume for the duration of the current order and which is not expected to be renewed.",
            "display": "Short course (acute) therapy",
        }
    )
    """
    Short course (acute) therapy

    A medication which the patient is only expected to consume for the duration of the current order and which is not expected to be renewed.
    """

    seasonal = CodeSystemConcept(
        {
            "code": "seasonal",
            "definition": "A medication which is expected to be used on a part time basis at certain times of the year",
            "display": "Seasonal",
        }
    )
    """
    Seasonal

    A medication which is expected to be used on a part time basis at certain times of the year
    """

    class Meta:
        resource = _resource
