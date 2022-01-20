from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3EducationLevel"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3EducationLevel:
    """
    v3 Code System EducationLevel

     Years of education that a person has completed

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-EducationLevel
    """

    assoc = CodeSystemConcept(
        {
            "code": "ASSOC",
            "definition": "Associate's or technical degree complete",
            "display": "Associate's or technical degree complete",
        }
    )
    """
    Associate's or technical degree complete

    Associate's or technical degree complete
    """

    bd = CodeSystemConcept(
        {
            "code": "BD",
            "definition": "College or baccalaureate degree complete",
            "display": "College or baccalaureate degree complete",
        }
    )
    """
    College or baccalaureate degree complete

    College or baccalaureate degree complete
    """

    elem = CodeSystemConcept(
        {
            "code": "ELEM",
            "definition": "Elementary School",
            "display": "Elementary School",
        }
    )
    """
    Elementary School

    Elementary School
    """

    gd = CodeSystemConcept(
        {
            "code": "GD",
            "definition": "Graduate or professional Degree complete",
            "display": "Graduate or professional Degree complete",
        }
    )
    """
    Graduate or professional Degree complete

    Graduate or professional Degree complete
    """

    hs = CodeSystemConcept(
        {
            "code": "HS",
            "definition": "High School or secondary school degree complete",
            "display": "High School or secondary school degree complete",
        }
    )
    """
    High School or secondary school degree complete

    High School or secondary school degree complete
    """

    pb = CodeSystemConcept(
        {
            "code": "PB",
            "definition": "Some post-baccalaureate education",
            "display": "Some post-baccalaureate education",
        }
    )
    """
    Some post-baccalaureate education

    Some post-baccalaureate education
    """

    postg = CodeSystemConcept(
        {
            "code": "POSTG",
            "definition": "Doctoral or post graduate education",
            "display": "Doctoral or post graduate education",
        }
    )
    """
    Doctoral or post graduate education

    Doctoral or post graduate education
    """

    scol = CodeSystemConcept(
        {
            "code": "SCOL",
            "definition": "Some College education",
            "display": "Some College education",
        }
    )
    """
    Some College education

    Some College education
    """

    sec = CodeSystemConcept(
        {
            "code": "SEC",
            "definition": "Some secondary or high school education",
            "display": "Some secondary or high school education",
        }
    )
    """
    Some secondary or high school education

    Some secondary or high school education
    """

    class Meta:
        resource = _resource
