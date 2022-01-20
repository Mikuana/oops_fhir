from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_null_flavor import v3NullFlavor as v3NullFlavor_


__all__ = ["v3NullFlavor"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3NullFlavor(v3NullFlavor_):
    """
    v3 Code System NullFlavor

     A collection of codes specifying why a valid value is not present.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-NullFlavor
    """

    class Meta:
        resource = _resource
