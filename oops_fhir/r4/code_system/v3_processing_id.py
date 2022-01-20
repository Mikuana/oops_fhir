from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ProcessingID"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ProcessingID:
    """
    v3 Code System ProcessingID

     Codes used to specify whether a message is part of a production,
training, or debugging system.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ProcessingID
    """

    d = CodeSystemConcept(
        {
            "code": "D",
            "definition": "Identifies debugging type of processing.",
            "display": "Debugging",
        }
    )
    """
    Debugging

    Identifies debugging type of processing.
    """

    p = CodeSystemConcept(
        {
            "code": "P",
            "definition": "Identifies production type of processing.",
            "display": "Production",
        }
    )
    """
    Production

    Identifies production type of processing.
    """

    t = CodeSystemConcept(
        {
            "code": "T",
            "definition": "Identifies training type of processing.",
            "display": "Training",
        }
    )
    """
    Training

    Identifies training type of processing.
    """

    class Meta:
        resource = _resource
