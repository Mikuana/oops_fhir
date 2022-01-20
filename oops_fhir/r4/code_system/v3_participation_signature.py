from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ParticipationSignature"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ParticipationSignature:
    """
    v3 Code System ParticipationSignature

     A set of codes specifying whether and how the participant has attested
his participation through a signature and or whether such a signature is
needed.  Examples:  A surgical Procedure act object (representing a
procedure report) requires a signature of the performing and responsible
surgeon, and possibly other participants. (See also:
Participation.signatureText.)

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ParticipationSignature
    """

    i = CodeSystemConcept(
        {
            "code": "I",
            "definition": "The particpant intends to provide a signature.",
            "display": "intended",
        }
    )
    """
    intended

    The particpant intends to provide a signature.
    """

    s = CodeSystemConcept(
        {
            "code": "S",
            "definition": "Signature has been affixed, either written on file, or electronic (incl. digital) signature in Participation.signatureText.",
            "display": "signed",
        }
    )
    """
    signed

    Signature has been affixed, either written on file, or electronic (incl. digital) signature in Participation.signatureText.
    """

    x = CodeSystemConcept(
        {
            "code": "X",
            "definition": "A signature for the service is required of this actor.",
            "display": "required",
        }
    )
    """
    required

    A signature for the service is required of this actor.
    """

    class Meta:
        resource = _resource
