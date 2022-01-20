from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["GroupType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class GroupType:
    """
    GroupType

    Types of resources that are part of group.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/group-type
    """

    person = CodeSystemConcept(
        {
            "code": "person",
            "definition": 'Group contains "person" Patient resources.',
            "display": "Person",
        }
    )
    """
    Person

    Group contains "person" Patient resources.
    """

    animal = CodeSystemConcept(
        {
            "code": "animal",
            "definition": 'Group contains "animal" Patient resources.',
            "display": "Animal",
        }
    )
    """
    Animal

    Group contains "animal" Patient resources.
    """

    practitioner = CodeSystemConcept(
        {
            "code": "practitioner",
            "definition": "Group contains healthcare practitioner resources (Practitioner or PractitionerRole).",
            "display": "Practitioner",
        }
    )
    """
    Practitioner

    Group contains healthcare practitioner resources (Practitioner or PractitionerRole).
    """

    device = CodeSystemConcept(
        {
            "code": "device",
            "definition": "Group contains Device resources.",
            "display": "Device",
        }
    )
    """
    Device

    Group contains Device resources.
    """

    medication = CodeSystemConcept(
        {
            "code": "medication",
            "definition": "Group contains Medication resources.",
            "display": "Medication",
        }
    )
    """
    Medication

    Group contains Medication resources.
    """

    substance = CodeSystemConcept(
        {
            "code": "substance",
            "definition": "Group contains Substance resources.",
            "display": "Substance",
        }
    )
    """
    Substance

    Group contains Substance resources.
    """

    class Meta:
        resource = _resource
