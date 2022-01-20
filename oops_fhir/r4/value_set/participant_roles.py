from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["ParticipantRoles"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ParticipantRoles(ValueSet):
    """
    Participant Roles

    Roles of participants that may be included in a care team.  Defined as:
Is a Person, Healthcare professional (occupation) or Healthcare related
organization (qualifier value).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/participant-role
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
