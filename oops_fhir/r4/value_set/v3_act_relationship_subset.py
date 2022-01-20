from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_relationship_subset import (
    v3ActRelationshipSubset as v3ActRelationshipSubset_,
)


__all__ = ["v3ActRelationshipSubset"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActRelationshipSubset(v3ActRelationshipSubset_):
    """
    v3 Code System ActRelationshipSubset

     <ns1:p>Used to indicate that the target of the relationship will be a
filtered subset of the total related set of targets.</ns1:p><ns1:p>Used
when there is a need to limit the number of components to the first, the
last, the next, the total, the average or some other filtered or
calculated subset.</ns1:p>

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ActRelationshipSubset
    """

    class Meta:
        resource = _resource
