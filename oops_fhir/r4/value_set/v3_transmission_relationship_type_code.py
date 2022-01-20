from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_transmission_relationship_type_code import (
    v3TransmissionRelationshipTypeCode as v3TransmissionRelationshipTypeCode_,
)


__all__ = ["v3TransmissionRelationshipTypeCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3TransmissionRelationshipTypeCode(v3TransmissionRelationshipTypeCode_):
    """
    v3 Code System TransmissionRelationshipTypeCode

      Description:  A code specifying the meaning and purpose of every
TransmissionRelationship instance. Each of its values implies specific
constraints to what kinds of Transmission objects can be related and in
which way.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-TransmissionRelationshipTypeCode
    """

    class Meta:
        resource = _resource
