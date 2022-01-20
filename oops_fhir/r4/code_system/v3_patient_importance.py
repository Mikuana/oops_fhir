from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3PatientImportance"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3PatientImportance:
    """
    v3 Code System PatientImportance

     Patient VIP code

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-PatientImportance
    """

    bm = CodeSystemConcept(
        {
            "code": "BM",
            "definition": "Board member of health care organization",
            "display": "Board Member",
        }
    )
    """
    Board Member

    Board member of health care organization
    """

    dfm = CodeSystemConcept(
        {
            "code": "DFM",
            "definition": "Family member of staff physician",
            "display": "Physician Family Member",
        }
    )
    """
    Physician Family Member

    Family member of staff physician
    """

    dr = CodeSystemConcept(
        {
            "code": "DR",
            "definition": "Member of the health care organization physician staff",
            "display": "Staff Physician",
        }
    )
    """
    Staff Physician

    Member of the health care organization physician staff
    """

    fd = CodeSystemConcept(
        {
            "code": "FD",
            "definition": "Financial donor to the health care organization",
            "display": "Financial Donor",
        }
    )
    """
    Financial Donor

    Financial donor to the health care organization
    """

    for_ = CodeSystemConcept(
        {
            "code": "FOR",
            "definition": "Foreign citizen dignitary of interest to the health care organization",
            "display": "Foreign Dignitary",
        }
    )
    """
    Foreign Dignitary

    Foreign citizen dignitary of interest to the health care organization
    """

    govt = CodeSystemConcept(
        {
            "code": "GOVT",
            "definition": "Government dignitary of interest to the organization",
            "display": "Government Dignitary",
        }
    )
    """
    Government Dignitary

    Government dignitary of interest to the organization
    """

    sfm = CodeSystemConcept(
        {
            "code": "SFM",
            "definition": "Family member of staff member",
            "display": "Staff Family Member",
        }
    )
    """
    Staff Family Member

    Family member of staff member
    """

    stf = CodeSystemConcept(
        {
            "code": "STF",
            "definition": "Staff member of the health care organization",
            "display": "Staff Member",
        }
    )
    """
    Staff Member

    Staff member of the health care organization
    """

    vip = CodeSystemConcept(
        {
            "code": "VIP",
            "definition": "Very important person of interest to the health care organization",
            "display": "Very Important Person",
        }
    )
    """
    Very Important Person

    Very important person of interest to the health care organization
    """

    class Meta:
        resource = _resource
