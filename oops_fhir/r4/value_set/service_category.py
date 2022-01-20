from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.service_category import (
    ServiceCategory as ServiceCategory_,
)


__all__ = ["ServiceCategory"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ServiceCategory(ServiceCategory_):
    """
    Service category

    This value set defines an example set of codes that can be used to
classify groupings of service-types/specialties.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/service-category
    """

    class Meta:
        resource = _resource
