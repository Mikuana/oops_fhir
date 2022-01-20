from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.consent_policy_rule_codes import (
    ConsentPolicyRuleCodes as ConsentPolicyRuleCodes_,
)


__all__ = ["ConsentPolicyRuleCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConsentPolicyRuleCodes(ConsentPolicyRuleCodes_):
    """
    Consent PolicyRule Codes

    This value set includes sample Regulatory consent policy types from the
US and other regions.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/consent-policy
    """

    class Meta:
        resource = _resource
