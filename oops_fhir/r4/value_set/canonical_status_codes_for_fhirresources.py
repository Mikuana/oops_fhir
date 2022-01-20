from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.canonical_status_codes_for_fhir_resources import (
    CanonicalStatusCodesforFHIRResources,
)


__all__ = ["CanonicalStatusCodesForFHIRResources"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CanonicalStatusCodesForFHIRResources(CanonicalStatusCodesforFHIRResources):
    """
    Canonical Status Codes for FHIR Resources

    The master set of status codes used throughout FHIR. All status codes
are mapped to one of these codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/resource-status
    """

    class Meta:
        resource = _resource
