from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["ConditionStageType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConditionStageType(ValueSet):
    """
    Condition Stage Type

    Example value set for the type of stages of cancer and other conditions

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/condition-stage-type
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
