from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3CalendarCycle"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3CalendarCycle:
    """
    v3 Code System CalendarCycle

     Calendar cycle identifiers

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-CalendarCycle
    """

    underscore_calendar_cycle_one_letter = CodeSystemConcept(
        {
            "code": "_CalendarCycleOneLetter",
            "concept": [
                {
                    "code": "CW",
                    "definition": "week (continuous)",
                    "display": "week (continuous)",
                },
                {"code": "CY", "definition": "year", "display": "year"},
                {
                    "code": "D",
                    "definition": "day of the month",
                    "display": "day of the month",
                },
                {
                    "code": "DW",
                    "definition": "day of the week (begins with Monday)",
                    "display": "day of the week (begins with Monday)",
                },
                {
                    "code": "H",
                    "definition": "hour of the day",
                    "display": "hour of the day",
                },
                {
                    "code": "M",
                    "definition": "month of the year",
                    "display": "month of the year",
                },
                {
                    "code": "N",
                    "definition": "minute of the hour",
                    "display": "minute of the hour",
                },
                {
                    "code": "S",
                    "definition": "second of the minute",
                    "display": "second of the minute",
                },
            ],
            "definition": "CalendarCycleOneLetter",
            "display": "CalendarCycleOneLetter",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "status", "valueCode": "deprecated"},
                {"code": "deprecationDate", "valueDateTime": "2013-06-29"},
            ],
        }
    )
    """
    CalendarCycleOneLetter

    CalendarCycleOneLetter
    """

    underscore_calendar_cycle_two_letter = CodeSystemConcept(
        {
            "code": "_CalendarCycleTwoLetter",
            "concept": [
                {
                    "code": "CD",
                    "definition": "day (continuous)",
                    "display": "day (continuous)",
                },
                {
                    "code": "CH",
                    "definition": "hour (continuous)",
                    "display": "hour (continuous)",
                },
                {
                    "code": "CM",
                    "definition": "month (continuous)",
                    "display": "month (continuous)",
                },
                {
                    "code": "CN",
                    "definition": "minute (continuous)",
                    "display": "minute (continuous)",
                },
                {
                    "code": "CS",
                    "definition": "second (continuous)",
                    "display": "second (continuous)",
                },
                {
                    "code": "DY",
                    "definition": "day of the year",
                    "display": "day of the year",
                },
                {
                    "code": "WY",
                    "definition": "week of the year",
                    "display": "week of the year",
                },
            ],
            "definition": "CalendarCycleTwoLetter",
            "display": "CalendarCycleTwoLetter",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "status", "valueCode": "deprecated"},
                {"code": "deprecationDate", "valueDateTime": "2013-06-29"},
                {"code": "child", "valueCode": "CW"},
                {"code": "child", "valueCode": "CY"},
                {"code": "child", "valueCode": "D"},
                {"code": "child", "valueCode": "DW"},
                {"code": "child", "valueCode": "H"},
                {"code": "child", "valueCode": "M"},
                {"code": "child", "valueCode": "N"},
                {"code": "child", "valueCode": "S"},
            ],
        }
    )
    """
    CalendarCycleTwoLetter

    CalendarCycleTwoLetter
    """

    wm = CodeSystemConcept(
        {
            "code": "WM",
            "definition": "The week with the month's first Thursday in it (analagous to the ISO 8601 definition for week of the year).",
            "display": "week of the month",
        }
    )
    """
    week of the month

    The week with the month's first Thursday in it (analagous to the ISO 8601 definition for week of the year).
    """

    class Meta:
        resource = _resource
