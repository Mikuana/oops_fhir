from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.consent_provision_type import (
    ConsentProvisionType as ConsentProvisionType_,
)


__all__ = ["ConsentProvisionType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConsentProvisionType(ConsentProvisionType_):
    """
    ConsentProvisionType

    How a rule statement is applied, such as adding additional consent or
removing consent.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/consent-provision-type
    """

    class Meta:
        resource = _resource
