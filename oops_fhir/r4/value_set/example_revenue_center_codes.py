from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.example_revenue_center_codes import (
    ExampleRevenueCenterCodes as ExampleRevenueCenterCodes_,
)


__all__ = ["ExampleRevenueCenterCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExampleRevenueCenterCodes(ExampleRevenueCenterCodes_):
    """
    Example Revenue Center Codes

    This value set includes sample Revenue Center codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/ex-revenue-center
    """

    class Meta:
        resource = _resource
