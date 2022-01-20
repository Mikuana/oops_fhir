from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_participation_type import v3ParticipationType


__all__ = ["v3ParticipationTargetLocation"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ParticipationTargetLocation(v3ParticipationType):
    """
    V3 Value SetParticipationTargetLocation

     The facility where the service is done.  May be a static building (or
room therein) or a moving location (e.g., ambulance, helicopter,
aircraft, train, truck, ship, etc.)

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ParticipationTargetLocation
    """

    class Meta:
        resource = _resource
