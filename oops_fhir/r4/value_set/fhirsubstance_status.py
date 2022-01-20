from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.fhirsubstance_status import (
    FHIRSubstanceStatus as FHIRSubstanceStatus_,
)


__all__ = ["FHIRSubstanceStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FHIRSubstanceStatus(FHIRSubstanceStatus_):
    """
    FHIRSubstanceStatus

    A code to indicate if the substance is actively used.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/substance-status
    """

    class Meta:
        resource = _resource
