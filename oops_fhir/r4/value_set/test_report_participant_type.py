from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.test_report_participant_type import (
    TestReportParticipantType as TestReportParticipantType_,
)


__all__ = ["TestReportParticipantType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TestReportParticipantType(TestReportParticipantType_):
    """
    TestReportParticipantType

    The type of participant.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/report-participant-type
    """

    class Meta:
        resource = _resource
