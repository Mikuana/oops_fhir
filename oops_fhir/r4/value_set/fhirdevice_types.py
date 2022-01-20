from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["FHIRDeviceTypes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FHIRDeviceTypes(SNOMEDCT):
    """
    FHIR Device Types

    Codes used to identify medical devices. Includes concepts from SNOMED CT
(http://www.snomed.org/) where concept is-a 49062001 (Device)  and is
provided as a suggestive example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/device-kind
    """

    class Meta:
        resource = _resource
