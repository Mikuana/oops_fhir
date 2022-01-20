from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContractContentDerivationCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContractContentDerivationCodes:
    """
    Contract Content Derivation Codes

    This is an example set of Content Derivative type codes, which represent
the minimal content derived from the basal information source at a
specific stage in its lifecycle, which is sufficient to manage that
source information, for example, in a repository, registry, processes
and workflows, for making access control decisions, and providing query
responses.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/contract-content-derivative
    """

    registration = CodeSystemConcept(
        {
            "code": "registration",
            "definition": "Content derivative that conveys sufficient information needed to register the source basal content from which it is derived.  This derivative content may be used to register the basal content as it changes status in its lifecycle.  For example, content registration may occur when the basal content is created, updated, inactive, or deleted.",
            "display": "Content Registration",
        }
    )
    """
    Content Registration

    Content derivative that conveys sufficient information needed to register the source basal content from which it is derived.  This derivative content may be used to register the basal content as it changes status in its lifecycle.  For example, content registration may occur when the basal content is created, updated, inactive, or deleted.
    """

    retrieval = CodeSystemConcept(
        {
            "code": "retrieval",
            "definition": "A content derivative that conveys sufficient information to locate and retrieve the content.",
            "display": "Content Retrieval",
        }
    )
    """
    Content Retrieval

    A content derivative that conveys sufficient information to locate and retrieve the content.
    """

    statement = CodeSystemConcept(
        {
            "code": "statement",
            "definition": "Content derivative that has less than full fidelity to the basal information source from which it was 'transcribed'. It provides recipients with the full content representation they may require for compliance purposes, and typically include a reference to or an attached unstructured representation for recipients needing an exact copy of the legal agreement.",
            "display": "Content Statement",
        }
    )
    """
    Content Statement

    Content derivative that has less than full fidelity to the basal information source from which it was 'transcribed'. It provides recipients with the full content representation they may require for compliance purposes, and typically include a reference to or an attached unstructured representation for recipients needing an exact copy of the legal agreement.
    """

    shareable = CodeSystemConcept(
        {
            "code": "shareable",
            "definition": "A Content Derivative that conveys sufficient information to determine the authorized entities with which the content may be shared.",
            "display": "Shareable Content",
        }
    )
    """
    Shareable Content

    A Content Derivative that conveys sufficient information to determine the authorized entities with which the content may be shared.
    """

    class Meta:
        resource = _resource
