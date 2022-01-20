from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_hl7_publishing_section import (
    v3hl7PublishingSection as v3hl7PublishingSection_,
)


__all__ = ["v3hl7PublishingSection"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7PublishingSection(v3hl7PublishingSection_):
    """
    v3 Code System hl7PublishingSection

      Description:  Codes for HL7 publishing sections (major business
categories)

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-hl7PublishingSection
    """

    class Meta:
        resource = _resource
