from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.feeding_device_codes import (
    FeedingDeviceCodes as FeedingDeviceCodes_,
)

from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["FeedingDeviceCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FeedingDeviceCodes(ValueSet):
    """
    Feeding Device Codes

    Materials used or needed to feed the patient.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/feeding-device
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
