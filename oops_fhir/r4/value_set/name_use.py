from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.name_use import NameUse as NameUse_


__all__ = ["NameUse"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class NameUse(NameUse_):
    """
    NameUse

    The use of a human name.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/name-use
    """

    class Meta:
        resource = _resource
