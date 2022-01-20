from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.transaction_mode import (
    TransactionMode as TransactionMode_,
)


__all__ = ["TransactionMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TransactionMode(TransactionMode_):
    """
    TransactionMode

    A code that indicates how transactions are supported.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/transaction-mode
    """

    class Meta:
        resource = _resource
