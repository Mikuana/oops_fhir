from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.observation_status import (
    ObservationStatus as ObservationStatus_,
)


__all__ = ["ObservationStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ObservationStatus(ObservationStatus_):
    """
    ObservationStatus

    Codes providing the status of an observation.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/observation-status
    """

    class Meta:
        resource = _resource
