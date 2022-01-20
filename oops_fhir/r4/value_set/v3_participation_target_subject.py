from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_participation_type import v3ParticipationType


__all__ = ["v3ParticipationTargetSubject"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ParticipationTargetSubject(v3ParticipationType):
    """
    V3 Value SetParticipationTargetSubject

     The principle target that the service acts on.  E.g. the patient in
physical examination, a specimen in a lab observation. May also be a
patient's family member (teaching) or a device or room (cleaning,
disinfecting, housekeeping). Note: not all direct targets are subjects,
consumables, and devices used as tools for a service are not subjects.
However, a device may be a subject of a maintenance service.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ParticipationTargetSubject
    """

    class Meta:
        resource = _resource
