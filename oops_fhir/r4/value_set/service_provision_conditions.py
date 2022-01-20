from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.service_provision_conditions import (
    ServiceProvisionConditions as ServiceProvisionConditions_,
)


__all__ = ["ServiceProvisionConditions"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ServiceProvisionConditions(ServiceProvisionConditions_):
    """
    ServiceProvisionConditions

    The code(s) that detail the conditions under which the healthcare
service is available/offered.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/service-provision-conditions
    """

    class Meta:
        resource = _resource
