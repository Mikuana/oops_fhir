from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.example_scenario_actor_type import (
    ExampleScenarioActorType as ExampleScenarioActorType_,
)


__all__ = ["ExampleScenarioActorType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExampleScenarioActorType(ExampleScenarioActorType_):
    """
    ExampleScenarioActorType

    The type of actor - system or human.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/examplescenario-actor-type
    """

    class Meta:
        resource = _resource
