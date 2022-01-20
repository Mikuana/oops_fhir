from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["OralSiteCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class OralSiteCodes:
    """
    Oral Site Codes

    This value set includes a smattering of FDI oral site codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/ex-tooth
    """

    zero = CodeSystemConcept(
        {"code": "0", "definition": "Oral cavity.", "display": "Oral cavity"}
    )
    """
    Oral cavity

    Oral cavity.
    """

    one = CodeSystemConcept(
        {"code": "1", "definition": "Permanent teeth Maxillary right.", "display": "1"}
    )
    """
    1

    Permanent teeth Maxillary right.
    """

    two = CodeSystemConcept(
        {"code": "2", "definition": "Permanent teeth Maxillary left.", "display": "2"}
    )
    """
    2

    Permanent teeth Maxillary left.
    """

    three = CodeSystemConcept(
        {"code": "3", "definition": "Permanent teeth Mandibular right.", "display": "3"}
    )
    """
    3

    Permanent teeth Mandibular right.
    """

    four = CodeSystemConcept(
        {"code": "4", "definition": "Permanent teeth Mandibular left.", "display": "4"}
    )
    """
    4

    Permanent teeth Mandibular left.
    """

    five = CodeSystemConcept(
        {"code": "5", "definition": "Deciduous teeth Maxillary right.", "display": "5"}
    )
    """
    5

    Deciduous teeth Maxillary right.
    """

    six = CodeSystemConcept(
        {"code": "6", "definition": "Deciduous teeth Maxillary left.", "display": "6"}
    )
    """
    6

    Deciduous teeth Maxillary left.
    """

    seven = CodeSystemConcept(
        {"code": "7", "definition": "Deciduous teeth Mandibular right.", "display": "7"}
    )
    """
    7

    Deciduous teeth Mandibular right.
    """

    eight = CodeSystemConcept(
        {"code": "8", "definition": "Deciduous teeth Mandibular left.", "display": "8"}
    )
    """
    8

    Deciduous teeth Mandibular left.
    """

    one1 = CodeSystemConcept(
        {
            "code": "11",
            "definition": "Upper Right Tooth 1 from the central axis, permanent dentition.",
            "display": "11",
        }
    )
    """
    11

    Upper Right Tooth 1 from the central axis, permanent dentition.
    """

    one2 = CodeSystemConcept(
        {
            "code": "12",
            "definition": "Upper Right Tooth 2 from the central axis, permanent dentition.",
            "display": "12",
        }
    )
    """
    12

    Upper Right Tooth 2 from the central axis, permanent dentition.
    """

    one3 = CodeSystemConcept(
        {
            "code": "13",
            "definition": "Upper Right Tooth 3 from the central axis, permanent dentition.",
            "display": "13",
        }
    )
    """
    13

    Upper Right Tooth 3 from the central axis, permanent dentition.
    """

    one4 = CodeSystemConcept(
        {
            "code": "14",
            "definition": "Upper Right Tooth 4 from the central axis, permanent dentition.",
            "display": "14",
        }
    )
    """
    14

    Upper Right Tooth 4 from the central axis, permanent dentition.
    """

    one5 = CodeSystemConcept(
        {
            "code": "15",
            "definition": "Upper Right Tooth 5 from the central axis, permanent dentition.",
            "display": "15",
        }
    )
    """
    15

    Upper Right Tooth 5 from the central axis, permanent dentition.
    """

    one6 = CodeSystemConcept(
        {
            "code": "16",
            "definition": "Upper Right Tooth 6 from the central axis, permanent dentition.",
            "display": "16",
        }
    )
    """
    16

    Upper Right Tooth 6 from the central axis, permanent dentition.
    """

    one7 = CodeSystemConcept(
        {
            "code": "17",
            "definition": "Upper Right Tooth 7 from the central axis, permanent dentition.",
            "display": "17",
        }
    )
    """
    17

    Upper Right Tooth 7 from the central axis, permanent dentition.
    """

    one8 = CodeSystemConcept(
        {
            "code": "18",
            "definition": "Upper Right Tooth 8 from the central axis, permanent dentition.",
            "display": "18",
        }
    )
    """
    18

    Upper Right Tooth 8 from the central axis, permanent dentition.
    """

    two1 = CodeSystemConcept(
        {
            "code": "21",
            "definition": "Upper Left Tooth 1 from the central axis, permanent dentition.",
            "display": "21",
        }
    )
    """
    21

    Upper Left Tooth 1 from the central axis, permanent dentition.
    """

    two2 = CodeSystemConcept(
        {
            "code": "22",
            "definition": "Upper Left Tooth 2 from the central axis, permanent dentition.",
            "display": "22",
        }
    )
    """
    22

    Upper Left Tooth 2 from the central axis, permanent dentition.
    """

    two3 = CodeSystemConcept(
        {
            "code": "23",
            "definition": "Upper Left Tooth 3 from the central axis, permanent dentition.",
            "display": "23",
        }
    )
    """
    23

    Upper Left Tooth 3 from the central axis, permanent dentition.
    """

    two4 = CodeSystemConcept(
        {
            "code": "24",
            "definition": "Upper Left Tooth 4 from the central axis, permanent dentition.",
            "display": "24",
        }
    )
    """
    24

    Upper Left Tooth 4 from the central axis, permanent dentition.
    """

    two5 = CodeSystemConcept(
        {
            "code": "25",
            "definition": "Upper Left Tooth 5 from the central axis, permanent dentition.",
            "display": "25",
        }
    )
    """
    25

    Upper Left Tooth 5 from the central axis, permanent dentition.
    """

    two6 = CodeSystemConcept(
        {
            "code": "26",
            "definition": "Upper Left Tooth 6 from the central axis, permanent dentition.",
            "display": "26",
        }
    )
    """
    26

    Upper Left Tooth 6 from the central axis, permanent dentition.
    """

    two7 = CodeSystemConcept(
        {
            "code": "27",
            "definition": "Upper Left Tooth 7 from the central axis, permanent dentition.",
            "display": "27",
        }
    )
    """
    27

    Upper Left Tooth 7 from the central axis, permanent dentition.
    """

    two8 = CodeSystemConcept(
        {
            "code": "28",
            "definition": "Upper Left Tooth 8 from the central axis, permanent dentition.",
            "display": "28",
        }
    )
    """
    28

    Upper Left Tooth 8 from the central axis, permanent dentition.
    """

    three1 = CodeSystemConcept(
        {
            "code": "31",
            "definition": "Lower Left Tooth 1 from the central axis, permanent dentition.",
            "display": "31",
        }
    )
    """
    31

    Lower Left Tooth 1 from the central axis, permanent dentition.
    """

    three2 = CodeSystemConcept(
        {
            "code": "32",
            "definition": "Lower Left Tooth 2 from the central axis, permanent dentition.",
            "display": "32",
        }
    )
    """
    32

    Lower Left Tooth 2 from the central axis, permanent dentition.
    """

    three3 = CodeSystemConcept(
        {
            "code": "33",
            "definition": "Lower Left Tooth 3 from the central axis, permanent dentition.",
            "display": "33",
        }
    )
    """
    33

    Lower Left Tooth 3 from the central axis, permanent dentition.
    """

    three4 = CodeSystemConcept(
        {
            "code": "34",
            "definition": "Lower Left Tooth 4 from the central axis, permanent dentition.",
            "display": "34",
        }
    )
    """
    34

    Lower Left Tooth 4 from the central axis, permanent dentition.
    """

    three5 = CodeSystemConcept(
        {
            "code": "35",
            "definition": "Lower Left Tooth 5 from the central axis, permanent dentition.",
            "display": "35",
        }
    )
    """
    35

    Lower Left Tooth 5 from the central axis, permanent dentition.
    """

    three6 = CodeSystemConcept(
        {
            "code": "36",
            "definition": "Lower Left Tooth 6 from the central axis, permanent dentition.",
            "display": "36",
        }
    )
    """
    36

    Lower Left Tooth 6 from the central axis, permanent dentition.
    """

    three7 = CodeSystemConcept(
        {
            "code": "37",
            "definition": "Lower Left Tooth 7 from the central axis, permanent dentition.",
            "display": "37",
        }
    )
    """
    37

    Lower Left Tooth 7 from the central axis, permanent dentition.
    """

    three8 = CodeSystemConcept(
        {
            "code": "38",
            "definition": "Lower Left Tooth 8 from the central axis, permanent dentition.",
            "display": "38",
        }
    )
    """
    38

    Lower Left Tooth 8 from the central axis, permanent dentition.
    """

    four1 = CodeSystemConcept(
        {
            "code": "41",
            "definition": "Lower Right Tooth 1 from the central axis, permanent dentition.",
            "display": "41",
        }
    )
    """
    41

    Lower Right Tooth 1 from the central axis, permanent dentition.
    """

    four2 = CodeSystemConcept(
        {
            "code": "42",
            "definition": "Lower Right Tooth 2 from the central axis, permanent dentition.",
            "display": "42",
        }
    )
    """
    42

    Lower Right Tooth 2 from the central axis, permanent dentition.
    """

    four3 = CodeSystemConcept(
        {
            "code": "43",
            "definition": "Lower Right Tooth 3 from the central axis, permanent dentition.",
            "display": "43",
        }
    )
    """
    43

    Lower Right Tooth 3 from the central axis, permanent dentition.
    """

    four4 = CodeSystemConcept(
        {
            "code": "44",
            "definition": "Lower Right Tooth 4 from the central axis, permanent dentition.",
            "display": "44",
        }
    )
    """
    44

    Lower Right Tooth 4 from the central axis, permanent dentition.
    """

    four5 = CodeSystemConcept(
        {
            "code": "45",
            "definition": "Lower Right Tooth 5 from the central axis, permanent dentition.",
            "display": "45",
        }
    )
    """
    45

    Lower Right Tooth 5 from the central axis, permanent dentition.
    """

    four6 = CodeSystemConcept(
        {
            "code": "46",
            "definition": "Lower Right Tooth 6 from the central axis, permanent dentition.",
            "display": "46",
        }
    )
    """
    46

    Lower Right Tooth 6 from the central axis, permanent dentition.
    """

    four7 = CodeSystemConcept(
        {
            "code": "47",
            "definition": "Lower Right Tooth 7 from the central axis, permanent dentition.",
            "display": "47",
        }
    )
    """
    47

    Lower Right Tooth 7 from the central axis, permanent dentition.
    """

    four8 = CodeSystemConcept(
        {
            "code": "48",
            "definition": "Lower Right Tooth 8 from the central axis, permanent dentition.",
            "display": "48",
        }
    )
    """
    48

    Lower Right Tooth 8 from the central axis, permanent dentition.
    """

    class Meta:
        resource = _resource
