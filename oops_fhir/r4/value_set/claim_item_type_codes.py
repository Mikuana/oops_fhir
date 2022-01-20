from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.claim_item_type_codes import (
    ClaimItemTypeCodes as ClaimItemTypeCodes_,
)


__all__ = ["ClaimItemTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ClaimItemTypeCodes(ClaimItemTypeCodes_):
    """
    Claim Item Type Codes

    This value set includes sample Item Type codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/fm-itemtype
    """

    class Meta:
        resource = _resource
