from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["DeviceDefinitionPropertyCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DeviceDefinitionPropertyCode(ValueSet):
    """
    DeviceDefinitionPropertyCode

    Codes for identifying device properties.   This is based upon IEEE/HCD
specified codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/device-component-property
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
