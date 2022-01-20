from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.exposure_state import ExposureState as ExposureState_


__all__ = ["ExposureState"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExposureState(ExposureState_):
    """
    ExposureState

    Whether the results by exposure is describing the results for the
primary exposure of interest (exposure) or the alternative state
(exposureAlternative).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/exposure-state
    """

    class Meta:
        resource = _resource
