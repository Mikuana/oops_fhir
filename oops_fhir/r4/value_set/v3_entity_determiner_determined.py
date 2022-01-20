from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_entity_determiner import v3EntityDeterminer


__all__ = ["v3EntityDeterminerDetermined"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityDeterminerDetermined(v3EntityDeterminer):
    """
    V3 Value SetEntityDeterminerDetermined

     The described determiner is used to indicate that the given Entity is
taken as a general description of a kind of thing that can be taken in
whole, in part, or in multiples.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-EntityDeterminerDetermined
    """

    class Meta:
        resource = _resource
