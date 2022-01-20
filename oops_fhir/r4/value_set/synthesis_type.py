from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.synthesis_type import SynthesisType as SynthesisType_


__all__ = ["SynthesisType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SynthesisType(SynthesisType_):
    """
    SynthesisType

    Types of combining results from a body of evidence (eg. summary data
meta-analysis).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/synthesis-type
    """

    class Meta:
        resource = _resource
