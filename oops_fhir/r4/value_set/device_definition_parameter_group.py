from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.device_definition_parameter_group import (
    DeviceDefinitionParameterGroup as DeviceDefinitionParameterGroup_,
)


__all__ = ["DeviceDefinitionParameterGroup"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DeviceDefinitionParameterGroup(DeviceDefinitionParameterGroup_):
    """
    DeviceDefinitionParameterGroup

    Codes identifying groupings of parameters; e.g. Cardiovascular.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/parameter-group
    """

    class Meta:
        resource = _resource
