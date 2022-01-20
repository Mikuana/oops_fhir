from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["UDIEntryType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class UDIEntryType:
    """
    UDIEntryType

    Codes to identify how UDI data was entered.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/udi-entry-type
    """

    barcode = CodeSystemConcept(
        {
            "code": "barcode",
            "definition": "a barcodescanner captured the data from the device label.",
            "display": "Barcode",
        }
    )
    """
    Barcode

    a barcodescanner captured the data from the device label.
    """

    rfid = CodeSystemConcept(
        {
            "code": "rfid",
            "definition": "An RFID chip reader captured the data from the device label.",
            "display": "RFID",
        }
    )
    """
    RFID

    An RFID chip reader captured the data from the device label.
    """

    manual = CodeSystemConcept(
        {
            "code": "manual",
            "definition": "The data was read from the label by a person and manually entered. (e.g.  via a keyboard).",
            "display": "Manual",
        }
    )
    """
    Manual

    The data was read from the label by a person and manually entered. (e.g.  via a keyboard).
    """

    card = CodeSystemConcept(
        {
            "code": "card",
            "definition": "The data originated from a patient's implant card and was read by an operator.",
            "display": "Card",
        }
    )
    """
    Card

    The data originated from a patient's implant card and was read by an operator.
    """

    self_reported = CodeSystemConcept(
        {
            "code": "self-reported",
            "definition": "The data originated from a patient source and was not directly scanned or read from a label or card.",
            "display": "Self Reported",
        }
    )
    """
    Self Reported

    The data originated from a patient source and was not directly scanned or read from a label or card.
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": "The method of data capture has not been determined.",
            "display": "Unknown",
        }
    )
    """
    Unknown

    The method of data capture has not been determined.
    """

    class Meta:
        resource = _resource
