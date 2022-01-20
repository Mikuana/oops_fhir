from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.vision_base import VisionBase as VisionBase_


__all__ = ["VisionBase"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class VisionBase(VisionBase_):
    """
    VisionBase

    A coded concept listing the base codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/vision-base-codes
    """

    class Meta:
        resource = _resource
