from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["LanguagePreferenceType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class LanguagePreferenceType(ValueSet):
    """
    Language preference type

    This value set defines the set of codes for describing the type or mode
of the patient's preferred language.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/language-preference-type
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
