from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.graph_compartment_rule import (
    GraphCompartmentRule as GraphCompartmentRule_,
)


__all__ = ["GraphCompartmentRule"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class GraphCompartmentRule(GraphCompartmentRule_):
    """
    GraphCompartmentRule

    How a compartment must be linked.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/graph-compartment-rule
    """

    class Meta:
        resource = _resource
