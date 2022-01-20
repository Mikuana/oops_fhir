from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.sequence_status import sequenceStatus as sequenceStatus_


__all__ = ["sequenceStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class sequenceStatus(sequenceStatus_):
    """
    sequenceStatus

    Codes providing the status of the variant test result.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/variant-state
    """

    class Meta:
        resource = _resource
