from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["GraphCompartmentRule"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class GraphCompartmentRule:
    """
    GraphCompartmentRule

    How a compartment must be linked.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/graph-compartment-rule
    """

    identical = CodeSystemConcept(
        {
            "code": "identical",
            "definition": "The compartment must be identical (the same literal reference).",
            "display": "Identical",
        }
    )
    """
    Identical

    The compartment must be identical (the same literal reference).
    """

    matching = CodeSystemConcept(
        {
            "code": "matching",
            "definition": "The compartment must be the same - the record must be about the same patient, but the reference may be different.",
            "display": "Matching",
        }
    )
    """
    Matching

    The compartment must be the same - the record must be about the same patient, but the reference may be different.
    """

    different = CodeSystemConcept(
        {
            "code": "different",
            "definition": "The compartment must be different.",
            "display": "Different",
        }
    )
    """
    Different

    The compartment must be different.
    """

    custom = CodeSystemConcept(
        {
            "code": "custom",
            "definition": "The compartment rule is defined in the accompanying FHIRPath expression.",
            "display": "Custom",
        }
    )
    """
    Custom

    The compartment rule is defined in the accompanying FHIRPath expression.
    """

    class Meta:
        resource = _resource
