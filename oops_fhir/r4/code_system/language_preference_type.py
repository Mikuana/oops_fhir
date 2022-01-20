from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["LanguagePreferenceType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class LanguagePreferenceType:
    """
    Language preference type

    This value set defines the set of codes for describing the type or mode
of the patient's preferred language.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/language-preference-type
    """

    verbal = CodeSystemConcept(
        {
            "code": "verbal",
            "definition": "The patient prefers to verbally communicate with the associated language.",
            "display": "verbal",
        }
    )
    """
    verbal

    The patient prefers to verbally communicate with the associated language.
    """

    written = CodeSystemConcept(
        {
            "code": "written",
            "definition": "The patient prefers to communicate in writing with the associated language.",
            "display": "written",
        }
    )
    """
    written

    The patient prefers to communicate in writing with the associated language.
    """

    class Meta:
        resource = _resource
