from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ReferenceVersionRules"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ReferenceVersionRules:
    """
    ReferenceVersionRules

    Whether a reference needs to be version specific or version independent,
or whether either can be used.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/reference-version-rules
    """

    either = CodeSystemConcept(
        {
            "code": "either",
            "definition": "The reference may be either version independent or version specific.",
            "display": "Either Specific or independent",
        }
    )
    """
    Either Specific or independent

    The reference may be either version independent or version specific.
    """

    independent = CodeSystemConcept(
        {
            "code": "independent",
            "definition": "The reference must be version independent.",
            "display": "Version independent",
        }
    )
    """
    Version independent

    The reference must be version independent.
    """

    specific = CodeSystemConcept(
        {
            "code": "specific",
            "definition": "The reference must be version specific.",
            "display": "Version Specific",
        }
    )
    """
    Version Specific

    The reference must be version specific.
    """

    class Meta:
        resource = _resource
