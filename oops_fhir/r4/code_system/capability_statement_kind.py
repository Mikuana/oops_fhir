from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CapabilityStatementKind"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CapabilityStatementKind:
    """
    CapabilityStatementKind

    How a capability statement is intended to be used.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/capability-statement-kind
    """

    instance = CodeSystemConcept(
        {
            "code": "instance",
            "definition": "The CapabilityStatement instance represents the present capabilities of a specific system instance.  This is the kind returned by /metadata for a FHIR server end-point.",
            "display": "Instance",
        }
    )
    """
    Instance

    The CapabilityStatement instance represents the present capabilities of a specific system instance.  This is the kind returned by /metadata for a FHIR server end-point.
    """

    capability = CodeSystemConcept(
        {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments",
                    "valueString": "Elements marked as 'optional' represent configurable capabilities",
                }
            ],
            "code": "capability",
            "definition": "The CapabilityStatement instance represents the capabilities of a system or piece of software, independent of a particular installation.",
            "display": "Capability",
        }
    )
    """
    Capability

    The CapabilityStatement instance represents the capabilities of a system or piece of software, independent of a particular installation.
    """

    requirements = CodeSystemConcept(
        {
            "code": "requirements",
            "definition": "The CapabilityStatement instance represents a set of requirements for other systems to meet; e.g. as part of an implementation guide or 'request for proposal'.",
            "display": "Requirements",
        }
    )
    """
    Requirements

    The CapabilityStatement instance represents a set of requirements for other systems to meet; e.g. as part of an implementation guide or 'request for proposal'.
    """

    class Meta:
        resource = _resource
