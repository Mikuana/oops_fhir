from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SynthesisType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SynthesisType:
    """
    SynthesisType

    Types of combining results from a body of evidence (eg. summary data
meta-analysis).

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/synthesis-type
    """

    std_ma = CodeSystemConcept(
        {
            "code": "std-MA",
            "definition": "A meta-analysis of the summary data of estimates from individual studies or data sets.",
            "display": "summary data meta-analysis",
        }
    )
    """
    summary data meta-analysis

    A meta-analysis of the summary data of estimates from individual studies or data sets.
    """

    ipd_ma = CodeSystemConcept(
        {
            "code": "IPD-MA",
            "definition": "A meta-analysis of the individual participant data from individual studies or data sets.",
            "display": "individual patient data meta-analysis",
        }
    )
    """
    individual patient data meta-analysis

    A meta-analysis of the individual participant data from individual studies or data sets.
    """

    indirect_nma = CodeSystemConcept(
        {
            "code": "indirect-NMA",
            "definition": "An indirect meta-analysis derived from 2 or more direct comparisons in a network meta-analysis.",
            "display": "indirect network meta-analysis",
        }
    )
    """
    indirect network meta-analysis

    An indirect meta-analysis derived from 2 or more direct comparisons in a network meta-analysis.
    """

    combined_nma = CodeSystemConcept(
        {
            "code": "combined-NMA",
            "definition": "An composite meta-analysis derived from direct comparisons and indirect comparisons in a network meta-analysis.",
            "display": "combined direct plus indirect network meta-analysis",
        }
    )
    """
    combined direct plus indirect network meta-analysis

    An composite meta-analysis derived from direct comparisons and indirect comparisons in a network meta-analysis.
    """

    range_ = CodeSystemConcept(
        {
            "code": "range",
            "definition": "A range of results across a body of evidence.",
            "display": "range of results",
        }
    )
    """
    range of results

    A range of results across a body of evidence.
    """

    classification = CodeSystemConcept(
        {
            "code": "classification",
            "definition": "An approach describing a body of evidence by categorically classifying individual studies (eg 3 studies showed beneft and 2 studied found no effect).",
            "display": "classifcation of results",
        }
    )
    """
    classifcation of results

    An approach describing a body of evidence by categorically classifying individual studies (eg 3 studies showed beneft and 2 studied found no effect).
    """

    class Meta:
        resource = _resource
