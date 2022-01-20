from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CertaintySubcomponentRating"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CertaintySubcomponentRating:
    """
    CertaintySubcomponentRating

    The quality rating of the subcomponent of a quality of evidence rating.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/certainty-subcomponent-rating
    """

    no_change = CodeSystemConcept(
        {
            "code": "no-change",
            "definition": "no change to quality rating.",
            "display": "no change to rating",
        }
    )
    """
    no change to rating

    no change to quality rating.
    """

    downcode1 = CodeSystemConcept(
        {
            "code": "downcode1",
            "definition": "reduce quality rating by 1.",
            "display": "reduce rating: -1",
        }
    )
    """
    reduce rating: -1

    reduce quality rating by 1.
    """

    downcode2 = CodeSystemConcept(
        {
            "code": "downcode2",
            "definition": "reduce quality rating by 2.",
            "display": "reduce rating: -2",
        }
    )
    """
    reduce rating: -2

    reduce quality rating by 2.
    """

    downcode3 = CodeSystemConcept(
        {
            "code": "downcode3",
            "definition": "reduce quality rating by 3.",
            "display": "reduce rating: -3",
        }
    )
    """
    reduce rating: -3

    reduce quality rating by 3.
    """

    upcode1 = CodeSystemConcept(
        {
            "code": "upcode1",
            "definition": "increase quality rating by 1.",
            "display": "increase rating: +1",
        }
    )
    """
    increase rating: +1

    increase quality rating by 1.
    """

    upcode2 = CodeSystemConcept(
        {
            "code": "upcode2",
            "definition": "increase quality rating by 2.",
            "display": "increase rating: +2",
        }
    )
    """
    increase rating: +2

    increase quality rating by 2.
    """

    no_concern = CodeSystemConcept(
        {
            "code": "no-concern",
            "definition": "no serious concern.",
            "display": "no serious concern",
        }
    )
    """
    no serious concern

    no serious concern.
    """

    serious_concern = CodeSystemConcept(
        {
            "code": "serious-concern",
            "definition": "serious concern.",
            "display": "serious concern",
        }
    )
    """
    serious concern

    serious concern.
    """

    critical_concern = CodeSystemConcept(
        {
            "code": "critical-concern",
            "definition": "critical concern.",
            "display": "critical concern",
        }
    )
    """
    critical concern

    critical concern.
    """

    present = CodeSystemConcept(
        {
            "code": "present",
            "definition": "possible reason for increasing quality rating was checked and found to bepresent.",
            "display": "present",
        }
    )
    """
    present

    possible reason for increasing quality rating was checked and found to bepresent.
    """

    absent = CodeSystemConcept(
        {
            "code": "absent",
            "definition": "possible reason for increasing quality rating was checked and found to be absent.",
            "display": "absent",
        }
    )
    """
    absent

    possible reason for increasing quality rating was checked and found to be absent.
    """

    class Meta:
        resource = _resource
