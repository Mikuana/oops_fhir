from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.coverage_class_codes import (
    CoverageClassCodes as CoverageClassCodes_,
)


__all__ = ["CoverageClassCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CoverageClassCodes(CoverageClassCodes_):
    """
    Coverage Class Codes

    This value set includes Coverage Class codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/coverage-class
    """

    class Meta:
        resource = _resource
