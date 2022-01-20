from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["ProcedurePerformerRoleCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ProcedurePerformerRoleCodes(SNOMEDCT):
    """
    Procedure Performer Role Codes

    This example value set defines the set of codes that can be used to
indicate a role of a procedure performer.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/performer-role
    """

    class Meta:
        resource = _resource
