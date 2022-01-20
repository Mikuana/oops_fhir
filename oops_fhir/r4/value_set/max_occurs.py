from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.max_occurs import MaxOccurs as MaxOccurs_


__all__ = ["MaxOccurs"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MaxOccurs(MaxOccurs_):
    """
    MaxOccurs

    Flags an element as having unlimited repetitions.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/question-max-occurs
    """

    class Meta:
        resource = _resource
