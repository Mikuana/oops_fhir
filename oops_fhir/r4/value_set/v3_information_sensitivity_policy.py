from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_code import v3ActCode


__all__ = ["v3InformationSensitivityPolicy"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3InformationSensitivityPolicy(v3ActCode):
    """
    V3 Value SetInformationSensitivityPolicy

     Sensitivity codes are not useful for interoperability outside of a
policy domain because sensitivity policies are typically localized and
vary drastically across policy domains even for the same information
category because of differing organizational business rules, security
policies, and jurisdictional requirements.  For example, an "employee"
sensitivity code would make little sense for use outside of a policy
domain.   "Taboo" would rarely be useful outside of a policy domain
unless there are jurisdictional requirements requiring that a provider
disclose sensitive information to a patient directly. Sensitivity codes
may be more appropriate in a legacy system's Master Files in order to
notify those who access a patient's orders and observations about the
sensitivity policies that apply.  Newer systems may have a security
engine that uses a sensitivity policy's criteria directly. The
specializable Sensitivity Act.code may be useful in some scenarious if
used in combination with a sensitivity identifier and/or Act.title.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-InformationSensitivityPolicy
    """

    class Meta:
        resource = _resource
