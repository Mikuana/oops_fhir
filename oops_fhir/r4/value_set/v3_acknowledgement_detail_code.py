from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_acknowledgement_detail_code import (
    v3AcknowledgementDetailCode as v3AcknowledgementDetailCode_,
)


__all__ = ["v3AcknowledgementDetailCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3AcknowledgementDetailCode(v3AcknowledgementDetailCode_):
    """
    v3 Code System AcknowledgementDetailCode

      OpenIssue:  Missing description.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-AcknowledgementDetailCode
    """

    class Meta:
        resource = _resource
