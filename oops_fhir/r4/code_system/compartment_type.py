from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CompartmentType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CompartmentType:
    """
    CompartmentType

    Which type a compartment definition describes.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/compartment-type
    """

    patient = CodeSystemConcept(
        {
            "code": "Patient",
            "definition": "The compartment definition is for the patient compartment.",
            "display": "Patient",
        }
    )
    """
    Patient

    The compartment definition is for the patient compartment.
    """

    encounter = CodeSystemConcept(
        {
            "code": "Encounter",
            "definition": "The compartment definition is for the encounter compartment.",
            "display": "Encounter",
        }
    )
    """
    Encounter

    The compartment definition is for the encounter compartment.
    """

    related_person = CodeSystemConcept(
        {
            "code": "RelatedPerson",
            "definition": "The compartment definition is for the related-person compartment.",
            "display": "RelatedPerson",
        }
    )
    """
    RelatedPerson

    The compartment definition is for the related-person compartment.
    """

    practitioner = CodeSystemConcept(
        {
            "code": "Practitioner",
            "definition": "The compartment definition is for the practitioner compartment.",
            "display": "Practitioner",
        }
    )
    """
    Practitioner

    The compartment definition is for the practitioner compartment.
    """

    device = CodeSystemConcept(
        {
            "code": "Device",
            "definition": "The compartment definition is for the device compartment.",
            "display": "Device",
        }
    )
    """
    Device

    The compartment definition is for the device compartment.
    """

    class Meta:
        resource = _resource
