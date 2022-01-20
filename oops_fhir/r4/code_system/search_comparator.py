from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SearchComparator"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SearchComparator:
    """
    SearchComparator

    What Search Comparator Codes are supported in search.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/search-comparator
    """

    eq = CodeSystemConcept(
        {
            "code": "eq",
            "definition": "the value for the parameter in the resource is equal to the provided value.",
            "display": "Equals",
        }
    )
    """
    Equals

    the value for the parameter in the resource is equal to the provided value.
    """

    ne = CodeSystemConcept(
        {
            "code": "ne",
            "definition": "the value for the parameter in the resource is not equal to the provided value.",
            "display": "Not Equals",
        }
    )
    """
    Not Equals

    the value for the parameter in the resource is not equal to the provided value.
    """

    gt = CodeSystemConcept(
        {
            "code": "gt",
            "definition": "the value for the parameter in the resource is greater than the provided value.",
            "display": "Greater Than",
        }
    )
    """
    Greater Than

    the value for the parameter in the resource is greater than the provided value.
    """

    lt = CodeSystemConcept(
        {
            "code": "lt",
            "definition": "the value for the parameter in the resource is less than the provided value.",
            "display": "Less Than",
        }
    )
    """
    Less Than

    the value for the parameter in the resource is less than the provided value.
    """

    ge = CodeSystemConcept(
        {
            "code": "ge",
            "definition": "the value for the parameter in the resource is greater or equal to the provided value.",
            "display": "Greater or Equals",
        }
    )
    """
    Greater or Equals

    the value for the parameter in the resource is greater or equal to the provided value.
    """

    le = CodeSystemConcept(
        {
            "code": "le",
            "definition": "the value for the parameter in the resource is less or equal to the provided value.",
            "display": "Less of Equal",
        }
    )
    """
    Less of Equal

    the value for the parameter in the resource is less or equal to the provided value.
    """

    sa = CodeSystemConcept(
        {
            "code": "sa",
            "definition": "the value for the parameter in the resource starts after the provided value.",
            "display": "Starts After",
        }
    )
    """
    Starts After

    the value for the parameter in the resource starts after the provided value.
    """

    eb = CodeSystemConcept(
        {
            "code": "eb",
            "definition": "the value for the parameter in the resource ends before the provided value.",
            "display": "Ends Before",
        }
    )
    """
    Ends Before

    the value for the parameter in the resource ends before the provided value.
    """

    ap = CodeSystemConcept(
        {
            "code": "ap",
            "definition": "the value for the parameter in the resource is approximately the same to the provided value.",
            "display": "Approximately",
        }
    )
    """
    Approximately

    the value for the parameter in the resource is approximately the same to the provided value.
    """

    class Meta:
        resource = _resource
