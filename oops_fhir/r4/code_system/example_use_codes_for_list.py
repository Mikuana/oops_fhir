from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExampleUseCodesForList"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExampleUseCodesForList:
    """
    Example Use Codes for List

    Example use codes for the List resource - typical kinds of use.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/list-example-use-codes
    """

    alerts = CodeSystemConcept(
        {
            "code": "alerts",
            "definition": "A list of alerts for the patient.",
            "display": "Alerts",
        }
    )
    """
    Alerts

    A list of alerts for the patient.
    """

    adverserxns = CodeSystemConcept(
        {
            "code": "adverserxns",
            "definition": "A list of part adverse reactions.",
            "display": "Adverse Reactions",
        }
    )
    """
    Adverse Reactions

    A list of part adverse reactions.
    """

    allergies = CodeSystemConcept(
        {
            "code": "allergies",
            "definition": "A list of Allergies for the patient.",
            "display": "Allergies",
        }
    )
    """
    Allergies

    A list of Allergies for the patient.
    """

    medications = CodeSystemConcept(
        {
            "code": "medications",
            "definition": "A list of medication statements for the patient.",
            "display": "Medication List",
        }
    )
    """
    Medication List

    A list of medication statements for the patient.
    """

    problems = CodeSystemConcept(
        {
            "code": "problems",
            "definition": "A list of problems that the patient is known of have (or have had in the past).",
            "display": "Problem List",
        }
    )
    """
    Problem List

    A list of problems that the patient is known of have (or have had in the past).
    """

    worklist = CodeSystemConcept(
        {
            "code": "worklist",
            "definition": "A list of items that constitute a set of work to be performed (typically this code would be specialized for more specific uses, such as a ward round list).",
            "display": "Worklist",
        }
    )
    """
    Worklist

    A list of items that constitute a set of work to be performed (typically this code would be specialized for more specific uses, such as a ward round list).
    """

    waiting = CodeSystemConcept(
        {
            "code": "waiting",
            "definition": "A list of items waiting for an event (perhaps a surgical patient waiting list).",
            "display": "Waiting List",
        }
    )
    """
    Waiting List

    A list of items waiting for an event (perhaps a surgical patient waiting list).
    """

    protocols = CodeSystemConcept(
        {
            "code": "protocols",
            "definition": "A set of protocols to be followed.",
            "display": "Protocols",
        }
    )
    """
    Protocols

    A set of protocols to be followed.
    """

    plans = CodeSystemConcept(
        {
            "code": "plans",
            "definition": "A set of care plans that apply in a particular context of care.",
            "display": "Care Plans",
        }
    )
    """
    Care Plans

    A set of care plans that apply in a particular context of care.
    """

    class Meta:
        resource = _resource
