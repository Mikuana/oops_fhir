from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["RelatedArtifactType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class RelatedArtifactType:
    """
    RelatedArtifactType

    The type of relationship to the related artifact.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/related-artifact-type
    """

    documentation = CodeSystemConcept(
        {
            "code": "documentation",
            "definition": "Additional documentation for the knowledge resource. This would include additional instructions on usage as well as additional information on clinical context or appropriateness.",
            "display": "Documentation",
        }
    )
    """
    Documentation

    Additional documentation for the knowledge resource. This would include additional instructions on usage as well as additional information on clinical context or appropriateness.
    """

    justification = CodeSystemConcept(
        {
            "code": "justification",
            "definition": "A summary of the justification for the knowledge resource including supporting evidence, relevant guidelines, or other clinically important information. This information is intended to provide a way to make the justification for the knowledge resource available to the consumer of interventions or results produced by the knowledge resource.",
            "display": "Justification",
        }
    )
    """
    Justification

    A summary of the justification for the knowledge resource including supporting evidence, relevant guidelines, or other clinically important information. This information is intended to provide a way to make the justification for the knowledge resource available to the consumer of interventions or results produced by the knowledge resource.
    """

    citation = CodeSystemConcept(
        {
            "code": "citation",
            "definition": "Bibliographic citation for papers, references, or other relevant material for the knowledge resource. This is intended to allow for citation of related material, but that was not necessarily specifically prepared in connection with this knowledge resource.",
            "display": "Citation",
        }
    )
    """
    Citation

    Bibliographic citation for papers, references, or other relevant material for the knowledge resource. This is intended to allow for citation of related material, but that was not necessarily specifically prepared in connection with this knowledge resource.
    """

    predecessor = CodeSystemConcept(
        {
            "code": "predecessor",
            "definition": "The previous version of the knowledge resource.",
            "display": "Predecessor",
        }
    )
    """
    Predecessor

    The previous version of the knowledge resource.
    """

    successor = CodeSystemConcept(
        {
            "code": "successor",
            "definition": "The next version of the knowledge resource.",
            "display": "Successor",
        }
    )
    """
    Successor

    The next version of the knowledge resource.
    """

    derived_from = CodeSystemConcept(
        {
            "code": "derived-from",
            "definition": "The knowledge resource is derived from the related artifact. This is intended to capture the relationship in which a particular knowledge resource is based on the content of another artifact, but is modified to capture either a different set of overall requirements, or a more specific set of requirements such as those involved in a particular institution or clinical setting.",
            "display": "Derived From",
        }
    )
    """
    Derived From

    The knowledge resource is derived from the related artifact. This is intended to capture the relationship in which a particular knowledge resource is based on the content of another artifact, but is modified to capture either a different set of overall requirements, or a more specific set of requirements such as those involved in a particular institution or clinical setting.
    """

    depends_on = CodeSystemConcept(
        {
            "code": "depends-on",
            "definition": "The knowledge resource depends on the given related artifact.",
            "display": "Depends On",
        }
    )
    """
    Depends On

    The knowledge resource depends on the given related artifact.
    """

    composed_of = CodeSystemConcept(
        {
            "code": "composed-of",
            "definition": "The knowledge resource is composed of the given related artifact.",
            "display": "Composed Of",
        }
    )
    """
    Composed Of

    The knowledge resource is composed of the given related artifact.
    """

    class Meta:
        resource = _resource
