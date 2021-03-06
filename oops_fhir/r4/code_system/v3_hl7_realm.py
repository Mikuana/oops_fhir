from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3hl7Realm"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7Realm:
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

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-hl7Realm
    """

    binding_realms = CodeSystemConcept(
        {
            "code": "BindingRealms",
            "concept": [
                {
                    "code": "AffiliateRealms",
                    "concept": [
                        {
                            "code": "AR",
                            "definition": "Description: Realm code for use of Argentina",
                            "display": "Argentina",
                        },
                        {
                            "code": "AT",
                            "definition": "Description: Realm code for use of Austria",
                            "display": "Austria",
                        },
                        {
                            "code": "AU",
                            "definition": "Description: Realm code for use of Australia",
                            "display": "Australia",
                        },
                        {
                            "code": "BR",
                            "definition": "Description: Realm code for use of Brazil",
                            "display": "Brazil",
                        },
                        {
                            "code": "CA",
                            "definition": "Description: Realm code for use of Canada",
                            "display": "Canada",
                        },
                        {
                            "code": "CH",
                            "definition": "Description: Realm code for use of Switzerland",
                            "display": "Switzerland",
                        },
                        {
                            "code": "CL",
                            "definition": "Description: Realm code for use of Chile",
                            "display": "Chile",
                        },
                        {
                            "code": "CN",
                            "definition": "Description: Realm code for use of China",
                            "display": "China",
                        },
                        {
                            "code": "CO",
                            "definition": "Description: Realm code for use of Localized Version",
                            "display": "Columbia",
                        },
                        {
                            "code": "CZ",
                            "definition": "Description: Realm code for use of Czech Republic",
                            "display": "Czech Republic",
                        },
                        {
                            "code": "DE",
                            "definition": "Description: Realm code for use of Germany",
                            "display": "Germany",
                        },
                        {
                            "code": "DK",
                            "definition": "Description: Realm code for use of Denmark",
                            "display": "Denmark",
                        },
                        {
                            "code": "ES",
                            "definition": "Description: Realm code for use of Spain",
                            "display": "Spain",
                        },
                        {
                            "code": "FI",
                            "definition": "Description: Realm code for use of Finland",
                            "display": "Finland",
                        },
                        {
                            "code": "FR",
                            "definition": "Description: Realm code for use of France",
                            "display": "France",
                        },
                        {
                            "code": "GR",
                            "definition": "Description: Realm code for use of Greece",
                            "display": "Greece",
                        },
                        {
                            "code": "HR",
                            "definition": "Description: Realm code for use of Croatia",
                            "display": "Croatia",
                        },
                        {
                            "code": "IE",
                            "definition": "Description: Realm code for use of Ireland",
                            "display": "Ireland",
                        },
                        {
                            "code": "IN",
                            "definition": "Description: Realm code for use of India",
                            "display": "India",
                        },
                        {
                            "code": "IT",
                            "definition": "Description: Realm code for use of Italy",
                            "display": "Italy",
                        },
                        {
                            "code": "JP",
                            "definition": "Description: Realm code for use of Japan",
                            "display": "Japan",
                        },
                        {
                            "code": "KR",
                            "definition": "Description: Realm code for use of Korea",
                            "display": "Korea",
                        },
                        {
                            "code": "LT",
                            "definition": "Description: Realm code for use of Lithuania",
                            "display": "Lithuania",
                        },
                        {
                            "code": "MX",
                            "definition": "Description: Realm code for use of Mexico",
                            "display": "Mexico",
                        },
                        {
                            "code": "NL",
                            "definition": "Description: Realm code for use of The Netherlands",
                            "display": "The Netherlands",
                        },
                        {
                            "code": "NZ",
                            "definition": "Description: Realm code for use of New Zealand",
                            "display": "New Zealand",
                        },
                        {
                            "code": "RO",
                            "definition": "Description: Realm code for use of Romania",
                            "display": "Romania",
                        },
                        {
                            "code": "RU",
                            "definition": "Description: Realm code for use of Russian Federation",
                            "display": "Russian Federation",
                        },
                        {
                            "code": "SE",
                            "definition": "Description: Realm code for use of Sweden",
                            "display": "Sweden",
                        },
                        {
                            "code": "SG",
                            "definition": "Description: Realm code for use of Localized Version",
                            "display": "Singapore",
                        },
                        {
                            "code": "SOA",
                            "definition": "Description: Realm code for use of Southern Africa",
                            "display": "Southern Africa",
                        },
                        {
                            "code": "TR",
                            "definition": "Description: Realm code for use of Turkey",
                            "display": "Turkey",
                        },
                        {
                            "code": "TW",
                            "definition": "Description: Realm code for use of Taiwan",
                            "display": "Taiwan",
                        },
                        {
                            "code": "UK",
                            "definition": "Description: Realm code for use of United Kingdom",
                            "display": "United Kingdom",
                        },
                        {
                            "code": "US",
                            "definition": "Description: Realm code for use of United States of America",
                            "display": "United States of America",
                        },
                        {
                            "code": "UV",
                            "definition": "Description: Realm code for use of Universal realm or context, used in every instance",
                            "display": "Universal",
                        },
                        {
                            "code": "UY",
                            "definition": "Description: Realm code for use of Uruguay",
                            "display": "Uruguay",
                        },
                    ],
                    "definition": 'Description: Realm codes for official HL7 organizational bodies.  This includes both the HL7 International organization as well as all recognized international affiliates (past and present).  These groups have the ability to bind vocabulary and develop artifacts.  As well, they have the ability to have "ownership" over other binding realms and namespace realms via the owningAffiliate property of those other realm codes.',
                    "display": "Affiliate Realms",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "C1",
                    "definition": "Description: Realm code for use of Unclassified Realm",
                    "display": "Unclassified Realm",
                },
                {
                    "code": "GB",
                    "definition": "Description: Realm code for use of Great Britain",
                    "display": "Great Britain",
                },
                {
                    "code": "R1",
                    "definition": "Description: Realm code for use of Representative Realm",
                    "display": "Representative Realm",
                },
                {
                    "code": "X1",
                    "definition": "Description: Realm code for use of Example Realm",
                    "display": "Example Realm",
                },
            ],
            "definition": "Description: Concepts that can be used as Binding Realms when creating Binding Statements.  These codes are permitted to appear in the InfrastructureRoot.realmCode attribute.",
            "display": "binding realms",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    binding realms

    Description: Concepts that can be used as Binding Realms when creating Binding Statements.  These codes are permitted to appear in the InfrastructureRoot.realmCode attribute.
    """

    namespace_realms = CodeSystemConcept(
        {
            "code": "NamespaceRealms",
            "concept": [
                {
                    "code": "ZZ",
                    "definition": "Description: An artifact created for local use only.  This realm namespace has no owning affiliate.  Its use is uncontrolled, i.e. anyone can create artifacts using this realm namespace.  Because of this, there is a significant likelihood of artifact identifier collisions.  Implementers are encouraged to register their artifacts under an affiliate owned and controlled namespace to avoid such collision problems where possible.",
                    "display": "Localized Version",
                }
            ],
            "definition": 'Description: Codes that can be used in the "realm" portion of HL7 v3 artifact identifiers.',
            "display": "namespace realms",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "child", "valueCode": "AffiliateRealms"},
                {"code": "child", "valueCode": "GB"},
            ],
        }
    )
    """
    namespace realms

    Description: Codes that can be used in the "realm" portion of HL7 v3 artifact identifiers.
    """

    class Meta:
        resource = _resource
