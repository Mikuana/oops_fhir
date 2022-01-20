from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AdverseEventActuality"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AdverseEventActuality:
    """
    AdverseEventActuality

    Overall nature of the adverse event, e.g. real or potential.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/adverse-event-actuality
    """

    actual = CodeSystemConcept(
        {
            "code": "actual",
            "definition": "The adverse event actually happened regardless of whether anyone was affected or harmed.",
            "display": "Adverse Event",
        }
    )
    """
    Adverse Event

    The adverse event actually happened regardless of whether anyone was affected or harmed.
    """

    potential = CodeSystemConcept(
        {
            "code": "potential",
            "definition": "A potential adverse event.",
            "display": "Potential Adverse Event",
        }
    )
    """
    Potential Adverse Event

    A potential adverse event.
    """

    class Meta:
        resource = _resource
