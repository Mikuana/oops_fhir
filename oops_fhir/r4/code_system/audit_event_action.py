from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AuditEventAction"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AuditEventAction:
    """
    AuditEventAction

    Indicator for type of action performed during the event that generated
the event.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/audit-event-action
    """

    c = CodeSystemConcept(
        {
            "code": "C",
            "definition": "Create a new database object, such as placing an order.",
            "display": "Create",
        }
    )
    """
    Create

    Create a new database object, such as placing an order.
    """

    r = CodeSystemConcept(
        {
            "code": "R",
            "definition": "Display or print data, such as a doctor census.",
            "display": "Read/View/Print",
        }
    )
    """
    Read/View/Print

    Display or print data, such as a doctor census.
    """

    u = CodeSystemConcept(
        {
            "code": "U",
            "definition": "Update data, such as revise patient information.",
            "display": "Update",
        }
    )
    """
    Update

    Update data, such as revise patient information.
    """

    d = CodeSystemConcept(
        {
            "code": "D",
            "definition": "Delete items, such as a doctor master file record.",
            "display": "Delete",
        }
    )
    """
    Delete

    Delete items, such as a doctor master file record.
    """

    e = CodeSystemConcept(
        {
            "code": "E",
            "definition": "Perform a system or application function such as log-on, program execution or use of an object's method, or perform a query/search operation.",
            "display": "Execute",
        }
    )
    """
    Execute

    Perform a system or application function such as log-on, program execution or use of an object's method, or perform a query/search operation.
    """

    class Meta:
        resource = _resource
