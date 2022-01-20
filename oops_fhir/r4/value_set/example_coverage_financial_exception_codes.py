from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.example_coverage_financial_exception_codes import (
    ExampleCoverageFinancialExceptionCodes as ExampleCoverageFinancialExceptionCodes_,
)


__all__ = ["ExampleCoverageFinancialExceptionCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExampleCoverageFinancialExceptionCodes(ExampleCoverageFinancialExceptionCodes_):
    """
    Example Coverage Financial Exception Codes

    This value set includes Example Coverage Financial Exception Codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/coverage-financial-exception
    """

    class Meta:
        resource = _resource
