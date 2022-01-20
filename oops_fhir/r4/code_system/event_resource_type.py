from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["EventResourceType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class EventResourceType:
    """
    EventResourceType

    A list of all the event resource types defined in this version of the
FHIR specification.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/event-resource-types
    """

    charge_item = CodeSystemConcept(
        {
            "code": "ChargeItem",
            "definition": "Item containing charge code(s) associated with the provision of healthcare provider products.",
            "display": "ChargeItem",
        }
    )
    """
    ChargeItem

    Item containing charge code(s) associated with the provision of healthcare provider products.
    """

    claim_response = CodeSystemConcept(
        {
            "code": "ClaimResponse",
            "definition": "Remittance resource.",
            "display": "ClaimResponse",
        }
    )
    """
    ClaimResponse

    Remittance resource.
    """

    clinical_impression = CodeSystemConcept(
        {
            "code": "ClinicalImpression",
            "definition": "A clinical assessment performed when planning treatments and management strategies for a patient.",
            "display": "ClinicalImpression",
        }
    )
    """
    ClinicalImpression

    A clinical assessment performed when planning treatments and management strategies for a patient.
    """

    communication = CodeSystemConcept(
        {
            "code": "Communication",
            "definition": "A record of information transmitted from a sender to a receiver.",
            "display": "Communication",
        }
    )
    """
    Communication

    A record of information transmitted from a sender to a receiver.
    """

    composition = CodeSystemConcept(
        {
            "code": "Composition",
            "definition": "A set of resources composed into a single coherent clinical statement with clinical attestation.",
            "display": "Composition",
        }
    )
    """
    Composition

    A set of resources composed into a single coherent clinical statement with clinical attestation.
    """

    condition = CodeSystemConcept(
        {
            "code": "Condition",
            "definition": "Detailed information about conditions, problems or diagnoses.",
            "display": "Condition",
        }
    )
    """
    Condition

    Detailed information about conditions, problems or diagnoses.
    """

    consent = CodeSystemConcept(
        {
            "code": "Consent",
            "definition": "A healthcare consumer's policy choices to permits or denies recipients or roles to perform actions for specific purposes and periods of time.",
            "display": "Consent",
        }
    )
    """
    Consent

    A healthcare consumer's policy choices to permits or denies recipients or roles to perform actions for specific purposes and periods of time.
    """

    coverage = CodeSystemConcept(
        {
            "code": "Coverage",
            "definition": "Insurance or medical plan or a payment agreement.",
            "display": "Coverage",
        }
    )
    """
    Coverage

    Insurance or medical plan or a payment agreement.
    """

    device_use_statement = CodeSystemConcept(
        {
            "code": "DeviceUseStatement",
            "definition": "Record of use of a device.",
            "display": "DeviceUseStatement",
        }
    )
    """
    DeviceUseStatement

    Record of use of a device.
    """

    diagnostic_report = CodeSystemConcept(
        {
            "code": "DiagnosticReport",
            "definition": "A Diagnostic report - a combination of request information, atomic results, images, interpretation, as well as formatted reports.",
            "display": "DiagnosticReport",
        }
    )
    """
    DiagnosticReport

    A Diagnostic report - a combination of request information, atomic results, images, interpretation, as well as formatted reports.
    """

    document_manifest = CodeSystemConcept(
        {
            "code": "DocumentManifest",
            "definition": "A list that defines a set of documents.",
            "display": "DocumentManifest",
        }
    )
    """
    DocumentManifest

    A list that defines a set of documents.
    """

    document_reference = CodeSystemConcept(
        {
            "code": "DocumentReference",
            "definition": "A reference to a document.",
            "display": "DocumentReference",
        }
    )
    """
    DocumentReference

    A reference to a document.
    """

    encounter = CodeSystemConcept(
        {
            "code": "Encounter",
            "definition": "An interaction during which services are provided to the patient.",
            "display": "Encounter",
        }
    )
    """
    Encounter

    An interaction during which services are provided to the patient.
    """

    enrollment_response = CodeSystemConcept(
        {
            "code": "EnrollmentResponse",
            "definition": "EnrollmentResponse resource.",
            "display": "EnrollmentResponse",
        }
    )
    """
    EnrollmentResponse

    EnrollmentResponse resource.
    """

    episode_of_care = CodeSystemConcept(
        {
            "code": "EpisodeOfCare",
            "definition": "An association of a Patient with an Organization and  Healthcare Provider(s) for a period of time that the Organization assumes some level of responsibility.",
            "display": "EpisodeOfCare",
        }
    )
    """
    EpisodeOfCare

    An association of a Patient with an Organization and  Healthcare Provider(s) for a period of time that the Organization assumes some level of responsibility.
    """

    explanation_of_benefit = CodeSystemConcept(
        {
            "code": "ExplanationOfBenefit",
            "definition": "Explanation of Benefit resource.",
            "display": "ExplanationOfBenefit",
        }
    )
    """
    ExplanationOfBenefit

    Explanation of Benefit resource.
    """

    family_member_history = CodeSystemConcept(
        {
            "code": "FamilyMemberHistory",
            "definition": "Information about patient's relatives, relevant for patient.",
            "display": "FamilyMemberHistory",
        }
    )
    """
    FamilyMemberHistory

    Information about patient's relatives, relevant for patient.
    """

    guidance_response = CodeSystemConcept(
        {
            "code": "GuidanceResponse",
            "definition": "The formal response to a guidance request.",
            "display": "GuidanceResponse",
        }
    )
    """
    GuidanceResponse

    The formal response to a guidance request.
    """

    imaging_study = CodeSystemConcept(
        {
            "code": "ImagingStudy",
            "definition": "A set of images produced in single study (one or more series of references images).",
            "display": "ImagingStudy",
        }
    )
    """
    ImagingStudy

    A set of images produced in single study (one or more series of references images).
    """

    immunization = CodeSystemConcept(
        {
            "code": "Immunization",
            "definition": "Immunization event information.",
            "display": "Immunization",
        }
    )
    """
    Immunization

    Immunization event information.
    """

    measure_report = CodeSystemConcept(
        {
            "code": "MeasureReport",
            "definition": "Results of a measure evaluation.",
            "display": "MeasureReport",
        }
    )
    """
    MeasureReport

    Results of a measure evaluation.
    """

    media = CodeSystemConcept(
        {
            "code": "Media",
            "definition": "A photo, video, or audio recording acquired or used in healthcare. The actual content may be inline or provided by direct reference.",
            "display": "Media",
        }
    )
    """
    Media

    A photo, video, or audio recording acquired or used in healthcare. The actual content may be inline or provided by direct reference.
    """

    medication_administration = CodeSystemConcept(
        {
            "code": "MedicationAdministration",
            "definition": "Administration of medication to a patient.",
            "display": "MedicationAdministration",
        }
    )
    """
    MedicationAdministration

    Administration of medication to a patient.
    """

    medication_dispense = CodeSystemConcept(
        {
            "code": "MedicationDispense",
            "definition": "Dispensing a medication to a named patient.",
            "display": "MedicationDispense",
        }
    )
    """
    MedicationDispense

    Dispensing a medication to a named patient.
    """

    medication_statement = CodeSystemConcept(
        {
            "code": "MedicationStatement",
            "definition": "Record of medication being taken by a patient.",
            "display": "MedicationStatement",
        }
    )
    """
    MedicationStatement

    Record of medication being taken by a patient.
    """

    observation = CodeSystemConcept(
        {
            "code": "Observation",
            "definition": "Measurements and simple assertions.",
            "display": "Observation",
        }
    )
    """
    Observation

    Measurements and simple assertions.
    """

    payment_notice = CodeSystemConcept(
        {
            "code": "PaymentNotice",
            "definition": "PaymentNotice request.",
            "display": "PaymentNotice",
        }
    )
    """
    PaymentNotice

    PaymentNotice request.
    """

    payment_reconciliation = CodeSystemConcept(
        {
            "code": "PaymentReconciliation",
            "definition": "PaymentReconciliation resource.",
            "display": "PaymentReconciliation",
        }
    )
    """
    PaymentReconciliation

    PaymentReconciliation resource.
    """

    procedure = CodeSystemConcept(
        {
            "code": "Procedure",
            "definition": "An action that is being or was performed on a patient.",
            "display": "Procedure",
        }
    )
    """
    Procedure

    An action that is being or was performed on a patient.
    """

    process_response = CodeSystemConcept(
        {
            "code": "ProcessResponse",
            "definition": "ProcessResponse resource.",
            "display": "ProcessResponse",
        }
    )
    """
    ProcessResponse

    ProcessResponse resource.
    """

    questionnaire_response = CodeSystemConcept(
        {
            "code": "QuestionnaireResponse",
            "definition": "A structured set of questions and their answers.",
            "display": "QuestionnaireResponse",
        }
    )
    """
    QuestionnaireResponse

    A structured set of questions and their answers.
    """

    risk_assessment = CodeSystemConcept(
        {
            "code": "RiskAssessment",
            "definition": "Potential outcomes for a subject with likelihood.",
            "display": "RiskAssessment",
        }
    )
    """
    RiskAssessment

    Potential outcomes for a subject with likelihood.
    """

    supply_delivery = CodeSystemConcept(
        {
            "code": "SupplyDelivery",
            "definition": "Delivery of bulk Supplies.",
            "display": "SupplyDelivery",
        }
    )
    """
    SupplyDelivery

    Delivery of bulk Supplies.
    """

    task = CodeSystemConcept(
        {"code": "Task", "definition": "A task to be performed.", "display": "Task"}
    )
    """
    Task

    A task to be performed.
    """

    class Meta:
        resource = _resource
