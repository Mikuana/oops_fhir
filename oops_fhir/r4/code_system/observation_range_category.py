from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ObservationRangeCategory"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ObservationRangeCategory:
    """
    ObservationRangeCategory

    Codes identifying the category of observation range.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/observation-range-category
    """

    reference = CodeSystemConcept(
        {
            "code": "reference",
            "definition": "Reference (Normal) Range for Ordinal and Continuous Observations.",
            "display": "reference range",
        }
    )
    """
    reference range

    Reference (Normal) Range for Ordinal and Continuous Observations.
    """

    critical = CodeSystemConcept(
        {
            "code": "critical",
            "definition": "Critical Range for Ordinal and Continuous Observations.",
            "display": "critical range",
        }
    )
    """
    critical range

    Critical Range for Ordinal and Continuous Observations.
    """

    absolute = CodeSystemConcept(
        {
            "code": "absolute",
            "definition": "Absolute Range for Ordinal and Continuous Observations. Results outside this range are not possible.",
            "display": "absolute range",
        }
    )
    """
    absolute range

    Absolute Range for Ordinal and Continuous Observations. Results outside this range are not possible.
    """

    class Meta:
        resource = _resource
