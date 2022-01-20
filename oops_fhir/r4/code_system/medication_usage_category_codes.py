from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["Medicationusagecategorycodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class Medicationusagecategorycodes:
    """
    Medication usage category codes

    Medication Status Codes

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/medication-statement-category
    """

    inpatient = CodeSystemConcept(
        {
            "code": "inpatient",
            "definition": "Includes orders for medications to be administered or consumed in an inpatient or acute care setting",
            "display": "Inpatient",
        }
    )
    """
    Inpatient

    Includes orders for medications to be administered or consumed in an inpatient or acute care setting
    """

    outpatient = CodeSystemConcept(
        {
            "code": "outpatient",
            "definition": "Includes orders for medications to be administered or consumed in an outpatient setting (for example, Emergency Department, Outpatient Clinic, Outpatient Surgery, Doctor's office)",
            "display": "Outpatient",
        }
    )
    """
    Outpatient

    Includes orders for medications to be administered or consumed in an outpatient setting (for example, Emergency Department, Outpatient Clinic, Outpatient Surgery, Doctor's office)
    """

    community = CodeSystemConcept(
        {
            "code": "community",
            "definition": "Includes orders for medications to be administered or consumed by the patient in their home (this would include long term care or nursing homes, hospices, etc.).",
            "display": "Community",
        }
    )
    """
    Community

    Includes orders for medications to be administered or consumed by the patient in their home (this would include long term care or nursing homes, hospices, etc.).
    """

    patientspecified = CodeSystemConcept(
        {
            "code": "patientspecified",
            "definition": "Includes statements about medication use, including over the counter medication, provided by the patient, agent or another provider",
            "display": "Patient Specified",
        }
    )
    """
    Patient Specified

    Includes statements about medication use, including over the counter medication, provided by the patient, agent or another provider
    """

    class Meta:
        resource = _resource
