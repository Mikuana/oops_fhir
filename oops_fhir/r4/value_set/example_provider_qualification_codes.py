from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.example_provider_qualification_codes import (
    ExampleProviderQualificationCodes as ExampleProviderQualificationCodes_,
)


__all__ = ["ExampleProviderQualificationCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExampleProviderQualificationCodes(ExampleProviderQualificationCodes_):
    """
    Example Provider Qualification Codes

    This value set includes sample Provider Qualification codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/provider-qualification
    """

    class Meta:
        resource = _resource
