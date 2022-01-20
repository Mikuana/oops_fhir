from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.referral_method import ReferralMethod as ReferralMethod_


__all__ = ["ReferralMethod"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ReferralMethod(ReferralMethod_):
    """
    ReferralMethod

    The methods of referral can be used when referring to a specific
HealthCareService resource.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/service-referral-method
    """

    class Meta:
        resource = _resource
