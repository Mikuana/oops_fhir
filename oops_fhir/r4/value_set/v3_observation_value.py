from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_observation_value import (
    v3ObservationValue as v3ObservationValue_,
)


__all__ = ["v3ObservationValue"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ObservationValue(v3ObservationValue_):
    """
    v3 Code System ObservationValue

     This domain is the root domain to which all HL7-recognized value sets
for the Observation.value attribute will be linked when
Observation.value has a coded data type.  OpenIssue:  Description copied
from Concept Domain of same name.  Must be corrected..

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ObservationValue
    """

    class Meta:
        resource = _resource
