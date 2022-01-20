from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3hl7V3Conformance"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7V3Conformance:
    """
    v3 Code System hl7V3Conformance

      Description:  Identifies allowed codes for HL7aTMs v3 conformance
property.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-hl7V3Conformance
    """

    i = CodeSystemConcept(
        {
            "code": "I",
            "definition": 'Description: Implementers receiving this property must not raise an error if the data is received, but will not perform any useful function with the data.  This conformance level is not used in profiles or other artifacts that are specific to the "sender" or "initiator" of a communication.',
            "display": "ignored",
        }
    )
    """
    ignored

    Description: Implementers receiving this property must not raise an error if the data is received, but will not perform any useful function with the data.  This conformance level is not used in profiles or other artifacts that are specific to the "sender" or "initiator" of a communication.
    """

    np = CodeSystemConcept(
        {
            "code": "NP",
            "definition": "Description: All implementers are prohibited from transmitting this content, and may raise an error if they receive it.",
            "display": "not permitted",
        }
    )
    """
    not permitted

    Description: All implementers are prohibited from transmitting this content, and may raise an error if they receive it.
    """

    r = CodeSystemConcept(
        {
            "code": "R",
            "definition": "Description: All implementers must support this property.  I.e. they must be able to transmit, or to receive and usefully handle the concept.",
            "display": "required",
        }
    )
    """
    required

    Description: All implementers must support this property.  I.e. they must be able to transmit, or to receive and usefully handle the concept.
    """

    rc = CodeSystemConcept(
        {
            "code": "RC",
            "definition": 'Description: The element is considered "required" (i.e. must be supported) from the perspective of systems that consume  instances, but is "undetermined" for systems that generate instances.  Used only as part of specifications that define both initiator and consumer expectations.',
            "display": "required for consumer",
        }
    )
    """
    required for consumer

    Description: The element is considered "required" (i.e. must be supported) from the perspective of systems that consume  instances, but is "undetermined" for systems that generate instances.  Used only as part of specifications that define both initiator and consumer expectations.
    """

    ri = CodeSystemConcept(
        {
            "code": "RI",
            "definition": 'Description: The element is considered "required" (i.e. must be supported) from the perspective of systems that generate instances, but is "undetermined" for systems that consume instances.  Used only as part of specifications that define both initiator and consumer expectations.',
            "display": "required for initiator",
        }
    )
    """
    required for initiator

    Description: The element is considered "required" (i.e. must be supported) from the perspective of systems that generate instances, but is "undetermined" for systems that consume instances.  Used only as part of specifications that define both initiator and consumer expectations.
    """

    u = CodeSystemConcept(
        {
            "code": "U",
            "definition": "Description: The conformance expectations for this element have not yet been determined.",
            "display": "undetermined",
        }
    )
    """
    undetermined

    Description: The conformance expectations for this element have not yet been determined.
    """

    class Meta:
        resource = _resource
