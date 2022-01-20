from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MeasureType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MeasureType:
    """
    MeasureType

    The type of measure (includes codes from 2.16.840.1.113883.1.11.20368).

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/measure-type
    """

    process = CodeSystemConcept(
        {
            "code": "process",
            "definition": "A measure which focuses on a process which leads to a certain outcome, meaning that a scientific basis exists for believing that the process, when executed well, will increase the probability of achieving a desired outcome.",
            "display": "Process",
        }
    )
    """
    Process

    A measure which focuses on a process which leads to a certain outcome, meaning that a scientific basis exists for believing that the process, when executed well, will increase the probability of achieving a desired outcome.
    """

    outcome = CodeSystemConcept(
        {
            "code": "outcome",
            "definition": "A measure that indicates the result of the performance (or non-performance) of a function or process.",
            "display": "Outcome",
        }
    )
    """
    Outcome

    A measure that indicates the result of the performance (or non-performance) of a function or process.
    """

    structure = CodeSystemConcept(
        {
            "code": "structure",
            "definition": "A measure that focuses on a health care provider's capacity, systems, and processes to provide high-quality care.",
            "display": "Structure",
        }
    )
    """
    Structure

    A measure that focuses on a health care provider's capacity, systems, and processes to provide high-quality care.
    """

    patient_reported_outcome = CodeSystemConcept(
        {
            "code": "patient-reported-outcome",
            "definition": "A measure that focuses on patient-reported information such as patient engagement or patient experience measures.",
            "display": "Patient Reported Outcome",
        }
    )
    """
    Patient Reported Outcome

    A measure that focuses on patient-reported information such as patient engagement or patient experience measures.
    """

    composite = CodeSystemConcept(
        {
            "code": "composite",
            "definition": "A measure that combines multiple component measures in to a single quality measure.",
            "display": "Composite",
        }
    )
    """
    Composite

    A measure that combines multiple component measures in to a single quality measure.
    """

    class Meta:
        resource = _resource
