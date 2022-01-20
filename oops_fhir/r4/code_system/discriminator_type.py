from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DiscriminatorType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DiscriminatorType:
    """
    DiscriminatorType

    How an element value is interpreted when discrimination is evaluated.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/discriminator-type
    """

    value = CodeSystemConcept(
        {
            "code": "value",
            "definition": "The slices have different values in the nominated element.",
            "display": "Value",
        }
    )
    """
    Value

    The slices have different values in the nominated element.
    """

    exists = CodeSystemConcept(
        {
            "code": "exists",
            "definition": "The slices are differentiated by the presence or absence of the nominated element.",
            "display": "Exists",
        }
    )
    """
    Exists

    The slices are differentiated by the presence or absence of the nominated element.
    """

    pattern = CodeSystemConcept(
        {
            "code": "pattern",
            "definition": "The slices have different values in the nominated element, as determined by testing them against the applicable ElementDefinition.pattern[x].",
            "display": "Pattern",
        }
    )
    """
    Pattern

    The slices have different values in the nominated element, as determined by testing them against the applicable ElementDefinition.pattern[x].
    """

    type_ = CodeSystemConcept(
        {
            "code": "type",
            "definition": "The slices are differentiated by type of the nominated element.",
            "display": "Type",
        }
    )
    """
    Type

    The slices are differentiated by type of the nominated element.
    """

    profile = CodeSystemConcept(
        {
            "code": "profile",
            "definition": "The slices are differentiated by conformance of the nominated element to a specified profile. Note that if the path specifies .resolve() then the profile is the target profile on the reference. In this case, validation by the possible profiles is required to differentiate the slices.",
            "display": "Profile",
        }
    )
    """
    Profile

    The slices are differentiated by conformance of the nominated element to a specified profile. Note that if the path specifies .resolve() then the profile is the target profile on the reference. In this case, validation by the possible profiles is required to differentiate the slices.
    """

    class Meta:
        resource = _resource
