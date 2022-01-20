from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["AllLanguages"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AllLanguages(ValueSet):
    """
    All Languages

    This value set includes all possible codes from BCP-47
(http://tools.ietf.org/html/bcp47)

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/all-languages
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
