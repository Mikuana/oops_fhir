from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contact_point_system import (
    ContactPointSystem as ContactPointSystem_,
)


__all__ = ["ContactPointSystem"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContactPointSystem(ContactPointSystem_):
    """
    ContactPointSystem

    Telecommunications form for contact point.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contact-point-system
    """

    class Meta:
        resource = _resource
