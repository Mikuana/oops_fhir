from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_identifier_reliability import (
    v3IdentifierReliability as v3IdentifierReliability_,
)


__all__ = ["v3IdentifierReliability"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3IdentifierReliability(v3IdentifierReliability_):
    """
    v3 Code System IdentifierReliability

     Specifies the reliability with which the identifier is known. This
attribute MAY be used to assist with identifier matching algorithms.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-IdentifierReliability
    """

    class Meta:
        resource = _resource
