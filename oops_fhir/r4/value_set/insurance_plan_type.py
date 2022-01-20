from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.insurance_plan_type import (
    InsurancePlanType as InsurancePlanType_,
)


__all__ = ["InsurancePlanType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class InsurancePlanType(InsurancePlanType_):
    """
    Insurance plan type

    This example value set defines a set of codes that can be used to
indicate a type of insurance plan.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/insuranceplan-type
    """

    class Meta:
        resource = _resource
