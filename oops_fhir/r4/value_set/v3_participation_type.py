from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_participation_type import (
    v3ParticipationType as v3ParticipationType_,
)


__all__ = ["v3ParticipationType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ParticipationType(v3ParticipationType_):
    """
    v3 Code System ParticipationType

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ParticipationType
    """

    class Meta:
        resource = _resource