from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.document_mode import DocumentMode as DocumentMode_


__all__ = ["DocumentMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DocumentMode(DocumentMode_):
    """
    DocumentMode

    Whether the application produces or consumes documents.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/document-mode
    """

    class Meta:
        resource = _resource
