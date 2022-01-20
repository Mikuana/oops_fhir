from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["EncounterLocationStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class EncounterLocationStatus:
    """
    EncounterLocationStatus

    The status of the location.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/encounter-location-status
    """

    planned = CodeSystemConcept(
        {
            "code": "planned",
            "definition": "The patient is planned to be moved to this location at some point in the future.",
            "display": "Planned",
        }
    )
    """
    Planned

    The patient is planned to be moved to this location at some point in the future.
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "The patient is currently at this location, or was between the period specified.\r\rA system may update these records when the patient leaves the location to either reserved, or completed.",
            "display": "Active",
        }
    )
    """
    Active

    The patient is currently at this location, or was between the period specified.

A system may update these records when the patient leaves the location to either reserved, or completed.
    """

    reserved = CodeSystemConcept(
        {
            "code": "reserved",
            "definition": "This location is held empty for this patient.",
            "display": "Reserved",
        }
    )
    """
    Reserved

    This location is held empty for this patient.
    """

    completed = CodeSystemConcept(
        {
            "code": "completed",
            "definition": "The patient was at this location during the period specified.\r\rNot to be used when the patient is currently at the location.",
            "display": "Completed",
        }
    )
    """
    Completed

    The patient was at this location during the period specified.

Not to be used when the patient is currently at the location.
    """

    class Meta:
        resource = _resource
