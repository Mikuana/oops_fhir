from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.bundle_type import BundleType as BundleType_


__all__ = ["BundleType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class BundleType(BundleType_):
    """
    BundleType

    Indicates the purpose of a bundle - how it is intended to be used.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/bundle-type
    """

    class Meta:
        resource = _resource
