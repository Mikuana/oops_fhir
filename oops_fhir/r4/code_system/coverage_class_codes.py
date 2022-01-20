from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CoverageClassCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CoverageClassCodes:
    """
    Coverage Class Codes

    This value set includes Coverage Class codes.

    Status: draft - Version: 4.0.1

    Copyright HL7 Inc.

    http://terminology.hl7.org/CodeSystem/coverage-class
    """

    group = CodeSystemConcept(
        {"code": "group", "definition": "An employee group", "display": "Group"}
    )
    """
    Group

    An employee group
    """

    subgroup = CodeSystemConcept(
        {
            "code": "subgroup",
            "definition": "A sub-group of an employee group",
            "display": "SubGroup",
        }
    )
    """
    SubGroup

    A sub-group of an employee group
    """

    plan = CodeSystemConcept(
        {
            "code": "plan",
            "definition": "A specific suite of benefits.",
            "display": "Plan",
        }
    )
    """
    Plan

    A specific suite of benefits.
    """

    subplan = CodeSystemConcept(
        {
            "code": "subplan",
            "definition": "A subset of a specific suite of benefits.",
            "display": "SubPlan",
        }
    )
    """
    SubPlan

    A subset of a specific suite of benefits.
    """

    class_ = CodeSystemConcept(
        {"code": "class", "definition": "A class of benefits.", "display": "Class"}
    )
    """
    Class

    A class of benefits.
    """

    subclass = CodeSystemConcept(
        {
            "code": "subclass",
            "definition": "A subset of a class of benefits.",
            "display": "SubClass",
        }
    )
    """
    SubClass

    A subset of a class of benefits.
    """

    sequence = CodeSystemConcept(
        {
            "code": "sequence",
            "definition": "A sequence number associated with a short-term continuance of the coverage.",
            "display": "Sequence",
        }
    )
    """
    Sequence

    A sequence number associated with a short-term continuance of the coverage.
    """

    rxbin = CodeSystemConcept(
        {
            "code": "rxbin",
            "definition": "Pharmacy benefit manager's Business Identification Number.",
            "display": "RX BIN",
        }
    )
    """
    RX BIN

    Pharmacy benefit manager's Business Identification Number.
    """

    rxpcn = CodeSystemConcept(
        {
            "code": "rxpcn",
            "definition": "A Pharmacy Benefit Manager specified Processor Control Number.",
            "display": "RX PCN",
        }
    )
    """
    RX PCN

    A Pharmacy Benefit Manager specified Processor Control Number.
    """

    rxid = CodeSystemConcept(
        {
            "code": "rxid",
            "definition": "A Pharmacy Benefit Manager specified Member ID.",
            "display": "RX Id",
        }
    )
    """
    RX Id

    A Pharmacy Benefit Manager specified Member ID.
    """

    rxgroup = CodeSystemConcept(
        {
            "code": "rxgroup",
            "definition": "A Pharmacy Benefit Manager specified Group number.",
            "display": "RX Group",
        }
    )
    """
    RX Group

    A Pharmacy Benefit Manager specified Group number.
    """

    class Meta:
        resource = _resource
