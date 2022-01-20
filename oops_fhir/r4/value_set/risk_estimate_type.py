from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.risk_estimate_type import (
    RiskEstimateType as RiskEstimateType_,
)


__all__ = ["RiskEstimateType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class RiskEstimateType(RiskEstimateType_):
    """
    RiskEstimateType

    Whether the risk estimate is dichotomous, continuous or qualitative and
the specific type of risk estimate (eg proportion or median).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/risk-estimate-type
    """

    class Meta:
        resource = _resource
