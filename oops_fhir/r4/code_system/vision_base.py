from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["VisionBase"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class VisionBase:
    """
    VisionBase

    A coded concept listing the base codes.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/vision-base-codes
    """

    up = CodeSystemConcept({"code": "up", "definition": "top.", "display": "Up"})
    """
    Up

    top.
    """

    down = CodeSystemConcept(
        {"code": "down", "definition": "bottom.", "display": "Down"}
    )
    """
    Down

    bottom.
    """

    in_ = CodeSystemConcept(
        {"code": "in", "definition": "inner edge.", "display": "In"}
    )
    """
    In

    inner edge.
    """

    out = CodeSystemConcept(
        {"code": "out", "definition": "outer edge.", "display": "Out"}
    )
    """
    Out

    outer edge.
    """

    class Meta:
        resource = _resource
