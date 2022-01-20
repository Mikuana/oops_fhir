from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.definition_topic import (
    DefinitionTopic as DefinitionTopic_,
)


__all__ = ["DefinitionTopic"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DefinitionTopic(DefinitionTopic_):
    """
    DefinitionTopic

    High-level categorization of the definition, used for searching,
sorting, and filtering.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/definition-topic
    """

    class Meta:
        resource = _resource
