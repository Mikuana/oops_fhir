from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["RequestIntent"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class RequestIntent:
    """
    RequestIntent

    Codes indicating the degree of authority/intentionality associated with
a request.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/request-intent
    """

    proposal = CodeSystemConcept(
        {
            "code": "proposal",
            "definition": "The request is a suggestion made by someone/something that does not have an intention to ensure it occurs and without providing an authorization to act.",
            "display": "Proposal",
        }
    )
    """
    Proposal

    The request is a suggestion made by someone/something that does not have an intention to ensure it occurs and without providing an authorization to act.
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

    directive = CodeSystemConcept(
        {
            "code": "directive",
            "definition": "The request represents a legally binding instruction authored by a Patient or RelatedPerson.",
            "display": "Directive",
        }
    )
    """
    Directive

    The request represents a legally binding instruction authored by a Patient or RelatedPerson.
    """

    order = CodeSystemConcept(
        {
            "code": "order",
            "concept": [
                {
                    "code": "original-order",
                    "definition": "The request represents an original authorization for action.",
                    "display": "Original Order",
                },
                {
                    "code": "reflex-order",
                    "definition": "The request represents an automatically generated supplemental authorization for action based on a parent authorization together with initial results of the action taken against that parent authorization.",
                    "display": "Reflex Order",
                },
                {
                    "code": "filler-order",
                    "concept": [
                        {
                            "code": "instance-order",
                            "definition": "An order created in fulfillment of a broader order that represents the authorization for a single activity occurrence.  E.g. The administration of a single dose of a drug.",
                            "display": "Instance Order",
                        }
                    ],
                    "definition": "The request represents the view of an authorization instantiated by a fulfilling system representing the details of the fulfiller's intention to act upon a submitted order.",
                    "display": "Filler Order",
                },
            ],
            "definition": "The request represents a request/demand and authorization for action by a Practitioner.",
            "display": "Order",
        }
    )
    """
    Order

    The request represents a request/demand and authorization for action by a Practitioner.
    """

    option = CodeSystemConcept(
        {
            "code": "option",
            "definition": "The request represents a component or option for a RequestGroup that establishes timing, conditionality and/or other constraints among a set of requests.  Refer to [[[RequestGroup]]] for additional information on how this status is used.",
            "display": "Option",
        }
    )
    """
    Option

    The request represents a component or option for a RequestGroup that establishes timing, conditionality and/or other constraints among a set of requests.  Refer to [[[RequestGroup]]] for additional information on how this status is used.
    """

    class Meta:
        resource = _resource
