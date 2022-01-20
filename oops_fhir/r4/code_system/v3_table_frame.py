from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3TableFrame"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3TableFrame:
    """
    v3 Code System TableFrame

     These values are defined within the XHTML 4.0 Table Model

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-TableFrame
    """

    above = CodeSystemConcept(
        {"code": "above", "definition": "above", "display": "above"}
    )
    """
    above

    above
    """

    below = CodeSystemConcept(
        {"code": "below", "definition": "below", "display": "below"}
    )
    """
    below

    below
    """

    border = CodeSystemConcept(
        {"code": "border", "definition": "border", "display": "border"}
    )
    """
    border

    border
    """

    box = CodeSystemConcept({"code": "box", "definition": "box", "display": "box"})
    """
    box

    box
    """

    hsides = CodeSystemConcept(
        {"code": "hsides", "definition": "hsides", "display": "hsides"}
    )
    """
    hsides

    hsides
    """

    lhs = CodeSystemConcept({"code": "lhs", "definition": "lhs", "display": "lhs"})
    """
    lhs

    lhs
    """

    rhs = CodeSystemConcept({"code": "rhs", "definition": "rhs", "display": "rhs"})
    """
    rhs

    rhs
    """

    void = CodeSystemConcept({"code": "void", "definition": "void", "display": "void"})
    """
    void

    void
    """

    vsides = CodeSystemConcept(
        {"code": "vsides", "definition": "vsides", "display": "vsides"}
    )
    """
    vsides

    vsides
    """

    class Meta:
        resource = _resource
