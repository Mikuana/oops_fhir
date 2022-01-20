from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["ProcedureCodesSNOMEDCT"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ProcedureCodesSNOMEDCT(SNOMEDCT):
    """
    Procedure Codes (SNOMED CT)

    Procedure Code: All SNOMED CT procedure codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/procedure-code
    """

    class Meta:
        resource = _resource
