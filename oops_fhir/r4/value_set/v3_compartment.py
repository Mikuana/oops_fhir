from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_code import v3ActCode


__all__ = ["v3Compartment"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3Compartment(v3ActCode):
    """
    V3 Value SetCompartment

     A named tag set for metadata used to populate a security category label
field that "segments" an IT resource per policy by indicating that
access and use is restricted to members of a defined community or
project. (HL7 Healthcare Privacy and Security Classification System)
Usage Note:  This is the healthcare analog to the US Intelligence
Community's concept of a Special Access Program.  Compartment codes may
be used in as a field value in an initiator's clearance to indicate
permission to access and use an IT Resource with a security label having
the same compartment value in security category label field. Map: Aligns
with ISO 2382-8 definition of Compartment -  "A division of data into
isolated blocks with separate security controls for the purpose of
reducing risk."

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-Compartment
    """

    class Meta:
        resource = _resource
