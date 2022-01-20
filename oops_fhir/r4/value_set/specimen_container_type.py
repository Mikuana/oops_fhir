from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["SpecimenContainerType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SpecimenContainerType(SNOMEDCT):
    """
    Specimen Container Type

    Checks on the patient prior specimen collection. All SNOMED CT concepts
descendants of 706041008 |Device for body fluid and tissue
collection/transfer/processing (physical object)|

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/specimen-container-type
    """

    class Meta:
        resource = _resource
