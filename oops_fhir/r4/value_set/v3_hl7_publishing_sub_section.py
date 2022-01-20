from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_hl7_publishing_sub_section import (
    v3hl7PublishingSubSection as v3hl7PublishingSubSection_,
)


__all__ = ["v3hl7PublishingSubSection"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7PublishingSubSection(v3hl7PublishingSubSection_):
    """
    v3 Code System hl7PublishingSubSection

      Description:  Codes for HL7 publishing sub-sections (business sub-
categories)

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-hl7PublishingSubSection
    """

    class Meta:
        resource = _resource
