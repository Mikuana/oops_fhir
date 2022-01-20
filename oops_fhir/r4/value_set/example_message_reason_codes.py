from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.example_message_reason_codes import (
    ExampleMessageReasonCodes as ExampleMessageReasonCodes_,
)


__all__ = ["ExampleMessageReasonCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExampleMessageReasonCodes(ExampleMessageReasonCodes_):
    """
    Example Message Reason Codes

    Example Message Reasons. These are the set of codes that might be used
an updating an encounter using admin-update.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/message-reason-encounter
    """

    class Meta:
        resource = _resource
