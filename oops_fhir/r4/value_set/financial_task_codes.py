from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.financial_task_codes import (
    FinancialTaskCodes as FinancialTaskCodes_,
)


__all__ = ["FinancialTaskCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FinancialTaskCodes(FinancialTaskCodes_):
    """
    Financial Task Codes

    This value set includes Financial Task codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/financial-taskcode
    """

    class Meta:
        resource = _resource
