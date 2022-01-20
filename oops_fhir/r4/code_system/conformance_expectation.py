from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ConformanceExpectation"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ConformanceExpectation:
    """
    ConformanceExpectation

    Indicates the degree of adherence to a specified behavior or capability
expected for a system to be deemed conformant with a specification.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/conformance-expectation
    """

    shall = CodeSystemConcept(
        {
            "code": "SHALL",
            "definition": "Support for the specified capability is required to be considered conformant.",
            "display": "SHALL",
        }
    )
    """
    SHALL

    Support for the specified capability is required to be considered conformant.
    """

    should = CodeSystemConcept(
        {
            "code": "SHOULD",
            "definition": "Support for the specified capability is strongly encouraged, and failure to support it should only occur after careful consideration.",
            "display": "SHOULD",
        }
    )
    """
    SHOULD

    Support for the specified capability is strongly encouraged, and failure to support it should only occur after careful consideration.
    """

    may = CodeSystemConcept(
        {
            "code": "MAY",
            "definition": "Support for the specified capability is not necessary to be considered conformant, and the requirement should be considered strictly optional.",
            "display": "MAY",
        }
    )
    """
    MAY

    Support for the specified capability is not necessary to be considered conformant, and the requirement should be considered strictly optional.
    """

    should_not = CodeSystemConcept(
        {
            "code": "SHOULD-NOT",
            "definition": "Support for the specified capability is strongly discouraged and should occur only after careful consideration.",
            "display": "SHOULD-NOT",
        }
    )
    """
    SHOULD-NOT

    Support for the specified capability is strongly discouraged and should occur only after careful consideration.
    """

    class Meta:
        resource = _resource
