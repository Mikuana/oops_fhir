from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_participation_type import v3ParticipationType


__all__ = ["v3ParticipationTargetDirect"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ParticipationTargetDirect(v3ParticipationType):
    """
    V3 Value SetParticipationTargetDirect

     Target that is substantially present in the service and which is
directly affected by the service action (includes consumed material,
devices, etc.).

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ParticipationTargetDirect
    """

    class Meta:
        resource = _resource
