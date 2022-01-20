from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_equipment_alert_level import (
    v3EquipmentAlertLevel as v3EquipmentAlertLevel_,
)


__all__ = ["v3EquipmentAlertLevel"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EquipmentAlertLevel(v3EquipmentAlertLevel_):
    """
    v3 Code System EquipmentAlertLevel

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-EquipmentAlertLevel
    """

    class Meta:
        resource = _resource
