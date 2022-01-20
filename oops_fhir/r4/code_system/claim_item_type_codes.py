from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ClaimItemTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ClaimItemTypeCodes:
    """
    Claim Item Type Codes

    This value set includes sample Item Type codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://hl7.org/fhir/ex-claimitemtype
    """

    group = CodeSystemConcept(
        {
            "code": "group",
            "definition": "A group of products and/or Services, amount ar the summary or detail level products and services.",
            "display": "Group",
        }
    )
    """
    Group

    A group of products and/or Services, amount ar the summary or detail level products and services.
    """

    product = CodeSystemConcept(
        {
            "code": "product",
            "definition": "A billed product line item.",
            "display": "Product",
        }
    )
    """
    Product

    A billed product line item.
    """

    service = CodeSystemConcept(
        {
            "code": "service",
            "definition": "A billed service line item.",
            "display": "Service",
        }
    )
    """
    Service

    A billed service line item.
    """

    class Meta:
        resource = _resource
