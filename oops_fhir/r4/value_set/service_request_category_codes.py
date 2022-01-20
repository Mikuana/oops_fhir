from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ServiceRequestCategoryCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ServiceRequestCategoryCodes(ValueSet):
    """
    Service Request Category Codes

    An example value set of SNOMED CT concepts that can classify a requested
service

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/servicerequest-category
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
