from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3WorkClassificationODH"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3WorkClassificationODH:
    """
    v3 Code System WorkClassificationODH

     Code system of concepts representing a person's job type as defined by
compensation and sector (e.g. paid vs. unpaid, self-employed vs. not
self-employed, government vs. private, etc.).

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-WorkClassificationODH
    """

    pwaf = CodeSystemConcept(
        {
            "code": "PWAF",
            "definition": "A situation in which an individual serves in a government-sponsored military force.",
            "display": "Paid work, Armed Forces",
        }
    )
    """
    Paid work, Armed Forces

    A situation in which an individual serves in a government-sponsored military force.
    """

    pwfg = CodeSystemConcept(
        {
            "code": "PWFG",
            "definition": "A situation in which an individual works for a national government organization, not including armed forces, and receives a paid salary or wage.",
            "display": "Paid work, national government, not armed forces",
        }
    )
    """
    Paid work, national government, not armed forces

    A situation in which an individual works for a national government organization, not including armed forces, and receives a paid salary or wage.
    """

    pwlg = CodeSystemConcept(
        {
            "code": "PWLG",
            "definition": "A situation in which an individual works for a government organization with jurisdiction below the level of state/provincial/territorial/tribal government (e.g., city, town, township), not armed forces, and receives a paid salary or wage.",
            "display": "Paid work, local government, not armed forces",
        }
    )
    """
    Paid work, local government, not armed forces

    A situation in which an individual works for a government organization with jurisdiction below the level of state/provincial/territorial/tribal government (e.g., city, town, township), not armed forces, and receives a paid salary or wage.
    """

    pwnse = CodeSystemConcept(
        {
            "code": "PWNSE",
            "definition": "A situation in which an individual works for a business (not government) that they do not own and receives a paid salary or wage.",
            "display": "Paid non-governmental work, not self-employed",
        }
    )
    """
    Paid non-governmental work, not self-employed

    A situation in which an individual works for a business (not government) that they do not own and receives a paid salary or wage.
    """

    pwse = CodeSystemConcept(
        {
            "code": "PWSE",
            "definition": "A situation in which an individual earns a salary or wage working for himself or herself instead of working for an employer.",
            "display": "Paid work, self-employed",
        }
    )
    """
    Paid work, self-employed

    A situation in which an individual earns a salary or wage working for himself or herself instead of working for an employer.
    """

    pwsg = CodeSystemConcept(
        {
            "code": "PWSG",
            "definition": "A situation in which an individual works for a government organization with jurisdiction immediately below the level of national government (between national government and local government), not armed forces and receives a paid salary or wage.  Often called a state, provincial, territorial, or tribal government.",
            "display": "Paid work, state government, not armed forces",
        }
    )
    """
    Paid work, state government, not armed forces

    A situation in which an individual works for a government organization with jurisdiction immediately below the level of national government (between national government and local government), not armed forces and receives a paid salary or wage.  Often called a state, provincial, territorial, or tribal government.
    """

    uwnse = CodeSystemConcept(
        {
            "code": "UWNSE",
            "definition": "A situation in which an individual works for a business (not government) that they do not own without receiving a paid salary or wage.",
            "display": "Unpaid non-governmental work, not self-employed",
        }
    )
    """
    Unpaid non-governmental work, not self-employed

    A situation in which an individual works for a business (not government) that they do not own without receiving a paid salary or wage.
    """

    uwse = CodeSystemConcept(
        {
            "code": "UWSE",
            "definition": "A situation in which an individual works for himself or herself without receiving a paid salary or wage.",
            "display": "Unpaid work, self-employed",
        }
    )
    """
    Unpaid work, self-employed

    A situation in which an individual works for himself or herself without receiving a paid salary or wage.
    """

    vw = CodeSystemConcept(
        {
            "code": "VW",
            "definition": "A situation in which an individual chooses to do something, especially for other people or for an organization, willingly and without being forced or compensated to do it.  This can include formal activity undertaken through public, private and voluntary organizations as well as informal community participation.",
            "display": "Voluntary work",
        }
    )
    """
    Voluntary work

    A situation in which an individual chooses to do something, especially for other people or for an organization, willingly and without being forced or compensated to do it.  This can include formal activity undertaken through public, private and voluntary organizations as well as informal community participation.
    """

    class Meta:
        resource = _resource
