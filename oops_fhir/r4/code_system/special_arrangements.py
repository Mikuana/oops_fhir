from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SpecialArrangements"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SpecialArrangements:
    """
    Special arrangements

    This value set defines a set of codes that can be used to indicate the
kinds of special arrangements in place for a patients visit.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/encounter-special-arrangements
    """

    wheel = CodeSystemConcept(
        {
            "code": "wheel",
            "definition": "The patient requires a wheelchair to be made available for the encounter.",
            "display": "Wheelchair",
        }
    )
    """
    Wheelchair

    The patient requires a wheelchair to be made available for the encounter.
    """

    add_bed = CodeSystemConcept(
        {
            "code": "add-bed",
            "definition": "An additional bed made available for a person accompanying the patient, for example a parent accompanying a child.",
            "display": "Additional bedding",
        }
    )
    """
    Additional bedding

    An additional bed made available for a person accompanying the patient, for example a parent accompanying a child.
    """

    int_ = CodeSystemConcept(
        {
            "code": "int",
            "definition": "The patient is not fluent in the local language and requires an interpreter to be available. Refer to the Patient.Language property for the type of interpreter required.",
            "display": "Interpreter",
        }
    )
    """
    Interpreter

    The patient is not fluent in the local language and requires an interpreter to be available. Refer to the Patient.Language property for the type of interpreter required.
    """

    att = CodeSystemConcept(
        {
            "code": "att",
            "definition": "A person who accompanies a patient to provide assistive services necessary for the patient's care during the encounter.",
            "display": "Attendant",
        }
    )
    """
    Attendant

    A person who accompanies a patient to provide assistive services necessary for the patient's care during the encounter.
    """

    dog = CodeSystemConcept(
        {
            "code": "dog",
            "definition": "The patient has a guide dog and the location used for the encounter should be able to support the presence of the service animal.",
            "display": "Guide dog",
        }
    )
    """
    Guide dog

    The patient has a guide dog and the location used for the encounter should be able to support the presence of the service animal.
    """

    class Meta:
        resource = _resource
