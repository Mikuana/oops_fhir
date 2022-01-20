from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["TransactionMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class TransactionMode:
    """
    TransactionMode

    A code that indicates how transactions are supported.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/transaction-mode
    """

    not_supported = CodeSystemConcept(
        {
            "code": "not-supported",
            "definition": "Neither batch or transaction is supported.",
            "display": "None",
        }
    )
    """
    None

    Neither batch or transaction is supported.
    """

    batch = CodeSystemConcept(
        {
            "code": "batch",
            "definition": "Batches are  supported.",
            "display": "Batches supported",
        }
    )
    """
    Batches supported

    Batches are  supported.
    """

    transaction = CodeSystemConcept(
        {
            "code": "transaction",
            "definition": "Transactions are supported.",
            "display": "Transactions Supported",
        }
    )
    """
    Transactions Supported

    Transactions are supported.
    """

    both = CodeSystemConcept(
        {
            "code": "both",
            "definition": "Both batches and transactions are supported.",
            "display": "Batches & Transactions",
        }
    )
    """
    Batches & Transactions

    Both batches and transactions are supported.
    """

    class Meta:
        resource = _resource
