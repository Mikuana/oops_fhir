from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.match_grade import MatchGrade as MatchGrade_


__all__ = ["MatchGrade"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MatchGrade(MatchGrade_):
    """
    MatchGrade

    A Master Patient Index (MPI) assessment of whether a candidate patient
record is a match or not.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/match-grade
    """

    class Meta:
        resource = _resource
