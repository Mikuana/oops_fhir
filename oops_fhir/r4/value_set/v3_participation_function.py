from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_participation_function import (
    v3ParticipationFunction as v3ParticipationFunction_,
)


__all__ = ["v3ParticipationFunction"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ParticipationFunction(v3ParticipationFunction_):
    """
    v3 Code System ParticipationFunction

     This code is used to specify the exact function an actor had in a
service in all necessary detail. This domain may include local
extensions (CWE).

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ParticipationFunction
    """

    class Meta:
        resource = _resource
