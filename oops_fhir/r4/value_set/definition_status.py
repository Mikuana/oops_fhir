from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.definition_status import (
    DefinitionStatus as DefinitionStatus_,
)


__all__ = ["DefinitionStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DefinitionStatus(DefinitionStatus_):
    """
    DefinitionStatus

    Codes identifying the lifecycle stage of a definition.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/definition-status
    """

    class Meta:
        resource = _resource
