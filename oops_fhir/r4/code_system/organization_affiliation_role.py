from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["OrganizationAffiliationRole"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class OrganizationAffiliationRole:
    """
    Organization Affiliation Role

    This example value set defines a set of codes that can be used to
indicate the role of one Organization in relation to another.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/organization-role
    """

    provider = CodeSystemConcept({"code": "provider", "display": "Provider"})
    """
    Provider

    
    """

    agency = CodeSystemConcept(
        {
            "code": "agency",
            "definition": "An organization such as a public health agency, community/social services provider, etc.",
            "display": "Agency",
        }
    )
    """
    Agency

    An organization such as a public health agency, community/social services provider, etc.
    """

    research = CodeSystemConcept(
        {
            "code": "research",
            "definition": "An organization providing research-related services such as conducting research, recruiting research participants, analyzing data, etc.",
            "display": "Research",
        }
    )
    """
    Research

    An organization providing research-related services such as conducting research, recruiting research participants, analyzing data, etc.
    """

    payer = CodeSystemConcept(
        {
            "code": "payer",
            "definition": "An organization providing reimbursement, payment, or related services",
            "display": "Payer",
        }
    )
    """
    Payer

    An organization providing reimbursement, payment, or related services
    """

    diagnostics = CodeSystemConcept(
        {
            "code": "diagnostics",
            "definition": "An organization providing diagnostic testing/laboratory services",
            "display": "Diagnostics",
        }
    )
    """
    Diagnostics

    An organization providing diagnostic testing/laboratory services
    """

    supplier = CodeSystemConcept(
        {
            "code": "supplier",
            "definition": "An organization that provides medical supplies (e.g. medical devices, equipment, pharmaceutical products, etc.)",
            "display": "Supplier",
        }
    )
    """
    Supplier

    An organization that provides medical supplies (e.g. medical devices, equipment, pharmaceutical products, etc.)
    """

    hie_hio = CodeSystemConcept(
        {
            "code": "HIE/HIO",
            "definition": "An organization that facilitates electronic clinical data exchange between entities",
            "display": "HIE/HIO",
        }
    )
    """
    HIE/HIO

    An organization that facilitates electronic clinical data exchange between entities
    """

    member = CodeSystemConcept(
        {
            "code": "member",
            "definition": "A type of non-ownership relationship between entities (encompasses partnerships, collaboration, joint ventures, etc.)",
            "display": "Member",
        }
    )
    """
    Member

    A type of non-ownership relationship between entities (encompasses partnerships, collaboration, joint ventures, etc.)
    """

    class Meta:
        resource = _resource
