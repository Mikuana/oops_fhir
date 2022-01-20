from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ModifierTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ModifierTypeCodes:
    """
    Modifier type Codes

    This value set includes sample Modifier type codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/modifiers
    """

    a = CodeSystemConcept(
        {
            "code": "a",
            "definition": "Repair of prior service or installation.",
            "display": "Repair of prior service or installation",
        }
    )
    """
    Repair of prior service or installation

    Repair of prior service or installation.
    """

    b = CodeSystemConcept(
        {
            "code": "b",
            "definition": "Temporary service or installation.",
            "display": "Temporary service or installation",
        }
    )
    """
    Temporary service or installation

    Temporary service or installation.
    """

    c = CodeSystemConcept(
        {
            "code": "c",
            "definition": "Treatment associated with TMJ.",
            "display": "TMJ treatment",
        }
    )
    """
    TMJ treatment

    Treatment associated with TMJ.
    """

    e = CodeSystemConcept(
        {
            "code": "e",
            "definition": "Implant or associated with an implant.",
            "display": "Implant or associated with an implant",
        }
    )
    """
    Implant or associated with an implant

    Implant or associated with an implant.
    """

    rooh = CodeSystemConcept(
        {
            "code": "rooh",
            "definition": "A Rush service or service performed outside of normal office hours.",
            "display": "Rush or Outside of office hours",
        }
    )
    """
    Rush or Outside of office hours

    A Rush service or service performed outside of normal office hours.
    """

    x = CodeSystemConcept({"code": "x", "definition": "None.", "display": "None"})
    """
    None

    None.
    """

    class Meta:
        resource = _resource
