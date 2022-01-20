from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExampleScenarioActorType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExampleScenarioActorType:
    """
    ExampleScenarioActorType

    The type of actor - system or human.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/examplescenario-actor-type
    """

    person = CodeSystemConcept(
        {"code": "person", "definition": "A person.", "display": "Person"}
    )
    """
    Person

    A person.
    """

    entity = CodeSystemConcept(
        {"code": "entity", "definition": "A system.", "display": "System"}
    )
    """
    System

    A system.
    """

    class Meta:
        resource = _resource
