from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.sequence_type import sequenceType as sequenceType_


__all__ = ["sequenceType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class sequenceType(sequenceType_):
    """
    sequenceType

    Type if a sequence -- DNA, RNA, or amino acid sequence.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/sequence-type
    """

    class Meta:
        resource = _resource
