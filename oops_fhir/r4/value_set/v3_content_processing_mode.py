from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_content_processing_mode import (
    v3ContentProcessingMode as v3ContentProcessingMode_,
)


__all__ = ["v3ContentProcessingMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ContentProcessingMode(v3ContentProcessingMode_):
    """
    v3 Code System ContentProcessingMode

      Description:  Identifies the order in which content should be
processed.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ContentProcessingMode
    """

    class Meta:
        resource = _resource
