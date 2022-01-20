from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_entity_class import v3EntityClass


__all__ = ["v3EntityClassPlace"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityClassPlace(v3EntityClass):
    """
    V3 Value SetEntityClassPlace

     A physicial place or site with its containing structure. May be natural
or man-made.  The geographic position of a place may or may not be
constant.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-EntityClassPlace
    """

    class Meta:
        resource = _resource
