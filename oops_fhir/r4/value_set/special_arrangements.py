from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.special_arrangements import (
    SpecialArrangements as SpecialArrangements_,
)


__all__ = ["SpecialArrangements"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SpecialArrangements(SpecialArrangements_):
    """
    Special arrangements

    This value set defines a set of codes that can be used to indicate the
kinds of special arrangements in place for a patients visit.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/encounter-special-arrangements
    """

    class Meta:
        resource = _resource
