from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_participation_type import v3ParticipationType


__all__ = ["v3ParticipationIndirectTarget"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ParticipationIndirectTarget(v3ParticipationType):
    """
    V3 Value SetParticipationIndirectTarget

     Target that is not substantially present in the act and which is not
directly affected by the act, but which will be a focus of the record or
documentation of the act.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ParticipationIndirectTarget
    """

    class Meta:
        resource = _resource
