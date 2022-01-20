from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["RequestResourceType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class RequestResourceType:
    """
    RequestResourceType

    A list of all the request resource types defined in this version of the
FHIR specification.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/request-resource-types
    """

    appointment = CodeSystemConcept(
        {
            "code": "Appointment",
            "definition": "A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s).",
            "display": "Appointment",
        }
    )
    """
    Appointment

    A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s).
    """

    appointment_response = CodeSystemConcept(
        {
            "code": "AppointmentResponse",
            "definition": "A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection.",
            "display": "AppointmentResponse",
        }
    )
    """
    AppointmentResponse

    A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection.
    """

    care_plan = CodeSystemConcept(
        {
            "code": "CarePlan",
            "definition": "Healthcare plan for patient or group.",
            "display": "CarePlan",
        }
    )
    """
    CarePlan

    Healthcare plan for patient or group.
    """

    claim = CodeSystemConcept(
        {
            "code": "Claim",
            "definition": "Claim, Pre-determination or Pre-authorization.",
            "display": "Claim",
        }
    )
    """
    Claim

    Claim, Pre-determination or Pre-authorization.
    """

    communication_request = CodeSystemConcept(
        {
            "code": "CommunicationRequest",
            "definition": "A request for information to be sent to a receiver.",
            "display": "CommunicationRequest",
        }
    )
    """
    CommunicationRequest

    A request for information to be sent to a receiver.
    """

    contract = CodeSystemConcept(
        {"code": "Contract", "definition": "Legal Agreement.", "display": "Contract"}
    )
    """
    Contract

    Legal Agreement.
    """

    device_request = CodeSystemConcept(
        {
            "code": "DeviceRequest",
            "definition": "Medical device request.",
            "display": "DeviceRequest",
        }
    )
    """
    DeviceRequest

    Medical device request.
    """

    enrollment_request = CodeSystemConcept(
        {
            "code": "EnrollmentRequest",
            "definition": "Enrollment request.",
            "display": "EnrollmentRequest",
        }
    )
    """
    EnrollmentRequest

    Enrollment request.
    """

    immunization_recommendation = CodeSystemConcept(
        {
            "code": "ImmunizationRecommendation",
            "definition": "Guidance or advice relating to an immunization.",
            "display": "ImmunizationRecommendation",
        }
    )
    """
    ImmunizationRecommendation

    Guidance or advice relating to an immunization.
    """

    medication_request = CodeSystemConcept(
        {
            "code": "MedicationRequest",
            "definition": "Ordering of medication for patient or group.",
            "display": "MedicationRequest",
        }
    )
    """
    MedicationRequest

    Ordering of medication for patient or group.
    """

    nutrition_order = CodeSystemConcept(
        {
            "code": "NutritionOrder",
            "definition": "Diet, formula or nutritional supplement request.",
            "display": "NutritionOrder",
        }
    )
    """
    NutritionOrder

    Diet, formula or nutritional supplement request.
    """

    service_request = CodeSystemConcept(
        {
            "code": "ServiceRequest",
            "definition": "A record of a request for service such as diagnostic investigations, treatments, or operations to be performed.",
            "display": "ServiceRequest",
        }
    )
    """
    ServiceRequest

    A record of a request for service such as diagnostic investigations, treatments, or operations to be performed.
    """

    supply_request = CodeSystemConcept(
        {
            "code": "SupplyRequest",
            "definition": "Request for a medication, substance or device.",
            "display": "SupplyRequest",
        }
    )
    """
    SupplyRequest

    Request for a medication, substance or device.
    """

    task = CodeSystemConcept(
        {"code": "Task", "definition": "A task to be performed.", "display": "Task"}
    )
    """
    Task

    A task to be performed.
    """

    vision_prescription = CodeSystemConcept(
        {
            "code": "VisionPrescription",
            "definition": "Prescription for vision correction products for a patient.",
            "display": "VisionPrescription",
        }
    )
    """
    VisionPrescription

    Prescription for vision correction products for a patient.
    """

    class Meta:
        resource = _resource
