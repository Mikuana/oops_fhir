from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3TableRules"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3TableRules:
    """
    v3 Code System TableRules

     These values are defined within the XHTML 4.0 Table Model

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-TableRules
    """

    all_ = CodeSystemConcept({"code": "all", "definition": "all", "display": "all"})
    """
    all

    all
    """

    cols = CodeSystemConcept({"code": "cols", "definition": "cols", "display": "cols"})
    """
    cols

    cols
    """

    groups = CodeSystemConcept(
        {"code": "groups", "definition": "groups", "display": "groups"}
    )
    """
    groups

    groups
    """

    none = CodeSystemConcept({"code": "none", "definition": "none", "display": "none"})
    """
    none

    none
    """

    rows = CodeSystemConcept({"code": "rows", "definition": "rows", "display": "rows"})
    """
    rows

    rows
    """

    class Meta:
        resource = _resource
