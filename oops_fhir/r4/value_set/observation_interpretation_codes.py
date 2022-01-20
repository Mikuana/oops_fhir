from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_observation_interpretation import (
    v3ObservationInterpretation,
)


__all__ = ["ObservationInterpretationCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ObservationInterpretationCodes(v3ObservationInterpretation):
    """
    Observation Interpretation Codes

    A categorical assessment, providing a rough qualitative interpretation
of the observation value,    such as “normal”/ “abnormal”,”low” /
“high”, “better” / “worse”, “susceptible” / “resistant”, “expected”/
“not expected”.    The value set is intended to be for ANY use where
coded representation of an interpretation is needed.             Notes:
This is being communicated in v2.x in OBX-8 (Observation
Interpretation), in v3 in ObservationInterpretation (CWE) in R1
(Representative Realm) and in FHIR in    Observation.interpretation.
Historically these values come from the laboratory domain, and these
codes are extensively    used. The value set binding is extensible, so
codes outside the value set that are needed for interpretation concepts
(i.e. particular meanings) that are not included in the value set can be
used, and these new codes may also be added to    the value set and
published in a future version.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/observation-interpretation
    """

    class Meta:
        resource = _resource
