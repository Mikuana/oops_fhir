from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_compression_algorithm import (
    v3CompressionAlgorithm as v3CompressionAlgorithm_,
)


__all__ = ["v3CompressionAlgorithm"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3CompressionAlgorithm(v3CompressionAlgorithm_):
    """
    v3 Code System CompressionAlgorithm

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-CompressionAlgorithm
    """

    class Meta:
        resource = _resource
