from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_communication_function_type import (
    v3CommunicationFunctionType as v3CommunicationFunctionType_,
)


__all__ = ["v3CommunicationFunctionType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3CommunicationFunctionType(v3CommunicationFunctionType_):
    """
    v3 Code System CommunicationFunctionType

     Describes the type of communication function that the associated entity
plays in the associated transmission.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-CommunicationFunctionType
    """

    class Meta:
        resource = _resource
