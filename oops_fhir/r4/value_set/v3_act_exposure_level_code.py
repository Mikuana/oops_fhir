from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_exposure_level_code import (
    v3ActExposureLevelCode as v3ActExposureLevelCode_,
)


__all__ = ["v3ActExposureLevelCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActExposureLevelCode(v3ActExposureLevelCode_):
    """
    v3 Code System ActExposureLevelCode

     A qualitative measure of the degree of exposure to the causative agent.
This includes concepts such as "low", "medium" and "high".  This
quantifies how the quantity that was available to be administered to the
target differs from typical or background levels of the substance.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ActExposureLevelCode
    """

    class Meta:
        resource = _resource
