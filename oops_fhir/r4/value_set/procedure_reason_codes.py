from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["ProcedureReasonCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ProcedureReasonCodes(ValueSet):
    """
    Procedure Reason Codes

    This example value set defines the set of codes that can be used to
indicate a reason for a procedure.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/procedure-reason
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
