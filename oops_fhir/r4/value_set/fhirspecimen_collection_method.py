from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["FHIRSpecimenCollectionMethod"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FHIRSpecimenCollectionMethod(ValueSet):
    """
    FHIR Specimen Collection Method

     This example value set defines a set of codes that can be used to
indicate the method by which a specimen was collected.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/specimen-collection-method
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
