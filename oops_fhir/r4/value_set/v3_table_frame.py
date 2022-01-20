from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_table_frame import v3TableFrame as v3TableFrame_


__all__ = ["v3TableFrame"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3TableFrame(v3TableFrame_):
    """
    v3 Code System TableFrame

     These values are defined within the XHTML 4.0 Table Model

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-TableFrame
    """

    class Meta:
        resource = _resource
