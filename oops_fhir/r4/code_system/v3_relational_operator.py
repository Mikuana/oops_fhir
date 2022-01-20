from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3RelationalOperator"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3RelationalOperator:
    """
    v3 Code System RelationalOperator

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-RelationalOperator
    """

    ct = CodeSystemConcept(
        {
            "code": "CT",
            "definition": "Specified set of things includes value being evaluated.",
            "display": "Contains",
        }
    )
    """
    Contains

    Specified set of things includes value being evaluated.
    """

    eq = CodeSystemConcept(
        {
            "code": "EQ",
            "definition": "Equal condition applied to comparisons.",
            "display": "Equal",
        }
    )
    """
    Equal

    Equal condition applied to comparisons.
    """

    ge = CodeSystemConcept(
        {
            "code": "GE",
            "definition": "Greater than or equal condition applied to comparisons.",
            "display": "Greater than or equal",
        }
    )
    """
    Greater than or equal

    Greater than or equal condition applied to comparisons.
    """

    gn = CodeSystemConcept(
        {
            "code": "GN",
            "definition": "A generic comparison selects a record for inclusion in the response if the beginning of the designated element value matches the select string.",
            "display": "Generic",
        }
    )
    """
    Generic

    A generic comparison selects a record for inclusion in the response if the beginning of the designated element value matches the select string.
    """

    gt = CodeSystemConcept(
        {
            "code": "GT",
            "definition": "Greater than condition applied to comparisons.",
            "display": "Greater than",
        }
    )
    """
    Greater than

    Greater than condition applied to comparisons.
    """

    le = CodeSystemConcept(
        {
            "code": "LE",
            "definition": "Less than or equal condition applied to comparisons.",
            "display": "Less than or equal",
        }
    )
    """
    Less than or equal

    Less than or equal condition applied to comparisons.
    """

    lt = CodeSystemConcept(
        {
            "code": "LT",
            "definition": "Less than condition applied to comparisons.",
            "display": "Less than",
        }
    )
    """
    Less than

    Less than condition applied to comparisons.
    """

    ne = CodeSystemConcept(
        {
            "code": "NE",
            "definition": "Not equal condition applied to comparisons.",
            "display": "Not Equal",
        }
    )
    """
    Not Equal

    Not equal condition applied to comparisons.
    """

    class Meta:
        resource = _resource
