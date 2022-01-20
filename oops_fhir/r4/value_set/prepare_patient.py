from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["PreparePatient"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class PreparePatient(SNOMEDCT):
    """
    Patient preparation prior specimen collection

    Checks on the patient prior specimen collection. All SNOMED CT concepts
descendants of 703763000 |Precondition value (qualifier value)|

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/prepare-patient-prior-specimen-collection
    """

    class Meta:
        resource = _resource
