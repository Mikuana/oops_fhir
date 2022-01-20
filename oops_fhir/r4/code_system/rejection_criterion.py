from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["RejectionCriterion"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class RejectionCriterion:
    """
    RejectionCriterion

    Criterion for rejection of the specimen by laboratory.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/rejection-criteria
    """

    hemolized = CodeSystemConcept(
        {
            "code": "hemolized",
            "definition": "blood specimen hemolized.",
            "display": "hemolized specimen",
        }
    )
    """
    hemolized specimen

    blood specimen hemolized.
    """

    insufficient = CodeSystemConcept(
        {
            "code": "insufficient",
            "definition": "insufficient quantity of specimen.",
            "display": "insufficient specimen volume",
        }
    )
    """
    insufficient specimen volume

    insufficient quantity of specimen.
    """

    broken = CodeSystemConcept(
        {
            "code": "broken",
            "definition": "specimen container broken.",
            "display": "broken specimen container",
        }
    )
    """
    broken specimen container

    specimen container broken.
    """

    clotted = CodeSystemConcept(
        {
            "code": "clotted",
            "definition": "specimen clotted.",
            "display": "specimen clotted",
        }
    )
    """
    specimen clotted

    specimen clotted.
    """

    wrong_temperature = CodeSystemConcept(
        {
            "code": "wrong-temperature",
            "definition": "specimen temperature inappropriate.",
            "display": "specimen temperature inappropriate",
        }
    )
    """
    specimen temperature inappropriate

    specimen temperature inappropriate.
    """

    class Meta:
        resource = _resource
