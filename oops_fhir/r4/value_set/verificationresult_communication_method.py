from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.verificationresult_communication_method import (
    verificationresultcommunicationmethod as verificationresultcommunicationmethod_,
)


__all__ = ["verificationresultcommunicationmethod"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class verificationresultcommunicationmethod(verificationresultcommunicationmethod_):
    """
    VerificationResult Communication Method

    Attested information may be validated by process that are manual or
automated. For automated processes it may accomplished by the system of
record reaching out through another system's API or information may be
sent to the system of record. This value set defines a set of codes to
describing the process, the how, a resource or data element is
validated.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/verificationresult-communication-method
    """

    class Meta:
        resource = _resource
