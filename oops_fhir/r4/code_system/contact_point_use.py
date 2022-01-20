from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContactPointUse"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContactPointUse:
    """
    ContactPointUse

    Use of contact point.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/contact-point-use
    """

    home = CodeSystemConcept(
        {
            "code": "home",
            "definition": "A communication contact point at a home; attempted contacts for business purposes might intrude privacy and chances are one will contact family or other household members instead of the person one wishes to call. Typically used with urgent cases, or if no other contacts are available.",
            "display": "Home",
        }
    )
    """
    Home

    A communication contact point at a home; attempted contacts for business purposes might intrude privacy and chances are one will contact family or other household members instead of the person one wishes to call. Typically used with urgent cases, or if no other contacts are available.
    """

    work = CodeSystemConcept(
        {
            "code": "work",
            "definition": "An office contact point. First choice for business related contacts during business hours.",
            "display": "Work",
        }
    )
    """
    Work

    An office contact point. First choice for business related contacts during business hours.
    """

    temp = CodeSystemConcept(
        {
            "code": "temp",
            "definition": "A temporary contact point. The period can provide more detailed information.",
            "display": "Temp",
        }
    )
    """
    Temp

    A temporary contact point. The period can provide more detailed information.
    """

    old = CodeSystemConcept(
        {
            "code": "old",
            "definition": "This contact point is no longer in use (or was never correct, but retained for records).",
            "display": "Old",
        }
    )
    """
    Old

    This contact point is no longer in use (or was never correct, but retained for records).
    """

    mobile = CodeSystemConcept(
        {
            "code": "mobile",
            "definition": "A telecommunication device that moves and stays with its owner. May have characteristics of all other use codes, suitable for urgent matters, not the first choice for routine business.",
            "display": "Mobile",
        }
    )
    """
    Mobile

    A telecommunication device that moves and stays with its owner. May have characteristics of all other use codes, suitable for urgent matters, not the first choice for routine business.
    """

    class Meta:
        resource = _resource
