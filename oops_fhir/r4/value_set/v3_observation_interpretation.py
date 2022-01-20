from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_observation_interpretation import (
    v3ObservationInterpretation as v3ObservationInterpretation_,
)


__all__ = ["v3ObservationInterpretation"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ObservationInterpretation(v3ObservationInterpretation_):
    """
    v3 Code System ObservationInterpretation

    One or more codes providing a rough qualitative interpretation of the
observation, such as "normal" / "abnormal", "low" / "high", "better" /
"worse", "resistant" /  "susceptible", "expected" / "not expected". The
value set is intended to be for ANY use where coded representation of an
interpretation is needed.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ObservationInterpretation
    """

    class Meta:
        resource = _resource
