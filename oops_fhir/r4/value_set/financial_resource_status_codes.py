from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.financial_resource_status_codes import (
    FinancialResourceStatusCodes as FinancialResourceStatusCodes_,
)


__all__ = ["FinancialResourceStatusCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FinancialResourceStatusCodes(FinancialResourceStatusCodes_):
    """
    Financial Resource Status Codes

    This value set includes Status codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/fm-status
    """

    class Meta:
        resource = _resource
