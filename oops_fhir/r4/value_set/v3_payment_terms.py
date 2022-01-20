from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_payment_terms import v3PaymentTerms as v3PaymentTerms_


__all__ = ["v3PaymentTerms"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3PaymentTerms(v3PaymentTerms_):
    """
    v3 Code System PaymentTerms

     Describes payment terms for a financial transaction, used in an
invoice. This is typically expressed as a responsibility of the acceptor
or payor of an invoice.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-PaymentTerms
    """

    class Meta:
        resource = _resource
