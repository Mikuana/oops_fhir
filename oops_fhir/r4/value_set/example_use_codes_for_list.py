from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.example_use_codes_for_list import (
    ExampleUseCodesForList as ExampleUseCodesForList_,
)


__all__ = ["ExampleUseCodesForList"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExampleUseCodesForList(ExampleUseCodesForList_):
    """
    Example Use Codes for List

    Example use codes for the List resource - typical kinds of use.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/list-example-codes
    """

    class Meta:
        resource = _resource
