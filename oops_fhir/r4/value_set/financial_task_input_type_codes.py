from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.financial_task_input_type_codes import (
    FinancialTaskInputTypeCodes as FinancialTaskInputTypeCodes_,
)


__all__ = ["FinancialTaskInputTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FinancialTaskInputTypeCodes(FinancialTaskInputTypeCodes_):
    """
    Financial Task Input Type Codes

    This value set includes Financial Task Input Type codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/financial-taskinputtype
    """

    class Meta:
        resource = _resource
