from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ObservationDataType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ObservationDataType:
    """
    ObservationDataType

    Permitted data type for observation value.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/permitted-data-type
    """

    quantity = CodeSystemConcept(
        {"code": "Quantity", "definition": "A measured amount.", "display": "Quantity"}
    )
    """
    Quantity

    A measured amount.
    """

    codeable_concept = CodeSystemConcept(
        {
            "code": "CodeableConcept",
            "definition": "A coded concept from a reference terminology and/or text.",
            "display": "CodeableConcept",
        }
    )
    """
    CodeableConcept

    A coded concept from a reference terminology and/or text.
    """

    string = CodeSystemConcept(
        {
            "code": "string",
            "definition": "A sequence of Unicode characters.",
            "display": "string",
        }
    )
    """
    string

    A sequence of Unicode characters.
    """

    boolean = CodeSystemConcept(
        {"code": "boolean", "definition": "true or false.", "display": "boolean"}
    )
    """
    boolean

    true or false.
    """

    integer = CodeSystemConcept(
        {"code": "integer", "definition": "A signed integer.", "display": "integer"}
    )
    """
    integer

    A signed integer.
    """

    range_ = CodeSystemConcept(
        {
            "code": "Range",
            "definition": "A set of values bounded by low and high.",
            "display": "Range",
        }
    )
    """
    Range

    A set of values bounded by low and high.
    """

    ratio = CodeSystemConcept(
        {
            "code": "Ratio",
            "definition": "A ratio of two Quantity values - a numerator and a denominator.",
            "display": "Ratio",
        }
    )
    """
    Ratio

    A ratio of two Quantity values - a numerator and a denominator.
    """

    sampled_data = CodeSystemConcept(
        {
            "code": "SampledData",
            "definition": "A series of measurements taken by a device.",
            "display": "SampledData",
        }
    )
    """
    SampledData

    A series of measurements taken by a device.
    """

    time = CodeSystemConcept(
        {
            "code": "time",
            "definition": "A time during the day, in the format hh:mm:ss.",
            "display": "time",
        }
    )
    """
    time

    A time during the day, in the format hh:mm:ss.
    """

    date_time = CodeSystemConcept(
        {
            "code": "dateTime",
            "definition": "A date, date-time or partial date (e.g. just year or year + month) as used in human communication.",
            "display": "dateTime",
        }
    )
    """
    dateTime

    A date, date-time or partial date (e.g. just year or year + month) as used in human communication.
    """

    period = CodeSystemConcept(
        {
            "code": "Period",
            "definition": "A time range defined by start and end date/time.",
            "display": "Period",
        }
    )
    """
    Period

    A time range defined by start and end date/time.
    """

    class Meta:
        resource = _resource
