from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3LanguageAbilityProficiency"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3LanguageAbilityProficiency:
    """
    v3 Code System LanguageAbilityProficiency

     A value representing the level of proficiency in a language.  Example:
Excellent, good, fair, poor.  OpenIssue:  Description copied from
Concept Domain of same name.  Must be verified.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-LanguageAbilityProficiency
    """

    e = CodeSystemConcept(
        {"code": "E", "definition": "Excellent", "display": "Excellent"}
    )
    """
    Excellent

    Excellent
    """

    f = CodeSystemConcept({"code": "F", "definition": "Fair", "display": "Fair"})
    """
    Fair

    Fair
    """

    g = CodeSystemConcept({"code": "G", "definition": "Good", "display": "Good"})
    """
    Good

    Good
    """

    p = CodeSystemConcept({"code": "P", "definition": "Poor", "display": "Poor"})
    """
    Poor

    Poor
    """

    class Meta:
        resource = _resource
