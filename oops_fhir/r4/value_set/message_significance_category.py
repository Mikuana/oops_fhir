from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.message_significance_category import (
    MessageSignificanceCategory as MessageSignificanceCategory_,
)


__all__ = ["MessageSignificanceCategory"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MessageSignificanceCategory(MessageSignificanceCategory_):
    """
    MessageSignificanceCategory

    The impact of the content of a message.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/message-significance-category
    """

    class Meta:
        resource = _resource
