from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_invoice_element_modifier import (
    v3ActInvoiceElementModifier as v3ActInvoiceElementModifier_,
)


__all__ = ["v3ActInvoiceElementModifier"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActInvoiceElementModifier(v3ActInvoiceElementModifier_):
    """
    v3 Code System ActInvoiceElementModifier

     Processing consideration and clarification codes.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ActInvoiceElementModifier
    """

    class Meta:
        resource = _resource
