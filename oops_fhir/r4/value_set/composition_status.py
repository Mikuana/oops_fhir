from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.composition_status import (
    CompositionStatus as CompositionStatus_,
)


__all__ = ["CompositionStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CompositionStatus(CompositionStatus_):
    """
    CompositionStatus

    The workflow/clinical status of the composition.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/composition-status
    """

    class Meta:
        resource = _resource
