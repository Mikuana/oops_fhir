from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.research_study_primary_purpose_type import (
    ResearchStudyPrimaryPurposeType as ResearchStudyPrimaryPurposeType_,
)


__all__ = ["ResearchStudyPrimaryPurposeType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ResearchStudyPrimaryPurposeType(ResearchStudyPrimaryPurposeType_):
    """
    ResearchStudyPrimaryPurposeType

    Codes for the main intent of the study.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/research-study-prim-purp-type
    """

    class Meta:
        resource = _resource
