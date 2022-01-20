from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MedicationAdministrationCategoryCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MedicationAdministrationCategoryCodes:
    """
    Medication administration  category  codes

    MedicationAdministration Category Codes

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/medication-admin-category
    """

    inpatient = CodeSystemConcept(
        {
            "code": "inpatient",
            "definition": "Includes administrations in an inpatient or acute care setting",
            "display": "Inpatient",
        }
    )
    """
    Inpatient

    Includes administrations in an inpatient or acute care setting
    """

    outpatient = CodeSystemConcept(
        {
            "code": "outpatient",
            "definition": "Includes administrations in an outpatient setting (for example, Emergency Department, Outpatient Clinic, Outpatient Surgery, Doctor's office)",
            "display": "Outpatient",
        }
    )
    """
    Outpatient

    Includes administrations in an outpatient setting (for example, Emergency Department, Outpatient Clinic, Outpatient Surgery, Doctor's office)
    """

    community = CodeSystemConcept(
        {
            "code": "community",
            "definition": "Includes administrations by the patient in their home (this would include long term care or nursing homes, hospices, etc.)",
            "display": "Community",
        }
    )
    """
    Community

    Includes administrations by the patient in their home (this would include long term care or nursing homes, hospices, etc.)
    """

    class Meta:
        resource = _resource
