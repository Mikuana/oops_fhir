from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_style_type import v3styleType as v3styleType_


__all__ = ["v3styleType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3styleType(v3styleType_):
    """
    v3 Code System styleType

     <ns1:p>The style code is used within the CDA/SPL narrative block to
give the instance author some control over various aspects of
style</ns1:p>

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-styleType
    """

    class Meta:
        resource = _resource
