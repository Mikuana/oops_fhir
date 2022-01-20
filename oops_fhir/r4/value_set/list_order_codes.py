from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.list_order_codes import ListOrderCodes as ListOrderCodes_


__all__ = ["ListOrderCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ListOrderCodes(ListOrderCodes_):
    """
    List Order Codes

    Base values for the order of the items in a list resource.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/list-order
    """

    class Meta:
        resource = _resource
