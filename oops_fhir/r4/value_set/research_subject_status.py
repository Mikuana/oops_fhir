from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.research_subject_status import (
    ResearchSubjectStatus as ResearchSubjectStatus_,
)


__all__ = ["ResearchSubjectStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ResearchSubjectStatus(ResearchSubjectStatus_):
    """
    ResearchSubjectStatus

    Indicates the progression of a study subject through a study.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/research-subject-status
    """

    class Meta:
        resource = _resource
