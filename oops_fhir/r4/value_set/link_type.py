from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.link_type import LinkType as LinkType_


__all__ = ["LinkType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class LinkType(LinkType_):
    """
    LinkType

    The type of link between this patient resource and another patient
resource.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/link-type
    """

    class Meta:
        resource = _resource
