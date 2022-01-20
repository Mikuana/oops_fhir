from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.standards_status import (
    StandardsStatus as StandardsStatus_,
)


__all__ = ["StandardsStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class StandardsStatus(StandardsStatus_):
    """
    StandardsStatus

    HL7 Ballot/Standards status of artifact.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/standards-status
    """

    class Meta:
        resource = _resource
