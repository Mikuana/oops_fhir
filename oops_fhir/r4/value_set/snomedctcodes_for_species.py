from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["SNOMEDCTCodesForSpecies"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SNOMEDCTCodesForSpecies(SNOMEDCT):
    """
    SNOMED CT Codes for species

    Codes identifying atomic results of observations when value is type
codeableConcept. This value set includes all the children of SNOMED CT
Concepts from SCTIDs 404684003 Clinical finding (finding), 410607006
Organism (organism),362981000 Qualifier value (qualifier value),
105590001 Substance (substance), and 123037004 Body structure (body
structure).  It is provided as a suggestive example

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/sequence-species
    """

    class Meta:
        resource = _resource
