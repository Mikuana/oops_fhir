from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.benefit_type_codes import (
    BenefitTypeCodes as BenefitTypeCodes_,
)


__all__ = ["BenefitTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class BenefitTypeCodes(BenefitTypeCodes_):
    """
    Benefit Type Codes

    This value set includes a smattering of Benefit type codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/benefit-type
    """

    class Meta:
        resource = _resource
