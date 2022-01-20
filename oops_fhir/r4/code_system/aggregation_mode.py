from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AggregationMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AggregationMode:
    """
    AggregationMode

    How resource references can be aggregated.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/resource-aggregation-mode
    """

    contained = CodeSystemConcept(
        {
            "code": "contained",
            "definition": "The reference is a local reference to a contained resource.",
            "display": "Contained",
        }
    )
    """
    Contained

    The reference is a local reference to a contained resource.
    """

    referenced = CodeSystemConcept(
        {
            "code": "referenced",
            "concept": [
                {
                    "code": "bundled",
                    "definition": "The resource the reference points to will be found in the same bundle as the resource that includes the reference.",
                    "display": "Bundled",
                }
            ],
            "definition": "The reference to a resource that has to be resolved externally to the resource that includes the reference.",
            "display": "Referenced",
        }
    )
    """
    Referenced

    The reference to a resource that has to be resolved externally to the resource that includes the reference.
    """

    class Meta:
        resource = _resource
