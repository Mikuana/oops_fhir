from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.procedure_progress_status_codes import (
    ProcedureProgressStatusCodes as ProcedureProgressStatusCodes_,
)


__all__ = ["ProcedureProgressStatusCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ProcedureProgressStatusCodes(ProcedureProgressStatusCodes_):
    """
    Procedure Progress Status Codes

    This value set is provided as an example. The value set to instantiate
this attribute should be drawn from a robust terminology code system
that consists of or contains concepts to support the procedure
performance process.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/procedure-progress-status-codes
    """

    class Meta:
        resource = _resource
