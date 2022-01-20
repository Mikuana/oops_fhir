from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3Calendar"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3Calendar:
    """
    v3 Code System Calendar

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-Calendar
    """

    greg = CodeSystemConcept(
        {
            "code": "GREG",
            "definition": "The Gregorian calendar is the calendar in effect in most countries of Christian influence since approximately 1582. This calendar superceded the Julian calendar.",
            "display": "Gregorian",
        }
    )
    """
    Gregorian

    The Gregorian calendar is the calendar in effect in most countries of Christian influence since approximately 1582. This calendar superceded the Julian calendar.
    """

    class Meta:
        resource = _resource
