from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.knowledge_resource_type import (
    KnowledgeResourceType as KnowledgeResourceType_,
)


__all__ = ["KnowledgeResourceType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class KnowledgeResourceType(KnowledgeResourceType_):
    """
    KnowledgeResourceType

    A list of all the knowledge resource types defined in this version of
the FHIR specification.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/knowledge-resource-types
    """

    class Meta:
        resource = _resource
