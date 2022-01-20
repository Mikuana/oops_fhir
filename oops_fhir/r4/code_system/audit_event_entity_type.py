from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AuditEventEntityType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AuditEventEntityType:
    """
    Audit event entity type

    Code for the entity type involved in the audit event.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/audit-entity-type
    """

    one = CodeSystemConcept({"code": "1", "definition": "Person", "display": "Person"})
    """
    Person

    Person
    """

    two = CodeSystemConcept(
        {"code": "2", "definition": "System Object", "display": "System Object"}
    )
    """
    System Object

    System Object
    """

    three = CodeSystemConcept(
        {"code": "3", "definition": "Organization", "display": "Organization"}
    )
    """
    Organization

    Organization
    """

    four = CodeSystemConcept({"code": "4", "definition": "Other", "display": "Other"})
    """
    Other

    Other
    """

    class Meta:
        resource = _resource
