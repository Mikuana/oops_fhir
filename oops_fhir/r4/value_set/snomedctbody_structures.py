from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["SNOMEDCTBodyStructures"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SNOMEDCTBodyStructures(SNOMEDCT):
    """
    SNOMED CT Body Structures

    This value set includes all codes from [SNOMED
CT](http://snomed.info/sct) where concept is-a 442083009 (Anatomical or
acquired body site (body structure)).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/body-site
    """

    class Meta:
        resource = _resource
