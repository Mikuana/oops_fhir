from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_entity_name_part_qualifier_r2 import (
    v3EntityNamePartQualifierR2 as v3EntityNamePartQualifierR2_,
)


__all__ = ["v3EntityNamePartQualifierR2"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityNamePartQualifierR2(v3EntityNamePartQualifierR2_):
    """
    v3 Code System EntityNamePartQualifierR2

      Description:  The qualifier is a set of codes each of which specifies
a certain subcategory of the name part in addition to the main name part
type. For example, a given name may be flagged as a nickname, a family
name may be a pseudonym or a name of public records.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-EntityNamePartQualifierR2
    """

    class Meta:
        resource = _resource
