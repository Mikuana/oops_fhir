from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["sequenceStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class sequenceStatus:
    """
    sequenceStatus

    Codes providing the status of the variant test result.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/variant-state
    """

    positive = CodeSystemConcept(
        {
            "code": "positive",
            "definition": "the variant is detected.",
            "display": "positive",
        }
    )
    """
    positive

    the variant is detected.
    """

    negative = CodeSystemConcept(
        {
            "code": "negative",
            "definition": "no variant is detected.",
            "display": "negative",
        }
    )
    """
    negative

    no variant is detected.
    """

    absent = CodeSystemConcept(
        {
            "code": "absent",
            "definition": "result of the variant is missing.",
            "display": "absent",
        }
    )
    """
    absent

    result of the variant is missing.
    """

    class Meta:
        resource = _resource
