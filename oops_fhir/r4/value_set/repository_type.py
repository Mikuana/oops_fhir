from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.repository_type import repositoryType as repositoryType_


__all__ = ["repositoryType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class repositoryType(repositoryType_):
    """
    repositoryType

    Type for access of external URI.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/repository-type
    """

    class Meta:
        resource = _resource
