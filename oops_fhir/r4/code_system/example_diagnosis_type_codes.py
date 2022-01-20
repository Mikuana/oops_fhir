from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExampleDiagnosisTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExampleDiagnosisTypeCodes:
    """
    Example Diagnosis Type Codes

    This value set includes example Diagnosis Type codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/ex-diagnosistype
    """

    admitting = CodeSystemConcept(
        {
            "code": "admitting",
            "definition": "The diagnosis given as the reason why the patient was admitted to the hospital.",
            "display": "Admitting Diagnosis",
        }
    )
    """
    Admitting Diagnosis

    The diagnosis given as the reason why the patient was admitted to the hospital.
    """

    clinical = CodeSystemConcept(
        {
            "code": "clinical",
            "definition": "A diagnosis made on the basis of medical signs and patient-reported symptoms, rather than diagnostic tests.",
            "display": "Clinical Diagnosis",
        }
    )
    """
    Clinical Diagnosis

    A diagnosis made on the basis of medical signs and patient-reported symptoms, rather than diagnostic tests.
    """

    differential = CodeSystemConcept(
        {
            "code": "differential",
            "definition": "One of a set of the possible diagnoses that could be connected to the signs, symptoms, and lab findings.",
            "display": "Differential Diagnosis",
        }
    )
    """
    Differential Diagnosis

    One of a set of the possible diagnoses that could be connected to the signs, symptoms, and lab findings.
    """

    discharge = CodeSystemConcept(
        {
            "code": "discharge",
            "definition": "The diagnosis given when the patient is discharged from the hospital.",
            "display": "Discharge Diagnosis",
        }
    )
    """
    Discharge Diagnosis

    The diagnosis given when the patient is discharged from the hospital.
    """

    laboratory = CodeSystemConcept(
        {
            "code": "laboratory",
            "definition": "A diagnosis based significantly on laboratory reports or test results, rather than the physical examination of the patient.",
            "display": "Laboratory Diagnosis",
        }
    )
    """
    Laboratory Diagnosis

    A diagnosis based significantly on laboratory reports or test results, rather than the physical examination of the patient.
    """

    nursing = CodeSystemConcept(
        {
            "code": "nursing",
            "definition": "A diagnosis which identifies people's responses to situations in their lives, such as a readiness to change or a willingness to accept assistance.",
            "display": "Nursing Diagnosis",
        }
    )
    """
    Nursing Diagnosis

    A diagnosis which identifies people's responses to situations in their lives, such as a readiness to change or a willingness to accept assistance.
    """

    prenatal = CodeSystemConcept(
        {
            "code": "prenatal",
            "definition": "A diagnosis determined prior to birth.",
            "display": "Prenatal Diagnosis",
        }
    )
    """
    Prenatal Diagnosis

    A diagnosis determined prior to birth.
    """

    principal = CodeSystemConcept(
        {
            "code": "principal",
            "definition": "The single medical diagnosis that is most relevant to the patient's chief complaint or need for treatment.",
            "display": "Principal Diagnosis",
        }
    )
    """
    Principal Diagnosis

    The single medical diagnosis that is most relevant to the patient's chief complaint or need for treatment.
    """

    radiology = CodeSystemConcept(
        {
            "code": "radiology",
            "definition": "A diagnosis based primarily on the results from medical imaging studies.",
            "display": "Radiology Diagnosis",
        }
    )
    """
    Radiology Diagnosis

    A diagnosis based primarily on the results from medical imaging studies.
    """

    remote = CodeSystemConcept(
        {
            "code": "remote",
            "definition": "A diagnosis determined using telemedicine techniques.",
            "display": "Remote Diagnosis",
        }
    )
    """
    Remote Diagnosis

    A diagnosis determined using telemedicine techniques.
    """

    retrospective = CodeSystemConcept(
        {
            "code": "retrospective",
            "definition": "The labeling of an illness in a specific historical event using modern knowledge, methods and disease classifications.",
            "display": "Retrospective Diagnosis",
        }
    )
    """
    Retrospective Diagnosis

    The labeling of an illness in a specific historical event using modern knowledge, methods and disease classifications.
    """

    self = CodeSystemConcept(
        {
            "code": "self",
            "definition": "A diagnosis determined by the patient.",
            "display": "Self Diagnosis",
        }
    )
    """
    Self Diagnosis

    A diagnosis determined by the patient.
    """

    class Meta:
        resource = _resource
