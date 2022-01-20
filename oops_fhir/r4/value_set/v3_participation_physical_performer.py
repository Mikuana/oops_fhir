from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_participation_type import v3ParticipationType


__all__ = ["v3ParticipationPhysicalPerformer"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ParticipationPhysicalPerformer(v3ParticipationType):
    """
    V3 Value SetParticipationPhysicalPerformer

     A person  who actually and principally carries out the action.  Need
not be the principal responsible actor, e.g. a surgery resident
operating under supervision of attending surgeon, and may be the patient
in self-care, e.g. fingerstick blood sugar.  The traditional order
filler is a performer. This information should accompany every service
event.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ParticipationPhysicalPerformer
    """

    class Meta:
        resource = _resource
