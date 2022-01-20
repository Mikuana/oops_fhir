from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.episode_of_care_status import (
    EpisodeOfCareStatus as EpisodeOfCareStatus_,
)


__all__ = ["EpisodeOfCareStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EpisodeOfCareStatus(EpisodeOfCareStatus_):
    """
    EpisodeOfCareStatus

    The status of the episode of care.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/episode-of-care-status
    """

    class Meta:
        resource = _resource
