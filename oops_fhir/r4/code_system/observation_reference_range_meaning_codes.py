from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ObservationReferenceRangeMeaningCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ObservationReferenceRangeMeaningCodes:
    """
    Observation Reference Range Meaning Codes

    This value set defines a set of codes that can be used to indicate the
meaning/use of a reference range for a particular target population.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/referencerange-meaning
    """

    type_ = CodeSystemConcept(
        {
            "code": "type",
            "concept": [
                {
                    "code": "normal",
                    "definition": "Values expected for a normal member of the relevant control population being measured. Typically each results producer such as a laboratory has specific normal ranges and they are usually defined as within two standard deviations from the mean and account for 95.45% of this population.",
                    "display": "Normal Range",
                },
                {
                    "code": "recommended",
                    "definition": "The range that is recommended by a relevant professional body.",
                    "display": "Recommended Range",
                },
                {
                    "code": "treatment",
                    "definition": "The range at which treatment would/should be considered.",
                    "display": "Treatment Range",
                },
                {
                    "code": "therapeutic",
                    "concept": [
                        {
                            "code": "pre",
                            "definition": "The optimal range for best therapeutic outcomes for a specimen taken immediately before administration.",
                            "display": "Pre Therapeutic Desired Level",
                        },
                        {
                            "code": "post",
                            "definition": "The optimal range for best therapeutic outcomes for a specimen taken immediately after administration.",
                            "display": "Post Therapeutic Desired Level",
                        },
                    ],
                    "definition": "The optimal range for best therapeutic outcomes.",
                    "display": "Therapeutic Desired Level",
                },
            ],
            "definition": "General types of reference range.",
            "display": "Type",
            "property": [{"code": "abstract", "valueBoolean": True}],
        }
    )
    """
    Type

    General types of reference range.
    """

    endocrine = CodeSystemConcept(
        {
            "code": "endocrine",
            "concept": [
                {
                    "code": "pre-puberty",
                    "definition": "An expected range in an individual prior to puberty.",
                    "display": "Pre-Puberty",
                },
                {
                    "code": "follicular",
                    "definition": "An expected range in an individual during the follicular stage of the cycle.",
                    "display": "Follicular Stage",
                },
                {
                    "code": "midcycle",
                    "definition": "An expected range in an individual during the midcycle stage of the cycle.",
                    "display": "MidCycle",
                },
                {
                    "code": "luteal",
                    "definition": "An expected range in an individual during the luteal stage of the cycle.",
                    "display": "Luteal",
                },
                {
                    "code": "postmenopausal",
                    "definition": "An expected range in an individual post-menopause.",
                    "display": "Post-Menopause",
                },
            ],
            "definition": "Endocrine related states that change the expected value.",
            "display": "Endocrine",
            "property": [{"code": "abstract", "valueBoolean": True}],
        }
    )
    """
    Endocrine

    Endocrine related states that change the expected value.
    """

    class Meta:
        resource = _resource
