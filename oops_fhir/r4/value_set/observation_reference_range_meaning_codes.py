from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.observation_reference_range_meaning_codes import (
    ObservationReferenceRangeMeaningCodes as ObservationReferenceRangeMeaningCodes_,
)


__all__ = ["ObservationReferenceRangeMeaningCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ObservationReferenceRangeMeaningCodes(ObservationReferenceRangeMeaningCodes_):
    """
    Observation Reference Range Meaning Codes

    This value set defines a set of codes that can be used to indicate the
meaning/use of a reference range for a particular target population.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/referencerange-meaning
    """

    class Meta:
        resource = _resource
