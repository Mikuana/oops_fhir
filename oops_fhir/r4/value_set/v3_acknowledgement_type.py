from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_acknowledgement_type import (
    v3AcknowledgementType as v3AcknowledgementType_,
)


__all__ = ["v3AcknowledgementType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3AcknowledgementType(v3AcknowledgementType_):
    """
    v3 Code System AcknowledgementType

     This attribute contains an acknowledgement code as described in the HL7
message processing rules.  OpenIssue:  Description was copied from
attribute and needs to be improved to be appropriate for a code system.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-AcknowledgementType
    """

    class Meta:
        resource = _resource
