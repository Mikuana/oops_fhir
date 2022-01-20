from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.episode_of_care_type import (
    EpisodeOfCareType as EpisodeOfCareType_,
)


__all__ = ["EpisodeOfCareType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EpisodeOfCareType(EpisodeOfCareType_):
    """
    Episode of care type

    This example value set defines a set of codes that can be used to
express the usage type of an EpisodeOfCare record.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/episodeofcare-type
    """

    class Meta:
        resource = _resource
