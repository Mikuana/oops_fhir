from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["SNOMEDCTRouteCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SNOMEDCTRouteCodes(SNOMEDCT):
    """
    SNOMED CT Route Codes

    This value set includes all Route codes from SNOMED CT - provided as an
exemplar.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/route-codes
    """

    class Meta:
        resource = _resource
