from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_reason import v3ActReason


__all__ = ["v3SubstanceAdminSubstitutionReason"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3SubstanceAdminSubstitutionReason(v3ActReason):
    """
    V3 Value SetSubstanceAdminSubstitutionReason

    No Description Provided

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-SubstanceAdminSubstitutionReason
    """

    class Meta:
        resource = _resource
