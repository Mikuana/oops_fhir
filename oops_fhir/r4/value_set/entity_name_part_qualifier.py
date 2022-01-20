from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["EntityNamePartQualifier"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EntityNamePartQualifier(ValueSet):
    """
    EntityNamePartQualifier

    A set of codes each of which specifies a certain subcategory of the name
part in addition to the main name part type.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/name-part-qualifier
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
