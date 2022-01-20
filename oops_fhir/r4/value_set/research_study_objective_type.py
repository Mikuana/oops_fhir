from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.research_study_objective_type import (
    ResearchStudyObjectiveType as ResearchStudyObjectiveType_,
)


__all__ = ["ResearchStudyObjectiveType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ResearchStudyObjectiveType(ResearchStudyObjectiveType_):
    """
    ResearchStudyObjectiveType

    Codes for the kind of study objective.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/research-study-objective-type
    """

    class Meta:
        resource = _resource
