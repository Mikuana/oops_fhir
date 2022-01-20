from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_hl7_publishing_domain import (
    v3hl7PublishingDomain as v3hl7PublishingDomain_,
)


__all__ = ["v3hl7PublishingDomain"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7PublishingDomain(v3hl7PublishingDomain_):
    """
    v3 Code System hl7PublishingDomain

      Description:  Codes for HL7 publishing domains (specific content area)

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-hl7PublishingDomain
    """

    class Meta:
        resource = _resource
