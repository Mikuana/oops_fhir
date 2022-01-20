from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["BundleType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class BundleType:
    """
    BundleType

    Indicates the purpose of a bundle - how it is intended to be used.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/bundle-type
    """

    document = CodeSystemConcept(
        {
            "code": "document",
            "definition": "The bundle is a document. The first resource is a Composition.",
            "display": "Document",
        }
    )
    """
    Document

    The bundle is a document. The first resource is a Composition.
    """

    message = CodeSystemConcept(
        {
            "code": "message",
            "definition": "The bundle is a message. The first resource is a MessageHeader.",
            "display": "Message",
        }
    )
    """
    Message

    The bundle is a message. The first resource is a MessageHeader.
    """

    transaction = CodeSystemConcept(
        {
            "code": "transaction",
            "definition": "The bundle is a transaction - intended to be processed by a server as an atomic commit.",
            "display": "Transaction",
        }
    )
    """
    Transaction

    The bundle is a transaction - intended to be processed by a server as an atomic commit.
    """

    transaction_response = CodeSystemConcept(
        {
            "code": "transaction-response",
            "definition": "The bundle is a transaction response. Because the response is a transaction response, the transaction has succeeded, and all responses are error free.",
            "display": "Transaction Response",
        }
    )
    """
    Transaction Response

    The bundle is a transaction response. Because the response is a transaction response, the transaction has succeeded, and all responses are error free.
    """

    batch = CodeSystemConcept(
        {
            "code": "batch",
            "definition": "The bundle is a set of actions - intended to be processed by a server as a group of independent actions.",
            "display": "Batch",
        }
    )
    """
    Batch

    The bundle is a set of actions - intended to be processed by a server as a group of independent actions.
    """

    batch_response = CodeSystemConcept(
        {
            "code": "batch-response",
            "definition": "The bundle is a batch response. Note that as a batch, some responses may indicate failure and others success.",
            "display": "Batch Response",
        }
    )
    """
    Batch Response

    The bundle is a batch response. Note that as a batch, some responses may indicate failure and others success.
    """

    history = CodeSystemConcept(
        {
            "code": "history",
            "definition": "The bundle is a list of resources from a history interaction on a server.",
            "display": "History List",
        }
    )
    """
    History List

    The bundle is a list of resources from a history interaction on a server.
    """

    searchset = CodeSystemConcept(
        {
            "code": "searchset",
            "definition": "The bundle is a list of resources returned as a result of a search/query interaction, operation, or message.",
            "display": "Search Results",
        }
    )
    """
    Search Results

    The bundle is a list of resources returned as a result of a search/query interaction, operation, or message.
    """

    collection = CodeSystemConcept(
        {
            "code": "collection",
            "definition": "The bundle is a set of resources collected into a single package for ease of distribution that imposes no processing obligations or behavioral rules beyond persistence.",
            "display": "Collection",
        }
    )
    """
    Collection

    The bundle is a set of resources collected into a single package for ease of distribution that imposes no processing obligations or behavioral rules beyond persistence.
    """

    class Meta:
        resource = _resource
