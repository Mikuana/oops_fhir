from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_participation_type import v3ParticipationType


__all__ = ["v3ParticipationInformationTranscriber"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ParticipationInformationTranscriber(v3ParticipationType):
    """
    V3 Value SetParticipationInformationTranscriber

     An entity entering the data into the originating system. The data entry
entity is collected optionally for internal quality control purposes.
This includes the transcriptionist for dictated text transcribed into
electronic form.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ParticipationInformationTranscriber
    """

    class Meta:
        resource = _resource
