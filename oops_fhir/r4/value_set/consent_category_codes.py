from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.consent_category_codes import (
    ConsentCategoryCodes as ConsentCategoryCodes_,
)


__all__ = ["ConsentCategoryCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConsentCategoryCodes(ValueSet):
    """
    Consent Category Codes

    This value set includes sample Consent Directive Type codes, including
several consent directive related LOINC codes; HL7 VALUE SET:
ActConsentType(2.16.840.1.113883.1.11.19897); examples of US realm
consent directive legal descriptions and references to online and/or
downloadable forms such as the SSA-827 Authorization to Disclose
Information to the Social Security Administration; and other anticipated
consent directives related to participation in a clinical trial, medical
procedures, reproductive procedures; health care directive (Living
Will); advance directive, do not resuscitate (DNR); Physician Orders for
Life-Sustaining Treatment (POLST)

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/consent-category
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
