from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_hl7_vote_resolution import (
    v3hl7VoteResolution as v3hl7VoteResolution_,
)


__all__ = ["v3hl7VoteResolution"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7VoteResolution(v3hl7VoteResolution_):
    """
    v3 Code System hl7VoteResolution

      Description:  Based on concepts for resolutions from HL7 ballot
spreadsheet according to HL7's Governance & Operations Manual (GOM).

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-hl7VoteResolution
    """

    class Meta:
        resource = _resource
