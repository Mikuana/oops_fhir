from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ReferralMethod"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ReferralMethod:
    """
    ReferralMethod

    The methods of referral can be used when referring to a specific
HealthCareService resource.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/service-referral-method
    """

    fax = CodeSystemConcept(
        {
            "code": "fax",
            "definition": "Referrals may be accepted by fax.",
            "display": "Fax",
        }
    )
    """
    Fax

    Referrals may be accepted by fax.
    """

    phone = CodeSystemConcept(
        {
            "code": "phone",
            "definition": "Referrals may be accepted over the phone from a practitioner.",
            "display": "Phone",
        }
    )
    """
    Phone

    Referrals may be accepted over the phone from a practitioner.
    """

    elec = CodeSystemConcept(
        {
            "code": "elec",
            "definition": "Referrals may be accepted via a secure messaging system. To determine the types of secure messaging systems supported, refer to the identifiers collection. Callers will need to understand the specific identifier system used to know that they are able to transmit messages.",
            "display": "Secure Messaging",
        }
    )
    """
    Secure Messaging

    Referrals may be accepted via a secure messaging system. To determine the types of secure messaging systems supported, refer to the identifiers collection. Callers will need to understand the specific identifier system used to know that they are able to transmit messages.
    """

    semail = CodeSystemConcept(
        {
            "code": "semail",
            "definition": "Referrals may be accepted via a secure email. To send please encrypt with the services public key.",
            "display": "Secure Email",
        }
    )
    """
    Secure Email

    Referrals may be accepted via a secure email. To send please encrypt with the services public key.
    """

    mail = CodeSystemConcept(
        {
            "code": "mail",
            "definition": "Referrals may be accepted via regular postage (or hand delivered).",
            "display": "Mail",
        }
    )
    """
    Mail

    Referrals may be accepted via regular postage (or hand delivered).
    """

    class Meta:
        resource = _resource
