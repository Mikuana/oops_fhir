from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contact_entity_type import (
    ContactEntityType as ContactEntityType_,
)


__all__ = ["ContactEntityType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContactEntityType(ContactEntityType_):
    """
    Contact entity type

    This example value set defines a set of codes that can be used to
indicate the purpose for which you would contact a contact party.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contactentity-type
    """

    class Meta:
        resource = _resource
