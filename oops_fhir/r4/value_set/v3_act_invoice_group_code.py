from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_code import v3ActCode


__all__ = ["v3ActInvoiceGroupCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActInvoiceGroupCode(v3ActCode):
    """
    V3 Value SetActInvoiceGroupCode

     Type of invoice element that is used to assist in describing an Invoice
that is either submitted for adjudication or for which is returned on
adjudication results. Invoice elements of this type signify a grouping
of one or more children (detail) invoice elements.  They do not have
intrinsic costing associated with them, but merely reflect the sum of
all costing for it's immediate children invoice elements.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ActInvoiceGroupCode
    """

    class Meta:
        resource = _resource
