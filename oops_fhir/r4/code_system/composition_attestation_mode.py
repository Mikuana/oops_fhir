from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CompositionAttestationMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CompositionAttestationMode:
    """
    CompositionAttestationMode

    The way in which a person authenticated a composition.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/composition-attestation-mode
    """

    personal = CodeSystemConcept(
        {
            "code": "personal",
            "definition": "The person authenticated the content in their personal capacity.",
            "display": "Personal",
        }
    )
    """
    Personal

    The person authenticated the content in their personal capacity.
    """

    professional = CodeSystemConcept(
        {
            "code": "professional",
            "definition": "The person authenticated the content in their professional capacity.",
            "display": "Professional",
        }
    )
    """
    Professional

    The person authenticated the content in their professional capacity.
    """

    legal = CodeSystemConcept(
        {
            "code": "legal",
            "definition": "The person authenticated the content and accepted legal responsibility for its content.",
            "display": "Legal",
        }
    )
    """
    Legal

    The person authenticated the content and accepted legal responsibility for its content.
    """

    official = CodeSystemConcept(
        {
            "code": "official",
            "definition": "The organization authenticated the content as consistent with their policies and procedures.",
            "display": "Official",
        }
    )
    """
    Official

    The organization authenticated the content as consistent with their policies and procedures.
    """

    class Meta:
        resource = _resource
