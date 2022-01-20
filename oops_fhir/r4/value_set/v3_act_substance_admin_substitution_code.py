from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_substance_admin_substitution import (
    v3substanceAdminSubstitution,
)


__all__ = ["v3ActSubstanceAdminSubstitutionCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActSubstanceAdminSubstitutionCode(v3substanceAdminSubstitution):
    """
    V3 Value SetActSubstanceAdminSubstitutionCode

    No Description Provided

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ActSubstanceAdminSubstitutionCode
    """

    class Meta:
        resource = _resource
