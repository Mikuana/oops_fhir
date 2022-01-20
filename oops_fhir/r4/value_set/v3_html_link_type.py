from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_html_link_type import v3HtmlLinkType as v3HtmlLinkType_


__all__ = ["v3HtmlLinkType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3HtmlLinkType(v3HtmlLinkType_):
    """
    v3 Code System HtmlLinkType

     HtmlLinkType values are drawn from HTML 4.0 and describe the
relationship between the current document and the anchor that is the
target of the link

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-HtmlLinkType
    """

    class Meta:
        resource = _resource
