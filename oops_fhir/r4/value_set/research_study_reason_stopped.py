from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.research_study_reason_stopped import (
    ResearchStudyReasonStopped as ResearchStudyReasonStopped_,
)


__all__ = ["ResearchStudyReasonStopped"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ResearchStudyReasonStopped(ResearchStudyReasonStopped_):
    """
    ResearchStudyReasonStopped

    Codes for why the study ended prematurely.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/research-study-reason-stopped
    """

    class Meta:
        resource = _resource
