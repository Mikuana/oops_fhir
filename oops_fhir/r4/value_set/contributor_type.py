from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contributor_type import (
    ContributorType as ContributorType_,
)


__all__ = ["ContributorType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContributorType(ContributorType_):
    """
    ContributorType

    The type of contributor.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contributor-type
    """

    class Meta:
        resource = _resource
