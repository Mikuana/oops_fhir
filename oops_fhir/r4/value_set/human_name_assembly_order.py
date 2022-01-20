from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.human_name_assembly_order import (
    HumanNameAssemblyOrder as HumanNameAssemblyOrder_,
)


__all__ = ["HumanNameAssemblyOrder"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class HumanNameAssemblyOrder(ValueSet):
    """
    HumanNameAssemblyOrder

    A code that represents the preferred display order of the components of
a human name.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/name-assembly-order
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
