from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.slicing_rules import SlicingRules as SlicingRules_


__all__ = ["SlicingRules"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SlicingRules(SlicingRules_):
    """
    SlicingRules

    How slices are interpreted when evaluating an instance.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/resource-slicing-rules
    """

    class Meta:
        resource = _resource
