from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.abstract_type import AbstractType as AbstractType_


__all__ = ["AbstractType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AbstractType(AbstractType_):
    """
    AbstractType

    A list of the base types defined by this version of the FHIR
specification - types that are defined, but for which only
specializations actually are created.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/abstract-types
    """

    class Meta:
        resource = _resource
