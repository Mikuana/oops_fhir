from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DefinitionUseCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DefinitionUseCodes:
    """
    Structure Definition Use Codes / Keywords

    Structure Definition Use Codes / Keywords

    Status: active - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/definition-use
    """

    fhir_structure = CodeSystemConcept(
        {
            "code": "fhir-structure",
            "definition": "This structure is defined as part of the base FHIR Specification",
            "display": "FHIR Structure",
        }
    )
    """
    FHIR Structure

    This structure is defined as part of the base FHIR Specification
    """

    custom_resource = CodeSystemConcept(
        {
            "code": "custom-resource",
            "definition": "This structure is intended to be treated like a FHIR resource (e.g. on the FHIR API)",
            "display": "Custom Resource",
        }
    )
    """
    Custom Resource

    This structure is intended to be treated like a FHIR resource (e.g. on the FHIR API)
    """

    dam = CodeSystemConcept(
        {
            "code": "dam",
            "definition": "This structure captures an analysis of a domain",
            "display": "Domain Analysis Model",
        }
    )
    """
    Domain Analysis Model

    This structure captures an analysis of a domain
    """

    wire_format = CodeSystemConcept(
        {
            "code": "wire-format",
            "definition": "This structure represents and existing structure (e.g. CDA, HL7 v2)",
            "display": "Wire Format",
        }
    )
    """
    Wire Format

    This structure represents and existing structure (e.g. CDA, HL7 v2)
    """

    archetype = CodeSystemConcept(
        {
            "code": "archetype",
            "definition": "This structure captures an analysis of a domain",
            "display": "Domain Analysis Model",
        }
    )
    """
    Domain Analysis Model

    This structure captures an analysis of a domain
    """

    template = CodeSystemConcept(
        {
            "code": "template",
            "definition": "This structure is a template (n.b: 'template' has many meanings)",
            "display": "Template",
        }
    )
    """
    Template

    This structure is a template (n.b: 'template' has many meanings)
    """

    class Meta:
        resource = _resource
