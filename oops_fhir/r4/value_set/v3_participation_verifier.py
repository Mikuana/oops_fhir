from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_participation_type import v3ParticipationType


__all__ = ["v3ParticipationVerifier"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ParticipationVerifier(v3ParticipationType):
    """
    V3 Value SetParticipationVerifier

     A person who verifies the correctness and appropriateness of the
service (plan, order, event, etc.) and hence takes on accountability.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ParticipationVerifier
    """

    class Meta:
        resource = _resource
