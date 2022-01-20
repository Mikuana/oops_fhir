from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_observation_method import v3ObservationMethod


__all__ = ["v3VerificationMethod"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3VerificationMethod(v3ObservationMethod):
    """
    V3 Value SetVerificationMethod

    No Description Provided

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-VerificationMethod
    """

    class Meta:
        resource = _resource
