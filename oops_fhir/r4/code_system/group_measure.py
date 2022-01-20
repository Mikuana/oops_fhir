from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["GroupMeasure"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class GroupMeasure:
    """
    GroupMeasure

    Possible group measure aggregates (E.g. Mean, Median).

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/group-measure
    """

    mean = CodeSystemConcept(
        {
            "code": "mean",
            "definition": "Aggregated using Mean of participant values.",
            "display": "Mean",
        }
    )
    """
    Mean

    Aggregated using Mean of participant values.
    """

    median = CodeSystemConcept(
        {
            "code": "median",
            "definition": "Aggregated using Median of participant values.",
            "display": "Median",
        }
    )
    """
    Median

    Aggregated using Median of participant values.
    """

    mean_of_mean = CodeSystemConcept(
        {
            "code": "mean-of-mean",
            "definition": "Aggregated using Mean of study mean values.",
            "display": "Mean of Study Means",
        }
    )
    """
    Mean of Study Means

    Aggregated using Mean of study mean values.
    """

    mean_of_median = CodeSystemConcept(
        {
            "code": "mean-of-median",
            "definition": "Aggregated using Mean of study median values.",
            "display": "Mean of Study Medins",
        }
    )
    """
    Mean of Study Medins

    Aggregated using Mean of study median values.
    """

    median_of_mean = CodeSystemConcept(
        {
            "code": "median-of-mean",
            "definition": "Aggregated using Median of study mean values.",
            "display": "Median of Study Means",
        }
    )
    """
    Median of Study Means

    Aggregated using Median of study mean values.
    """

    median_of_median = CodeSystemConcept(
        {
            "code": "median-of-median",
            "definition": "Aggregated using Median of study median values.",
            "display": "Median of Study Medians",
        }
    )
    """
    Median of Study Medians

    Aggregated using Median of study median values.
    """

    class Meta:
        resource = _resource
