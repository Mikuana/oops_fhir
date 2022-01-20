from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["KnowledgeResourceType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class KnowledgeResourceType:
    """
    KnowledgeResourceType

    A list of all the knowledge resource types defined in this version of
the FHIR specification.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/knowledge-resource-types
    """

    activity_definition = CodeSystemConcept(
        {
            "code": "ActivityDefinition",
            "definition": "The definition of a specific activity to be taken, independent of any particular patient or context.",
            "display": "ActivityDefinition",
        }
    )
    """
    ActivityDefinition

    The definition of a specific activity to be taken, independent of any particular patient or context.
    """

    code_system = CodeSystemConcept(
        {
            "code": "CodeSystem",
            "definition": "A set of codes drawn from one or more code systems.",
            "display": "CodeSystem",
        }
    )
    """
    CodeSystem

    A set of codes drawn from one or more code systems.
    """

    concept_map = CodeSystemConcept(
        {
            "code": "ConceptMap",
            "definition": "A map from one set of concepts to one or more other concepts.",
            "display": "ConceptMap",
        }
    )
    """
    ConceptMap

    A map from one set of concepts to one or more other concepts.
    """

    library = CodeSystemConcept(
        {
            "code": "Library",
            "definition": "Represents a library of quality improvement components.",
            "display": "Library",
        }
    )
    """
    Library

    Represents a library of quality improvement components.
    """

    measure = CodeSystemConcept(
        {
            "code": "Measure",
            "definition": "A quality measure definition.",
            "display": "Measure",
        }
    )
    """
    Measure

    A quality measure definition.
    """

    plan_definition = CodeSystemConcept(
        {
            "code": "PlanDefinition",
            "definition": "The definition of a plan for a series of actions, independent of any specific patient or context.",
            "display": "PlanDefinition",
        }
    )
    """
    PlanDefinition

    The definition of a plan for a series of actions, independent of any specific patient or context.
    """

    structure_definition = CodeSystemConcept(
        {
            "code": "StructureDefinition",
            "definition": "Structural Definition.",
            "display": "StructureDefinition",
        }
    )
    """
    StructureDefinition

    Structural Definition.
    """

    structure_map = CodeSystemConcept(
        {
            "code": "StructureMap",
            "definition": "A Map of relationships between 2 factory that can be used to transform data.",
            "display": "StructureMap",
        }
    )
    """
    StructureMap

    A Map of relationships between 2 factory that can be used to transform data.
    """

    value_set = CodeSystemConcept(
        {
            "code": "ValueSet",
            "definition": "A set of codes drawn from one or more code systems.",
            "display": "ValueSet",
        }
    )
    """
    ValueSet

    A set of codes drawn from one or more code systems.
    """

    class Meta:
        resource = _resource
