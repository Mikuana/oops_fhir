from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AdverseEventCausalityAssessment"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AdverseEventCausalityAssessment:
    """
    AdverseEventCausalityAssessment

    Codes for the assessment of whether the entity caused the event.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/adverse-event-causality-assess
    """

    certain = CodeSystemConcept(
        {
            "code": "Certain",
            "definition": "i) Event or laboratory test abnormality, with plausible time relationship to drug intake; ii) Cannot be explained by disease or other drugs; iii) Response to withdrawal plausible (pharmacologically, pathologically); iv) Event definitive pharmacologically or phenomenologically (i.e. an objective and specific medical disorder or a recognized pharmacological phenomenon); or v) Re-challenge satisfactory, if necessary.",
            "display": "Certain",
        }
    )
    """
    Certain

    i) Event or laboratory test abnormality, with plausible time relationship to drug intake; ii) Cannot be explained by disease or other drugs; iii) Response to withdrawal plausible (pharmacologically, pathologically); iv) Event definitive pharmacologically or phenomenologically (i.e. an objective and specific medical disorder or a recognized pharmacological phenomenon); or v) Re-challenge satisfactory, if necessary.
    """

    probably_likely = CodeSystemConcept(
        {
            "code": "Probably-Likely",
            "definition": "i) Event or laboratory test abnormality, with reasonable time relationship to drug intake; ii) Unlikely to be attributed to disease or other drugs; iii) Response to withdrawal clinically reasonable; or iv) Re-challenge not required.",
            "display": "Probably/Likely",
        }
    )
    """
    Probably/Likely

    i) Event or laboratory test abnormality, with reasonable time relationship to drug intake; ii) Unlikely to be attributed to disease or other drugs; iii) Response to withdrawal clinically reasonable; or iv) Re-challenge not required.
    """

    possible = CodeSystemConcept(
        {
            "code": "Possible",
            "definition": "i) Event or laboratory test abnormality, with reasonable time relationship to drug intake; ii) Could also be explained by disease or other drugs; or iii) Information on drug withdrawal may be lacking or unclear.",
            "display": "Possible",
        }
    )
    """
    Possible

    i) Event or laboratory test abnormality, with reasonable time relationship to drug intake; ii) Could also be explained by disease or other drugs; or iii) Information on drug withdrawal may be lacking or unclear.
    """

    unlikely = CodeSystemConcept(
        {
            "code": "Unlikely",
            "definition": "i) Event or laboratory test abnormality, with a time to drug intake that makes a relationship improbable (but not impossible); or ii) Disease or other drugs provide plausible explanations.",
            "display": "Unlikely",
        }
    )
    """
    Unlikely

    i) Event or laboratory test abnormality, with a time to drug intake that makes a relationship improbable (but not impossible); or ii) Disease or other drugs provide plausible explanations.
    """

    conditional_classified = CodeSystemConcept(
        {
            "code": "Conditional-Classified",
            "definition": "i) Event or laboratory test abnormality; ii) More data for proper assessment needed; or iii) Additional data under examination.",
            "display": "Conditional/Classified",
        }
    )
    """
    Conditional/Classified

    i) Event or laboratory test abnormality; ii) More data for proper assessment needed; or iii) Additional data under examination.
    """

    unassessable_unclassifiable = CodeSystemConcept(
        {
            "code": "Unassessable-Unclassifiable",
            "definition": "i) Report suggesting an adverse reaction; ii) Cannot be judged because information is insufficient or contradictory; or iii) Data cannot be supplemented or verified.",
            "display": "Unassessable/Unclassifiable",
        }
    )
    """
    Unassessable/Unclassifiable

    i) Report suggesting an adverse reaction; ii) Cannot be judged because information is insufficient or contradictory; or iii) Data cannot be supplemented or verified.
    """

    class Meta:
        resource = _resource
