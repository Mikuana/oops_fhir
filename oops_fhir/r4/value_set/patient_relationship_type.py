from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_role_code import v3RoleCode


__all__ = ["PatientRelationshipType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class PatientRelationshipType(v3RoleCode):
    """
    Patient relationship type

    A set of codes that can be used to indicate the relationship between a
Patient and a Related Person.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/relatedperson-relationshiptype
    """

    class Meta:
        resource = _resource
