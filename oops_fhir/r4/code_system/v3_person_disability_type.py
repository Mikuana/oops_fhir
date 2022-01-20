from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3PersonDisabilityType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3PersonDisabilityType:
    """
    v3 Code System PersonDisabilityType

     A code identifying a person's disability.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-PersonDisabilityType
    """

    one = CodeSystemConcept(
        {"code": "1", "definition": "Vision impaired", "display": "Vision impaired"}
    )
    """
    Vision impaired

    Vision impaired
    """

    two = CodeSystemConcept(
        {"code": "2", "definition": "Hearing impaired", "display": "Hearing impaired"}
    )
    """
    Hearing impaired

    Hearing impaired
    """

    three = CodeSystemConcept(
        {"code": "3", "definition": "Speech impaired", "display": "Speech impaired"}
    )
    """
    Speech impaired

    Speech impaired
    """

    four = CodeSystemConcept(
        {"code": "4", "definition": "Mentally impaired", "display": "Mentally impaired"}
    )
    """
    Mentally impaired

    Mentally impaired
    """

    five = CodeSystemConcept(
        {
            "code": "5",
            "concept": [
                {
                    "code": "CB",
                    "definition": "A crib is required to move the person",
                    "display": "Requires crib",
                },
                {
                    "code": "CR",
                    "definition": "Person requires crutches to ambulate",
                    "display": "Requires crutches",
                },
                {
                    "code": "G",
                    "definition": "A gurney is required to move the person",
                    "display": "Requires gurney",
                },
                {
                    "code": "WC",
                    "definition": "Person requires a wheelchair to be ambulatory",
                    "display": "Requires wheelchair",
                },
                {
                    "code": "WK",
                    "definition": "Person requires a walker to ambulate",
                    "display": "Requires walker",
                },
            ],
            "definition": "Mobility impaired",
            "display": "Mobility impaired",
        }
    )
    """
    Mobility impaired

    Mobility impaired
    """

    class Meta:
        resource = _resource
