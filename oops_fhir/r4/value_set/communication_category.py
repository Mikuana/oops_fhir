from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.communication_category import (
    CommunicationCategory as CommunicationCategory_,
)


__all__ = ["CommunicationCategory"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CommunicationCategory(CommunicationCategory_):
    """
    CommunicationCategory

    Codes for general categories of communications such as alerts,
instructions, etc.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/communication-category
    """

    class Meta:
        resource = _resource
