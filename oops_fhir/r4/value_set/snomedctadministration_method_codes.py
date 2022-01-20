from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["SNOMEDCTAdministrationMethodCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SNOMEDCTAdministrationMethodCodes(SNOMEDCT):
    """
    SNOMED CT Administration Method Codes

    This value set includes some method codes from SNOMED CT - provided as
an exemplar

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/administration-method-codes
    """

    class Meta:
        resource = _resource
