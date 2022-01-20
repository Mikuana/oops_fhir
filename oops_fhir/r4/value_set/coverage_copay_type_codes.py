from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.coverage_copay_type_codes import (
    CoverageCopayTypeCodes as CoverageCopayTypeCodes_,
)


__all__ = ["CoverageCopayTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CoverageCopayTypeCodes(CoverageCopayTypeCodes_):
    """
    Coverage Copay Type Codes

    This value set includes sample Coverage Copayment Type codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/coverage-copay-type
    """

    class Meta:
        resource = _resource
