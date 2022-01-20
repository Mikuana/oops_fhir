from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.resource_type import ResourceType


__all__ = ["ConsentContentClass"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConsentContentClass(ValueSet):
    """
    Consent Content Class

    This value set includes the FHIR resource types, along with some other
important content class codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/consent-content-class
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
