from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.benefit_term_codes import (
    BenefitTermCodes as BenefitTermCodes_,
)


__all__ = ["BenefitTermCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class BenefitTermCodes(BenefitTermCodes_):
    """
    Benefit Term Codes

    This value set includes a smattering of Benefit Term codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/benefit-term
    """

    class Meta:
        resource = _resource
