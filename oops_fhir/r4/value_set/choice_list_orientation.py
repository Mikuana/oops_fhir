from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.choice_list_orientation import (
    ChoiceListOrientation as ChoiceListOrientation_,
)


__all__ = ["ChoiceListOrientation"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ChoiceListOrientation(ChoiceListOrientation_):
    """
    ChoiceListOrientation

    Direction in which lists of possible answers should be displayed.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/choice-list-orientation
    """

    class Meta:
        resource = _resource
