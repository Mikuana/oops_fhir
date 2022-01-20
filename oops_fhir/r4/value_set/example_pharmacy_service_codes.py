from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.example_pharmacy_service_codes import (
    ExamplePharmacyServiceCodes as ExamplePharmacyServiceCodes_,
)


__all__ = ["ExamplePharmacyServiceCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExamplePharmacyServiceCodes(ExamplePharmacyServiceCodes_):
    """
    Example Pharmacy Service Codes

    This value set includes a smattering of Pharmacy Service codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/service-pharmacy
    """

    class Meta:
        resource = _resource
