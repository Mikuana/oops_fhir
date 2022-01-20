from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["chromosomehuman"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class chromosomehuman:
    """
    chromosome-human

    Chromosome number for human.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/chromosome-human
    """

    one = CodeSystemConcept(
        {"code": "1", "definition": "chromosome 1.", "display": "chromosome 1"}
    )
    """
    chromosome 1

    chromosome 1.
    """

    two = CodeSystemConcept(
        {"code": "2", "definition": "chromosome 2.", "display": "chromosome 2"}
    )
    """
    chromosome 2

    chromosome 2.
    """

    three = CodeSystemConcept(
        {"code": "3", "definition": "chromosome 3.", "display": "chromosome 3"}
    )
    """
    chromosome 3

    chromosome 3.
    """

    four = CodeSystemConcept(
        {"code": "4", "definition": "chromosome 4.", "display": "chromosome 4"}
    )
    """
    chromosome 4

    chromosome 4.
    """

    five = CodeSystemConcept(
        {"code": "5", "definition": "chromosome 5.", "display": "chromosome 5"}
    )
    """
    chromosome 5

    chromosome 5.
    """

    six = CodeSystemConcept(
        {"code": "6", "definition": "chromosome 6.", "display": "chromosome 6"}
    )
    """
    chromosome 6

    chromosome 6.
    """

    seven = CodeSystemConcept(
        {"code": "7", "definition": "chromosome 7.", "display": "chromosome 7"}
    )
    """
    chromosome 7

    chromosome 7.
    """

    eight = CodeSystemConcept(
        {"code": "8", "definition": "chromosome 8.", "display": "chromosome 8"}
    )
    """
    chromosome 8

    chromosome 8.
    """

    nine = CodeSystemConcept(
        {"code": "9", "definition": "chromosome 9.", "display": "chromosome 9"}
    )
    """
    chromosome 9

    chromosome 9.
    """

    one0 = CodeSystemConcept(
        {"code": "10", "definition": "chromosome 10.", "display": "chromosome 10"}
    )
    """
    chromosome 10

    chromosome 10.
    """

    one1 = CodeSystemConcept(
        {"code": "11", "definition": "chromosome 11.", "display": "chromosome 11"}
    )
    """
    chromosome 11

    chromosome 11.
    """

    one2 = CodeSystemConcept(
        {"code": "12", "definition": "chromosome 12.", "display": "chromosome 12"}
    )
    """
    chromosome 12

    chromosome 12.
    """

    one3 = CodeSystemConcept(
        {"code": "13", "definition": "chromosome 13.", "display": "chromosome 13"}
    )
    """
    chromosome 13

    chromosome 13.
    """

    one4 = CodeSystemConcept(
        {"code": "14", "definition": "chromosome 14.", "display": "chromosome 14"}
    )
    """
    chromosome 14

    chromosome 14.
    """

    one5 = CodeSystemConcept(
        {"code": "15", "definition": "chromosome 15.", "display": "chromosome 15"}
    )
    """
    chromosome 15

    chromosome 15.
    """

    one6 = CodeSystemConcept(
        {"code": "16", "definition": "chromosome 16.", "display": "chromosome 16"}
    )
    """
    chromosome 16

    chromosome 16.
    """

    one7 = CodeSystemConcept(
        {"code": "17", "definition": "chromosome 17.", "display": "chromosome 17"}
    )
    """
    chromosome 17

    chromosome 17.
    """

    one8 = CodeSystemConcept(
        {"code": "18", "definition": "chromosome 18.", "display": "chromosome 18"}
    )
    """
    chromosome 18

    chromosome 18.
    """

    one9 = CodeSystemConcept(
        {"code": "19", "definition": "chromosome 19.", "display": "chromosome 19"}
    )
    """
    chromosome 19

    chromosome 19.
    """

    two0 = CodeSystemConcept(
        {"code": "20", "definition": "chromosome 20.", "display": "chromosome 20"}
    )
    """
    chromosome 20

    chromosome 20.
    """

    two1 = CodeSystemConcept(
        {"code": "21", "definition": "chromosome 21.", "display": "chromosome 21"}
    )
    """
    chromosome 21

    chromosome 21.
    """

    two2 = CodeSystemConcept(
        {"code": "22", "definition": "chromosome 22.", "display": "chromosome 22"}
    )
    """
    chromosome 22

    chromosome 22.
    """

    x = CodeSystemConcept(
        {"code": "X", "definition": "chromosome X.", "display": "chromosome X"}
    )
    """
    chromosome X

    chromosome X.
    """

    y = CodeSystemConcept(
        {"code": "Y", "definition": "chromosome Y.", "display": "chromosome Y"}
    )
    """
    chromosome Y

    chromosome Y.
    """

    class Meta:
        resource = _resource
