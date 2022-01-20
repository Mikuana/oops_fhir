from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["PatientContactRelationship"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class PatientContactRelationship(ValueSet):
    """
    Patient Contact Relationship 

    The nature of the relationship between the patient and the contact
person.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/patient-contactrelationship
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
