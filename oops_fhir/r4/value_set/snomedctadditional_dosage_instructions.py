from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["SNOMEDCTAdditionalDosageInstructions"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SNOMEDCTAdditionalDosageInstructions(SNOMEDCT):
    """
    SNOMED CT Additional Dosage Instructions

    This value set includes all SNOMED CT Additional Dosage Instructions.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/additional-instruction-codes
    """

    class Meta:
        resource = _resource
