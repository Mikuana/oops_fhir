from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["FHIRVersion"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class FHIRVersion:
    """
    FHIRVersion

    All published FHIR Versions.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/FHIR-version
    """

    zero_01 = CodeSystemConcept(
        {
            "code": "0.01",
            "definition": "Oldest archived version of FHIR.",
            "display": "0.01",
        }
    )
    """
    0.01

    Oldest archived version of FHIR.
    """

    zero_05 = CodeSystemConcept(
        {
            "code": "0.05",
            "definition": "1st Draft for Comment (Sept 2012 Ballot).",
            "display": "0.05",
        }
    )
    """
    0.05

    1st Draft for Comment (Sept 2012 Ballot).
    """

    zero_06 = CodeSystemConcept(
        {
            "code": "0.06",
            "definition": "2nd Draft for Comment (January 2013 Ballot).",
            "display": "0.06",
        }
    )
    """
    0.06

    2nd Draft for Comment (January 2013 Ballot).
    """

    zero_11 = CodeSystemConcept(
        {"code": "0.11", "definition": "DSTU 1 Ballot version.", "display": "0.11"}
    )
    """
    0.11

    DSTU 1 Ballot version.
    """

    zero_0_80 = CodeSystemConcept(
        {
            "code": "0.0.80",
            "definition": "DSTU 1 Official version.",
            "display": "0.0.80",
        }
    )
    """
    0.0.80

    DSTU 1 Official version.
    """

    zero_0_81 = CodeSystemConcept(
        {
            "code": "0.0.81",
            "definition": "DSTU 1 Official version Technical Errata #1.",
            "display": "0.0.81",
        }
    )
    """
    0.0.81

    DSTU 1 Official version Technical Errata #1.
    """

    zero_0_82 = CodeSystemConcept(
        {
            "code": "0.0.82",
            "definition": "DSTU 1 Official version Technical Errata #2.",
            "display": "0.0.82",
        }
    )
    """
    0.0.82

    DSTU 1 Official version Technical Errata #2.
    """

    zero_4_0 = CodeSystemConcept(
        {
            "code": "0.4.0",
            "definition": "Draft For Comment (January 2015 Ballot).",
            "display": "0.4.0",
        }
    )
    """
    0.4.0

    Draft For Comment (January 2015 Ballot).
    """

    zero_5_0 = CodeSystemConcept(
        {
            "code": "0.5.0",
            "definition": "DSTU 2 Ballot version (May 2015 Ballot).",
            "display": "0.5.0",
        }
    )
    """
    0.5.0

    DSTU 2 Ballot version (May 2015 Ballot).
    """

    one_0_0 = CodeSystemConcept(
        {
            "code": "1.0.0",
            "definition": "DSTU 2 QA Preview + CQIF Ballot (Sep 2015).",
            "display": "1.0.0",
        }
    )
    """
    1.0.0

    DSTU 2 QA Preview + CQIF Ballot (Sep 2015).
    """

    one_0_1 = CodeSystemConcept(
        {
            "code": "1.0.1",
            "definition": "DSTU 2 (Official version).",
            "display": "1.0.1",
        }
    )
    """
    1.0.1

    DSTU 2 (Official version).
    """

    one_0_2 = CodeSystemConcept(
        {
            "code": "1.0.2",
            "definition": "DSTU 2 (Official version) with 1 technical errata.",
            "display": "1.0.2",
        }
    )
    """
    1.0.2

    DSTU 2 (Official version) with 1 technical errata.
    """

    one_1_0 = CodeSystemConcept(
        {
            "code": "1.1.0",
            "definition": "GAO Ballot + draft changes to main FHIR standard.",
            "display": "1.1.0",
        }
    )
    """
    1.1.0

    GAO Ballot + draft changes to main FHIR standard.
    """

    one_4_0 = CodeSystemConcept(
        {
            "code": "1.4.0",
            "definition": "CQF on FHIR Ballot + Connectathon 12 (Montreal).",
            "display": "1.4.0",
        }
    )
    """
    1.4.0

    CQF on FHIR Ballot + Connectathon 12 (Montreal).
    """

    one_6_0 = CodeSystemConcept(
        {
            "code": "1.6.0",
            "definition": "FHIR STU3 Ballot + Connectathon 13 (Baltimore).",
            "display": "1.6.0",
        }
    )
    """
    1.6.0

    FHIR STU3 Ballot + Connectathon 13 (Baltimore).
    """

    one_8_0 = CodeSystemConcept(
        {
            "code": "1.8.0",
            "definition": "FHIR STU3 Candidate + Connectathon 14 (San Antonio).",
            "display": "1.8.0",
        }
    )
    """
    1.8.0

    FHIR STU3 Candidate + Connectathon 14 (San Antonio).
    """

    three_0_0 = CodeSystemConcept(
        {"code": "3.0.0", "definition": "FHIR Release 3 (STU).", "display": "3.0.0"}
    )
    """
    3.0.0

    FHIR Release 3 (STU).
    """

    three_0_1 = CodeSystemConcept(
        {
            "code": "3.0.1",
            "definition": "FHIR Release 3 (STU) with 1 technical errata.",
            "display": "3.0.1",
        }
    )
    """
    3.0.1

    FHIR Release 3 (STU) with 1 technical errata.
    """

    three_3_0 = CodeSystemConcept(
        {"code": "3.3.0", "definition": "R4 Ballot #1.", "display": "3.3.0"}
    )
    """
    3.3.0

    R4 Ballot #1.
    """

    three_5_0 = CodeSystemConcept(
        {"code": "3.5.0", "definition": "R4 Ballot #2.", "display": "3.5.0"}
    )
    """
    3.5.0

    R4 Ballot #2.
    """

    four_0_0 = CodeSystemConcept(
        {
            "code": "4.0.0",
            "definition": "FHIR Release 4 (Normative + STU).",
            "display": "4.0.0",
        }
    )
    """
    4.0.0

    FHIR Release 4 (Normative + STU).
    """

    four_0_1 = CodeSystemConcept(
        {
            "code": "4.0.1",
            "definition": "FHIR Release 4 Technical Correction.",
            "display": "4.0.1",
        }
    )
    """
    4.0.1

    FHIR Release 4 Technical Correction.
    """

    class Meta:
        resource = _resource
