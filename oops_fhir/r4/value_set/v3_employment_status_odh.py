from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_observation_value import v3ObservationValue


__all__ = ["v3employmentStatusODH"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3employmentStatusODH(v3ObservationValue):
    """
    V3 Value SetemploymentStatusODH

     Concepts representing whether a person does or does not currently have
a job or is not currently in the labor pool seeking employment.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-employmentStatusODH
    """

    class Meta:
        resource = _resource
