from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["PlanDefinitionType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class PlanDefinitionType:
    """
    PlanDefinitionType

    The type of PlanDefinition.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/plan-definition-type
    """

    order_set = CodeSystemConcept(
        {
            "code": "order-set",
            "definition": "A pre-defined and approved group of orders related to a particular clinical condition (e.g. hypertension treatment and monitoring) or stage of care (e.g. hospital admission to Coronary Care Unit). An order set is used as a checklist for the clinician when managing a patient with a specific condition. It is a structured collection of orders relevant to that condition and presented to the clinician in a computerized provider order entry (CPOE) system.",
            "display": "Order Set",
        }
    )
    """
    Order Set

    A pre-defined and approved group of orders related to a particular clinical condition (e.g. hypertension treatment and monitoring) or stage of care (e.g. hospital admission to Coronary Care Unit). An order set is used as a checklist for the clinician when managing a patient with a specific condition. It is a structured collection of orders relevant to that condition and presented to the clinician in a computerized provider order entry (CPOE) system.
    """

    clinical_protocol = CodeSystemConcept(
        {
            "code": "clinical-protocol",
            "definition": "Defines a desired/typical sequence of clinical activities including preconditions, triggers and temporal relationships.",
            "display": "Clinical Protocol",
        }
    )
    """
    Clinical Protocol

    Defines a desired/typical sequence of clinical activities including preconditions, triggers and temporal relationships.
    """

    eca_rule = CodeSystemConcept(
        {
            "code": "eca-rule",
            "definition": "A decision support rule of the form [on Event] if Condition then Action. It is intended to be a shareable, computable definition of actions that should be taken whenever some condition is met in response to a particular event or events.",
            "display": "ECA Rule",
        }
    )
    """
    ECA Rule

    A decision support rule of the form [on Event] if Condition then Action. It is intended to be a shareable, computable definition of actions that should be taken whenever some condition is met in response to a particular event or events.
    """

    workflow_definition = CodeSystemConcept(
        {
            "code": "workflow-definition",
            "definition": "Defines the steps for a group of one or more systems in an event flow process along with the step constraints, sequence, pre-conditions and decision points to complete a particular objective.",
            "display": "Workflow Definition",
        }
    )
    """
    Workflow Definition

    Defines the steps for a group of one or more systems in an event flow process along with the step constraints, sequence, pre-conditions and decision points to complete a particular objective.
    """

    class Meta:
        resource = _resource
