from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_exposure_mode import v3ExposureMode as v3ExposureMode_


__all__ = ["v3ExposureMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ExposureMode(v3ExposureMode_):
    """
    v3 Code System ExposureMode

     Code for the mechanism by which the exposure agent was exchanged or
potentially exchanged by the participants involved in the exposure.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ExposureMode
    """

    class Meta:
        resource = _resource
