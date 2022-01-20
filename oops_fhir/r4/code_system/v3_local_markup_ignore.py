from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3LocalMarkupIgnore"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3LocalMarkupIgnore:
    """
    v3 Code System LocalMarkupIgnore

     Tells a receiver to ignore just the local markup tags (local_markup,
local_header, local_attr) when value="markup", or to ignore the local
markup tags and all contained content when value="all"

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-LocalMarkupIgnore
    """

    all_ = CodeSystemConcept({"code": "all", "definition": "all", "display": "all"})
    """
    all

    all
    """

    markup = CodeSystemConcept(
        {"code": "markup", "definition": "markup", "display": "markup"}
    )
    """
    markup

    markup
    """

    class Meta:
        resource = _resource
