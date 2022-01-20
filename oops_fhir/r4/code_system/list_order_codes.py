from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ListOrderCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ListOrderCodes:
    """
    List Order Codes

    Base values for the order of the items in a list resource.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/list-order
    """

    user = CodeSystemConcept(
        {
            "code": "user",
            "definition": "The list was sorted by a user. The criteria the user used are not specified.",
            "display": "Sorted by User",
        }
    )
    """
    Sorted by User

    The list was sorted by a user. The criteria the user used are not specified.
    """

    system = CodeSystemConcept(
        {
            "code": "system",
            "definition": "The list was sorted by the system. The criteria the user used are not specified; define additional codes to specify a particular order (or use other defined codes).",
            "display": "Sorted by System",
        }
    )
    """
    Sorted by System

    The list was sorted by the system. The criteria the user used are not specified; define additional codes to specify a particular order (or use other defined codes).
    """

    event_date = CodeSystemConcept(
        {
            "code": "event-date",
            "definition": "The list is sorted by the data of the event. This can be used when the list has items which are dates with past or future events.",
            "display": "Sorted by Event Date",
        }
    )
    """
    Sorted by Event Date

    The list is sorted by the data of the event. This can be used when the list has items which are dates with past or future events.
    """

    entry_date = CodeSystemConcept(
        {
            "code": "entry-date",
            "definition": "The list is sorted by the date the item was added to the list. Note that the date added to the list is not explicit in the list itself.",
            "display": "Sorted by Item Date",
        }
    )
    """
    Sorted by Item Date

    The list is sorted by the date the item was added to the list. Note that the date added to the list is not explicit in the list itself.
    """

    priority = CodeSystemConcept(
        {
            "code": "priority",
            "definition": "The list is sorted by priority. The exact method in which priority has been determined is not specified.",
            "display": "Sorted by Priority",
        }
    )
    """
    Sorted by Priority

    The list is sorted by priority. The exact method in which priority has been determined is not specified.
    """

    alphabetic = CodeSystemConcept(
        {
            "code": "alphabetic",
            "definition": "The list is sorted alphabetically by an unspecified property of the items in the list.",
            "display": "Sorted Alphabetically",
        }
    )
    """
    Sorted Alphabetically

    The list is sorted alphabetically by an unspecified property of the items in the list.
    """

    category = CodeSystemConcept(
        {
            "code": "category",
            "definition": "The list is sorted categorically by an unspecified property of the items in the list.",
            "display": "Sorted by Category",
        }
    )
    """
    Sorted by Category

    The list is sorted categorically by an unspecified property of the items in the list.
    """

    patient = CodeSystemConcept(
        {
            "code": "patient",
            "definition": "The list is sorted by patient, with items for each patient grouped together.",
            "display": "Sorted by Patient",
        }
    )
    """
    Sorted by Patient

    The list is sorted by patient, with items for each patient grouped together.
    """

    class Meta:
        resource = _resource
