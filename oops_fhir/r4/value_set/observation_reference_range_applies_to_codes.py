from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ObservationReferenceRangeAppliesToCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ObservationReferenceRangeAppliesToCodes(ValueSet):
    """
    Observation Reference Range Applies To Codes

    This value set defines a set of codes that can be used to indicate the
particular target population the reference range applies to.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/referencerange-appliesto
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
