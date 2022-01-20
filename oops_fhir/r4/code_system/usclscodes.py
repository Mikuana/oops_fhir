from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["USCLSCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class USCLSCodes:
    """
    USCLS Codes

    This value set includes a smattering of USCLS codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/ex-USCLS
    """

    one101 = CodeSystemConcept(
        {
            "code": "1101",
            "definition": "Exam, comp, primary",
            "display": "Exam, comp, primary",
        }
    )
    """
    Exam, comp, primary

    Exam, comp, primary
    """

    one102 = CodeSystemConcept(
        {
            "code": "1102",
            "definition": "Exam, comp, mixed",
            "display": "Exam, comp, mixed",
        }
    )
    """
    Exam, comp, mixed

    Exam, comp, mixed
    """

    one103 = CodeSystemConcept(
        {
            "code": "1103",
            "definition": "Exam, comp, permanent",
            "display": "Exam, comp, permanent",
        }
    )
    """
    Exam, comp, permanent

    Exam, comp, permanent
    """

    one201 = CodeSystemConcept(
        {"code": "1201", "definition": "Exam, recall", "display": "Exam, recall"}
    )
    """
    Exam, recall

    Exam, recall
    """

    one205 = CodeSystemConcept(
        {"code": "1205", "definition": "Exam, emergency", "display": "Exam, emergency"}
    )
    """
    Exam, emergency

    Exam, emergency
    """

    two101 = CodeSystemConcept(
        {
            "code": "2101",
            "definition": "Radiograph, series (12)",
            "display": "Radiograph, series (12)",
        }
    )
    """
    Radiograph, series (12)

    Radiograph, series (12)
    """

    two102 = CodeSystemConcept(
        {
            "code": "2102",
            "definition": "Radiograph, series (16)",
            "display": "Radiograph, series (16)",
        }
    )
    """
    Radiograph, series (16)

    Radiograph, series (16)
    """

    two141 = CodeSystemConcept(
        {
            "code": "2141",
            "definition": "Radiograph, bitewing",
            "display": "Radiograph, bitewing",
        }
    )
    """
    Radiograph, bitewing

    Radiograph, bitewing
    """

    two601 = CodeSystemConcept(
        {
            "code": "2601",
            "definition": "Radiograph, panoramic",
            "display": "Radiograph, panoramic",
        }
    )
    """
    Radiograph, panoramic

    Radiograph, panoramic
    """

    one1101 = CodeSystemConcept(
        {
            "code": "11101",
            "definition": "Polishing, 1 unit",
            "display": "Polishing, 1 unit",
        }
    )
    """
    Polishing, 1 unit

    Polishing, 1 unit
    """

    one1102 = CodeSystemConcept(
        {
            "code": "11102",
            "definition": "Polishing, 2 unit",
            "display": "Polishing, 2 unit",
        }
    )
    """
    Polishing, 2 unit

    Polishing, 2 unit
    """

    one1103 = CodeSystemConcept(
        {
            "code": "11103",
            "definition": "Polishing, 3 unit",
            "display": "Polishing, 3 unit",
        }
    )
    """
    Polishing, 3 unit

    Polishing, 3 unit
    """

    one1104 = CodeSystemConcept(
        {
            "code": "11104",
            "definition": "Polishing, 4 unit",
            "display": "Polishing, 4 unit",
        }
    )
    """
    Polishing, 4 unit

    Polishing, 4 unit
    """

    two1211 = CodeSystemConcept(
        {
            "code": "21211",
            "definition": "Amalgam, 1 surface",
            "display": "Amalgam, 1 surface",
        }
    )
    """
    Amalgam, 1 surface

    Amalgam, 1 surface
    """

    two1212 = CodeSystemConcept(
        {
            "code": "21212",
            "definition": "Amalgam, 2 surface",
            "display": "Amalgam, 2 surface",
        }
    )
    """
    Amalgam, 2 surface

    Amalgam, 2 surface
    """

    two7211 = CodeSystemConcept(
        {"code": "27211", "definition": "Crown, PFM", "display": "Crown, PFM"}
    )
    """
    Crown, PFM

    Crown, PFM
    """

    six7211 = CodeSystemConcept(
        {"code": "67211", "definition": "Maryland Bridge", "display": "Maryland Bridge"}
    )
    """
    Maryland Bridge

    Maryland Bridge
    """

    nine9111 = CodeSystemConcept(
        {"code": "99111", "definition": "Lab, commercial", "display": "Lab, commercial"}
    )
    """
    Lab, commercial

    Lab, commercial
    """

    nine9333 = CodeSystemConcept(
        {"code": "99333", "definition": "Lab, in office", "display": "Lab, in office"}
    )
    """
    Lab, in office

    Lab, in office
    """

    nine9555 = CodeSystemConcept(
        {"code": "99555", "definition": "Expense", "display": "Expense"}
    )
    """
    Expense

    Expense
    """

    class Meta:
        resource = _resource
