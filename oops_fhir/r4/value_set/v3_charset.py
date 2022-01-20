from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_charset import v3Charset as v3Charset_


__all__ = ["v3Charset"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3Charset(v3Charset_):
    """
    v3 Code System Charset

     Internet Assigned Numbers Authority (IANA) Charset Types

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-Charset
    """

    class Meta:
        resource = _resource
