from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ConsentProvisionType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ConsentProvisionType:
    """
    ConsentProvisionType

    How a rule statement is applied, such as adding additional consent or
removing consent.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/consent-provision-type
    """

    deny = CodeSystemConcept(
        {
            "code": "deny",
            "definition": "Consent is denied for actions meeting these rules.",
            "display": "Opt Out",
        }
    )
    """
    Opt Out

    Consent is denied for actions meeting these rules.
    """

    permit = CodeSystemConcept(
        {
            "code": "permit",
            "definition": "Consent is provided for actions meeting these rules.",
            "display": "Opt In",
        }
    )
    """
    Opt In

    Consent is provided for actions meeting these rules.
    """

    class Meta:
        resource = _resource
