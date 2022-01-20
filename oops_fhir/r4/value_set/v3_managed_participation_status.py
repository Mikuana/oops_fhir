from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_managed_participation_status import (
    v3ManagedParticipationStatus as v3ManagedParticipationStatus_,
)


__all__ = ["v3ManagedParticipationStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ManagedParticipationStatus(v3ManagedParticipationStatus_):
    """
    v3 Code System ManagedParticipationStatus

     Codes representing the defined possible states of a Managed
Participation, as defined by the Managed Participation class state
machine.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ManagedParticipationStatus
    """

    class Meta:
        resource = _resource
