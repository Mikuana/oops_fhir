from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.risk_probability import (
    RiskProbability as RiskProbability_,
)


__all__ = ["RiskProbability"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class RiskProbability(RiskProbability_):
    """
    Risk Probability

    Codes representing the likelihood of a particular outcome in a risk
assessment.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/risk-probability
    """

    class Meta:
        resource = _resource
