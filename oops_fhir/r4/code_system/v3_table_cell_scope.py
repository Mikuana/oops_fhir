from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3TableCellScope"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3TableCellScope:
    """
    v3 Code System TableCellScope

     These values are defined within the XHTML 4.0 Table Model

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-TableCellScope
    """

    col = CodeSystemConcept({"code": "col", "definition": "col", "display": "col"})
    """
    col

    col
    """

    colgroup = CodeSystemConcept(
        {"code": "colgroup", "definition": "colgroup", "display": "colgroup"}
    )
    """
    colgroup

    colgroup
    """

    row = CodeSystemConcept({"code": "row", "definition": "row", "display": "row"})
    """
    row

    row
    """

    rowgroup = CodeSystemConcept(
        {"code": "rowgroup", "definition": "rowgroup", "display": "rowgroup"}
    )
    """
    rowgroup

    rowgroup
    """

    class Meta:
        resource = _resource
