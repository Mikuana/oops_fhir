from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.xpath_usage_type import XPathUsageType as XPathUsageType_


__all__ = ["XPathUsageType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class XPathUsageType(XPathUsageType_):
    """
    XPathUsageType

    How a search parameter relates to the set of elements returned by
evaluating its xpath query.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/search-xpath-usage
    """

    class Meta:
        resource = _resource
