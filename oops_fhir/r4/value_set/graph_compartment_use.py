from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.graph_compartment_use import (
    GraphCompartmentUse as GraphCompartmentUse_,
)


__all__ = ["GraphCompartmentUse"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class GraphCompartmentUse(GraphCompartmentUse_):
    """
    GraphCompartmentUse

    Defines how a compartment rule is used.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/graph-compartment-use
    """

    class Meta:
        resource = _resource
