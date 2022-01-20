from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["OrganizationType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class OrganizationType:
    """
    Organization type

    This example value set defines a set of codes that can be used to
indicate a type of organization.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/organization-type
    """

    prov = CodeSystemConcept(
        {
            "code": "prov",
            "definition": "An organization that provides healthcare services.",
            "display": "Healthcare Provider",
        }
    )
    """
    Healthcare Provider

    An organization that provides healthcare services.
    """

    dept = CodeSystemConcept(
        {
            "code": "dept",
            "definition": "A department or ward within a hospital (Generally is not applicable to top level organizations)",
            "display": "Hospital Department",
        }
    )
    """
    Hospital Department

    A department or ward within a hospital (Generally is not applicable to top level organizations)
    """

    team = CodeSystemConcept(
        {
            "code": "team",
            "definition": "An organizational team is usually a grouping of practitioners that perform a specific function within an organization (which could be a top level organization, or a department).",
            "display": "Organizational team",
        }
    )
    """
    Organizational team

    An organizational team is usually a grouping of practitioners that perform a specific function within an organization (which could be a top level organization, or a department).
    """

    govt = CodeSystemConcept(
        {
            "code": "govt",
            "definition": "A political body, often used when including organization records for government bodies such as a Federal Government, State or Local Government.",
            "display": "Government",
        }
    )
    """
    Government

    A political body, often used when including organization records for government bodies such as a Federal Government, State or Local Government.
    """

    ins = CodeSystemConcept(
        {
            "code": "ins",
            "definition": "A company that provides insurance to its subscribers that may include healthcare related policies.",
            "display": "Insurance Company",
        }
    )
    """
    Insurance Company

    A company that provides insurance to its subscribers that may include healthcare related policies.
    """

    pay = CodeSystemConcept(
        {
            "code": "pay",
            "definition": "A company, charity, or governmental organization, which processes claims and/or issues payments to providers on behalf of patients or groups of patients.",
            "display": "Payer",
        }
    )
    """
    Payer

    A company, charity, or governmental organization, which processes claims and/or issues payments to providers on behalf of patients or groups of patients.
    """

    edu = CodeSystemConcept(
        {
            "code": "edu",
            "definition": "An educational institution that provides education or research facilities.",
            "display": "Educational Institute",
        }
    )
    """
    Educational Institute

    An educational institution that provides education or research facilities.
    """

    reli = CodeSystemConcept(
        {
            "code": "reli",
            "definition": "An organization that is identified as a part of a religious institution.",
            "display": "Religious Institution",
        }
    )
    """
    Religious Institution

    An organization that is identified as a part of a religious institution.
    """

    crs = CodeSystemConcept(
        {
            "code": "crs",
            "definition": "An organization that is identified as a Pharmaceutical/Clinical Research Sponsor.",
            "display": "Clinical Research Sponsor",
        }
    )
    """
    Clinical Research Sponsor

    An organization that is identified as a Pharmaceutical/Clinical Research Sponsor.
    """

    cg = CodeSystemConcept(
        {
            "code": "cg",
            "definition": "An un-incorporated community group.",
            "display": "Community Group",
        }
    )
    """
    Community Group

    An un-incorporated community group.
    """

    bus = CodeSystemConcept(
        {
            "code": "bus",
            "definition": "An organization that is a registered business or corporation but not identified by other types.",
            "display": "Non-Healthcare Business or Corporation",
        }
    )
    """
    Non-Healthcare Business or Corporation

    An organization that is a registered business or corporation but not identified by other types.
    """

    other = CodeSystemConcept(
        {
            "code": "other",
            "definition": "Other type of organization not already specified.",
            "display": "Other",
        }
    )
    """
    Other

    Other type of organization not already specified.
    """

    class Meta:
        resource = _resource
