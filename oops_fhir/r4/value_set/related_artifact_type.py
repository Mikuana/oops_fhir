from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.related_artifact_type import (
    RelatedArtifactType as RelatedArtifactType_,
)


__all__ = ["RelatedArtifactType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class RelatedArtifactType(RelatedArtifactType_):
    """
    RelatedArtifactType

    The type of relationship to the related artifact.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/related-artifact-type
    """

    class Meta:
        resource = _resource
