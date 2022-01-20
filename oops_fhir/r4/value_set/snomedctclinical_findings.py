from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["SNOMEDCTClinicalFindings"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SNOMEDCTClinicalFindings(SNOMEDCT):
    """
    SNOMED CT Clinical Findings

    This value set includes all the "Clinical finding" [SNOMED
CT](http://snomed.info/sct) codes - concepts where concept is-a
404684003 (Clinical finding (finding)).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/clinical-findings
    """

    class Meta:
        resource = _resource
