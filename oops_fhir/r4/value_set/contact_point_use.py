from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contact_point_use import (
    ContactPointUse as ContactPointUse_,
)


__all__ = ["ContactPointUse"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContactPointUse(ContactPointUse_):
    """
    ContactPointUse

    Use of contact point.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contact-point-use
    """

    class Meta:
        resource = _resource
