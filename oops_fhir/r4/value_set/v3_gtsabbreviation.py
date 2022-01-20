from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_gtsabbreviation import (
    v3GTSAbbreviation as v3GTSAbbreviation_,
)


__all__ = ["v3GTSAbbreviation"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3GTSAbbreviation(v3GTSAbbreviation_):
    """
    v3 Code System GTSAbbreviation

      Open Issue:  It appears that the printnames are suboptimal and should
be improved for many of the existing codes.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-GTSAbbreviation
    """

    class Meta:
        resource = _resource
