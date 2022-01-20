from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ObservationCategoryCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ObservationCategoryCodes:
    """
    Observation Category Codes

    Codes to denote a guideline or policy statement.when a genetic test
result is being shared as a secondary finding.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/secondary-finding
    """

    acmg_version1 = CodeSystemConcept(
        {
            "code": "acmg-version1",
            "definition": "First release (2013): ACMG Recommendations for Reporting of Incidental Findings in Clinical Exome and Genome Sequencing.  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3727274/",
            "display": "ACMG Version 1",
        }
    )
    """
    ACMG Version 1

    First release (2013): ACMG Recommendations for Reporting of Incidental Findings in Clinical Exome and Genome Sequencing.  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3727274/
    """

    acmg_version2 = CodeSystemConcept(
        {
            "code": "acmg-version2",
            "definition": "Second release (2016): Recommendations for reporting of secondary findings in clinical exome and genome sequencing, 2016 update (ACMG SF v2.0): a policy statement of the American College of Medical Genetics and Genomics. https://www.ncbi.nlm.nih.gov/pubmed/27854360",
            "display": "ACMG Version 2",
        }
    )
    """
    ACMG Version 2

    Second release (2016): Recommendations for reporting of secondary findings in clinical exome and genome sequencing, 2016 update (ACMG SF v2.0): a policy statement of the American College of Medical Genetics and Genomics. https://www.ncbi.nlm.nih.gov/pubmed/27854360
    """

    class Meta:
        resource = _resource
