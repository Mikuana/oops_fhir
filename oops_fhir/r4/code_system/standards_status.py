from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["StandardsStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class StandardsStatus:
    """
    StandardsStatus

    HL7 Ballot/Standards status of artifact.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/standards-status
    """

    draft = CodeSystemConcept(
        {
            "code": "draft",
            "definition": 'This portion of the specification is not considered to be complete enough or sufficiently reviewed to be safe for implementation. It may have known issues or still be in the "in development" stage. It is included in the publication as a place-holder, to solicit feedback from the implementation community and/or to give implementers some insight as to functionality likely to be included in future versions of the specification. Content at this level should only be implemented by the brave or desperate and is very much "use at your own risk". The content that is Draft that will usually be elevated to Trial Use once review and correction is complete after it has been subjected to ballot.',
            "display": "Draft",
        }
    )
    """
    Draft

    This portion of the specification is not considered to be complete enough or sufficiently reviewed to be safe for implementation. It may have known issues or still be in the "in development" stage. It is included in the publication as a place-holder, to solicit feedback from the implementation community and/or to give implementers some insight as to functionality likely to be included in future versions of the specification. Content at this level should only be implemented by the brave or desperate and is very much "use at your own risk". The content that is Draft that will usually be elevated to Trial Use once review and correction is complete after it has been subjected to ballot.
    """

    normative = CodeSystemConcept(
        {
            "code": "normative",
            "definition": "This content has been subject to review and production implementation in a wide variety of environments. The content is considered to be stable and has been 'locked', subjecting it to FHIR Inter-version Compatibility Rules. While changes are possible, they are expected to be infrequent and are tightly constrained. Compatibility Rules.",
            "display": "Normative",
        }
    )
    """
    Normative

    This content has been subject to review and production implementation in a wide variety of environments. The content is considered to be stable and has been 'locked', subjecting it to FHIR Inter-version Compatibility Rules. While changes are possible, they are expected to be infrequent and are tightly constrained. Compatibility Rules.
    """

    trial_use = CodeSystemConcept(
        {
            "code": "trial-use",
            "definition": "This content has been well reviewed and is considered by the authors to be ready for use in production systems. It has been subjected to ballot and approved as an official standard. However, it has not yet seen widespread use in production across the full spectrum of environments it is intended to be used in. In some cases, there may be documented known issues that require implementation experience to determine appropriate resolutions for.\n\nFuture versions of FHIR may make significant changes to Trial Use content that are not compatible with previously published content.",
            "display": "Trial-Use",
        }
    )
    """
    Trial-Use

    This content has been well reviewed and is considered by the authors to be ready for use in production systems. It has been subjected to ballot and approved as an official standard. However, it has not yet seen widespread use in production across the full spectrum of environments it is intended to be used in. In some cases, there may be documented known issues that require implementation experience to determine appropriate resolutions for.

Future versions of FHIR may make significant changes to Trial Use content that are not compatible with previously published content.
    """

    informative = CodeSystemConcept(
        {
            "code": "informative",
            "definition": "This portion of the specification is provided for implementer assistance, and does not make rules that implementers are required to follow. Typical examples of this content in the FHIR specification are tables of contents, registries, examples, and implementer advice.",
            "display": "Informative",
        }
    )
    """
    Informative

    This portion of the specification is provided for implementer assistance, and does not make rules that implementers are required to follow. Typical examples of this content in the FHIR specification are tables of contents, registries, examples, and implementer advice.
    """

    deprecated = CodeSystemConcept(
        {
            "code": "deprecated",
            "definition": "This portion of the specification is provided for implementer assistance, and does not make rules that implementers are required to follow. Typical examples of this content in the FHIR specification are tables of contents, registries, examples, and implementer advice.",
            "display": "Deprecated",
        }
    )
    """
    Deprecated

    This portion of the specification is provided for implementer assistance, and does not make rules that implementers are required to follow. Typical examples of this content in the FHIR specification are tables of contents, registries, examples, and implementer advice.
    """

    external = CodeSystemConcept(
        {
            "code": "external",
            "definition": "This is content that is managed outside the FHIR Specification, but included for implementer convenience.",
            "display": "External",
        }
    )
    """
    External

    This is content that is managed outside the FHIR Specification, but included for implementer convenience.
    """

    class Meta:
        resource = _resource
