from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.imaging_study_status import (
    ImagingStudyStatus as ImagingStudyStatus_,
)


__all__ = ["ImagingStudyStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ImagingStudyStatus(ImagingStudyStatus_):
    """
    ImagingStudyStatus

    The status of the ImagingStudy.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/imagingstudy-status
    """

    class Meta:
        resource = _resource
