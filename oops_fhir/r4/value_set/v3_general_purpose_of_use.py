from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["v3GeneralPurposeOfUse"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3GeneralPurposeOfUse(ValueSet):
    """
    V3 Value SetGeneralPurposeOfUse

     Supports communication of purpose of use at a general level.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-GeneralPurposeOfUse
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
