from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CompositionStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CompositionStatus:
    """
    CompositionStatus

    The workflow/clinical status of the composition.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/composition-status
    """

    preliminary = CodeSystemConcept(
        {
            "code": "preliminary",
            "definition": "This is a preliminary composition or document (also known as initial or interim). The content may be incomplete or unverified.",
            "display": "Preliminary",
        }
    )
    """
    Preliminary

    This is a preliminary composition or document (also known as initial or interim). The content may be incomplete or unverified.
    """

    final = CodeSystemConcept(
        {
            "code": "final",
            "definition": "This version of the composition is complete and verified by an appropriate person and no further work is planned. Any subsequent updates would be on a new version of the composition.",
            "display": "Final",
        }
    )
    """
    Final

    This version of the composition is complete and verified by an appropriate person and no further work is planned. Any subsequent updates would be on a new version of the composition.
    """

    amended = CodeSystemConcept(
        {
            "code": "amended",
            "definition": 'The composition content or the referenced resources have been modified (edited or added to) subsequent to being released as "final" and the composition is complete and verified by an authorized person.',
            "display": "Amended",
        }
    )
    """
    Amended

    The composition content or the referenced resources have been modified (edited or added to) subsequent to being released as "final" and the composition is complete and verified by an authorized person.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The composition or document was originally created/issued in error, and this is an amendment that marks that the entire series should not be considered as valid.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The composition or document was originally created/issued in error, and this is an amendment that marks that the entire series should not be considered as valid.
    """

    class Meta:
        resource = _resource
