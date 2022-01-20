from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["UsageContextType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class UsageContextType:
    """
    UsageContextType

    A code that specifies a type of context being specified by a usage
context.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/usage-context-type
    """

    gender = CodeSystemConcept(
        {
            "code": "gender",
            "definition": "The gender of the patient. For this context type, appropriate values can be found in the http://hl7.org/fhir/ValueSet/administrative-gender value set.",
            "display": "Gender",
        }
    )
    """
    Gender

    The gender of the patient. For this context type, appropriate values can be found in the http://hl7.org/fhir/ValueSet/administrative-gender value set.
    """

    age = CodeSystemConcept(
        {
            "code": "age",
            "definition": "The age of the patient. For this context type, the value could be a range that specifies the applicable ages or a code from an appropriate value set such as the MeSH value set http://terminology.hl7.org/ValueSet/v3-AgeGroupObservationValue.",
            "display": "Age Range",
        }
    )
    """
    Age Range

    The age of the patient. For this context type, the value could be a range that specifies the applicable ages or a code from an appropriate value set such as the MeSH value set http://terminology.hl7.org/ValueSet/v3-AgeGroupObservationValue.
    """

    focus = CodeSystemConcept(
        {
            "code": "focus",
            "definition": "The clinical concept(s) addressed by the artifact. For example, disease, diagnostic test interpretation, medication ordering as in http://hl7.org/fhir/ValueSet/condition-code.",
            "display": "Clinical Focus",
        }
    )
    """
    Clinical Focus

    The clinical concept(s) addressed by the artifact. For example, disease, diagnostic test interpretation, medication ordering as in http://hl7.org/fhir/ValueSet/condition-code.
    """

    user = CodeSystemConcept(
        {
            "code": "user",
            "definition": "The clinical specialty of the context in which the patient is being treated - For example, PCP, Patient, Cardiologist, Behavioral Professional, Oral Health Professional, Prescriber, etc... taken from a specialty value set such as the NUCC Health Care provider taxonomy value set http://hl7.org/fhir/ValueSet/provider-taxonomy.",
            "display": "User Type",
        }
    )
    """
    User Type

    The clinical specialty of the context in which the patient is being treated - For example, PCP, Patient, Cardiologist, Behavioral Professional, Oral Health Professional, Prescriber, etc... taken from a specialty value set such as the NUCC Health Care provider taxonomy value set http://hl7.org/fhir/ValueSet/provider-taxonomy.
    """

    workflow = CodeSystemConcept(
        {
            "code": "workflow",
            "definition": "The settings in which the artifact is intended for use. For example, admission, pre-op, etc. For example, the ActEncounterCode value set http://terminology.hl7.org/ValueSet/v3-ActEncounterCode.",
            "display": "Workflow Setting",
        }
    )
    """
    Workflow Setting

    The settings in which the artifact is intended for use. For example, admission, pre-op, etc. For example, the ActEncounterCode value set http://terminology.hl7.org/ValueSet/v3-ActEncounterCode.
    """

    task = CodeSystemConcept(
        {
            "code": "task",
            "definition": "The context for the clinical task(s) represented by this artifact. For example, this could be any task context represented by the HL7 ActTaskCode value set http://terminology.hl7.org/ValueSet/v3-ActTaskCode. General categories include: order entry, patient documentation and patient information review.",
            "display": "Workflow Task",
        }
    )
    """
    Workflow Task

    The context for the clinical task(s) represented by this artifact. For example, this could be any task context represented by the HL7 ActTaskCode value set http://terminology.hl7.org/ValueSet/v3-ActTaskCode. General categories include: order entry, patient documentation and patient information review.
    """

    venue = CodeSystemConcept(
        {
            "code": "venue",
            "definition": "The venue in which an artifact could be used. For example, Outpatient, Inpatient, Home, Nursing home. The code value may originate from the HL7 ServiceDeliveryLocationRoleType value set (http://terminology.hl7.org/ValueSet/v3-ServiceDeliveryLocationRoleType).",
            "display": "Clinical Venue",
        }
    )
    """
    Clinical Venue

    The venue in which an artifact could be used. For example, Outpatient, Inpatient, Home, Nursing home. The code value may originate from the HL7 ServiceDeliveryLocationRoleType value set (http://terminology.hl7.org/ValueSet/v3-ServiceDeliveryLocationRoleType).
    """

    species = CodeSystemConcept(
        {
            "code": "species",
            "definition": "The species to which an artifact applies. For example, SNOMED - 387961004 | Kingdom Animalia (organism).",
            "display": "Species",
        }
    )
    """
    Species

    The species to which an artifact applies. For example, SNOMED - 387961004 | Kingdom Animalia (organism).
    """

    program = CodeSystemConcept(
        {
            "code": "program",
            "definition": "A program/project of work for which this artifact is applicable.",
            "display": "Program",
        }
    )
    """
    Program

    A program/project of work for which this artifact is applicable.
    """

    class Meta:
        resource = _resource
