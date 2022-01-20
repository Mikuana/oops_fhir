from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_relationship_type import v3ActRelationshipType


__all__ = ["v3ActRelationshipPertains"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActRelationshipPertains(v3ActRelationshipType):
    """
    V3 Value SetActRelationshipPertains

     This is a very unspecific relationship from one item of clinical
information to another.  It does not judge about the role the pertinent
information plays.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ActRelationshipPertains
    """

    class Meta:
        resource = _resource
