from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3TableCellVerticalAlign"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3TableCellVerticalAlign:
    """
    v3 Code System TableCellVerticalAlign

     These values are defined within the XHTML 4.0 Table Model

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-TableCellVerticalAlign
    """

    baseline = CodeSystemConcept(
        {"code": "baseline", "definition": "baseline", "display": "baseline"}
    )
    """
    baseline

    baseline
    """

    bottom = CodeSystemConcept(
        {"code": "bottom", "definition": "bottom", "display": "bottom"}
    )
    """
    bottom

    bottom
    """

    middle = CodeSystemConcept(
        {"code": "middle", "definition": "middle", "display": "middle"}
    )
    """
    middle

    middle
    """

    top = CodeSystemConcept({"code": "top", "definition": "top", "display": "top"})
    """
    top

    top
    """

    class Meta:
        resource = _resource
