from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["SNOMEDCTDrugTherapyStatusCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SNOMEDCTDrugTherapyStatusCodes(ValueSet):
    """
    SNOMED CT Drug Therapy Status codes 

    This value set includes some taken and not taken reason codes from
SNOMED CT - provided as an exemplar

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/reason-medication-status-codes
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
