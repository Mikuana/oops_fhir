from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_relationship_conjunction import (
    v3RelationshipConjunction as v3RelationshipConjunction_,
)


__all__ = ["v3RelationshipConjunction"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3RelationshipConjunction(v3RelationshipConjunction_):
    """
    v3 Code System RelationshipConjunction

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-RelationshipConjunction
    """

    class Meta:
        resource = _resource
