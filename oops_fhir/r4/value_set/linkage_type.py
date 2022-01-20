from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.linkage_type import LinkageType as LinkageType_


__all__ = ["LinkageType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class LinkageType(LinkageType_):
    """
    LinkageType

    Used to distinguish different roles a resource can play within a set of
linked resources.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/linkage-type
    """

    class Meta:
        resource = _resource
