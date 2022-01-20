from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.vision_eyes import VisionEyes as VisionEyes_


__all__ = ["VisionEyes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class VisionEyes(VisionEyes_):
    """
    VisionEyes

    A coded concept listing the eye codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/vision-eye-codes
    """

    class Meta:
        resource = _resource
