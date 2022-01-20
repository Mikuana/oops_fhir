from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.strand_type import strandType as strandType_


__all__ = ["strandType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class strandType(strandType_):
    """
    strandType

    Type for strand.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/strand-type
    """

    class Meta:
        resource = _resource
