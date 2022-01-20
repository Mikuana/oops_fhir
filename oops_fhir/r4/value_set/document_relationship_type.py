from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.document_relationship_type import (
    DocumentRelationshipType as DocumentRelationshipType_,
)


__all__ = ["DocumentRelationshipType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DocumentRelationshipType(DocumentRelationshipType_):
    """
    DocumentRelationshipType

    The type of relationship between documents.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/document-relationship-type
    """

    class Meta:
        resource = _resource
