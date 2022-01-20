from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["BindingStrength"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class BindingStrength:
    """
    BindingStrength

    Indication of the degree of conformance expectations associated with a
binding.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/binding-strength
    """

    required = CodeSystemConcept(
        {
            "code": "required",
            "definition": "To be conformant, the concept in this element SHALL be from the specified value set.",
            "display": "Required",
        }
    )
    """
    Required

    To be conformant, the concept in this element SHALL be from the specified value set.
    """

    extensible = CodeSystemConcept(
        {
            "code": "extensible",
            "definition": "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.",
            "display": "Extensible",
        }
    )
    """
    Extensible

    To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.
    """

    preferred = CodeSystemConcept(
        {
            "code": "preferred",
            "definition": "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.",
            "display": "Preferred",
        }
    )
    """
    Preferred

    Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.
    """

    example = CodeSystemConcept(
        {
            "code": "example",
            "definition": "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.",
            "display": "Example",
        }
    )
    """
    Example

    Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.
    """

    class Meta:
        resource = _resource
