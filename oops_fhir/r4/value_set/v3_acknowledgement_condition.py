from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_acknowledgement_condition import (
    v3AcknowledgementCondition as v3AcknowledgementCondition_,
)


__all__ = ["v3AcknowledgementCondition"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3AcknowledgementCondition(v3AcknowledgementCondition_):
    """
    v3 Code System AcknowledgementCondition

     The codes identify the conditions under which accept acknowledgements
are required to be returned in response to this message. Note that
accept acknowledgement address two different issues at the same time:
reliable transport as well as syntactical correctness

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-AcknowledgementCondition
    """

    class Meta:
        resource = _resource
