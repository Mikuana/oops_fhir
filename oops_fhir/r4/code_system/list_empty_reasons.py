from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ListEmptyReasons"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ListEmptyReasons:
    """
    List Empty Reasons

    General reasons for a list to be empty. Reasons are either related to a
summary list (i.e. problem or medication list) or to a workflow related
list (i.e. consultation list).

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/list-empty-reason
    """

    nilknown = CodeSystemConcept(
        {
            "code": "nilknown",
            "definition": "Clinical judgment that there are no known items for this list after reasonable investigation. Note that this a positive statement by a clinical user, and not a default position asserted by a computer system in the lack of other information. Example uses:  * For allergies: the patient or patient's agent/guardian has asserted that he/she is not aware of any allergies (NKA - nil known allergies)  * For medications: the patient or patient's agent/guardian has asserted that the patient is known to be taking no medications  * For diagnoses, problems and procedures: the patient or patient's agent/guardian has asserted that there is no known event to record.",
            "display": "Nil Known",
        }
    )
    """
    Nil Known

    Clinical judgment that there are no known items for this list after reasonable investigation. Note that this a positive statement by a clinical user, and not a default position asserted by a computer system in the lack of other information. Example uses:  * For allergies: the patient or patient's agent/guardian has asserted that he/she is not aware of any allergies (NKA - nil known allergies)  * For medications: the patient or patient's agent/guardian has asserted that the patient is known to be taking no medications  * For diagnoses, problems and procedures: the patient or patient's agent/guardian has asserted that there is no known event to record.
    """

    notasked = CodeSystemConcept(
        {
            "code": "notasked",
            "definition": "The investigation to find out whether there are items for this list has not occurred.",
            "display": "Not Asked",
        }
    )
    """
    Not Asked

    The investigation to find out whether there are items for this list has not occurred.
    """

    withheld = CodeSystemConcept(
        {
            "code": "withheld",
            "definition": "The content of the list was not provided due to privacy or confidentiality concerns. Note that it should not be assumed that this means that the particular information in question was withheld due to its contents - it can also be a policy decision.",
            "display": "Information Withheld",
        }
    )
    """
    Information Withheld

    The content of the list was not provided due to privacy or confidentiality concerns. Note that it should not be assumed that this means that the particular information in question was withheld due to its contents - it can also be a policy decision.
    """

    unavailable = CodeSystemConcept(
        {
            "code": "unavailable",
            "definition": "Information to populate this list cannot be obtained; e.g. unconscious patient.",
            "display": "Unavailable",
        }
    )
    """
    Unavailable

    Information to populate this list cannot be obtained; e.g. unconscious patient.
    """

    notstarted = CodeSystemConcept(
        {
            "code": "notstarted",
            "definition": "The work to populate this list has not yet begun.",
            "display": "Not Started",
        }
    )
    """
    Not Started

    The work to populate this list has not yet begun.
    """

    closed = CodeSystemConcept(
        {
            "code": "closed",
            "definition": "This list has now closed or has ceased to be relevant or useful.",
            "display": "Closed",
        }
    )
    """
    Closed

    This list has now closed or has ceased to be relevant or useful.
    """

    class Meta:
        resource = _resource
