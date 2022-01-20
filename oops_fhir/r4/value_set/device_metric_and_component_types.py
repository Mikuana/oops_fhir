from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["DeviceMetricAndComponentTypes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DeviceMetricAndComponentTypes(ValueSet):
    """
    Device Metric and Component Types

    Codes used to identify health care device metric types and units and
component types as part of the ISO/IEEE 11073-10101 Medical Device
Communication Nomenclature.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/devicemetric-type
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
