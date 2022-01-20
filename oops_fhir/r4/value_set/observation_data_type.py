from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.observation_data_type import (
    ObservationDataType as ObservationDataType_,
)


__all__ = ["ObservationDataType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ObservationDataType(ObservationDataType_):
    """
    ObservationDataType

    Permitted data type for observation value.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/permitted-data-type
    """

    class Meta:
        resource = _resource
