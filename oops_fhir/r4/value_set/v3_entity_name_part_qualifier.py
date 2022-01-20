from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_entity_name_part_qualifier import (
    v3EntityNamePartQualifier as v3EntityNamePartQualifier_,
)


__all__ = ["v3EntityNamePartQualifier"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityNamePartQualifier(v3EntityNamePartQualifier_):
    """
    v3 Code System EntityNamePartQualifier

      OpenIssue:  Needs description

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-EntityNamePartQualifier
    """

    class Meta:
        resource = _resource
