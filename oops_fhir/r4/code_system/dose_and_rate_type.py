from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DoseAndRateType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DoseAndRateType:
    """
    DoseAndRateType

    The kind of dose or rate specified.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/dose-rate-type
    """

    calculated = CodeSystemConcept(
        {
            "code": "calculated",
            "definition": "The dose specified is calculated by the prescriber or the system.",
            "display": "Calculated",
        }
    )
    """
    Calculated

    The dose specified is calculated by the prescriber or the system.
    """

    ordered = CodeSystemConcept(
        {
            "code": "ordered",
            "definition": "The dose specified is as ordered by the prescriber.",
            "display": "Ordered",
        }
    )
    """
    Ordered

    The dose specified is as ordered by the prescriber.
    """

    class Meta:
        resource = _resource
