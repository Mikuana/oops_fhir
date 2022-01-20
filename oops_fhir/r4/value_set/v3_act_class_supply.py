from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_class import v3ActClass


__all__ = ["v3ActClassSupply"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActClassSupply(v3ActClass):
    """
    V3 Value SetActClassSupply

     Supply orders and deliveries are simple Acts that focus on the
delivered product. The product is associated with the Supply Act via
Participation.typeCode="product". With general Supply Acts, the precise
identification of the Material (manufacturer, serial numbers, etc.) is
important.  Most of the detailed information about the Supply should be
represented using the Material class.  If delivery needs to be
scheduled, tracked, and billed separately, one can associate a
Transportation Act with the Supply Act.  Pharmacy dispense services are
represented as Supply Acts, associated with a SubstanceAdministration
Act. The SubstanceAdministration class represents the administration of
medication, while dispensing is supply.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ActClassSupply
    """

    class Meta:
        resource = _resource
