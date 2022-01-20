from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.surface_codes import SurfaceCodes as SurfaceCodes_


__all__ = ["SurfaceCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SurfaceCodes(SurfaceCodes_):
    """
    Surface Codes

    This value set includes a smattering of FDI tooth surface codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/surface
    """

    class Meta:
        resource = _resource
