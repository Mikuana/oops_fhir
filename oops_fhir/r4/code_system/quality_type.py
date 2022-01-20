from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["qualityType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class qualityType:
    """
    qualityType

    Type for quality report.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/quality-type
    """

    indel = CodeSystemConcept(
        {
            "code": "indel",
            "definition": "INDEL Comparison.",
            "display": "INDEL Comparison",
        }
    )
    """
    INDEL Comparison

    INDEL Comparison.
    """

    snp = CodeSystemConcept(
        {"code": "snp", "definition": "SNP Comparison.", "display": "SNP Comparison"}
    )
    """
    SNP Comparison

    SNP Comparison.
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": "UNKNOWN Comparison.",
            "display": "UNKNOWN Comparison",
        }
    )
    """
    UNKNOWN Comparison

    UNKNOWN Comparison.
    """

    class Meta:
        resource = _resource
