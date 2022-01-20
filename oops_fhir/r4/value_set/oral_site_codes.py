from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.oral_site_codes import OralSiteCodes as OralSiteCodes_


__all__ = ["OralSiteCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class OralSiteCodes(OralSiteCodes_):
    """
    Oral Site Codes

    This value set includes a smattering of FDI oral site codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/tooth
    """

    class Meta:
        resource = _resource
