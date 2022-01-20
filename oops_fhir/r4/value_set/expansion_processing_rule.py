from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.expansion_processing_rule import (
    ExpansionProcessingRule as ExpansionProcessingRule_,
)


__all__ = ["ExpansionProcessingRule"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExpansionProcessingRule(ExpansionProcessingRule_):
    """
    ExpansionProcessingRule

    Defines how concepts are processed into the expansion when it's for UI
presentation.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/expansion-processing-rule
    """

    class Meta:
        resource = _resource
