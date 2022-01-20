from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_participation_mode import (
    v3ParticipationMode as v3ParticipationMode_,
)


__all__ = ["v3ParticipationMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ParticipationMode(v3ParticipationMode_):
    """
    v3 Code System ParticipationMode

     A set of codes specifying the modality by which the Entity playing the
Role is participating in the Act.  Examples:  Physically present, over
the telephone, written communication.  Rationale:  Particularly for
author (originator) participants this is used to specify whether the
information represented by the act was initially provided verbally,
(hand-)written, or electronically.  Open Issue:  There needs to be a
reexamination of the hierarchies as there seems to be some muddling
between ELECTRONIC and other concepts that involve electronic
communication that are in other hierarchies.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ParticipationMode
    """

    class Meta:
        resource = _resource
