from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ResponseModality"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ResponseModality:
    """
    v3 Code System ResponseModality

     Defines the timing and grouping of the response instances.  OpenIssue:
Description copied from Concept Domain of same name.  Must be verified.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ResponseModality
    """

    b = CodeSystemConcept(
        {
            "code": "B",
            "definition": "Query response to be sent as an HL7 Batch.",
            "display": "Batch",
        }
    )
    """
    Batch

    Query response to be sent as an HL7 Batch.
    """

    r = CodeSystemConcept(
        {
            "code": "R",
            "definition": "Query response to occur in real time.",
            "display": "Real Time",
        }
    )
    """
    Real Time

    Query response to occur in real time.
    """

    t = CodeSystemConcept(
        {
            "code": "T",
            "definition": "Query response to sent as a series of responses at the same time without the use of batch formatting.",
            "display": "Bolus",
        }
    )
    """
    Bolus

    Query response to sent as a series of responses at the same time without the use of batch formatting.
    """

    class Meta:
        resource = _resource
