from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_telecommunication_capabilities import (
    v3TelecommunicationCapabilities as v3TelecommunicationCapabilities_,
)


__all__ = ["v3TelecommunicationCapabilities"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3TelecommunicationCapabilities(v3TelecommunicationCapabilities_):
    """
    v3 Code System TelecommunicationCapabilities

      Description:  Concepts that define the telecommunication capabilities
of a particular device. Used to identify the expected capabilities to be
found at a particular telecommunication address.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-TelecommunicationCapabilities
    """

    class Meta:
        resource = _resource
