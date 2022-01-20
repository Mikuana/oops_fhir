from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_participation_signature import (
    v3ParticipationSignature as v3ParticipationSignature_,
)


__all__ = ["v3ParticipationSignature"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ParticipationSignature(v3ParticipationSignature_):
    """
    v3 Code System ParticipationSignature

     A set of codes specifying whether and how the participant has attested
his participation through a signature and or whether such a signature is
needed.  Examples:  A surgical Procedure act object (representing a
procedure report) requires a signature of the performing and responsible
surgeon, and possibly other participants. (See also:
Participation.signatureText.)

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ParticipationSignature
    """

    class Meta:
        resource = _resource
