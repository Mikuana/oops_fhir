from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.claim_information_category_codes import (
    ClaimInformationCategoryCodes as ClaimInformationCategoryCodes_,
)


__all__ = ["ClaimInformationCategoryCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ClaimInformationCategoryCodes(ClaimInformationCategoryCodes_):
    """
    Claim Information Category Codes

    This value set includes sample Information Category codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/claim-informationcategory
    """

    class Meta:
        resource = _resource
