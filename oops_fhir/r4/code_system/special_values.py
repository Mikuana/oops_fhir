from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SpecialValues"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SpecialValues:
    """
    SpecialValues

    A set of generally useful codes defined so they can be included in value
sets.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/special-values
    """

    true = CodeSystemConcept(
        {"code": "true", "definition": "Boolean true.", "display": "true"}
    )
    """
    true

    Boolean true.
    """

    false = CodeSystemConcept(
        {"code": "false", "definition": "Boolean false.", "display": "false"}
    )
    """
    false

    Boolean false.
    """

    trace = CodeSystemConcept(
        {
            "code": "trace",
            "definition": "The content is greater than zero, but too small to be quantified.",
            "display": "Trace Amount Detected",
        }
    )
    """
    Trace Amount Detected

    The content is greater than zero, but too small to be quantified.
    """

    sufficient = CodeSystemConcept(
        {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments",
                    "valueString": "used in formulations (e.g. 'Add 10mg of ingredient X, 50mg of ingredient Y, and sufficient quantity of water to 100mL.' This code would be used to express the quantity of water. )",
                }
            ],
            "code": "sufficient",
            "definition": "The specific quantity is not known, but is known to be non-zero and is not specified because it makes up the bulk of the material.",
            "display": "Sufficient Quantity",
        }
    )
    """
    Sufficient Quantity

    The specific quantity is not known, but is known to be non-zero and is not specified because it makes up the bulk of the material.
    """

    withdrawn = CodeSystemConcept(
        {
            "code": "withdrawn",
            "definition": "The value is no longer available.",
            "display": "Value Withdrawn",
        }
    )
    """
    Value Withdrawn

    The value is no longer available.
    """

    nil_known = CodeSystemConcept(
        {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments",
                    "valueString": "The existence of this subject to review",
                }
            ],
            "code": "nil-known",
            "definition": "The are no known applicable values in this context.",
            "display": "Nil Known",
        }
    )
    """
    Nil Known

    The are no known applicable values in this context.
    """

    class Meta:
        resource = _resource
