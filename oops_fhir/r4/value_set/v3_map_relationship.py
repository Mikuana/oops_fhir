from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_map_relationship import (
    v3MapRelationship as v3MapRelationship_,
)


__all__ = ["v3MapRelationship"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3MapRelationship(v3MapRelationship_):
    """
    v3 Code System MapRelationship

     The closeness or quality of the mapping between the HL7 concept (as
represented by the HL7 concept identifier) and the source coding system.
The values are patterned after the similar relationships used in the
UMLS Metathesaurus. Because the HL7 coding sy

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-MapRelationship
    """

    class Meta:
        resource = _resource
