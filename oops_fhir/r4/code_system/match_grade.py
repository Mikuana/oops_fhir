from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MatchGrade"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MatchGrade:
    """
    MatchGrade

    A Master Patient Index (MPI) assessment of whether a candidate patient
record is a match or not.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/match-grade
    """

    certain = CodeSystemConcept(
        {
            "code": "certain",
            "definition": "This record meets the matching criteria to be automatically considered as a full match.",
            "display": "Certain Match",
        }
    )
    """
    Certain Match

    This record meets the matching criteria to be automatically considered as a full match.
    """

    probable = CodeSystemConcept(
        {
            "code": "probable",
            "definition": "This record is a close match, but not a certain match. Additional review (e.g. by a human) may be required before using this as a match.",
            "display": "Probable Match",
        }
    )
    """
    Probable Match

    This record is a close match, but not a certain match. Additional review (e.g. by a human) may be required before using this as a match.
    """

    possible = CodeSystemConcept(
        {
            "code": "possible",
            "definition": "This record may be a matching one. Additional review (e.g. by a human) SHOULD be performed before using this as a match.",
            "display": "Possible Match",
        }
    )
    """
    Possible Match

    This record may be a matching one. Additional review (e.g. by a human) SHOULD be performed before using this as a match.
    """

    certainly_not = CodeSystemConcept(
        {
            "code": "certainly-not",
            "definition": "This record is known not to be a match. Note that usually non-matching records are not returned, but in some cases records previously or likely considered as a match may specifically be negated by the matching engine.",
            "display": "Certainly Not a Match",
        }
    )
    """
    Certainly Not a Match

    This record is known not to be a match. Note that usually non-matching records are not returned, but in some cases records previously or likely considered as a match may specifically be negated by the matching engine.
    """

    class Meta:
        resource = _resource
