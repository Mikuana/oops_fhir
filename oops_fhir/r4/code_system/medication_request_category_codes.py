from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["medicationRequestCategoryCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class medicationRequestCategoryCodes:
    """
    Medication request  category  codes

    MedicationRequest Category Codes

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/medicationrequest-category
    """

    inpatient = CodeSystemConcept(
        {
            "code": "inpatient",
            "definition": "Includes requests for medications to be administered or consumed in an inpatient or acute care setting",
            "display": "Inpatient",
        }
    )
    """
    Inpatient

    Includes requests for medications to be administered or consumed in an inpatient or acute care setting
    """

    outpatient = CodeSystemConcept(
        {
            "code": "outpatient",
            "definition": "Includes requests for medications to be administered or consumed in an outpatient setting (for example, Emergency Department, Outpatient Clinic, Outpatient Surgery, Doctor's office)",
            "display": "Outpatient",
        }
    )
    """
    Outpatient

    Includes requests for medications to be administered or consumed in an outpatient setting (for example, Emergency Department, Outpatient Clinic, Outpatient Surgery, Doctor's office)
    """

    community = CodeSystemConcept(
        {
            "code": "community",
            "definition": "Includes requests for medications to be administered or consumed by the patient in their home (this would include long term care or nursing homes, hospices, etc.)",
            "display": "Community",
        }
    )
    """
    Community

    Includes requests for medications to be administered or consumed by the patient in their home (this would include long term care or nursing homes, hospices, etc.)
    """

    discharge = CodeSystemConcept(
        {
            "code": "discharge",
            "definition": "Includes requests for medications created when the patient is being released from a facility",
            "display": "Discharge",
        }
    )
    """
    Discharge

    Includes requests for medications created when the patient is being released from a facility
    """

    class Meta:
        resource = _resource
