from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AssertionOperatorType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AssertionOperatorType:
    """
    AssertionOperatorType

    The type of operator to use for assertion.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/assert-operator-codes
    """

    equals = CodeSystemConcept(
        {
            "code": "equals",
            "definition": "Default value. Equals comparison.",
            "display": "equals",
        }
    )
    """
    equals

    Default value. Equals comparison.
    """

    not_equals = CodeSystemConcept(
        {
            "code": "notEquals",
            "definition": "Not equals comparison.",
            "display": "notEquals",
        }
    )
    """
    notEquals

    Not equals comparison.
    """

    in_ = CodeSystemConcept(
        {
            "code": "in",
            "definition": "Compare value within a known set of values.",
            "display": "in",
        }
    )
    """
    in

    Compare value within a known set of values.
    """

    not_in = CodeSystemConcept(
        {
            "code": "notIn",
            "definition": "Compare value not within a known set of values.",
            "display": "notIn",
        }
    )
    """
    notIn

    Compare value not within a known set of values.
    """

    greater_than = CodeSystemConcept(
        {
            "code": "greaterThan",
            "definition": "Compare value to be greater than a known value.",
            "display": "greaterThan",
        }
    )
    """
    greaterThan

    Compare value to be greater than a known value.
    """

    less_than = CodeSystemConcept(
        {
            "code": "lessThan",
            "definition": "Compare value to be less than a known value.",
            "display": "lessThan",
        }
    )
    """
    lessThan

    Compare value to be less than a known value.
    """

    empty = CodeSystemConcept(
        {"code": "empty", "definition": "Compare value is empty.", "display": "empty"}
    )
    """
    empty

    Compare value is empty.
    """

    not_empty = CodeSystemConcept(
        {
            "code": "notEmpty",
            "definition": "Compare value is not empty.",
            "display": "notEmpty",
        }
    )
    """
    notEmpty

    Compare value is not empty.
    """

    contains = CodeSystemConcept(
        {
            "code": "contains",
            "definition": "Compare value string contains a known value.",
            "display": "contains",
        }
    )
    """
    contains

    Compare value string contains a known value.
    """

    not_contains = CodeSystemConcept(
        {
            "code": "notContains",
            "definition": "Compare value string does not contain a known value.",
            "display": "notContains",
        }
    )
    """
    notContains

    Compare value string does not contain a known value.
    """

    eval_ = CodeSystemConcept(
        {
            "code": "eval",
            "definition": "Evaluate the FHIRPath expression as a boolean condition.",
            "display": "evaluate",
        }
    )
    """
    evaluate

    Evaluate the FHIRPath expression as a boolean condition.
    """

    class Meta:
        resource = _resource
