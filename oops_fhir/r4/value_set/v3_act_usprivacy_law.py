from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_usprivacy_law import (
    v3ActUSPrivacyLaw as v3ActUSPrivacyLaw_,
)


__all__ = ["v3ActUSPrivacyLaw"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActUSPrivacyLaw(v3ActUSPrivacyLaw_):
    """
    v3 Code System ActUSPrivacyLaw

     A jurisdictional mandate in the US relating to privacy.   Deprecation
Comment:  Content moved to ActCode under _ActPrivacyLaw; use that
instead.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ActUSPrivacyLaw
    """

    class Meta:
        resource = _resource
