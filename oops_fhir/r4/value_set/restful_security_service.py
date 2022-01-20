from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.restful_security_service import (
    RestfulSecurityService as RestfulSecurityService_,
)


__all__ = ["RestfulSecurityService"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class RestfulSecurityService(RestfulSecurityService_):
    """
    RestfulSecurityService

    Types of security services used with FHIR.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/restful-security-service
    """

    class Meta:
        resource = _resource
