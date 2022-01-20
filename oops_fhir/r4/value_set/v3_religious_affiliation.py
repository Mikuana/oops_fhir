from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_religious_affiliation import (
    v3ReligiousAffiliation as v3ReligiousAffiliation_,
)


__all__ = ["v3ReligiousAffiliation"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ReligiousAffiliation(v3ReligiousAffiliation_):
    """
    v3 Code System ReligiousAffiliation

     Assigment of spiritual faith affiliation

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ReligiousAffiliation
    """

    class Meta:
        resource = _resource
