from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.activity_definition_category import (
    ActivityDefinitionCategory as ActivityDefinitionCategory_,
)


__all__ = ["ActivityDefinitionCategory"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ActivityDefinitionCategory(ActivityDefinitionCategory_):
    """
    ActivityDefinitionCategory

    High-level categorization of the type of activity.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/activity-definition-category
    """

    class Meta:
        resource = _resource
