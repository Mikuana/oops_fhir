from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.fhirversion import FHIRVersion as FHIRVersion_


__all__ = ["FHIRVersion"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FHIRVersion(FHIRVersion_):
    """
    FHIRVersion

    All published FHIR Versions.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/FHIR-version
    """

    class Meta:
        resource = _resource
