from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.research_study_status import (
    ResearchStudyStatus as ResearchStudyStatus_,
)


__all__ = ["ResearchStudyStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ResearchStudyStatus(ResearchStudyStatus_):
    """
    ResearchStudyStatus

    Codes that convey the current status of the research study.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/research-study-status
    """

    class Meta:
        resource = _resource
