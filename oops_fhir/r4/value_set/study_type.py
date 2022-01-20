from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.study_type import StudyType as StudyType_


__all__ = ["StudyType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class StudyType(StudyType_):
    """
    StudyType

    Types of research studies (types of research methods).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/study-type
    """

    class Meta:
        resource = _resource
