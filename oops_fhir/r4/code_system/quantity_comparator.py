from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["QuantityComparator"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class QuantityComparator:
    """
    QuantityComparator

    How the Quantity should be understood and represented.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/quantity-comparator
    """

    less_than = CodeSystemConcept(
        {
            "code": "<",
            "definition": "The actual value is less than the given value.",
            "display": "Less than",
        }
    )
    """
    Less than

    The actual value is less than the given value.
    """

    less_than = CodeSystemConcept(
        {
            "code": "<=",
            "definition": "The actual value is less than or equal to the given value.",
            "display": "Less or Equal to",
        }
    )
    """
    Less or Equal to

    The actual value is less than or equal to the given value.
    """

    greater_than = CodeSystemConcept(
        {
            "code": ">=",
            "definition": "The actual value is greater than or equal to the given value.",
            "display": "Greater or Equal to",
        }
    )
    """
    Greater or Equal to

    The actual value is greater than or equal to the given value.
    """

    greater_than = CodeSystemConcept(
        {
            "code": ">",
            "definition": "The actual value is greater than the given value.",
            "display": "Greater than",
        }
    )
    """
    Greater than

    The actual value is greater than the given value.
    """

    class Meta:
        resource = _resource
