from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_site import v3ActSite as v3ActSite_


__all__ = ["v3ActSite"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActSite(v3ActSite_):
    """
    v3 Code System ActSite

     An anatomical location on an organism which can be the focus of an act.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ActSite
    """

    class Meta:
        resource = _resource
