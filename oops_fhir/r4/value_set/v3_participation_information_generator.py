from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_participation_type import v3ParticipationType


__all__ = ["v3ParticipationInformationGenerator"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ParticipationInformationGenerator(v3ParticipationType):
    """
    V3 Value SetParticipationInformationGenerator

     Parties that may or should contribute or have contributed information
to the Act. Such information includes information leading to the
decision to perform the Act and how to perform the Act (e.g.,
consultant), information that the Act itself seeks to reveal (e.g.,
informant of clinical history), or information about what Act was
performed (e.g., informant witness).

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ParticipationInformationGenerator
    """

    class Meta:
        resource = _resource
