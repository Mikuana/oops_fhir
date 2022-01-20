from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_entity_class import v3EntityClass as v3EntityClass_


__all__ = ["v3EntityClass"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityClass(v3EntityClass_):
    """
    v3 Code System EntityClass

     Classifies the Entity class and all of its subclasses.  The terminology
is hierarchical.  At the top is this  HL7-defined domain of high-level
categories (such as represented by the Entity subclasses). Each of these
terms must be harmonized and is specializable. The value sets beneath
are drawn from multiple, frequently external, domains that reflect much
more fine-grained typing.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-EntityClass
    """

    class Meta:
        resource = _resource
