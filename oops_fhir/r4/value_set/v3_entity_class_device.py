from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_entity_class import v3EntityClass


__all__ = ["v3EntityClassDevice"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityClassDevice(v3EntityClass):
    """
    V3 Value SetEntityClassDevice

     A subtype of ManufacturedMaterial used in an activity, without being
substantially changed through that activity.  The kind of device is
identified by the code attribute inherited from Entity.  Usage:  This
includes durable (reusable) medical equipment as well as disposable
equipment.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-EntityClassDevice
    """

    class Meta:
        resource = _resource
