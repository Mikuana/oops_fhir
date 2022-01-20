from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_class import v3ActClass


__all__ = ["v3ActClassProcedure"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActClassProcedure(v3ActClass):
    """
    V3 Value SetActClassProcedure

     An Act whose immediate and primary outcome (post-condition) is the
alteration of the physical condition of the subject.  Examples:  :
Procedures may involve the disruption of some body surface (e.g. an
incision in a surgical procedure), but they also include conservative
procedures such as reduction of a luxated join, chiropractic treatment,
massage, balneotherapy, acupuncture, shiatsu, etc. Outside of clinical
medicine, procedures may be such things as alteration of environments
(e.g. straightening rivers, draining swamps, building dams) or the
repair or change of machinery etc.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ActClassProcedure
    """

    class Meta:
        resource = _resource
