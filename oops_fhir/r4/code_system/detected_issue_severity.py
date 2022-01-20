from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DetectedIssueSeverity"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DetectedIssueSeverity:
    """
    DetectedIssueSeverity

    Indicates the potential degree of impact of the identified issue on the
patient.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/detectedissue-severity
    """

    high = CodeSystemConcept(
        {
            "code": "high",
            "definition": "Indicates the issue may be life-threatening or has the potential to cause permanent injury.",
            "display": "High",
        }
    )
    """
    High

    Indicates the issue may be life-threatening or has the potential to cause permanent injury.
    """

    moderate = CodeSystemConcept(
        {
            "code": "moderate",
            "definition": "Indicates the issue may result in noticeable adverse consequences but is unlikely to be life-threatening or cause permanent injury.",
            "display": "Moderate",
        }
    )
    """
    Moderate

    Indicates the issue may result in noticeable adverse consequences but is unlikely to be life-threatening or cause permanent injury.
    """

    low = CodeSystemConcept(
        {
            "code": "low",
            "definition": "Indicates the issue may result in some adverse consequences but is unlikely to substantially affect the situation of the subject.",
            "display": "Low",
        }
    )
    """
    Low

    Indicates the issue may result in some adverse consequences but is unlikely to substantially affect the situation of the subject.
    """

    class Meta:
        resource = _resource
