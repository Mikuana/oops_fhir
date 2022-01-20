from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.operation_outcome_codes import (
    OperationOutcomeCodes as OperationOutcomeCodes_,
)


__all__ = ["OperationOutcomeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class OperationOutcomeCodes(OperationOutcomeCodes_):
    """
    Operation Outcome Codes

    Operation Outcome codes used by FHIR test servers (see Implementation
file translations.xml)

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/operation-outcome
    """

    class Meta:
        resource = _resource
