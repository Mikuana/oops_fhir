from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SpecimenStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SpecimenStatus:
    """
    SpecimenStatus

    Codes providing the status/availability of a specimen.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/specimen-status
    """

    available = CodeSystemConcept(
        {
            "code": "available",
            "definition": "The physical specimen is present and in good condition.",
            "display": "Available",
        }
    )
    """
    Available

    The physical specimen is present and in good condition.
    """

    unavailable = CodeSystemConcept(
        {
            "code": "unavailable",
            "definition": "There is no physical specimen because it is either lost, destroyed or consumed.",
            "display": "Unavailable",
        }
    )
    """
    Unavailable

    There is no physical specimen because it is either lost, destroyed or consumed.
    """

    unsatisfactory = CodeSystemConcept(
        {
            "code": "unsatisfactory",
            "definition": "The specimen cannot be used because of a quality issue such as a broken container, contamination, or too old.",
            "display": "Unsatisfactory",
        }
    )
    """
    Unsatisfactory

    The specimen cannot be used because of a quality issue such as a broken container, contamination, or too old.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The specimen was entered in error and therefore nullified.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The specimen was entered in error and therefore nullified.
    """

    class Meta:
        resource = _resource
