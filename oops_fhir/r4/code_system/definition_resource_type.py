from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DefinitionResourceType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DefinitionResourceType:
    """
    DefinitionResourceType

    A list of all the definition resource types defined in this version of
the FHIR specification.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/definition-resource-types
    """

    activity_definition = CodeSystemConcept(
        {
            "code": "ActivityDefinition",
            "definition": "This resource allows for the definition of some activity to be performed, independent of a particular patient, practitioner, or other performance context.",
            "display": "ActivityDefinition",
        }
    )
    """
    ActivityDefinition

    This resource allows for the definition of some activity to be performed, independent of a particular patient, practitioner, or other performance context.
    """

    event_definition = CodeSystemConcept(
        {
            "code": "EventDefinition",
            "definition": "The EventDefinition resource provides a reusable description of when a particular event can occur.",
            "display": "EventDefinition",
        }
    )
    """
    EventDefinition

    The EventDefinition resource provides a reusable description of when a particular event can occur.
    """

    measure = CodeSystemConcept(
        {
            "code": "Measure",
            "definition": "The Measure resource provides the definition of a quality measure.",
            "display": "Measure",
        }
    )
    """
    Measure

    The Measure resource provides the definition of a quality measure.
    """

    operation_definition = CodeSystemConcept(
        {
            "code": "OperationDefinition",
            "definition": "A formal computable definition of an operation (on the RESTful interface) or a named query (using the search interaction).",
            "display": "OperationDefinition",
        }
    )
    """
    OperationDefinition

    A formal computable definition of an operation (on the RESTful interface) or a named query (using the search interaction).
    """

    plan_definition = CodeSystemConcept(
        {
            "code": "PlanDefinition",
            "definition": "This resource allows for the definition of various types of plans as a sharable, consumable, and executable artifact. The resource is general enough to support the description of a broad range of clinical artifacts such as clinical decision support rules, order sets and protocols.",
            "display": "PlanDefinition",
        }
    )
    """
    PlanDefinition

    This resource allows for the definition of various types of plans as a sharable, consumable, and executable artifact. The resource is general enough to support the description of a broad range of clinical artifacts such as clinical decision support rules, order sets and protocols.
    """

    questionnaire = CodeSystemConcept(
        {
            "code": "Questionnaire",
            "definition": "A structured set of questions intended to guide the collection of answers from end-users. Questionnaires provide detailed control over order, presentation, phraseology and grouping to allow coherent, consistent data collection.",
            "display": "Questionnaire",
        }
    )
    """
    Questionnaire

    A structured set of questions intended to guide the collection of answers from end-users. Questionnaires provide detailed control over order, presentation, phraseology and grouping to allow coherent, consistent data collection.
    """

    class Meta:
        resource = _resource
