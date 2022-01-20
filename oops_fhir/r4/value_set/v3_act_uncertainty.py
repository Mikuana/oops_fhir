from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_uncertainty import (
    v3ActUncertainty as v3ActUncertainty_,
)


__all__ = ["v3ActUncertainty"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActUncertainty(v3ActUncertainty_):
    """
    v3 Code System ActUncertainty

      OpenIssue:  Missing Description

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ActUncertainty
    """

    class Meta:
        resource = _resource
