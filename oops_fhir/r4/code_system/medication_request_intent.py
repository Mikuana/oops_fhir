from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["medicationRequestIntent"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class medicationRequestIntent:
    """
    Medication request  intent

    MedicationRequest Intent Codes

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/CodeSystem/medicationrequest-intent
    """

    proposal = CodeSystemConcept(
        {
            "code": "proposal",
            "definition": "The request is a suggestion made by someone/something that doesn't have an intention to ensure it occurs and without providing an authorization to act",
            "display": "Proposal",
        }
    )
    """
    Proposal

    The request is a suggestion made by someone/something that doesn't have an intention to ensure it occurs and without providing an authorization to act
    """

    plan = CodeSystemConcept(
        {
            "code": "plan",
            "definition": "The request represents an intention to ensure something occurs without providing an authorization for others to act.",
            "display": "Plan",
        }
    )
    """
    Plan

    The request represents an intention to ensure something occurs without providing an authorization for others to act.
    """

    order = CodeSystemConcept(
        {
            "code": "order",
            "definition": "The request represents a request/demand and authorization for action",
            "display": "Order",
        }
    )
    """
    Order

    The request represents a request/demand and authorization for action
    """

    original_order = CodeSystemConcept(
        {
            "code": "original-order",
            "definition": "The request represents the original authorization for the medication request.",
            "display": "Original Order",
        }
    )
    """
    Original Order

    The request represents the original authorization for the medication request.
    """

    reflex_order = CodeSystemConcept(
        {
            "code": "reflex-order",
            "definition": "The request represents an automatically generated supplemental authorization for action based on a parent authorization together with initial results of the action taken against that parent authorization..",
            "display": "Reflex Order",
        }
    )
    """
    Reflex Order

    The request represents an automatically generated supplemental authorization for action based on a parent authorization together with initial results of the action taken against that parent authorization..
    """

    filler_order = CodeSystemConcept(
        {
            "code": "filler-order",
            "definition": "The request represents the view of an authorization instantiated by a fulfilling system representing the details of the fulfiller's intention to act upon a submitted order.",
            "display": "Filler Order",
        }
    )
    """
    Filler Order

    The request represents the view of an authorization instantiated by a fulfilling system representing the details of the fulfiller's intention to act upon a submitted order.
    """

    instance_order = CodeSystemConcept(
        {
            "code": "instance-order",
            "definition": "The request represents an instance for the particular order, for example a medication administration record.",
            "display": "Instance Order",
        }
    )
    """
    Instance Order

    The request represents an instance for the particular order, for example a medication administration record.
    """

    option = CodeSystemConcept(
        {
            "code": "option",
            "definition": "The request represents a component or option for a RequestGroup that establishes timing, conditionality and/or  other constraints among a set of requests.",
            "display": "Option",
        }
    )
    """
    Option

    The request represents a component or option for a RequestGroup that establishes timing, conditionality and/or  other constraints among a set of requests.
    """

    class Meta:
        resource = _resource
