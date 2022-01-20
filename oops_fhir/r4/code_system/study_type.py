from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["StudyType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class StudyType:
    """
    StudyType

    Types of research studies (types of research methods).

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/study-type
    """

    rct = CodeSystemConcept(
        {
            "code": "RCT",
            "definition": "randomized controlled trial.",
            "display": "randomized trial",
        }
    )
    """
    randomized trial

    randomized controlled trial.
    """

    cct = CodeSystemConcept(
        {
            "code": "CCT",
            "definition": "controlled (but not randomized) trial.",
            "display": "controlled trial (non-randomized)",
        }
    )
    """
    controlled trial (non-randomized)

    controlled (but not randomized) trial.
    """

    cohort = CodeSystemConcept(
        {
            "code": "cohort",
            "definition": "observational study comparing cohorts.",
            "display": "comparative cohort study",
        }
    )
    """
    comparative cohort study

    observational study comparing cohorts.
    """

    case_control = CodeSystemConcept(
        {
            "code": "case-control",
            "definition": "case-control study.",
            "display": "case-control study",
        }
    )
    """
    case-control study

    case-control study.
    """

    series = CodeSystemConcept(
        {
            "code": "series",
            "definition": "uncontrolled cohort or case series.",
            "display": "uncontrolled cohort or case series",
        }
    )
    """
    uncontrolled cohort or case series

    uncontrolled cohort or case series.
    """

    case_report = CodeSystemConcept(
        {
            "code": "case-report",
            "definition": "a single case report.",
            "display": "case report",
        }
    )
    """
    case report

    a single case report.
    """

    mixed = CodeSystemConcept(
        {
            "code": "mixed",
            "definition": "a combination of 1 or more types of studies.",
            "display": "mixed methods",
        }
    )
    """
    mixed methods

    a combination of 1 or more types of studies.
    """

    class Meta:
        resource = _resource
