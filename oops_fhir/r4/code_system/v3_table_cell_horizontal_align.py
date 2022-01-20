from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3TableCellHorizontalAlign"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3TableCellHorizontalAlign:
    """
    v3 Code System TableCellHorizontalAlign

     These values are defined within the XHTML 4.0 Table Model

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-TableCellHorizontalAlign
    """

    center = CodeSystemConcept(
        {"code": "center", "definition": "center", "display": "center"}
    )
    """
    center

    center
    """

    char = CodeSystemConcept({"code": "char", "definition": "char", "display": "char"})
    """
    char

    char
    """

    justify = CodeSystemConcept(
        {"code": "justify", "definition": "justify", "display": "justify"}
    )
    """
    justify

    justify
    """

    left = CodeSystemConcept({"code": "left", "definition": "left", "display": "left"})
    """
    left

    left
    """

    right = CodeSystemConcept(
        {"code": "right", "definition": "right", "display": "right"}
    )
    """
    right

    right
    """

    class Meta:
        resource = _resource
