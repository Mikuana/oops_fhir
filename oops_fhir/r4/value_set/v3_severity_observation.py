from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_observation_value import v3ObservationValue


__all__ = ["v3SeverityObservation"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3SeverityObservation(v3ObservationValue):
    """
    V3 Value SetSeverityObservation

     Potential values for observations of severity.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-SeverityObservation
    """

    class Meta:
        resource = _resource
