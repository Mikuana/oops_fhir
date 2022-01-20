from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["SNOMEDCTMedicationAsNeededReasonCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SNOMEDCTMedicationAsNeededReasonCodes(SNOMEDCT):
    """
    SNOMED CT Medication As Needed Reason Codes

    This value set includes all clinical findings from SNOMED CT - provided
as an exemplar value set.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/medication-as-needed-reason
    """

    class Meta:
        resource = _resource
