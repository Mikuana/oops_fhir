from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_table_cell_scope import (
    v3TableCellScope as v3TableCellScope_,
)


__all__ = ["v3TableCellScope"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3TableCellScope(v3TableCellScope_):
    """
    v3 Code System TableCellScope

     These values are defined within the XHTML 4.0 Table Model

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-TableCellScope
    """

    class Meta:
        resource = _resource
