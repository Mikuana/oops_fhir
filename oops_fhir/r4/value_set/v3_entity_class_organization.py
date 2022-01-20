from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_entity_class import v3EntityClass


__all__ = ["v3EntityClassOrganization"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityClassOrganization(v3EntityClass):
    """
    V3 Value SetEntityClassOrganization

     A social or legal structure formed by human beings.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-EntityClassOrganization
    """

    class Meta:
        resource = _resource
