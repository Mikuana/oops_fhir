from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.smart_capabilities import (
    SmartCapabilities as SmartCapabilities_,
)


__all__ = ["SmartCapabilities"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SmartCapabilities(SmartCapabilities_):
    """
    SmartCapabilities

    Codes that define what the server is capable of.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/smart-capabilities
    """

    class Meta:
        resource = _resource
