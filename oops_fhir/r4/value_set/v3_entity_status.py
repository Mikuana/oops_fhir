from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_entity_status import v3EntityStatus as v3EntityStatus_


__all__ = ["v3EntityStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityStatus(v3EntityStatus_):
    """
    v3 Code System EntityStatus

     Codes representing the defined possible states of an Entity, as defined
by the Entity class state machine.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-EntityStatus
    """

    class Meta:
        resource = _resource
