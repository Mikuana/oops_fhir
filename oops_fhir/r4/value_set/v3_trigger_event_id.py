from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_trigger_event_id import (
    v3triggerEventID as v3triggerEventID_,
)


__all__ = ["v3triggerEventID"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3triggerEventID(v3triggerEventID_):
    """
    v3 Code System triggerEventID

      Description:  This code system contains all HL7 artifacts of type TE
(Trigger Event) that are created by HL7 or its affiliates or their
designates using the realm namespacing rules approved by HL7.  Local
implementations who create trigger events outside of these namespacing
rules, (e.g. using the ZZ realm code) must register their own code
system.  The specific list of legal codes can be found by consulting the
HL7 publications (editions, ballots, implementation guides, etc.)
published by HL7 Inc. and by the various HL7 affiliates and their
designates.  Codes shall be expressed in upper case, with separator as
shown in HL7 publications with no version id.  E.g. PORX_TE123456UV.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-triggerEventID
    """

    class Meta:
        resource = _resource
