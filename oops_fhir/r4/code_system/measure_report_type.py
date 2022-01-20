from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MeasureReportType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MeasureReportType:
    """
    MeasureReportType

    The type of the measure report.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/measure-report-type
    """

    individual = CodeSystemConcept(
        {
            "code": "individual",
            "definition": "An individual report that provides information on the performance for a given measure with respect to a single subject.",
            "display": "Individual",
        }
    )
    """
    Individual

    An individual report that provides information on the performance for a given measure with respect to a single subject.
    """

    subject_list = CodeSystemConcept(
        {
            "code": "subject-list",
            "definition": "A subject list report that includes a listing of subjects that satisfied each population criteria in the measure.",
            "display": "Subject List",
        }
    )
    """
    Subject List

    A subject list report that includes a listing of subjects that satisfied each population criteria in the measure.
    """

    summary = CodeSystemConcept(
        {
            "code": "summary",
            "definition": "A summary report that returns the number of members in each population criteria for the measure.",
            "display": "Summary",
        }
    )
    """
    Summary

    A summary report that returns the number of members in each population criteria for the measure.
    """

    data_collection = CodeSystemConcept(
        {
            "code": "data-collection",
            "definition": "A data collection report that contains data-of-interest for the measure.",
            "display": "Data Collection",
        }
    )
    """
    Data Collection

    A data collection report that contains data-of-interest for the measure.
    """

    class Meta:
        resource = _resource
