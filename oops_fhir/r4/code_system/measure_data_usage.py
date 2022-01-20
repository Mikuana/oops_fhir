from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MeasureDataUsage"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MeasureDataUsage:
    """
    MeasureDataUsage

    The intended usage for supplemental data elements in the measure.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/measure-data-usage
    """

    supplemental_data = CodeSystemConcept(
        {
            "code": "supplemental-data",
            "definition": "The data is intended to be provided as additional information alongside the measure results.",
            "display": "Supplemental Data",
        }
    )
    """
    Supplemental Data

    The data is intended to be provided as additional information alongside the measure results.
    """

    risk_adjustment_factor = CodeSystemConcept(
        {
            "code": "risk-adjustment-factor",
            "definition": "The data is intended to be used to calculate and apply a risk adjustment model for the measure.",
            "display": "Risk Adjustment Factor",
        }
    )
    """
    Risk Adjustment Factor

    The data is intended to be used to calculate and apply a risk adjustment model for the measure.
    """

    class Meta:
        resource = _resource
