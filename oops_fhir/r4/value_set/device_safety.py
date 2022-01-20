from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["DeviceSafety"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DeviceSafety(ValueSet):
    """
    Device safety

    Codes used to identify medical devices safety characteristics. These
codes are taken from the [NCI
Thesaurus](https://ncit.nci.nih.gov/ncitbrowser/pages/home.jsf) and are
provided here as a suggestive example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/device-safety
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
