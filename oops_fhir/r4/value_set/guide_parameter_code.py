from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.guide_parameter_code import (
    GuideParameterCode as GuideParameterCode_,
)


__all__ = ["GuideParameterCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class GuideParameterCode(GuideParameterCode_):
    """
    GuideParameterCode

    Code of parameter that is input to the guide.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/guide-parameter-code
    """

    class Meta:
        resource = _resource
