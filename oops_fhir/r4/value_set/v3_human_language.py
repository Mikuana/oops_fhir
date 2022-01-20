from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["v3HumanLanguage"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3HumanLanguage(ValueSet):
    """
    V3 Value SetHumanLanguage

     Codes for the representation of the names of human languages.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-HumanLanguage
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
