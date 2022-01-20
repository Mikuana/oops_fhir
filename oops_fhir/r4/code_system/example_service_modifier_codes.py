from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExampleServiceModifierCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExampleServiceModifierCodes:
    """
    Example Service Modifier Codes

    This value set includes sample Service Modifier codes which may support
differential payment.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://hl7.org/fhir/ex-servicemodifier
    """

    sr = CodeSystemConcept(
        {
            "code": "sr",
            "definition": "Services provided on the side of the road or such other non-conventional setting.",
            "display": "Side of the Road",
        }
    )
    """
    Side of the Road

    Services provided on the side of the road or such other non-conventional setting.
    """

    ah = CodeSystemConcept(
        {
            "code": "ah",
            "definition": "Services provided outside or normal business hours.",
            "display": "After hours",
        }
    )
    """
    After hours

    Services provided outside or normal business hours.
    """

    class Meta:
        resource = _resource
