from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.special_values import SpecialValues as SpecialValues_


__all__ = ["SpecialValues"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SpecialValues(SpecialValues_):
    """
    SpecialValues

    A set of generally useful codes defined so they can be included in value
sets.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/special-values
    """

    class Meta:
        resource = _resource
