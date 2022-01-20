from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["EndpointPayloadType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class EndpointPayloadType:
    """
    Endpoint Payload Type

    This is an example value set defined by the FHIR project, that could be
used to represent possible payload document types.

    Status: draft - Version: 4.0.1

    Copyright Some content from IHE® Copyright © 2015 IHE International, Inc.    This content is from the IHE Technical Frameworks and Supplements,    available for free download and use at http://www.ihe.net/Technical_Frameworks/

    http://terminology.hl7.org/CodeSystem/endpoint-payload-type
    """

    any_ = CodeSystemConcept(
        {
            "code": "any",
            "definition": "Any payload type can be used with this endpoint, it is either a payload agnostic infrastructure (such as a storage repository), or some other type of endpoint where payload considerations are internally handled, and not available",
            "display": "Any",
        }
    )
    """
    Any

    Any payload type can be used with this endpoint, it is either a payload agnostic infrastructure (such as a storage repository), or some other type of endpoint where payload considerations are internally handled, and not available
    """

    none = CodeSystemConcept(
        {
            "code": "none",
            "definition": "This endpoint does not require any content to be sent; simply connecting to the endpoint is enough notification. This can be used as a 'ping' to wakeup a service to retrieve content, which could be to ensure security considerations are correctly handled",
            "display": "None",
        }
    )
    """
    None

    This endpoint does not require any content to be sent; simply connecting to the endpoint is enough notification. This can be used as a 'ping' to wakeup a service to retrieve content, which could be to ensure security considerations are correctly handled
    """

    class Meta:
        resource = _resource
