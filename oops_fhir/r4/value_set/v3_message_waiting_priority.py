from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_message_waiting_priority import (
    v3MessageWaitingPriority as v3MessageWaitingPriority_,
)


__all__ = ["v3MessageWaitingPriority"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3MessageWaitingPriority(v3MessageWaitingPriority_):
    """
    v3 Code System MessageWaitingPriority

     Indicates that the receiver has messages for the sender  OpenIssue:
Description does not make sense relative to name of coding system.  Must
be reviewed and improved.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-MessageWaitingPriority
    """

    class Meta:
        resource = _resource
