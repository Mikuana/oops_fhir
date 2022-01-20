from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.coverage_self_pay_codes import (
    CoverageSelfPayCodes as CoverageSelfPayCodes_,
)


__all__ = ["CoverageSelfPayCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CoverageSelfPayCodes(CoverageSelfPayCodes_):
    """
    Coverage SelfPay Codes

    This value set includes Coverage SelfPay codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/coverage-selfpay
    """

    class Meta:
        resource = _resource
