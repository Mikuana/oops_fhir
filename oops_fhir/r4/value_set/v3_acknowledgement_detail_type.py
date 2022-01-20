from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_acknowledgement_detail_type import (
    v3AcknowledgementDetailType as v3AcknowledgementDetailType_,
)


__all__ = ["v3AcknowledgementDetailType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3AcknowledgementDetailType(v3AcknowledgementDetailType_):
    """
    v3 Code System AcknowledgementDetailType

     A code identifying the specific message to be provided.  Discussion:  A
textual value may be specified as the print name, or for non-coded
messages, as the original text.  Examples:  'Required attribute xxx is
missing', 'System will be unavailable March 19 from 0100 to 0300'

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-AcknowledgementDetailType
    """

    class Meta:
        resource = _resource
