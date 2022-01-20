from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.benefit_cost_applicability import (
    BenefitCostApplicability as BenefitCostApplicability_,
)


__all__ = ["BenefitCostApplicability"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class BenefitCostApplicability(BenefitCostApplicability_):
    """
    Benefit cost applicability

    Whether the cost applies to in-network or out-of-network providers.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/insuranceplan-applicability
    """

    class Meta:
        resource = _resource
