from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3LanguageAbilityMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3LanguageAbilityMode:
    """
    v3 Code System LanguageAbilityMode

     A value representing the method of expression of the language.
Example:  Expressed spoken, expressed written, expressed signed,
received spoken, received written, received signed.  OpenIssue:
Description copied from Concept Domain of same name.  Must be verified.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-LanguageAbilityMode
    """

    esgn = CodeSystemConcept(
        {
            "code": "ESGN",
            "definition": "Expressed signed",
            "display": "Expressed signed",
        }
    )
    """
    Expressed signed

    Expressed signed
    """

    esp = CodeSystemConcept(
        {"code": "ESP", "definition": "Expressed spoken", "display": "Expressed spoken"}
    )
    """
    Expressed spoken

    Expressed spoken
    """

    ewr = CodeSystemConcept(
        {
            "code": "EWR",
            "definition": "Expressed written",
            "display": "Expressed written",
        }
    )
    """
    Expressed written

    Expressed written
    """

    rsgn = CodeSystemConcept(
        {"code": "RSGN", "definition": "Received signed", "display": "Received signed"}
    )
    """
    Received signed

    Received signed
    """

    rsp = CodeSystemConcept(
        {"code": "RSP", "definition": "Received spoken", "display": "Received spoken"}
    )
    """
    Received spoken

    Received spoken
    """

    rwr = CodeSystemConcept(
        {"code": "RWR", "definition": "Received written", "display": "Received written"}
    )
    """
    Received written

    Received written
    """

    class Meta:
        resource = _resource
