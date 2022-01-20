from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_entity_determiner import (
    v3EntityDeterminer as v3EntityDeterminer_,
)


__all__ = ["v3EntityDeterminer"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityDeterminer(v3EntityDeterminer_):
    """
    v3 Code System EntityDeterminer

     EntityDeterminer in natural language grammar is the class of words that
comprises articles, demonstrative pronouns, and quantifiers. In the RIM,
determiner is a structural code in the Entity class to distinguish
whether any given Entity object stands for some, any one, or a specific
thing.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-EntityDeterminer
    """

    class Meta:
        resource = _resource
