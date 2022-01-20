from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ProvenanceParticipantRole"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ProvenanceParticipantRole:
    """
    Provenance participant role

    The role that a provenance participant played

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/provenance-participant-role
    """

    enterer = CodeSystemConcept(
        {
            "code": "enterer",
            "definition": "A person entering the data into the originating system",
            "display": "Enterer",
        }
    )
    """
    Enterer

    A person entering the data into the originating system
    """

    performer = CodeSystemConcept(
        {
            "code": "performer",
            "definition": "A person, animal, organization or device that who actually and principally carries out the activity",
            "display": "Performer",
        }
    )
    """
    Performer

    A person, animal, organization or device that who actually and principally carries out the activity
    """

    author = CodeSystemConcept(
        {
            "code": "author",
            "definition": "A party that originates the resource and therefore has responsibility for the information given in the resource and ownership of this resource",
            "display": "Author",
        }
    )
    """
    Author

    A party that originates the resource and therefore has responsibility for the information given in the resource and ownership of this resource
    """

    verifier = CodeSystemConcept(
        {
            "code": "verifier",
            "concept": [
                {
                    "code": "legal",
                    "definition": "The person authenticated the content and accepted legal responsibility for its content",
                    "display": "Legal Authenticator",
                }
            ],
            "definition": "A person who verifies the correctness and appropriateness of activity",
            "display": "Verifier",
        }
    )
    """
    Verifier

    A person who verifies the correctness and appropriateness of activity
    """

    attester = CodeSystemConcept(
        {
            "code": "attester",
            "definition": "A verifier who attests to the accuracy of the resource",
            "display": "Attester",
        }
    )
    """
    Attester

    A verifier who attests to the accuracy of the resource
    """

    informant = CodeSystemConcept(
        {
            "code": "informant",
            "definition": "A person who reported information that contributed to the resource",
            "display": "Informant",
        }
    )
    """
    Informant

    A person who reported information that contributed to the resource
    """

    custodian = CodeSystemConcept(
        {
            "code": "custodian",
            "definition": "The entity that is accountable for maintaining a true an accurate copy of the original record",
            "display": "Custodian",
        }
    )
    """
    Custodian

    The entity that is accountable for maintaining a true an accurate copy of the original record
    """

    assembler = CodeSystemConcept(
        {
            "code": "assembler",
            "definition": "A device that operates independently of an author on custodian's algorithms for data extraction of existing information for purpose of generating a new artifact.",
            "display": "Assembler",
        }
    )
    """
    Assembler

    A device that operates independently of an author on custodian's algorithms for data extraction of existing information for purpose of generating a new artifact.
    """

    composer = CodeSystemConcept(
        {
            "code": "composer",
            "definition": "A device used by an author to record new information, which may also be used by the author to select existing information for aggregation with newly recorded information for the purpose of generating a new artifact.",
            "display": "Composer",
        }
    )
    """
    Composer

    A device used by an author to record new information, which may also be used by the author to select existing information for aggregation with newly recorded information for the purpose of generating a new artifact.
    """

    class Meta:
        resource = _resource
