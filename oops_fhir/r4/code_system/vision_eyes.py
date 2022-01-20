from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["VisionEyes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class VisionEyes:
    """
    VisionEyes

    A coded concept listing the eye codes.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/vision-eye-codes
    """

    right = CodeSystemConcept(
        {"code": "right", "definition": "Right Eye.", "display": "Right Eye"}
    )
    """
    Right Eye

    Right Eye.
    """

    left = CodeSystemConcept(
        {"code": "left", "definition": "Left Eye.", "display": "Left Eye"}
    )
    """
    Left Eye

    Left Eye.
    """

    class Meta:
        resource = _resource
