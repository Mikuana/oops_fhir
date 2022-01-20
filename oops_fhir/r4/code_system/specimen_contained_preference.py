from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SpecimenContainedPreference"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SpecimenContainedPreference:
    """
    SpecimenContainedPreference

    Degree of preference of a type of conditioned specimen.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/specimen-contained-preference
    """

    preferred = CodeSystemConcept(
        {
            "code": "preferred",
            "definition": "This type of contained specimen is preferred to collect this kind of specimen.",
            "display": "Preferred",
        }
    )
    """
    Preferred

    This type of contained specimen is preferred to collect this kind of specimen.
    """

    alternate = CodeSystemConcept(
        {
            "code": "alternate",
            "definition": "This type of conditioned specimen is an alternate.",
            "display": "Alternate",
        }
    )
    """
    Alternate

    This type of conditioned specimen is an alternate.
    """

    class Meta:
        resource = _resource
