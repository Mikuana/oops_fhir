from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["SNOMEDCTReasonMedicationNotGivenCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SNOMEDCTReasonMedicationNotGivenCodes(ValueSet):
    """
    SNOMED CT Reason Medication Not Given Codes

    This value set includes all medication refused, medication not
administered, and non-administration of necessary drug or medicine codes
from SNOMED CT - provided as an exemplar value set.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/reason-medication-not-given-codes
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
