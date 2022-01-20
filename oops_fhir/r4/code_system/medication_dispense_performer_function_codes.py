from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MedicationDispensePerformerFunctionCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MedicationDispensePerformerFunctionCodes:
    """
    Medication dispense  performer  function  codes

    MedicationDispense Performer Function Codes

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/medicationdispense-performer-function
    """

    dataenterer = CodeSystemConcept(
        {
            "code": "dataenterer",
            "definition": "Recorded the details of the request",
            "display": "Data Enterer",
        }
    )
    """
    Data Enterer

    Recorded the details of the request
    """

    packager = CodeSystemConcept(
        {
            "code": "packager",
            "definition": "Prepared the medication.",
            "display": "Packager",
        }
    )
    """
    Packager

    Prepared the medication.
    """

    checker = CodeSystemConcept(
        {
            "code": "checker",
            "definition": "Performed initial quality assurance on the prepared medication",
            "display": "Checker",
        }
    )
    """
    Checker

    Performed initial quality assurance on the prepared medication
    """

    finalchecker = CodeSystemConcept(
        {
            "code": "finalchecker",
            "definition": "Performed the final quality assurance on the prepared medication against the request. Typically, this is a pharmacist function.",
            "display": "Final Checker",
        }
    )
    """
    Final Checker

    Performed the final quality assurance on the prepared medication against the request. Typically, this is a pharmacist function.
    """

    class Meta:
        resource = _resource
