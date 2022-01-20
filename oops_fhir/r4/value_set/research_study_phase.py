from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.research_study_phase import (
    ResearchStudyPhase as ResearchStudyPhase_,
)


__all__ = ["ResearchStudyPhase"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ResearchStudyPhase(ResearchStudyPhase_):
    """
    ResearchStudyPhase

    Codes for the stage in the progression of a therapy from initial
experimental use in humans in clinical trials to post-market evaluation.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/research-study-phase
    """

    class Meta:
        resource = _resource
