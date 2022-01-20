from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_code import v3ActCode as v3ActCode_


__all__ = ["v3ActCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActCode(v3ActCode_):
    """
    v3 Code System ActCode

     A code specifying the particular kind of Act that the Act-instance
represents within its class.  Constraints:  The kind of Act (e.g.
physical examination, serum potassium, inpatient encounter, charge
financial transaction, etc.) is specified with a code from one of
several, typically external, coding systems.  The coding system will
depend on the class of Act, such as LOINC for observations, etc.
Conceptually, the Act.code must be a specialization of the
Act.classCode. This is why the structure of ActClass domain should be
reflected in the superstructure of the ActCode domain and then
individual codes or externally referenced vocabularies subordinated
under these domains that reflect the ActClass structure. Act.classCode
and Act.code are not modifiers of each other but the Act.code concept
should really imply the Act.classCode concept. For a negative example,
it is not appropriate to use an Act.code "potassium" together with and
Act.classCode for "laboratory observation" to somehow mean "potassium
laboratory observation" and then use the same Act.code for "potassium"
together with Act.classCode for "medication" to mean "substitution of
potassium". This mutually modifying use of Act.code and Act.classCode is
not permitted.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ActCode
    """

    class Meta:
        resource = _resource
