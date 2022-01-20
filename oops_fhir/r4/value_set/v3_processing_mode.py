from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_processing_mode import (
    v3ProcessingMode as v3ProcessingMode_,
)


__all__ = ["v3ProcessingMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ProcessingMode(v3ProcessingMode_):
    """
    v3 Code System ProcessingMode

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ProcessingMode
    """

    class Meta:
        resource = _resource
