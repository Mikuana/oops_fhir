from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DaysOfWeek"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DaysOfWeek:
    """
    DaysOfWeek

    The days of the week.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/days-of-week
    """

    mon = CodeSystemConcept(
        {"code": "mon", "definition": "Monday.", "display": "Monday"}
    )
    """
    Monday

    Monday.
    """

    tue = CodeSystemConcept(
        {"code": "tue", "definition": "Tuesday.", "display": "Tuesday"}
    )
    """
    Tuesday

    Tuesday.
    """

    wed = CodeSystemConcept(
        {"code": "wed", "definition": "Wednesday.", "display": "Wednesday"}
    )
    """
    Wednesday

    Wednesday.
    """

    thu = CodeSystemConcept(
        {"code": "thu", "definition": "Thursday.", "display": "Thursday"}
    )
    """
    Thursday

    Thursday.
    """

    fri = CodeSystemConcept(
        {"code": "fri", "definition": "Friday.", "display": "Friday"}
    )
    """
    Friday

    Friday.
    """

    sat = CodeSystemConcept(
        {"code": "sat", "definition": "Saturday.", "display": "Saturday"}
    )
    """
    Saturday

    Saturday.
    """

    sun = CodeSystemConcept(
        {"code": "sun", "definition": "Sunday.", "display": "Sunday"}
    )
    """
    Sunday

    Sunday.
    """

    class Meta:
        resource = _resource
