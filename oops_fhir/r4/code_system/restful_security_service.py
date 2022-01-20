from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["RestfulSecurityService"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class RestfulSecurityService:
    """
    RestfulSecurityService

    Types of security services used with FHIR.

    Status: active - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/restful-security-service
    """

    oauth = CodeSystemConcept(
        {
            "code": "OAuth",
            "definition": "OAuth (unspecified version see oauth.net).",
            "display": "OAuth",
        }
    )
    """
    OAuth

    OAuth (unspecified version see oauth.net).
    """

    smart_on_fhir = CodeSystemConcept(
        {
            "code": "SMART-on-FHIR",
            "definition": "OAuth2 using SMART-on-FHIR profile (see http://docs.smarthealthit.org/).",
            "display": "SMART-on-FHIR",
        }
    )
    """
    SMART-on-FHIR

    OAuth2 using SMART-on-FHIR profile (see http://docs.smarthealthit.org/).
    """

    ntlm = CodeSystemConcept(
        {
            "code": "NTLM",
            "definition": "Microsoft NTLM Authentication.",
            "display": "NTLM",
        }
    )
    """
    NTLM

    Microsoft NTLM Authentication.
    """

    basic = CodeSystemConcept(
        {
            "code": "Basic",
            "definition": "Basic authentication defined in HTTP specification.",
            "display": "Basic",
        }
    )
    """
    Basic

    Basic authentication defined in HTTP specification.
    """

    kerberos = CodeSystemConcept(
        {
            "code": "Kerberos",
            "definition": "see http://www.ietf.org/rfc/rfc4120.txt.",
            "display": "Kerberos",
        }
    )
    """
    Kerberos

    see http://www.ietf.org/rfc/rfc4120.txt.
    """

    certificates = CodeSystemConcept(
        {
            "code": "Certificates",
            "definition": "SSL where client must have a certificate registered with the server.",
            "display": "Certificates",
        }
    )
    """
    Certificates

    SSL where client must have a certificate registered with the server.
    """

    class Meta:
        resource = _resource
