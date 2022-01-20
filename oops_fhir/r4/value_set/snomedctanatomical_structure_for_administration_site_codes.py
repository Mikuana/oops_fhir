from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["SNOMEDCTAnatomicalStructureForAdministrationSiteCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SNOMEDCTAnatomicalStructureForAdministrationSiteCodes(SNOMEDCT):
    """
    SNOMED CT Anatomical Structure for Administration Site Codes

    This value set includes Anatomical Structure codes from SNOMED CT -
provided as an exemplar.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/approach-site-codes
    """

    class Meta:
        resource = _resource
