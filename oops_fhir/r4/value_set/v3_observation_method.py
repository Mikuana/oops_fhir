from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_observation_method import (
    v3ObservationMethod as v3ObservationMethod_,
)


__all__ = ["v3ObservationMethod"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ObservationMethod(v3ObservationMethod_):
    """
    v3 Code System ObservationMethod

     A code that provides additional detail about the means or technique
used to ascertain the observation.  Examples:  Blood pressure
measurement method: arterial puncture vs. sphygmomanometer (Riva-Rocci),
sitting vs. supine position, etc.  OpenIssue:  Description copied from
Concept Domain of same name.  Must be verified.  Note that the Domain
has a full discussion about use of the attribute and constraining that
is not appropriate for the code system description.  Needs to be
improved.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ObservationMethod
    """

    class Meta:
        resource = _resource
