from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3MaritalStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3MaritalStatus:
    """
    v3 Code System MaritalStatus

     * * * No description supplied * * *  Open Issue:  The specific meanings
of these codes can vary somewhat by jurisdiction and implementation so
caution should be used when determining equivalency.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-MaritalStatus
    """

    a = CodeSystemConcept(
        {
            "code": "A",
            "definition": "Marriage contract has been declared null and to not have existed",
            "display": "Annulled",
        }
    )
    """
    Annulled

    Marriage contract has been declared null and to not have existed
    """

    d = CodeSystemConcept(
        {
            "code": "D",
            "definition": "Marriage contract has been declared dissolved and inactive",
            "display": "Divorced",
        }
    )
    """
    Divorced

    Marriage contract has been declared dissolved and inactive
    """

    i = CodeSystemConcept(
        {
            "code": "I",
            "definition": "Subject to an Interlocutory Decree.",
            "display": "Interlocutory",
        }
    )
    """
    Interlocutory

    Subject to an Interlocutory Decree.
    """

    l = CodeSystemConcept(
        {"code": "L", "definition": "Legally Separated", "display": "Legally Separated"}
    )
    """
    Legally Separated

    Legally Separated
    """

    m = CodeSystemConcept(
        {
            "code": "M",
            "definition": "A current marriage contract is active",
            "display": "Married",
        }
    )
    """
    Married

    A current marriage contract is active
    """

    p = CodeSystemConcept(
        {
            "code": "P",
            "definition": "More than 1 current spouse",
            "display": "Polygamous",
        }
    )
    """
    Polygamous

    More than 1 current spouse
    """

    s = CodeSystemConcept(
        {
            "code": "S",
            "definition": "No marriage contract has ever been entered",
            "display": "Never Married",
        }
    )
    """
    Never Married

    No marriage contract has ever been entered
    """

    t = CodeSystemConcept(
        {
            "code": "T",
            "definition": "Person declares that a domestic partner relationship exists.",
            "display": "Domestic partner",
        }
    )
    """
    Domestic partner

    Person declares that a domestic partner relationship exists.
    """

    u = CodeSystemConcept(
        {
            "code": "U",
            "definition": "Currently not in a marriage contract.",
            "display": "unmarried",
        }
    )
    """
    unmarried

    Currently not in a marriage contract.
    """

    w = CodeSystemConcept(
        {"code": "W", "definition": "The spouse has died", "display": "Widowed"}
    )
    """
    Widowed

    The spouse has died
    """

    class Meta:
        resource = _resource
