from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_integrity_check_algorithm import (
    v3IntegrityCheckAlgorithm as v3IntegrityCheckAlgorithm_,
)


__all__ = ["v3IntegrityCheckAlgorithm"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3IntegrityCheckAlgorithm(v3IntegrityCheckAlgorithm_):
    """
    v3 Code System IntegrityCheckAlgorithm

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-IntegrityCheckAlgorithm
    """

    class Meta:
        resource = _resource
