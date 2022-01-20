from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DocumentMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DocumentMode:
    """
    DocumentMode

    Whether the application produces or consumes documents.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/document-mode
    """

    producer = CodeSystemConcept(
        {
            "code": "producer",
            "definition": "The application produces documents of the specified type.",
            "display": "Producer",
        }
    )
    """
    Producer

    The application produces documents of the specified type.
    """

    consumer = CodeSystemConcept(
        {
            "code": "consumer",
            "definition": "The application consumes documents of the specified type.",
            "display": "Consumer",
        }
    )
    """
    Consumer

    The application consumes documents of the specified type.
    """

    class Meta:
        resource = _resource
