from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.detected_issue_severity import (
    DetectedIssueSeverity as DetectedIssueSeverity_,
)


__all__ = ["DetectedIssueSeverity"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DetectedIssueSeverity(DetectedIssueSeverity_):
    """
    DetectedIssueSeverity

    Indicates the potential degree of impact of the identified issue on the
patient.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/detectedissue-severity
    """

    class Meta:
        resource = _resource
