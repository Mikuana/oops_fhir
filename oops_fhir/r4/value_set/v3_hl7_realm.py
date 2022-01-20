from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_hl7_realm import v3hl7Realm as v3hl7Realm_


__all__ = ["v3hl7Realm"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7Realm(v3hl7Realm_):
    """
    v3 Code System hl7Realm

      Description:  Coded concepts representing Binding Realms (used for
Context Binding of terminology in HL7 models)  and/or Namespace Realms
(used to help ensure unique identification of HL7 artifacts). This code
system is partitioned into three sections: Affiliate realms, Binding
realms and Namespace realms.  All affiliate realm codes may
automatically be used as both binding realms and namespace realms.
Furthermore, affiliate realms are the only realms that have authority
over the creation of binding realms.  (Note that 'affiliate' includes
the idea of both international affiliates and the HL7 International
organization.)  All other codes must be associated with an owning
affiliate realm and must appear as a specialization of _BindingRealm or
_NamespaceRealm.  For affiliates whose concepts align with nations, the
country codes from ISO 3166-1 2-character alpha are used for the code
when possible so these codes should not be used for other realm types.
It is recommended that binding realm and namespace codes submitted by
affiliates use the realm code as a prefix to avoid possible collisions
with ISO codes.  However, tooling does not currently support namepace
realm codes greater than 2 characters.  Open Issue:  The name of the
concept property "owningAffiliate" should be changed to better reflect
that the property value is the human readable name of the organizational
entity that manages the Realm identified by the Realm Code.  Open Issue:
In spite of the inability of tooling to process codes longer than 2
characters, there is at least one realm codes ('SOA') that was added
that is 3 characters in length.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-hl7Realm
    """

    class Meta:
        resource = _resource
