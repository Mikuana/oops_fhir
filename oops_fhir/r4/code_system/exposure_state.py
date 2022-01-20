from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExposureState"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExposureState:
    """
    ExposureState

    Whether the results by exposure is describing the results for the
primary exposure of interest (exposure) or the alternative state
(exposureAlternative).

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/exposure-state
    """

    exposure = CodeSystemConcept(
        {
            "code": "exposure",
            "definition": "used when the results by exposure is describing the results for the primary exposure of interest.",
            "display": "Exposure",
        }
    )
    """
    Exposure

    used when the results by exposure is describing the results for the primary exposure of interest.
    """

    exposure_alternative = CodeSystemConcept(
        {
            "code": "exposure-alternative",
            "definition": "used when the results by exposure is describing the results for the alternative exposure state, control state or comparator state.",
            "display": "Exposure Alternative",
        }
    )
    """
    Exposure Alternative

    used when the results by exposure is describing the results for the alternative exposure state, control state or comparator state.
    """

    class Meta:
        resource = _resource
