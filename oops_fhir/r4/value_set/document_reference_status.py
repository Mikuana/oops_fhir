from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.document_reference_status import (
    DocumentReferenceStatus as DocumentReferenceStatus_,
)


__all__ = ["DocumentReferenceStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DocumentReferenceStatus(DocumentReferenceStatus_):
    """
    DocumentReferenceStatus

    The status of the document reference.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/document-reference-status
    """

    class Meta:
        resource = _resource
