from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_substance_admin_substitution import (
    v3substanceAdminSubstitution as v3substanceAdminSubstitution_,
)


__all__ = ["v3substanceAdminSubstitution"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3substanceAdminSubstitution(v3substanceAdminSubstitution_):
    """
    v3 Code System substanceAdminSubstitution

     Identifies what sort of change is permitted or has occurred between the
therapy that was ordered and the therapy that was/will be provided.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-substanceAdminSubstitution
    """

    class Meta:
        resource = _resource
