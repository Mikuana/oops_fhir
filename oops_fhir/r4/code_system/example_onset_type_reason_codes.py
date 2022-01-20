from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExampleOnsetTypeReasonCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExampleOnsetTypeReasonCodes:
    """
    Example Onset Type (Reason) Codes

    This value set includes example Onset Type codes which are used to
identify the event for which the onset, starting date, is required.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://hl7.org/fhir/ex-onsettype
    """

    lxm = CodeSystemConcept(
        {
            "code": "lxm",
            "definition": "Date of last examination.",
            "display": "Last Exam",
        }
    )
    """
    Last Exam

    Date of last examination.
    """

    sym = CodeSystemConcept(
        {
            "code": "sym",
            "definition": "Date when symptoms were first noticed.",
            "display": "Start of Symptoms",
        }
    )
    """
    Start of Symptoms

    Date when symptoms were first noticed.
    """

    lmn = CodeSystemConcept(
        {
            "code": "lmn",
            "definition": "Start date of last menstruation.",
            "display": "Last Menstruation",
        }
    )
    """
    Last Menstruation

    Start date of last menstruation.
    """

    class Meta:
        resource = _resource
