from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3TargetAwareness"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3TargetAwareness:
    """
    v3 Code System TargetAwareness

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-TargetAwareness
    """

    d = CodeSystemConcept(
        {
            "code": "D",
            "definition": "Target person has been informed about the issue but currently denies it.",
            "display": "denying",
        }
    )
    """
    denying

    Target person has been informed about the issue but currently denies it.
    """

    f = CodeSystemConcept(
        {
            "code": "F",
            "definition": "Target person is fully aware of the issue.",
            "display": "full awareness",
        }
    )
    """
    full awareness

    Target person is fully aware of the issue.
    """

    i = CodeSystemConcept(
        {
            "code": "I",
            "definition": "Target person is not capable of comprehending the issue.",
            "display": "incapable",
        }
    )
    """
    incapable

    Target person is not capable of comprehending the issue.
    """

    m = CodeSystemConcept(
        {
            "code": "M",
            "definition": "Target person is marginally aware of the issue.",
            "display": "marginal",
        }
    )
    """
    marginal

    Target person is marginally aware of the issue.
    """

    p = CodeSystemConcept(
        {
            "code": "P",
            "definition": "Target person is partially aware of the issue.",
            "display": "partial",
        }
    )
    """
    partial

    Target person is partially aware of the issue.
    """

    u = CodeSystemConcept(
        {
            "code": "U",
            "definition": "Target person has not yet been informed of the issue.",
            "display": "uninformed",
        }
    )
    """
    uninformed

    Target person has not yet been informed of the issue.
    """

    class Meta:
        resource = _resource
