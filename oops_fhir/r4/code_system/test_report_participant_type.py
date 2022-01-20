from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["TestReportParticipantType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class TestReportParticipantType:
    """
    TestReportParticipantType

    The type of participant.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/report-participant-type
    """

    test_engine = CodeSystemConcept(
        {
            "code": "test-engine",
            "definition": "The test execution engine.",
            "display": "Test Engine",
        }
    )
    """
    Test Engine

    The test execution engine.
    """

    client = CodeSystemConcept(
        {"code": "client", "definition": "A FHIR Client.", "display": "Client"}
    )
    """
    Client

    A FHIR Client.
    """

    server = CodeSystemConcept(
        {"code": "server", "definition": "A FHIR Server.", "display": "Server"}
    )
    """
    Server

    A FHIR Server.
    """

    class Meta:
        resource = _resource
