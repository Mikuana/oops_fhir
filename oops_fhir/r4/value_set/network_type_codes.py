from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.network_type_codes import (
    NetworkTypeCodes as NetworkTypeCodes_,
)


__all__ = ["NetworkTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class NetworkTypeCodes(NetworkTypeCodes_):
    """
    Network Type Codes

    This value set includes a smattering of Network type codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/benefit-network
    """

    class Meta:
        resource = _resource
