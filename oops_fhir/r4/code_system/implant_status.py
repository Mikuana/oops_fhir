from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ImplantStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ImplantStatus:
    """
    Implant Status

    A set codes that define the functional status of an implanted device.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/implantStatus
    """

    functional = CodeSystemConcept(
        {
            "code": "functional",
            "definition": "The implanted device is working normally.",
            "display": "Functional",
        }
    )
    """
    Functional

    The implanted device is working normally.
    """

    non_functional = CodeSystemConcept(
        {
            "code": "non-functional",
            "definition": "The implanted device is not working.",
            "display": "Non-Functional",
        }
    )
    """
    Non-Functional

    The implanted device is not working.
    """

    disabled = CodeSystemConcept(
        {
            "code": "disabled",
            "definition": "The implanted device has been turned off.",
            "display": "Disabled",
        }
    )
    """
    Disabled

    The implanted device has been turned off.
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": "the functional status of the implant has not been determined.",
            "display": "Unknown",
        }
    )
    """
    Unknown

    the functional status of the implant has not been determined.
    """

    class Meta:
        resource = _resource
