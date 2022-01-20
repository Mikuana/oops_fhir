from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3RoleCode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3RoleCode:
    """
    v3 Code System RoleCode

     A set of codes further specifying the kind of Role; specific
classification codes for further qualifying RoleClass codes.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-RoleCode
    """

    underscore_affiliation_role_type = CodeSystemConcept(
        {
            "code": "_AffiliationRoleType",
            "concept": [
                {
                    "code": "_AgentRoleType",
                    "concept": [
                        {
                            "code": "AMENDER",
                            "definition": "An entity which corrected, edited, or amended pre-existing information.",
                            "display": "amender",
                        },
                        {
                            "code": "CLASSIFIER",
                            "definition": "An individual authorized to assign an original classification to information, including compilations of unclassified information, based on a determination that the information requires protection against unauthorized disclosure. The individual marks the information with immutable, computable, and human readable security labels in accordance with applicable security labeling policies.  The labeling policies provide instructions on whether and if so how the security labels may be later reclassified [i.e., upgraded, downgraded, used in derivative classification, or declassified] in a manner that preserves the overridden original classification binding and provenance.",
                            "display": "classifier",
                        },
                        {
                            "code": "CONSENTER",
                            "definition": "An entity or an entity's delegatee who is the grantee in an agreement such as a consent for services, advanced directive, or a privacy consent directive in accordance with jurisdictional, organizational, or patient policy.",
                            "display": "consenter",
                        },
                        {
                            "code": "CONSWIT",
                            "definition": "An entity which has witnessed and attests to observing another entity being counseled about an agreement such as a consent for services, advanced directive, or a privacy consent directive.",
                            "display": "consent witness",
                        },
                        {
                            "code": "COPART",
                            "definition": "An entity which participates in the generation of and attest to veracity of content, but is not an author or coauthor. For example a surgeon who is required by institutional, regulatory, or legal rules to sign an operative report, but who was not involved in the authorship of that report.",
                            "display": "co-participant",
                        },
                        {
                            "code": "DECLASSIFIER",
                            "definition": "An individual which is authorized to declassify information based on a determination that the information no longer requires protection against unauthorized disclosure.  The individual marks the information being declassified using computable and human readable security labels indicating that this is copy of previously classified information is unclassified in accordance with applicable security labeling policies.  The labeling policies provide instructions on whether and if so how the security labels may be later reclassified [i.e., upgraded or used in derivative classification] in a manner that preserves the overridden original classification binding and provenance.",
                            "display": "declassifier",
                        },
                        {
                            "code": "DELEGATEE",
                            "definition": "A party to whom some right or authority is granted by a delegator.",
                            "display": "delegatee",
                        },
                        {
                            "code": "DELEGATOR",
                            "definition": "A party that grants all or some portion its right or authority to another party.",
                            "display": "delegator",
                        },
                        {
                            "code": "DOWNGRDER",
                            "definition": "An individual authorized to lower the classification level of labeled content and provide rationale for doing so as directed by a classification guide.",
                            "display": "downgrader",
                        },
                        {
                            "code": "DRIVCLASSIFIER",
                            "definition": "An individual who is only authorized to classify reproduced, extracted, or summarized classified information, or compile classified and unclassified information by applying classification markings derived from source material or as directed by a classification guide.",
                            "display": "derivative classifier",
                        },
                        {
                            "code": "GRANTEE",
                            "definition": "An entity which accepts certain rights or authority from a grantor.",
                            "display": "grantee",
                        },
                        {
                            "code": "GRANTOR",
                            "definition": "An entity which agrees to confer certain rights or authority to a grantee.",
                            "display": "grantor",
                        },
                        {
                            "code": "INTPRTER",
                            "definition": "An entity which converts spoken or written language into the language of key participants in an event such as when a provider is obtaining a patient's consent to treatment or permission to disclose information.",
                            "display": "interpreter",
                        },
                        {
                            "code": "REVIEWER",
                            "definition": "An entity authorized to filter information according to approved criteria.",
                            "display": "reviewer",
                        },
                        {
                            "code": "VALIDATOR",
                            "definition": "An entity authorized to validate information for inclusion in a record.",
                            "display": "validator",
                        },
                    ],
                    "definition": "Parties that may or should contribute or have contributed to an Act.",
                    "display": "AgentRoleType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_CoverageSponsorRoleType",
                    "concept": [
                        {
                            "code": "FULLINS",
                            "definition": "Description:An employer or organization that contracts with an underwriter to assumes the financial risk and administrative responsibility for coverage of health services for covered parties.",
                            "display": "Fully insured coverage sponsor",
                        },
                        {
                            "code": "SELFINS",
                            "definition": "Description:An employer or organization that assumes the financial risk and administrative responsibility for coverage of health services for covered parties.",
                            "display": "Self insured coverage sponsor",
                        },
                    ],
                    "definition": "Description:Codes that indicate a specific type of sponsor.  Used when the sponsor's role is only either as a fully insured sponsor or only as a self-insured sponsor.  NOTE: Where a sponsor may be either, use the SponsorParticipationFunction.code (fully insured or self insured) to indicate the type of responsibility. (CO6-0057)",
                    "display": "CoverageSponsorRoleType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_PayorRoleType",
                    "concept": [
                        {
                            "code": "ENROLBKR",
                            "definition": "Description:A payor that is responsible for functions related to the enrollment of covered parties.",
                            "display": "Enrollment Broker",
                        },
                        {
                            "code": "TPA",
                            "definition": "Description:Third party administrator (TPA) is a payor organization that processes health care claims without carrying insurance risk. Third party administrators are prominent players in the managed care industry and have the expertise and capability to administer all or a portion of the claims process. They are normally contracted by a health insurer or self-insuring companies to administer services, including claims administration, premium collection, enrollment and other administrative activities.\r\n\n                        Self-insured employers often contract with third party administrator to handle their insurance functions. Insurance companies oftentimes outsource the claims, utilization review or membership functions to a TPA. Sometimes TPAs only manage provider networks, only claims or only utilization review.\r\n\n                        While some third-party administrators may operate as units of insurance companies, they are often independent. However, hospitals or provider organizations desiring to set up their own health plans will often outsource certain responsibilities to TPAs.  TPAs may perform one or several payor functions, specified by the PayorParticipationFunction value set, such as provider management, enrollment, utilization management, and fee for service claims adjudication management.",
                            "display": "Third party administrator",
                        },
                        {
                            "code": "UMO",
                            "definition": "Description:A payor that is responsible for review and case management of health services covered under a policy or program.",
                            "display": "Utilization management organization",
                        },
                    ],
                    "definition": "Description:PayorRoleType for a particular type of policy or program benefit package or plan where more detail about the coverage administration role of the Payor is required.  The functions performed by a Payor qualified by a PayorRoleType may be specified by the PayorParticpationFunction value set.\r\n\n                        \n                           Examples:A Payor that is a TPA may administer a managed care plan without underwriting the risk.",
                    "display": "PayorRoleType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "RESPRSN",
                    "concept": [
                        {
                            "code": "EXCEST",
                            "definition": "The role played by a person acting as the estate executor for a deceased subscriber or policyholder who was the responsible party",
                            "display": "executor of estate",
                        },
                        {
                            "code": "GUADLTM",
                            "definition": "The role played by a person appointed by the court to look out for the best interests of a minor child during the course of legal proceedings.",
                            "display": "guardian ad lidem",
                        },
                        {
                            "code": "GUARD",
                            "definition": "The role played by a person or institution legally empowered with responsibility for the care of a ward.",
                            "display": "guardian",
                        },
                        {
                            "code": "POWATT",
                            "concept": [
                                {
                                    "code": "DPOWATT",
                                    "definition": "A relationship between two people in which one person authorizes another, usually a family member or relative, to act for him or her in a manner which is a legally binding upon the person giving such authority as if he or she personally were to do the acts that is often limited in the kinds of powers that can be assigned.  Unlike ordinary powers of attorney, durable powers can survive for long periods of time, and again, unlike standard powers of attorney, durable powers can continue after incompetency.",
                                    "display": "durable power of attorney",
                                },
                                {
                                    "code": "HPOWATT",
                                    "definition": "A relationship between two people in which one person authorizes another to act for him or her in a manner which is a legally binding upon the person giving such authority as if he or she personally were to do the acts that continues (by its terms) to be effective even though the grantor has become mentally incompetent after signing the document.",
                                    "display": "healthcare power of attorney",
                                },
                                {
                                    "code": "SPOWATT",
                                    "definition": "A relationship between two people in which one person authorizes another to act for him or her in a manner which is a legally binding upon the person giving such authority as if he or she personally were to do the acts that is often limited in the kinds of powers that can be assigned.",
                                    "display": "special power of attorney",
                                },
                            ],
                            "definition": "A relationship between two people in which one person authorizes another to act for him in a manner which is a legally binding upon the person giving such authority as if he or she personally were to do the acts.",
                            "display": "power of attorney",
                        },
                    ],
                    "definition": "The role played by a party who has legal responsibility for another party.",
                    "display": "responsible party",
                },
            ],
            "definition": "Concepts characterizing the type of association formed by player and scoper when there is a recognized Affiliate role by which the two parties are related.\r\n\n                        \n                           Examples: Business Partner, Business Associate, Colleague",
            "display": "AffiliationRoleType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    AffiliationRoleType

    Concepts characterizing the type of association formed by player and scoper when there is a recognized Affiliate role by which the two parties are related.

                        
                           Examples: Business Partner, Business Associate, Colleague
    """

    underscore_assigned_role_type = CodeSystemConcept(
        {
            "code": "_AssignedRoleType",
            "concept": [
                {
                    "code": "_AssignedNonPersonLivingSubjectRoleType",
                    "concept": [
                        {
                            "code": "ASSIST",
                            "definition": "Description:Dogs trained to assist the ill or physically challenged.",
                            "display": "Assistive non-person living subject",
                        },
                        {
                            "code": "BIOTH",
                            "concept": [
                                {
                                    "code": "ANTIBIOT",
                                    "definition": "Description:Non-person living subject used as antibiotic.\r\n\n                        \n                           Examples:Bacteriophage, is a virus that infects bacteria.",
                                    "display": "Antibiotic",
                                },
                                {
                                    "code": "DEBR",
                                    "definition": "Description:Maggots raised for biodebridement.\r\n\n                        \n                           Discussion: Maggot Debridement Therapy is the medical use of live maggots for cleaning non-healing wounds.\r\n\n                        \n                           Examples:Removal of burnt skin.",
                                    "display": "Debridement",
                                },
                            ],
                            "definition": "Description:Animals, including fish and insects, and microorganisms which may participate as assigned entities in biotherapies.",
                            "display": "Biotherapeutic non-person living subject",
                        },
                        {
                            "code": "CCO",
                            "definition": "Description:Companion animals, such as dogs, cats, and rabbits, which may be provided to patients to improve general mood, decrease depression and loneliness, and distract from stress-inducing concerns to improve quality of life.",
                            "display": "Clinical Companion",
                        },
                        {
                            "code": "SEE",
                            "definition": "Description:Dogs trained to assist persons who are seeing impaired or blind.",
                            "display": "Seeing",
                        },
                        {
                            "code": "SNIFF",
                            "definition": "Description:Dogs trained or having the ability to detect imminent seizures or cancers in humans, probably as a result of volatile chemical (odors) given off by the malignancy of the host.",
                            "display": "Sniffing",
                        },
                    ],
                    "definition": "Description:A role type that is used to further qualify a non-person subject playing a role where the role class attribute is set to RoleClass AssignedEntity",
                    "display": "AssignedNonPersonLivingSubjectRoleType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                }
            ],
            "definition": "AssignedRoleType",
            "display": "AssignedRoleType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    AssignedRoleType

    AssignedRoleType
    """

    underscore_certified_entity_type = CodeSystemConcept(
        {
            "code": "_CertifiedEntityType",
            "definition": "Defines types of certifications for all entities",
            "display": "CertifiedEntityType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    CertifiedEntityType

    Defines types of certifications for all entities
    """

    underscore_citizen_role_type = CodeSystemConcept(
        {
            "code": "_CitizenRoleType",
            "concept": [
                {
                    "code": "CAS",
                    "concept": [
                        {
                            "code": "CASM",
                            "definition": "A person who is someone of below legal age who has fled his or her home country, without his or her parents, to find a safe place elsewhere at time of categorization.",
                            "display": "single minor asylum seeker",
                        }
                    ],
                    "definition": "A person who has fled his or her home country to find a safe place elsewhere.",
                    "display": "asylum seeker",
                },
                {
                    "code": "CN",
                    "definition": "A person who is legally recognized as a member of a nation or country, with associated rights and obligations.",
                    "display": "national",
                },
                {
                    "code": "CNRP",
                    "concept": [
                        {
                            "code": "CNRPM",
                            "definition": "A person who is below legal age present in a country, without his or her parents, (which is foreign to him/her) unlawfully or without the country's authorization.",
                            "display": "non-country member minor without residence permit",
                        }
                    ],
                    "definition": "A foreigner who is present in a country (which is foreign to him/her) unlawfully or without the country's authorization (may be called an illegal alien).",
                    "display": "non-country member without residence permit",
                },
                {
                    "code": "CPCA",
                    "definition": "A non-country member admitted to the territory of a nation or country as a non-resident for an explicit purpose.",
                    "display": "permit card applicant",
                },
                {
                    "code": "CRP",
                    "concept": [
                        {
                            "code": "CRPM",
                            "definition": "A person who is a resident below legal age of the country without his or her parents and does not have citizenship.",
                            "display": "non-country member minor with residence permit",
                        }
                    ],
                    "definition": "A foreigner who is a resident of the country but does not have citizenship.",
                    "display": "non-country member with residence permit",
                },
            ],
            "definition": "A role type used to qualify a person's legal status within a country or nation.",
            "display": "CitizenRoleType",
        }
    )
    """
    CitizenRoleType

    A role type used to qualify a person's legal status within a country or nation.
    """

    underscore_contact_role_type = CodeSystemConcept(
        {
            "code": "_ContactRoleType",
            "concept": [
                {
                    "code": "_AdministrativeContactRoleType",
                    "concept": [
                        {
                            "code": "BILL",
                            "definition": "A contact role used to identify a person within a Provider organization that can be contacted for billing purposes (e.g. about the content of the Invoice).",
                            "display": "Billing Contact",
                        },
                        {
                            "code": "ORG",
                            "definition": "A contact for an organization for administrative purposes. Contact role specifies a person acting as a liason for the organization.\r\n\n                        Example: HR Department representative.",
                            "display": "organizational contact",
                        },
                        {
                            "code": "PAYOR",
                            "definition": "A contact role used to identify a person within a Payor organization to whom this communication is addressed.",
                            "display": "Payor Contact",
                        },
                    ],
                    "definition": "A contact role used for business and/or administrative purposes.",
                    "display": "AdministrativeContactRoleType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "ECON",
                    "definition": "A contact designated for contact in emergent situations.",
                    "display": "emergency contact",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2008-12-19"},
                    ],
                },
                {
                    "code": "NOK",
                    "definition": "Played by an individual who is designated as the next of kin for another individual which scopes the role.",
                    "display": "next of kin",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2008-12-19"},
                    ],
                },
            ],
            "definition": 'Types of contact for Role code "CON"',
            "display": "ContactRoleType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ContactRoleType

    Types of contact for Role code "CON"
    """

    underscore_identified_entity_type = CodeSystemConcept(
        {
            "code": "_IdentifiedEntityType",
            "concept": [
                {
                    "code": "_LocationIdentifiedEntityRoleCode",
                    "concept": [
                        {
                            "code": "ACHFID",
                            "definition": "Description:Identifier assigned to a  location by the organization responsible for accrediting the location.",
                            "display": "accreditation location identifier",
                        },
                        {
                            "code": "JURID",
                            "definition": "Description:Identifier assigned to a location by a jurisdiction.",
                            "display": "jurisdiction location identifier",
                        },
                        {
                            "code": "LOCHFID",
                            "definition": "Description:Identifier assigned to a  location by a local party (which could be the facility itself or organization overseeing a group of facilities).",
                            "display": "local location identifier",
                        },
                    ],
                    "definition": "Description:Describes types of identifiers other than the primary location registry identifier for a service delivery location.  Identifiers may be assigned by a local service delivery organization, a formal body capable of accrediting the location for the capability to provide specific services or the identifier may be assigned at a jurisdictional level.",
                    "display": "LocationIdentifiedEntityRoleCode",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                }
            ],
            "definition": "Definition: A code representing the type of identifier that has been assigned to the identified entity (IDENT).\r\n\n                        \n                           Examples: Example values include Social Insurance Number, Product Catalog ID, Product Model Number.",
            "display": "IdentifiedEntityType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    IdentifiedEntityType

    Definition: A code representing the type of identifier that has been assigned to the identified entity (IDENT).

                        
                           Examples: Example values include Social Insurance Number, Product Catalog ID, Product Model Number.
    """

    underscore_living_subject_production_class = CodeSystemConcept(
        {
            "code": "_LivingSubjectProductionClass",
            "concept": [
                {
                    "code": "BF",
                    "definition": "Cattle used for meat production",
                    "display": "Beef",
                },
                {
                    "code": "BL",
                    "definition": "Chickens raised for meat",
                    "display": "Broiler",
                },
                {
                    "code": "BR",
                    "definition": "Breeding/genetic stock",
                    "display": "Breeder",
                },
                {
                    "code": "CO",
                    "definition": "Companion animals",
                    "display": "Companion",
                },
                {"code": "DA", "definition": "Milk production", "display": "Dairy"},
                {"code": "DR", "definition": "Draft animals", "display": "Draft"},
                {
                    "code": "DU",
                    "definition": "Dual purpose.  Defined purposes based on species and breed",
                    "display": "Dual",
                },
                {
                    "code": "FI",
                    "definition": "Animals raised for their fur, hair or skins",
                    "display": "Fiber",
                },
                {
                    "code": "LY",
                    "definition": "Chickens raised for egg production",
                    "display": "Layer",
                },
                {
                    "code": "MT",
                    "definition": "Animals raised for meat production",
                    "display": "Meat",
                },
                {
                    "code": "MU",
                    "definition": "Poultry flocks used for chick/poult production",
                    "display": "Multiplier",
                },
                {
                    "code": "PL",
                    "definition": "Animals rasied for recreation",
                    "display": "Pleasure",
                },
                {
                    "code": "RC",
                    "definition": "Animals raised for racing perfomance",
                    "display": "Racing",
                },
                {
                    "code": "SH",
                    "definition": "Animals raised for shows",
                    "display": "Show",
                },
                {
                    "code": "VL",
                    "definition": "Cattle raised for veal meat production.  Implicit is the husbandry method.",
                    "display": "Veal",
                },
                {
                    "code": "WL",
                    "definition": "Sheep, goats and other mammals raised for their fiber",
                    "display": "Wool",
                },
                {
                    "code": "WO",
                    "definition": "Animals used to perform work",
                    "display": "Working",
                },
            ],
            "definition": "Code indicating the primary use for which a living subject is bred or grown",
            "display": "LivingSubjectProductionClass",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    LivingSubjectProductionClass

    Code indicating the primary use for which a living subject is bred or grown
    """

    underscore_medication_generalization_role_type = CodeSystemConcept(
        {
            "code": "_MedicationGeneralizationRoleType",
            "concept": [
                {
                    "code": "DC",
                    "definition": "Description:A categorization of medicinal products by their therapeutic properties and/or main therapeutic use.",
                    "display": "therapeutic class",
                },
                {
                    "code": "GD",
                    "concept": [
                        {
                            "code": "GDF",
                            "definition": "Relates a manufactured drug product to the non-proprietary (generic) representation of its ingredients and dose form, independent of strength of the ingredients. The scoping entity identifies a unique combination of medicine ingredients in a specific dose form.",
                            "display": "generic drug form",
                        },
                        {
                            "code": "GDS",
                            "definition": "Relates a manufactured drug product to the non-proprietary (generic) representation of is ingredients with their strength.  The scoping entity identifies a unique combination of medicine ingredients with their strength.",
                            "display": "generic drug strength",
                        },
                        {
                            "code": "GDSF",
                            "definition": "Relates a manufactured drug product to the non-proprietary (generic) representation of its ingredients with their strength in a specific dose form. The scoping entity identifies a unique combination of medicine ingredients with their strength in a single dose form.",
                            "display": "generic drug strength form",
                        },
                    ],
                    "definition": 'Relates a manufactured drug product to the non-proprietary (generic) representation of its ingredients independent of strength, and form.\r\n\n                        The scoping entity identifies a unique combination of medicine ingredients; sometimes referred to as "ingredient set".',
                    "display": "generic drug",
                },
                {
                    "code": "MGDSF",
                    "definition": "Relates a manufactured drug product to the non-proprietary (generic) representation of its ingredients with their strength in a specific dose form. The scoping entity identifies a unique combination of medicine ingredients with their strength in a single dose form.",
                    "display": "manufactured drug strength form",
                },
            ],
            "definition": "Identifies the specific hierarchical relationship between the playing and scoping medications. \r\n\n                        \n                           Examples: Generic, Generic Formulation, Therapeutic Class, etc.",
            "display": "MedicationGeneralizationRoleType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    MedicationGeneralizationRoleType

    Identifies the specific hierarchical relationship between the playing and scoping medications. 

                        
                           Examples: Generic, Generic Formulation, Therapeutic Class, etc.
    """

    underscore_member_role_type = CodeSystemConcept(
        {
            "code": "_MemberRoleType",
            "concept": [
                {
                    "code": "TRB",
                    "definition": "A person who is a member of a tribe.",
                    "display": "Tribal Member",
                }
            ],
            "definition": 'Types of membership for Role code "MBR"',
            "display": "MemberRoleType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    MemberRoleType

    Types of membership for Role code "MBR"
    """

    underscore_personal_relationship_role_type = CodeSystemConcept(
        {
            "code": "_PersonalRelationshipRoleType",
            "concept": [
                {
                    "code": "FAMMEMB",
                    "concept": [
                        {
                            "code": "CHILD",
                            "concept": [
                                {
                                    "code": "CHLDADOPT",
                                    "concept": [
                                        {
                                            "code": "DAUADOPT",
                                            "definition": "The player of the role is a female child taken into a family through legal means and raised by the scoping person (parent) as his or her own child.",
                                            "display": "adopted daughter",
                                        },
                                        {
                                            "code": "SONADOPT",
                                            "definition": "The player of the role is a male child taken into a family through legal means and raised by the scoping person (parent) as his or her own child.",
                                            "display": "adopted son",
                                        },
                                    ],
                                    "definition": "The player of the role is a child taken into a family through legal means and raised by the scoping person (parent) as his or her own child.",
                                    "display": "adopted child",
                                },
                                {
                                    "code": "CHLDFOST",
                                    "concept": [
                                        {
                                            "code": "DAUFOST",
                                            "definition": "The player of the role is a female child receiving parental care and nurture from the scoping person (parent) but not related to him or her through legal or blood ties.",
                                            "display": "foster daughter",
                                        },
                                        {
                                            "code": "SONFOST",
                                            "definition": "The player of the role is a male child receiving parental care and nurture from the scoping person (parent) but not related to him or her through legal or blood ties.",
                                            "display": "foster son",
                                        },
                                    ],
                                    "definition": "The player of the role is a child receiving parental care and nurture from the scoping person (parent) but not related to him or her through legal or blood ties.",
                                    "display": "foster child",
                                },
                                {
                                    "code": "DAUC",
                                    "concept": [
                                        {
                                            "code": "DAU",
                                            "definition": "The player of the role is a female offspring of the scoping entity (parent).",
                                            "display": "natural daughter",
                                        },
                                        {
                                            "code": "STPDAU",
                                            "definition": "The player of the role is a daughter of the scoping person's spouse by a previous union.",
                                            "display": "stepdaughter",
                                        },
                                    ],
                                    "definition": "Description: The player of the role is a female child (of any type) of scoping entity (parent)",
                                    "display": "daughter",
                                    "property": [
                                        {"code": "child", "valueCode": "DAUADOPT"},
                                        {"code": "child", "valueCode": "DAUFOST"},
                                    ],
                                },
                                {
                                    "code": "NCHILD",
                                    "concept": [
                                        {
                                            "code": "SON",
                                            "definition": "The player of the role is a male offspring of the scoping entity (parent).",
                                            "display": "natural son",
                                        }
                                    ],
                                    "definition": "The player of the role is an offspring of the scoping entity as determined by birth.",
                                    "display": "natural child",
                                    "property": [{"code": "child", "valueCode": "DAU"}],
                                },
                                {
                                    "code": "SONC",
                                    "concept": [
                                        {
                                            "code": "STPSON",
                                            "definition": "The player of the role is a son of the scoping person's spouse by a previous union.",
                                            "display": "stepson",
                                        }
                                    ],
                                    "definition": "Description: The player of the role is a male child (of any type) of scoping entity (parent)",
                                    "display": "son",
                                    "property": [
                                        {"code": "child", "valueCode": "SONADOPT"},
                                        {"code": "child", "valueCode": "SONFOST"},
                                        {"code": "child", "valueCode": "SON"},
                                    ],
                                },
                                {
                                    "code": "STPCHLD",
                                    "definition": "The player of the role is a child of the scoping person's spouse by a previous union.",
                                    "display": "step child",
                                    "property": [
                                        {"code": "child", "valueCode": "STPDAU"},
                                        {"code": "child", "valueCode": "STPSON"},
                                    ],
                                },
                            ],
                            "definition": "The player of the role is a child of the scoping entity.",
                            "display": "child",
                        },
                        {
                            "code": "EXT",
                            "concept": [
                                {
                                    "code": "AUNT",
                                    "concept": [
                                        {
                                            "code": "MAUNT",
                                            "definition": "Description:The player of the role is a biological sister of the scoping person's biological mother.",
                                            "display": "maternal aunt",
                                        },
                                        {
                                            "code": "PAUNT",
                                            "definition": "Description:The player of the role is a biological sister of the scoping person's biological father.",
                                            "display": "paternal aunt",
                                        },
                                    ],
                                    "definition": "The player of the role is a sister of the scoping person's mother or father.",
                                    "display": "aunt",
                                },
                                {
                                    "code": "COUSN",
                                    "concept": [
                                        {
                                            "code": "MCOUSN",
                                            "definition": "Description:The player of the role is a biological relative of the scoping person descended from a common ancestor on the player's mother's side, such as a grandparent, by two or more steps in a diverging line.",
                                            "display": "maternal cousin",
                                        },
                                        {
                                            "code": "PCOUSN",
                                            "definition": "Description:The player of the role is a biological relative of the scoping person descended from a common ancestor on the player's father's side, such as a grandparent, by two or more steps in a diverging line.",
                                            "display": "paternal cousin",
                                        },
                                    ],
                                    "definition": "The player of the role is a relative of the scoping person descended from a common ancestor, such as a \tgrandparent, by two or more steps in a diverging line.",
                                    "display": "cousin",
                                },
                                {
                                    "code": "GGRPRN",
                                    "concept": [
                                        {
                                            "code": "GGRFTH",
                                            "concept": [
                                                {
                                                    "code": "MGGRFTH",
                                                    "definition": "Description:The player of the role is the biological father of the scoping person's biological mother's parent.",
                                                    "display": "maternal great-grandfather",
                                                },
                                                {
                                                    "code": "PGGRFTH",
                                                    "definition": "Description:The player of the role is the biological father of the scoping person's biological father's parent.",
                                                    "display": "paternal great-grandfather",
                                                },
                                            ],
                                            "definition": "The player of the role is the father of the scoping person's grandparent.",
                                            "display": "great grandfather",
                                        },
                                        {
                                            "code": "GGRMTH",
                                            "concept": [
                                                {
                                                    "code": "MGGRMTH",
                                                    "definition": "Description:The player of the role is the biological mother of the scoping person's biological mother's parent.",
                                                    "display": "maternal great-grandmother",
                                                },
                                                {
                                                    "code": "PGGRMTH",
                                                    "definition": "Description:The player of the role is the biological mother of the scoping person's biological father's parent.",
                                                    "display": "paternal great-grandmother",
                                                },
                                            ],
                                            "definition": "The player of the role is the mother of the scoping person's grandparent.",
                                            "display": "great grandmother",
                                        },
                                        {
                                            "code": "MGGRPRN",
                                            "definition": "Description:The player of the role is a biological parent of the scoping person's biological mother's parent.",
                                            "display": "maternal great-grandparent",
                                            "property": [
                                                {
                                                    "code": "child",
                                                    "valueCode": "MGGRFTH",
                                                },
                                                {
                                                    "code": "child",
                                                    "valueCode": "MGGRMTH",
                                                },
                                            ],
                                        },
                                        {
                                            "code": "PGGRPRN",
                                            "definition": "Description:The player of the role is a biological parent of the scoping person's biological father's parent.",
                                            "display": "paternal great-grandparent",
                                            "property": [
                                                {
                                                    "code": "child",
                                                    "valueCode": "PGGRFTH",
                                                },
                                                {
                                                    "code": "child",
                                                    "valueCode": "PGGRMTH",
                                                },
                                            ],
                                        },
                                    ],
                                    "definition": "The player of the role is a parent of the scoping person's grandparent.",
                                    "display": "great grandparent",
                                },
                                {
                                    "code": "GRNDCHILD",
                                    "concept": [
                                        {
                                            "code": "GRNDDAU",
                                            "definition": "The player of the role is a daughter of the scoping person's son or daughter.",
                                            "display": "granddaughter",
                                        },
                                        {
                                            "code": "GRNDSON",
                                            "definition": "The player of the role is a son of the scoping person's son or daughter.",
                                            "display": "grandson",
                                        },
                                    ],
                                    "definition": "The player of the role is a child of the scoping person's son or daughter.",
                                    "display": "grandchild",
                                },
                                {
                                    "code": "GRPRN",
                                    "concept": [
                                        {
                                            "code": "GRFTH",
                                            "concept": [
                                                {
                                                    "code": "MGRFTH",
                                                    "definition": "Description:The player of the role is the biological father of the scoping person's biological mother.",
                                                    "display": "maternal grandfather",
                                                },
                                                {
                                                    "code": "PGRFTH",
                                                    "definition": "Description:The player of the role is the biological father of the scoping person's biological father.",
                                                    "display": "paternal grandfather",
                                                },
                                            ],
                                            "definition": "The player of the role is the father of the scoping person's mother or father.",
                                            "display": "grandfather",
                                        },
                                        {
                                            "code": "GRMTH",
                                            "concept": [
                                                {
                                                    "code": "MGRMTH",
                                                    "definition": "Description:The player of the role is the biological mother of the scoping person's biological mother.",
                                                    "display": "maternal grandmother",
                                                },
                                                {
                                                    "code": "PGRMTH",
                                                    "definition": "Description:The player of the role is the biological mother of the scoping person's biological father.",
                                                    "display": "paternal grandmother",
                                                },
                                            ],
                                            "definition": "The player of the role is the mother of the scoping person's mother or father.",
                                            "display": "grandmother",
                                        },
                                        {
                                            "code": "MGRPRN",
                                            "definition": "Description:The player of the role is the biological parent of the scoping person's biological mother.",
                                            "display": "maternal grandparent",
                                            "property": [
                                                {
                                                    "code": "child",
                                                    "valueCode": "MGRFTH",
                                                },
                                                {
                                                    "code": "child",
                                                    "valueCode": "MGRMTH",
                                                },
                                            ],
                                        },
                                        {
                                            "code": "PGRPRN",
                                            "definition": "Description:The player of the role is the biological parent of the scoping person's biological father.",
                                            "display": "paternal grandparent",
                                            "property": [
                                                {
                                                    "code": "child",
                                                    "valueCode": "PGRFTH",
                                                },
                                                {
                                                    "code": "child",
                                                    "valueCode": "PGRMTH",
                                                },
                                            ],
                                        },
                                    ],
                                    "definition": "The player of the role is a parent of the scoping person's mother or father.",
                                    "display": "grandparent",
                                },
                                {
                                    "code": "INLAW",
                                    "concept": [
                                        {
                                            "code": "CHLDINLAW",
                                            "concept": [
                                                {
                                                    "code": "DAUINLAW",
                                                    "definition": "The player of the role is the wife of scoping person's son.",
                                                    "display": "daughter in-law",
                                                },
                                                {
                                                    "code": "SONINLAW",
                                                    "definition": "The player of the role is the husband of scoping person's daughter.",
                                                    "display": "son in-law",
                                                },
                                            ],
                                            "definition": "The player of the role is the spouse of scoping person's child.",
                                            "display": "child-in-law",
                                        },
                                        {
                                            "code": "PRNINLAW",
                                            "concept": [
                                                {
                                                    "code": "FTHINLAW",
                                                    "definition": "The player of the role is the father of the scoping person's husband or wife.",
                                                    "display": "father-in-law",
                                                },
                                                {
                                                    "code": "MTHINLAW",
                                                    "definition": "The player of the role is the mother of the scoping person's husband or wife.",
                                                    "display": "mother-in-law",
                                                },
                                            ],
                                            "definition": "The player of the role is the parent of scoping person's husband or wife.",
                                            "display": "parent in-law",
                                        },
                                        {
                                            "code": "SIBINLAW",
                                            "concept": [
                                                {
                                                    "code": "BROINLAW",
                                                    "definition": "The player of the role is: (1) a brother of the scoping person's spouse, or (2) the husband of the scoping person's sister, or (3) the husband of a sister of the scoping person's spouse.",
                                                    "display": "brother-in-law",
                                                },
                                                {
                                                    "code": "SISINLAW",
                                                    "definition": "The player of the role is: (1) a sister of the scoping person's spouse, or (2) the wife of the scoping person's brother, or (3) the wife of a brother of the scoping person's spouse.",
                                                    "display": "sister-in-law",
                                                },
                                            ],
                                            "definition": "The player of the role is: (1) a sibling of the scoping person's spouse, or (2) the spouse of the scoping person's sibling, or (3) the spouse of a sibling of the scoping person's spouse.",
                                            "display": "sibling in-law",
                                        },
                                    ],
                                    "definition": "A relationship between an individual and a member of their spousal partner's immediate family.",
                                    "display": "inlaw",
                                },
                                {
                                    "code": "NIENEPH",
                                    "concept": [
                                        {
                                            "code": "NEPHEW",
                                            "definition": "The player of the role is a son of the scoping person's brother or sister or of the brother or sister of the \tscoping person's spouse.",
                                            "display": "nephew",
                                        },
                                        {
                                            "code": "NIECE",
                                            "definition": "The player of the role is a daughter of the scoping person's brother or sister or of the brother or sister of the \tscoping person's spouse.",
                                            "display": "niece",
                                        },
                                    ],
                                    "definition": "The player of the role is a child of scoping person's brother or sister or of the brother or sister of the \tscoping person's spouse.",
                                    "display": "niece/nephew",
                                },
                                {
                                    "code": "UNCLE",
                                    "concept": [
                                        {
                                            "code": "MUNCLE",
                                            "definition": "Description:The player of the role is a biological brother of the scoping person's biological mother.",
                                            "display": "maternal uncle",
                                        },
                                        {
                                            "code": "PUNCLE",
                                            "definition": "Description:The player of the role is a biological brother of the scoping person's biological father.",
                                            "display": "paternal uncle",
                                        },
                                    ],
                                    "definition": "The player of the role is a brother of the scoping person's mother or father.",
                                    "display": "uncle",
                                },
                            ],
                            "definition": "Description: A family member not having an immediate genetic or legal relationship e.g. Aunt, cousin, great grandparent, grandchild, grandparent, niece, nephew or uncle.",
                            "display": "extended family member",
                        },
                        {
                            "code": "PRN",
                            "concept": [
                                {
                                    "code": "ADOPTP",
                                    "concept": [
                                        {
                                            "code": "ADOPTF",
                                            "definition": "The player of the role (father) is a male who has taken the scoper (child) into their family through legal means and raises them as his own child.",
                                            "display": "adoptive father",
                                        },
                                        {
                                            "code": "ADOPTM",
                                            "definition": "The player of the role (father) is a female who has taken the scoper (child) into their family through legal means and raises them as her own child.",
                                            "display": "adoptive mother",
                                        },
                                    ],
                                    "definition": "The player of the role (parent) has taken the scoper (child) into their family through legal means and raises them as his or her own child.",
                                    "display": "adoptive parent",
                                },
                                {
                                    "code": "FTH",
                                    "concept": [
                                        {
                                            "code": "FTHFOST",
                                            "definition": "The player of the role (parent) who is a male state-certified caregiver responsible for the scoper (child) who has been placed in the parent's care. The placement of the child is usually arranged through the government or a social-service agency, and temporary.\r\n\n                        The state, via a jurisdiction recognized child protection agency, stands as in loco parentis to the child, making all legal decisions while the foster parent is responsible for the day-to-day care of the specified child.",
                                            "display": "foster father",
                                        },
                                        {
                                            "code": "NFTH",
                                            "concept": [
                                                {
                                                    "code": "NFTHF",
                                                    "definition": "Indicates the biologic male parent of a fetus.",
                                                    "display": "natural father of fetus",
                                                }
                                            ],
                                            "definition": "The player of the role is a male who begets the scoping entity (child).",
                                            "display": "natural father",
                                        },
                                        {
                                            "code": "STPFTH",
                                            "definition": "The player of the role is the husband of scoping person's mother and not the scoping person's natural father.",
                                            "display": "stepfather",
                                        },
                                    ],
                                    "definition": "The player of the role is a male who begets or raises or nurtures the scoping entity (child).",
                                    "display": "father",
                                    "property": [
                                        {"code": "child", "valueCode": "ADOPTF"}
                                    ],
                                },
                                {
                                    "code": "MTH",
                                    "concept": [
                                        {
                                            "code": "GESTM",
                                            "definition": "The player is a female whose womb carries the fetus of the scoper.  Generally used when the gestational mother and natural mother are not the same.",
                                            "display": "gestational mother",
                                        },
                                        {
                                            "code": "MTHFOST",
                                            "definition": "The player of the role (parent) who is a female state-certified caregiver responsible for the scoper (child) who has been placed in the parent's care. The placement of the child is usually arranged through the government or a social-service agency, and temporary.\r\n\n                        The state, via a jurisdiction recognized child protection agency, stands as in loco parentis to the child, making all legal decisions while the foster parent is responsible for the day-to-day care of the specified child.",
                                            "display": "foster mother",
                                        },
                                        {
                                            "code": "NMTH",
                                            "concept": [
                                                {
                                                    "code": "NMTHF",
                                                    "definition": "The player is the biologic female parent of the scoping fetus.",
                                                    "display": "natural mother of fetus",
                                                }
                                            ],
                                            "definition": "The player of the role is a female who conceives or gives birth to the scoping entity (child).",
                                            "display": "natural mother",
                                        },
                                        {
                                            "code": "STPMTH",
                                            "definition": "The player of the role is the wife of scoping person's father and not the scoping person's natural mother.",
                                            "display": "stepmother",
                                        },
                                    ],
                                    "definition": "The player of the role is a female who conceives, gives birth to, or raises and nurtures the scoping entity (child).",
                                    "display": "mother",
                                    "property": [
                                        {"code": "child", "valueCode": "ADOPTM"}
                                    ],
                                },
                                {
                                    "code": "NPRN",
                                    "definition": "natural parent",
                                    "display": "natural parent",
                                    "property": [
                                        {"code": "child", "valueCode": "NFTH"},
                                        {"code": "child", "valueCode": "NMTH"},
                                    ],
                                },
                                {
                                    "code": "PRNFOST",
                                    "definition": "The player of the role (parent) who is a state-certified caregiver responsible for the scoper (child) who has been placed in the parent's care. The placement of the child is usually arranged through the government or a social-service agency, and temporary.\r\n\n                        The state, via a jurisdiction recognized child protection agency, stands as in loco parentis to the child, making all legal decisions while the foster parent is responsible for the day-to-day care of the specified child.",
                                    "display": "foster parent",
                                    "property": [
                                        {"code": "child", "valueCode": "FTHFOST"},
                                        {"code": "child", "valueCode": "MTHFOST"},
                                    ],
                                },
                                {
                                    "code": "STPPRN",
                                    "definition": "The player of the role is the spouse of the scoping person's parent and not the scoping person's natural parent.",
                                    "display": "step parent",
                                    "property": [
                                        {"code": "child", "valueCode": "STPFTH"},
                                        {"code": "child", "valueCode": "STPMTH"},
                                    ],
                                },
                            ],
                            "definition": "The player of the role is one who begets, gives birth to, or nurtures and raises the scoping entity (child).",
                            "display": "parent",
                        },
                        {
                            "code": "SIB",
                            "concept": [
                                {
                                    "code": "BRO",
                                    "concept": [
                                        {
                                            "code": "HBRO",
                                            "definition": "The player of the role is a male related to the scoping entity by sharing only one biological parent.",
                                            "display": "half-brother",
                                        },
                                        {
                                            "code": "NBRO",
                                            "concept": [
                                                {
                                                    "code": "TWINBRO",
                                                    "concept": [
                                                        {
                                                            "code": "FTWINBRO",
                                                            "definition": "The scoper was carried in the same womb as the male player and shares common biological parents but is the product of a distinct egg/sperm pair.",
                                                            "display": "fraternal twin brother",
                                                        },
                                                        {
                                                            "code": "ITWINBRO",
                                                            "definition": "The male scoper is an offspring of the same egg-sperm pair as the male player.",
                                                            "display": "identical twin brother",
                                                        },
                                                    ],
                                                    "definition": "The scoper was carried in the same womb as the male player and shares common biological parents.",
                                                    "display": "twin brother",
                                                }
                                            ],
                                            "definition": "The player of the role is a male having the same biological parents as the scoping entity.",
                                            "display": "natural brother",
                                        },
                                        {
                                            "code": "STPBRO",
                                            "definition": "The player of the role is a son of the scoping person's stepparent.",
                                            "display": "stepbrother",
                                        },
                                    ],
                                    "definition": "The player of the role is a male sharing one or both parents in common with the scoping entity.",
                                    "display": "brother",
                                },
                                {
                                    "code": "HSIB",
                                    "concept": [
                                        {
                                            "code": "HSIS",
                                            "definition": "The player of the role is a female related to the scoping entity by sharing only one biological parent.",
                                            "display": "half-sister",
                                        }
                                    ],
                                    "definition": "The player of the role is related to the scoping entity by sharing only one biological parent.",
                                    "display": "half-sibling",
                                    "property": [
                                        {"code": "child", "valueCode": "HBRO"}
                                    ],
                                },
                                {
                                    "code": "NSIB",
                                    "concept": [
                                        {
                                            "code": "NSIS",
                                            "concept": [
                                                {
                                                    "code": "TWINSIS",
                                                    "concept": [
                                                        {
                                                            "code": "FTWINSIS",
                                                            "definition": "The scoper was carried in the same womb as the female player and shares common biological parents but is the product of a distinct egg/sperm pair.",
                                                            "display": "fraternal twin sister",
                                                        },
                                                        {
                                                            "code": "ITWINSIS",
                                                            "definition": "The female scoper is an offspring of the same egg-sperm pair as the female player.",
                                                            "display": "identical twin sister",
                                                        },
                                                    ],
                                                    "definition": "The scoper was carried in the same womb as the female player and shares common biological parents.",
                                                    "display": "twin sister",
                                                }
                                            ],
                                            "definition": "The player of the role is a female having the same biological parents as the scoping entity.",
                                            "display": "natural sister",
                                        },
                                        {
                                            "code": "TWIN",
                                            "concept": [
                                                {
                                                    "code": "FTWIN",
                                                    "definition": "The scoper and player were carried in the same womb and share common biological parents but are the product of distinct egg/sperm pairs.",
                                                    "display": "fraternal twin",
                                                    "property": [
                                                        {
                                                            "code": "child",
                                                            "valueCode": "FTWINBRO",
                                                        },
                                                        {
                                                            "code": "child",
                                                            "valueCode": "FTWINSIS",
                                                        },
                                                    ],
                                                },
                                                {
                                                    "code": "ITWIN",
                                                    "definition": "The scoper and player are offspring of the same egg-sperm pair.",
                                                    "display": "identical twin",
                                                    "property": [
                                                        {
                                                            "code": "child",
                                                            "valueCode": "ITWINBRO",
                                                        },
                                                        {
                                                            "code": "child",
                                                            "valueCode": "ITWINSIS",
                                                        },
                                                    ],
                                                },
                                            ],
                                            "definition": "The scoper and player were carried in the same womb and shared common biological parents.",
                                            "display": "twin",
                                            "property": [
                                                {
                                                    "code": "child",
                                                    "valueCode": "TWINBRO",
                                                },
                                                {
                                                    "code": "child",
                                                    "valueCode": "TWINSIS",
                                                },
                                            ],
                                        },
                                    ],
                                    "definition": "The player of the role has both biological parents in common with the scoping entity.",
                                    "display": "natural sibling",
                                    "property": [
                                        {"code": "child", "valueCode": "NBRO"}
                                    ],
                                },
                                {
                                    "code": "SIS",
                                    "concept": [
                                        {
                                            "code": "STPSIS",
                                            "definition": "The player of the role is a daughter of the scoping person's stepparent.",
                                            "display": "stepsister",
                                        }
                                    ],
                                    "definition": "The player of the role is a female sharing one or both parents in common with the scoping entity.",
                                    "display": "sister",
                                    "property": [
                                        {"code": "child", "valueCode": "HSIS"},
                                        {"code": "child", "valueCode": "NSIS"},
                                    ],
                                },
                                {
                                    "code": "STPSIB",
                                    "definition": "The player of the role is a child of the scoping person's stepparent.",
                                    "display": "step sibling",
                                    "property": [
                                        {"code": "child", "valueCode": "STPBRO"},
                                        {"code": "child", "valueCode": "STPSIS"},
                                    ],
                                },
                            ],
                            "definition": "The player of the role shares one or both parents in common with the scoping entity.",
                            "display": "sibling",
                        },
                        {
                            "code": "SIGOTHR",
                            "concept": [
                                {
                                    "code": "DOMPART",
                                    "definition": "The player of the role cohabits with the scoping person but is not the scoping person's spouse.",
                                    "display": "domestic partner",
                                },
                                {
                                    "code": "FMRSPS",
                                    "definition": "Player of the role was previously joined to the scoping person in marriage and this marriage is now dissolved and inactive.\r\n\n                        \n                           Usage Note: This is significant to indicate as some jurisdictions have different legal requirements for former spouse to access the patient's record, from a general friend.",
                                    "display": "former spouse",
                                },
                                {
                                    "code": "SPS",
                                    "concept": [
                                        {
                                            "code": "HUSB",
                                            "definition": "The player of the role is a man joined to a woman (scoping person) in marriage.",
                                            "display": "husband",
                                        },
                                        {
                                            "code": "WIFE",
                                            "definition": "The player of the role is a woman joined to a man (scoping person) in marriage.",
                                            "display": "wife",
                                        },
                                    ],
                                    "definition": "The player of the role is a marriage partner of the scoping person.",
                                    "display": "spouse",
                                },
                            ],
                            "definition": "A person who is important to one's well being; especially a spouse or one in a similar relationship.  (The player is the one who is important)",
                            "display": "significant other",
                        },
                    ],
                    "definition": 'A relationship between two people characterizing their "familial" relationship',
                    "display": "family member",
                },
                {
                    "code": "FRND",
                    "definition": "The player of the role is a person who is known, liked, and trusted by the scoping person.",
                    "display": "unrelated friend",
                },
                {
                    "code": "NBOR",
                    "definition": "The player of the role lives near or next to the \tscoping person.",
                    "display": "neighbor",
                },
                {
                    "code": "ONESELF",
                    "definition": "The relationship that a person has with his or her self.",
                    "display": "self",
                },
                {
                    "code": "ROOM",
                    "definition": "One who shares living quarters with the subject.",
                    "display": "Roommate",
                },
            ],
            "definition": "PersonalRelationshipRoleType",
            "display": "PersonalRelationshipRoleType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    PersonalRelationshipRoleType

    PersonalRelationshipRoleType
    """

    underscore_policy_or_program_coverage_role_type = CodeSystemConcept(
        {
            "code": "_PolicyOrProgramCoverageRoleType",
            "concept": [
                {
                    "code": "_CoverageRoleType",
                    "concept": [
                        {
                            "code": "FAMDEP",
                            "definition": "The player of the role is dependent of the scoping entity.",
                            "display": "family dependent",
                        },
                        {
                            "code": "HANDIC",
                            "definition": "Covered party is a dependent of the policy holder with a physical or mental disability causing a disadvantage that makes independent achievement unusually difficult.",
                            "display": "handicapped dependent",
                        },
                        {
                            "code": "INJ",
                            "definition": "Covered party is an injured party with a legal claim for compensation against a policy holder under an insurance policy.",
                            "display": "injured plaintiff",
                        },
                        {
                            "code": "SELF",
                            "definition": "Covered party is the policy holder.  Also known as the subscriber.",
                            "display": "self",
                        },
                        {
                            "code": "SPON",
                            "definition": "Covered party is an individual that the policy holder has assumed responsibility for, such as foster child or legal ward.",
                            "display": "sponsored dependent",
                        },
                        {
                            "code": "STUD",
                            "concept": [
                                {
                                    "code": "FSTUD",
                                    "definition": "Covered party to an insurance policy has coverage through full-time attendance at a recognized educational institution as defined by a particular insurance policy.",
                                    "display": "full-time student",
                                },
                                {
                                    "code": "PSTUD",
                                    "definition": "Covered party to an insurance policy has coverage through part-time attendance at a recognized educational institution as defined by a particular insurance policy.",
                                    "display": "part-time student",
                                },
                            ],
                            "definition": "Covered party to an insurance policy has coverage through full-time or part-time attendance at a recognized educational institution as defined by a particular insurance policy.",
                            "display": "student",
                        },
                        {
                            "code": "ADOPT",
                            "definition": "A child taken into one's family through legal means and raised as one's own child.",
                            "display": "adopted child",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                        {
                            "code": "GCHILD",
                            "definition": "A child of one's son or daughter.",
                            "display": "grandchild",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                        {
                            "code": "GPARNT",
                            "definition": "parent of a parent of the subject.",
                            "display": "grandparent",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                        {
                            "code": "NAT",
                            "definition": "A child as determined by birth.",
                            "display": "natural child",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                        {
                            "code": "NIENE",
                            "definition": "A child of one's brother or sister or of the brother or sister of one's spouse.",
                            "display": "niece/nephew",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                        {
                            "code": "PARNT",
                            "definition": "One that begets or brings forth offspring or a person who brings up and cares for for another (Webster's Collegiate Dictionary)",
                            "display": "parent",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                        {
                            "code": "SPSE",
                            "definition": "A marriage partner; a husband or wife.",
                            "display": "spouse",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                        {
                            "code": "STEP",
                            "definition": "A child receiving parental care and nurture from a person who is related to them through marriage to their parent.",
                            "display": "step child",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                    ],
                    "definition": "Role recognized through the issuance of insurance coverage to an identified covered party who has this relationship with the policy holder such as the policy holder themselves (self), spouse, child, etc",
                    "display": "CoverageRoleType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_CoveredPartyRoleType",
                    "concept": [
                        {
                            "code": "_ClaimantCoveredPartyRoleType",
                            "concept": [
                                {
                                    "code": "CRIMEVIC",
                                    "definition": 'Description: A person playing the role of program eligible under a program based on allegations of being the victim of a crime.\r\n\n                        \n                           Discussion: This CoveredPartyRoleType.code is typically used when the CoveredPartyRole class code is "program eligible" and the person\'s status as a crime victim meets jurisdictional or program criteria.',
                                    "display": "crime victim",
                                },
                                {
                                    "code": "INJWKR",
                                    "definition": 'Description: A person playing the role of program eligible under a workers compensation program based on the filing of work-related injury claim.\r\n\n                        \n                           Discussion:  This CoveredPartyRoleType.code is used when the CoveredPartyRole class code is either "program eligible", a "named insured", and "individual insured",  or "dependent", and the person\'s status as differently abled or "handicapped" meets jurisdictional, policy, or program criteria.',
                                    "display": "injured worker",
                                },
                            ],
                            "definition": "DescriptionA role recognized through the eligibility of a party play a claimant for benefits covered or provided under an insurance policy.",
                            "display": "ClaimantCoveredPartyRoleType",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_DependentCoveredPartyRoleType",
                            "concept": [
                                {
                                    "code": "COCBEN",
                                    "definition": 'Description: A person playing the role of an individual insured with continuity of coverage under a policy which is being terminated based on loss of original status that was the basis for coverage.  Criteria for qualifying for continuity of coverage may be set by law.\r\n\n                        \n                           Discussion: This CoveredPartyRoleType.code is typically used when the CoveredPartyRole class code is either "program eligible" or "subscriber" and the person\'s status as a continuity of coverage beneficiary meets jurisdictional or policy criteria.',
                                    "display": "continuity of coverage beneficiary",
                                },
                                {
                                    "code": "DIFFABL",
                                    "definition": 'Description: A person playing the role of program eligible under a program based on meeting criteria for health or functional limitation set by law or by the program.\r\n\n                        \n                           Discussion: This CoveredPartyRoleType.code is typically used when the CoveredPartyRole class code is either "program eligible", "named insured", "individual insured", or "dependent", and the person\'s status as differently abled meets jurisdictional, policy, or program criteria.',
                                    "display": "differently abled",
                                },
                                {
                                    "code": "WARD",
                                    "definition": 'Description: A person, who is a minor or is deemed incompetent, who plays the role of a program eligible where eligibility for coverage is based on meeting program eligibility criteria for status as a ward of a court or jurisdiction.\r\n\n                        \n                           Discussion: This CoveredPartyRoleType.code is typically used when the CoveredPartyRole class code is a "claimant", "program eligible", a "named insured", an "individual Insured" or a "dependent", and the person\'s status as a ward meets program or policy criteria. In the case of a ward covered under a program providing financial or health benefits, a governmental agency may take temporary custody of a minor or incompetent for his/her protection and care, e.g., if the ward is suffering from neglect or abuse, or has been in trouble with the law.',
                                    "display": "ward",
                                },
                            ],
                            "definition": "Description: A role recognized through the eligibility of a party to play a dependent for benefits covered or provided under a health insurance policy because of an association with the subscriber that is recognized by the policy underwriter.",
                            "display": "DependentCoveredPartyRoleType",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_IndividualInsuredPartyRoleType",
                            "concept": [
                                {
                                    "code": "RETIREE",
                                    "definition": 'Description: A person playing the role of an individual insured under a policy based on meeting criteria for the employment status of retired set by law or the policy.\r\n\n                        \n                           Discussion: This CoveredPartyRoleType.code is typically used when the CoveredPartyRole class code is either "program eligible" or "subscriber" and the person\'s status as a retiree meets jurisdictional or policy criteria.',
                                    "display": "retiree",
                                }
                            ],
                            "definition": "A role recognized through the eligibility of a party to play an individual insured for benefits covered or provided under an insurance policy where the party is also the policy holder.",
                            "display": "IndividualInsuredPartyRoleType",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True},
                                {"code": "child", "valueCode": "COCBEN"},
                            ],
                        },
                        {
                            "code": "_ProgramEligiblePartyRoleType",
                            "concept": [
                                {
                                    "code": "INDIG",
                                    "definition": 'Description: A person playing the role of program eligible under a program based on aboriginal ancestry or as a member of an aboriginal community.\r\n\n                        \n                           Discussion: This CoveredPartyRoleType.code is typically used when the CoveredPartyRole class code is "program eligible" and the person\'s status as a member of an indigenous people meets jurisdictional or program criteria.',
                                    "display": "member of an indigenous people",
                                },
                                {
                                    "code": "MIL",
                                    "concept": [
                                        {
                                            "code": "ACTMIL",
                                            "definition": 'Description: A person playing the role of program eligible under a program based on active military status.\r\n\n                        \n                           Discussion: This CoveredPartyRoleType.code is typically used when the CoveredPartyRole class code is either "program eligible" or "subscriber" and the persons status as active duty military meets jurisdictional or program criteria.',
                                            "display": "active duty military",
                                        },
                                        {
                                            "code": "RETMIL",
                                            "definition": 'Description: A person playing the role of program eligible under a program based on retired military status.\r\n\n                        \n                           Discussion: This CoveredPartyRoleType.code is typically used when the CoveredPartyRole class code is either "program eligible" or "subscriber" and the persons status as retired military meets jurisdictional or program criteria.',
                                            "display": "retired military",
                                        },
                                        {
                                            "code": "VET",
                                            "definition": 'Description: A person playing the role of program eligible under a program based on status as a military veteran.\r\n\n                        \n                           Discussion: This CoveredPartyRoleType.code is typically used when the CoveredPartyRole class code is either "program eligible" or "subscriber" and the persons status as a veteran meets jurisdictional or program criteria.',
                                            "display": "veteran",
                                        },
                                    ],
                                    "definition": 'Definition: A person playing the role of program eligible under a program based on military status.\r\n\n                        \n                           Discussion:  This CoveredPartyRoleType.code is typically used when the CoveredPartyRole class code is either "program eligible" or "subscriber" and the person\'s status as a member of the military meets jurisdictional or program criteria',
                                    "display": "military",
                                },
                            ],
                            "definition": "Description:A role recognized through the eligibility of a party to play a program eligible for benefits covered or provided under a program.",
                            "display": "ProgramEligiblePartyRoleType",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True},
                                {"code": "child", "valueCode": "CRIMEVIC"},
                                {"code": "child", "valueCode": "INJWKR"},
                                {"code": "child", "valueCode": "DIFFABL"},
                                {"code": "child", "valueCode": "WARD"},
                            ],
                        },
                        {
                            "code": "_SubscriberCoveredPartyRoleType",
                            "definition": "Description: A role recognized through the eligibility of a party to play a subscriber for benefits covered or provided under a health insurance policy.",
                            "display": "SubscriberCoveredPartyRoleType",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True},
                                {"code": "child", "valueCode": "COCBEN"},
                                {"code": "child", "valueCode": "RETIREE"},
                                {"code": "child", "valueCode": "MIL"},
                            ],
                        },
                    ],
                    "definition": 'A role recognized through the eligibility of an identified living subject for benefits covered under an insurance policy or a program.  Eligibility as a covered party may be conditioned on a relationship with (1) the policy holder such as the policy holder who is covered as an individual under a poliy or as a party sponsored for coverage by the policy holder.\r\n\n                        \n                           Example:An employee as a subscriber; or (2) on being scoped another covered party such as the subscriber, as in the case of a dependent. \r\n\n                        \n                           Discussion:  The Abstract Value Set "CoverageRoleType", which was developed for use in the Canadian realm "pre-coordinate" coverage roles with other roles that a covered party must play in order to be eligible for coverage, e.g., "handicapped dependent".  Other codes in the Abstract Value Set CoveredPartyRoleType domain can be "post-coordinated" with the EligiblePartyRoleType codes to denote comparable concepts.  Decoupling the concepts is intended to support a wider range of concepts and semantic comparability of coded concepts.',
                    "display": "covered party role type",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": 'Description: A role recognized through the eligibility of an identified party for benefits covered under an insurance policy or a program based on meeting eligibility criteria.\r\n\n                        Eligibility as a covered party may be conditioned on the party meeting criteria to qualify for coverage under a policy or program, which may be mandated by law.  These criteria may be: \r\n\n                        \n                           \n                              The sole basis for coverage, e.g., being differently abled may qualify a person for disability coverage\r\n\n                           \n                           \n                              May more fully qualify a covered party role e.g, being differently abled may qualify an adult child as a dependent\r\n\n                           \n                           \n                              May impact the level of coverage for a covered party under a policy or program, e.g., being differently abled may qualify a program eligible for additional benefits.\r\n\n                           \n                        \n                        \n                           Discussion:  The Abstract Value Set "CoverageRoleType", which was developed for use in the Canadian realm "pre-coordinate" coverage roles with other roles that a covered party must play in order to be eligible for coverage, e.g., "handicapped dependent".   These role.codes may only be used with COVPTY to avoid overlapping concepts that would result from using them to specify the specializations of COVPTY, e.g., the role.class DEPEN should not be used with the role.code family dependent because that relationship has overlapping concepts due to the role.code precoodination and is conveyed in FICO with the personal relationship role that has a PART role link to the covered party role.  For the same reasons, the role.class DEPEN should not be used with the role.code HANDIC (handicapped dependent); the role.code DIFFABLE (differently abled) should be used instead.\r\n\n                        In summary, the coded concepts in the Abstract Value Set "CoveredPartyRoleType" can be "post-coordinated" with the "RoleClassCoveredParty" Abstract Value Set.  Decoupling these concepts is intended to support an expansive range of covered party concepts and their semantic comparability.',
            "display": "PolicyOrProgramCoverageRoleType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    PolicyOrProgramCoverageRoleType

    Description: A role recognized through the eligibility of an identified party for benefits covered under an insurance policy or a program based on meeting eligibility criteria.

                        Eligibility as a covered party may be conditioned on the party meeting criteria to qualify for coverage under a policy or program, which may be mandated by law.  These criteria may be: 

                        
                           
                              The sole basis for coverage, e.g., being differently abled may qualify a person for disability coverage

                           
                           
                              May more fully qualify a covered party role e.g, being differently abled may qualify an adult child as a dependent

                           
                           
                              May impact the level of coverage for a covered party under a policy or program, e.g., being differently abled may qualify a program eligible for additional benefits.

                           
                        
                        
                           Discussion:  The Abstract Value Set "CoverageRoleType", which was developed for use in the Canadian realm "pre-coordinate" coverage roles with other roles that a covered party must play in order to be eligible for coverage, e.g., "handicapped dependent".   These role.codes may only be used with COVPTY to avoid overlapping concepts that would result from using them to specify the specializations of COVPTY, e.g., the role.class DEPEN should not be used with the role.code family dependent because that relationship has overlapping concepts due to the role.code precoodination and is conveyed in FICO with the personal relationship role that has a PART role link to the covered party role.  For the same reasons, the role.class DEPEN should not be used with the role.code HANDIC (handicapped dependent); the role.code DIFFABLE (differently abled) should be used instead.

                        In summary, the coded concepts in the Abstract Value Set "CoveredPartyRoleType" can be "post-coordinated" with the "RoleClassCoveredParty" Abstract Value Set.  Decoupling these concepts is intended to support an expansive range of covered party concepts and their semantic comparability.
    """

    underscore_research_subject_role_basis = CodeSystemConcept(
        {
            "code": "_ResearchSubjectRoleBasis",
            "concept": [
                {
                    "code": "ERL",
                    "definition": "Definition:The specific role being played by a research subject participating in the active treatment or primary data collection portion of a research study.",
                    "display": "enrollment",
                },
                {
                    "code": "SCN",
                    "definition": "Definition:The specific role being played by a research subject participating in the pre-enrollment evaluation portion of  a research study.",
                    "display": "screening",
                },
            ],
            "definition": "Specifies the administrative functionality within a formal experimental design for which the ResearchSubject role was established.  Examples: screening - role is used for pre-enrollment evaluation portion of the design; enrolled - role is used for subjects admitted to the active treatment portion of the design.",
            "display": "ResearchSubjectRoleBasis",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ResearchSubjectRoleBasis

    Specifies the administrative functionality within a formal experimental design for which the ResearchSubject role was established.  Examples: screening - role is used for pre-enrollment evaluation portion of the design; enrolled - role is used for subjects admitted to the active treatment portion of the design.
    """

    underscore_service_delivery_location_role_type = CodeSystemConcept(
        {
            "code": "_ServiceDeliveryLocationRoleType",
            "concept": [
                {
                    "code": "_DedicatedServiceDeliveryLocationRoleType",
                    "concept": [
                        {
                            "code": "_DedicatedClinicalLocationRoleType",
                            "concept": [
                                {
                                    "code": "DX",
                                    "concept": [
                                        {
                                            "code": "CVDX",
                                            "concept": [
                                                {
                                                    "code": "CATH",
                                                    "definition": "Cardiac catheterization lab",
                                                    "display": "Cardiac catheterization lab",
                                                },
                                                {
                                                    "code": "ECHO",
                                                    "definition": "Echocardiography lab",
                                                    "display": "Echocardiography lab",
                                                },
                                            ],
                                            "definition": "A practice setting where cardiovascular diagnostic procedures or therapeutic interventions are performed (e.g., cardiac catheterization lab, echocardiography suite)",
                                            "display": "Cardiovascular diagnostics or therapeutics unit",
                                        },
                                        {
                                            "code": "GIDX",
                                            "concept": [
                                                {
                                                    "code": "ENDOS",
                                                    "definition": "(X12N 261QD0000N)",
                                                    "display": "Endoscopy lab",
                                                }
                                            ],
                                            "definition": "A practice setting where GI procedures (such as endoscopies) are performed",
                                            "display": "Gastroenterology diagnostics or therapeutics lab",
                                        },
                                        {
                                            "code": "RADDX",
                                            "concept": [
                                                {
                                                    "code": "RADO",
                                                    "definition": "(X12N 261QX0203N)",
                                                    "display": "Radiation oncology unit",
                                                },
                                                {
                                                    "code": "RNEU",
                                                    "definition": "Neuroradiology unit",
                                                    "display": "Neuroradiology unit",
                                                },
                                            ],
                                            "definition": "A practice setting where radiology services (diagnostic or therapeutic) are provided            (X12N 261QR0200N)",
                                            "display": "Radiology diagnostics or therapeutics unit",
                                        },
                                    ],
                                    "definition": "A practice setting where diagnostic procedures or therapeutic interventions are performed",
                                    "display": "Diagnostics or therapeutics unit",
                                },
                                {
                                    "code": "HOSP",
                                    "concept": [
                                        {
                                            "code": "CHR",
                                            "definition": "(1) A hospital including a physical plant and personnel that provides multidisciplinary diagnosis and treatment for diseases that have one or more of the following characteristics: is permanent; leaves residual disability; is caused by nonreversible pathological alteration; requires special training of the patient for rehabilitation; and/or may be expected to require a long period of supervision or care. In addition, patients require the safety, security, and shelter of these specialized inpatient or partial hospitalization settings. (2) A hospital that provides medical and skilled nursing services to patients with long-term illnesses who are not in an acute phase but who require an intensity of services not available in nursing homes",
                                            "display": "Chronic Care Facility",
                                        },
                                        {
                                            "code": "GACH",
                                            "definition": "(X12N 282N00000N)",
                                            "display": "Hospitals; General Acute Care Hospital",
                                        },
                                        {
                                            "code": "MHSP",
                                            "definition": "A health care facility operated by the Department of Defense or other military operation.",
                                            "display": "Military Hospital",
                                        },
                                        {
                                            "code": "PSYCHF",
                                            "definition": "Healthcare facility that cares for patients with psychiatric illness(s).",
                                            "display": "Psychatric Care Facility",
                                        },
                                        {
                                            "code": "RH",
                                            "concept": [
                                                {
                                                    "code": "RHAT",
                                                    "definition": "Description: A location that plays the role of delivering services which may include life training and/or social support to people with addictions.",
                                                    "display": "addiction treatment center",
                                                },
                                                {
                                                    "code": "RHII",
                                                    "definition": "Description: A location that plays the role of delivering services which may include adaptation, rehabilitation and social integration services for people with intellectual and/or pervasive development disorders such as autism or severe behaviour disorder.",
                                                    "display": "intellectual impairment center",
                                                },
                                                {
                                                    "code": "RHMAD",
                                                    "definition": "Description: A location that plays the role of delivering services which may social support services for adolescents who are pregnant or have child and are experiencing adaptation issues/difficulties in their current or eventual parenting role.",
                                                    "display": "parents with adjustment difficulties center",
                                                },
                                                {
                                                    "code": "RHPI",
                                                    "concept": [
                                                        {
                                                            "code": "RHPIH",
                                                            "definition": "Description: A location that plays the role of delivering services for people with hearing impairments.",
                                                            "display": "physical impairment - hearing center",
                                                        },
                                                        {
                                                            "code": "RHPIMS",
                                                            "definition": "Description: A location that plays the role of delivering services for people with motor skill impairments.",
                                                            "display": "physical impairment - motor skills center",
                                                        },
                                                        {
                                                            "code": "RHPIVS",
                                                            "definition": "Description: A location that plays the role of delivering services for people with visual skill impairments.",
                                                            "display": "physical impairment - visual skills center",
                                                        },
                                                    ],
                                                    "definition": "Description: A location that plays the role of delivering services which may include adaptation, rehabilitation and social integration services for people with physical impairments.",
                                                    "display": "physical impairment center",
                                                },
                                                {
                                                    "code": "RHYAD",
                                                    "definition": "Description: A location that plays the role of delivering services which may include life training and/or social support services for the adaption, rehabilitation and social integration of youths with adjustment difficulties.",
                                                    "display": "youths with adjustment difficulties center",
                                                },
                                            ],
                                            "definition": "(X12N 283X00000N)",
                                            "display": "Rehabilitation hospital",
                                        },
                                    ],
                                    "definition": "An acute care institution that provides medical, surgical, or psychiatric care and treatment for the sick or the injured.",
                                    "display": "Hospital",
                                },
                                {
                                    "code": "HU",
                                    "concept": [
                                        {
                                            "code": "BMTU",
                                            "definition": "Bone marrow transplant unit",
                                            "display": "Bone marrow transplant unit",
                                        },
                                        {
                                            "code": "CCU",
                                            "definition": "Coronary care unit",
                                            "display": "Coronary care unit",
                                        },
                                        {
                                            "code": "CHEST",
                                            "definition": "A specialty unit in hospital that focuses on chronic respirator patients and pulmonary failure",
                                            "display": "Chest unit",
                                        },
                                        {
                                            "code": "EPIL",
                                            "definition": "Epilepsy unit",
                                            "display": "Epilepsy unit",
                                        },
                                        {
                                            "code": "ER",
                                            "concept": [
                                                {
                                                    "code": "ETU",
                                                    "definition": "Emergency trauma unit",
                                                    "display": "Emergency trauma unit",
                                                }
                                            ],
                                            "definition": "The section of a health care facility for providing rapid treatment to victims of sudden illness or trauma.",
                                            "display": "Emergency room",
                                        },
                                        {
                                            "code": "HD",
                                            "definition": "Hemodialysis unit",
                                            "display": "Hemodialysis unit",
                                        },
                                        {
                                            "code": "HLAB",
                                            "concept": [
                                                {
                                                    "code": "INLAB",
                                                    "definition": "Description: A location that plays the role of delivering services which may include tests are done on clinical specimens to get health information about a patient pertaining to the diagnosis, treatment, and prevention of disease for a hospital visit longer than one day.",
                                                    "display": "inpatient laboratory",
                                                },
                                                {
                                                    "code": "OUTLAB",
                                                    "definition": "Description: A location that plays the role of delivering services which may include tests are done on clinical specimens to get health information about a patient pertaining to the diagnosis, treatment, and prevention of disease for same day visits.",
                                                    "display": "outpatient laboratory",
                                                },
                                            ],
                                            "definition": "Description: A location that plays the role of delivering services which may include tests done based on clinical specimens to get health information about a patient as pertaining to the diagnosis, treatment and prevention of disease.  Hospital laboratories may be further divided into specialized units such as Anatomic Pathology, Microbiology, and Biochemistry.",
                                            "display": "hospital laboratory",
                                        },
                                        {
                                            "code": "HRAD",
                                            "definition": "Description: A location that plays the role of delivering services which may include the branch of medicine that uses ionizing and non-ionizing radiation to diagnose and treat diseases.  The radiology unit may be further divided into subspecialties such as Imaging, Cardiovascular, Thoracic, and Ultrasound.",
                                            "display": "radiology unit",
                                        },
                                        {
                                            "code": "HUSCS",
                                            "definition": "Description: A location that plays the role of delivering services which may include collecting specimens and/or samples from patients for laboratory testing purposes, but does not perform any tests or analysis functions.",
                                            "display": "specimen collection site",
                                        },
                                        {
                                            "code": "ICU",
                                            "concept": [
                                                {
                                                    "code": "PEDICU",
                                                    "concept": [
                                                        {
                                                            "code": "PEDNICU",
                                                            "definition": "Pediatric neonatal intensive care unit",
                                                            "display": "Pediatric neonatal intensive care unit",
                                                        }
                                                    ],
                                                    "definition": "Pediatric intensive care unit",
                                                    "display": "Pediatric intensive care unit",
                                                }
                                            ],
                                            "definition": "Intensive care unit",
                                            "display": "Intensive care unit",
                                        },
                                        {
                                            "code": "INPHARM",
                                            "definition": "Description: A location that plays the role of delivering services which may include providing judicious, safe, efficacious, appropriate and cost effective use of medicines for treatment of patients for visits longer than one day. The distinction between inpatient pharmacies and retail (or outpatient) pharmacies is that they are part of a patient's continuity of care while staying in the hospital.",
                                            "display": "inpatient pharmacy",
                                        },
                                        {
                                            "code": "MBL",
                                            "definition": "Description: A location that plays the role of delivering services which include biochemistry, hematology, microbiology, immunochemistry, and toxicology.",
                                            "display": "medical laboratory",
                                        },
                                        {
                                            "code": "NCCS",
                                            "definition": "Neurology critical care and stroke unit",
                                            "display": "Neurology critical care and stroke unit",
                                        },
                                        {
                                            "code": "NS",
                                            "definition": "Neurosurgery unit",
                                            "display": "Neurosurgery unit",
                                        },
                                        {
                                            "code": "OUTPHARM",
                                            "definition": "Description: A location that plays the role of delivering services which may include providing judicious, safe, efficacious, appropriate and cost effective use of medicines for treatment of patients for outpatient visits and may also be used for discharge prescriptions.",
                                            "display": "outpatient pharmacy",
                                        },
                                        {
                                            "code": "PEDU",
                                            "definition": "Pediatric unit",
                                            "display": "Pediatric unit",
                                            "property": [
                                                {"code": "child", "valueCode": "PEDICU"}
                                            ],
                                        },
                                        {
                                            "code": "PHU",
                                            "definition": "(X12N 273R00000N)",
                                            "display": "Psychiatric hospital unit",
                                        },
                                        {
                                            "code": "RHU",
                                            "definition": "Rehabilitation hospital unit",
                                            "display": "Rehabilitation hospital unit",
                                        },
                                        {
                                            "code": "SLEEP",
                                            "definition": "(X12N 261QA1200N)",
                                            "display": "Sleep disorders unit",
                                        },
                                    ],
                                    "definition": "Hospital unit",
                                    "display": "Hospital unit",
                                },
                                {
                                    "code": "NCCF",
                                    "concept": [
                                        {
                                            "code": "SNF",
                                            "definition": "(X12N 314000000N)",
                                            "display": "Skilled nursing facility",
                                        }
                                    ],
                                    "definition": "Nursing or custodial care facility",
                                    "display": "Nursing or custodial care facility",
                                },
                                {
                                    "code": "OF",
                                    "concept": [
                                        {
                                            "code": "ALL",
                                            "definition": "Allergy clinic",
                                            "display": "Allergy clinic",
                                        },
                                        {
                                            "code": "AMPUT",
                                            "definition": "Amputee clinic",
                                            "display": "Amputee clinic",
                                        },
                                        {
                                            "code": "BMTC",
                                            "definition": "Bone marrow transplant clinic",
                                            "display": "Bone marrow transplant clinic",
                                        },
                                        {
                                            "code": "BREAST",
                                            "definition": "Breast clinic",
                                            "display": "Breast clinic",
                                        },
                                        {
                                            "code": "CANC",
                                            "definition": "Child and adolescent neurology clinic",
                                            "display": "Child and adolescent neurology clinic",
                                        },
                                        {
                                            "code": "CAPC",
                                            "definition": "Child and adolescent psychiatry clinic",
                                            "display": "Child and adolescent psychiatry clinic",
                                        },
                                        {
                                            "code": "CARD",
                                            "concept": [
                                                {
                                                    "code": "PEDCARD",
                                                    "definition": "Pediatric cardiology clinic",
                                                    "display": "Pediatric cardiology clinic",
                                                }
                                            ],
                                            "definition": "Ambulatory Health Care Facilities; Clinic/Center; Rehabilitation: Cardiac Facilities",
                                            "display": "Ambulatory Health Care Facilities; Clinic/Center; Rehabilitation: Cardiac Facilities",
                                        },
                                        {
                                            "code": "COAG",
                                            "definition": "Coagulation clinic",
                                            "display": "Coagulation clinic",
                                        },
                                        {
                                            "code": "CRS",
                                            "definition": "Colon and rectal surgery clinic",
                                            "display": "Colon and rectal surgery clinic",
                                        },
                                        {
                                            "code": "DERM",
                                            "definition": "Dermatology clinic",
                                            "display": "Dermatology clinic",
                                        },
                                        {
                                            "code": "ENDO",
                                            "concept": [
                                                {
                                                    "code": "PEDE",
                                                    "definition": "Pediatric endocrinology clinic",
                                                    "display": "Pediatric endocrinology clinic",
                                                }
                                            ],
                                            "definition": "Endocrinology clinic",
                                            "display": "Endocrinology clinic",
                                        },
                                        {
                                            "code": "ENT",
                                            "definition": "Otorhinolaryngology clinic",
                                            "display": "Otorhinolaryngology clinic",
                                        },
                                        {
                                            "code": "FMC",
                                            "definition": "Family medicine clinic",
                                            "display": "Family medicine clinic",
                                        },
                                        {
                                            "code": "GI",
                                            "concept": [
                                                {
                                                    "code": "PEDGI",
                                                    "definition": "Pediatric gastroenterology clinic",
                                                    "display": "Pediatric gastroenterology clinic",
                                                }
                                            ],
                                            "definition": "Gastroenterology clinic",
                                            "display": "Gastroenterology clinic",
                                        },
                                        {
                                            "code": "GIM",
                                            "definition": "General internal medicine clinic",
                                            "display": "General internal medicine clinic",
                                        },
                                        {
                                            "code": "GYN",
                                            "definition": "Gynecology clinic",
                                            "display": "Gynecology clinic",
                                        },
                                        {
                                            "code": "HEM",
                                            "concept": [
                                                {
                                                    "code": "PEDHEM",
                                                    "definition": "Pediatric hematology clinic",
                                                    "display": "Pediatric hematology clinic",
                                                }
                                            ],
                                            "definition": "Hematology clinic",
                                            "display": "Hematology clinic",
                                        },
                                        {
                                            "code": "HTN",
                                            "definition": "Hypertension clinic",
                                            "display": "Hypertension clinic",
                                        },
                                        {
                                            "code": "IEC",
                                            "definition": "Focuses on assessing disability",
                                            "display": "Impairment evaluation center",
                                        },
                                        {
                                            "code": "INFD",
                                            "concept": [
                                                {
                                                    "code": "PEDID",
                                                    "definition": "Pediatric infectious disease clinic",
                                                    "display": "Pediatric infectious disease clinic",
                                                }
                                            ],
                                            "definition": "Infectious disease clinic",
                                            "display": "Infectious disease clinic",
                                        },
                                        {
                                            "code": "INV",
                                            "definition": "Infertility clinic",
                                            "display": "Infertility clinic",
                                        },
                                        {
                                            "code": "LYMPH",
                                            "definition": "Lympedema clinic",
                                            "display": "Lympedema clinic",
                                        },
                                        {
                                            "code": "MGEN",
                                            "definition": "Medical genetics clinic",
                                            "display": "Medical genetics clinic",
                                        },
                                        {
                                            "code": "NEPH",
                                            "concept": [
                                                {
                                                    "code": "PEDNEPH",
                                                    "definition": "Pediatric nephrology clinic",
                                                    "display": "Pediatric nephrology clinic",
                                                }
                                            ],
                                            "definition": "Nephrology clinic",
                                            "display": "Nephrology clinic",
                                        },
                                        {
                                            "code": "NEUR",
                                            "definition": "Neurology clinic",
                                            "display": "Neurology clinic",
                                        },
                                        {
                                            "code": "OB",
                                            "definition": "Obstetrics clinic",
                                            "display": "Obstetrics clinic",
                                        },
                                        {
                                            "code": "OMS",
                                            "definition": "Oral and maxillofacial surgery clinic",
                                            "display": "Oral and maxillofacial surgery clinic",
                                        },
                                        {
                                            "code": "ONCL",
                                            "concept": [
                                                {
                                                    "code": "PEDHO",
                                                    "definition": "Pediatric oncology clinic",
                                                    "display": "Pediatric oncology clinic",
                                                }
                                            ],
                                            "definition": "Medical oncology clinic",
                                            "display": "Medical oncology clinic",
                                        },
                                        {
                                            "code": "OPH",
                                            "definition": "Opthalmology clinic",
                                            "display": "Opthalmology clinic",
                                        },
                                        {
                                            "code": "OPTC",
                                            "definition": "Description: A location that plays the role of delivering services which may include examination, diagnosis, treatment, management, and prevention of diseases and disorders of the eye as well as prescribing and fitting appropriate corrective lenses (glasses or contact lenses) as needed.  Optometry clinics may also provide tests for visual field screening, measuring intra-ocular pressure and ophthalmoscopy, as and when required.",
                                            "display": "optometry clinic",
                                        },
                                        {
                                            "code": "ORTHO",
                                            "concept": [
                                                {
                                                    "code": "HAND",
                                                    "definition": "Hand clinic",
                                                    "display": "Hand clinic",
                                                }
                                            ],
                                            "definition": "Orthopedics clinic",
                                            "display": "Orthopedics clinic",
                                        },
                                        {
                                            "code": "PAINCL",
                                            "definition": "(X12N 261QP3300N)",
                                            "display": "Pain clinic",
                                        },
                                        {
                                            "code": "PC",
                                            "definition": "(X12N 261QP2300N)",
                                            "display": "Primary care clinic",
                                        },
                                        {
                                            "code": "PEDC",
                                            "concept": [
                                                {
                                                    "code": "PEDRHEUM",
                                                    "definition": "Pediatric rheumatology clinic",
                                                    "display": "Pediatric rheumatology clinic",
                                                }
                                            ],
                                            "definition": "Pediatrics clinic",
                                            "display": "Pediatrics clinic",
                                            "property": [
                                                {
                                                    "code": "child",
                                                    "valueCode": "PEDCARD",
                                                },
                                                {"code": "child", "valueCode": "PEDE"},
                                                {"code": "child", "valueCode": "PEDGI"},
                                                {
                                                    "code": "child",
                                                    "valueCode": "PEDHEM",
                                                },
                                                {"code": "child", "valueCode": "PEDID"},
                                                {
                                                    "code": "child",
                                                    "valueCode": "PEDNEPH",
                                                },
                                                {"code": "child", "valueCode": "PEDHO"},
                                            ],
                                        },
                                        {
                                            "code": "POD",
                                            "definition": "(X12N 261QP1100N)",
                                            "display": "Podiatry clinic",
                                        },
                                        {
                                            "code": "PREV",
                                            "definition": "Preventive medicine clinic",
                                            "display": "Preventive medicine clinic",
                                        },
                                        {
                                            "code": "PROCTO",
                                            "definition": "Proctology clinic",
                                            "display": "Proctology clinic",
                                        },
                                        {
                                            "code": "PROFF",
                                            "definition": "Location where healthcare service was delivered, identified as the healthcare provider's practice office.",
                                            "display": "Provider's Office",
                                        },
                                        {
                                            "code": "PROS",
                                            "definition": "Prosthodontics clinic",
                                            "display": "Prosthodontics clinic",
                                        },
                                        {
                                            "code": "PSI",
                                            "definition": "Psychology clinic",
                                            "display": "Psychology clinic",
                                        },
                                        {
                                            "code": "PSY",
                                            "definition": "Psychiatry clinic",
                                            "display": "Psychiatry clinic",
                                        },
                                        {
                                            "code": "RHEUM",
                                            "definition": "Rheumatology clinic",
                                            "display": "Rheumatology clinic",
                                            "property": [
                                                {
                                                    "code": "child",
                                                    "valueCode": "PEDRHEUM",
                                                }
                                            ],
                                        },
                                        {
                                            "code": "SPMED",
                                            "definition": "Sports medicine clinic",
                                            "display": "Sports medicine clinic",
                                        },
                                        {
                                            "code": "SU",
                                            "concept": [
                                                {
                                                    "code": "PLS",
                                                    "definition": "Plastic surgery clinic",
                                                    "display": "Plastic surgery clinic",
                                                },
                                                {
                                                    "code": "URO",
                                                    "definition": "Urology clinic",
                                                    "display": "Urology clinic",
                                                },
                                            ],
                                            "definition": "Surgery clinic",
                                            "display": "Surgery clinic",
                                        },
                                        {
                                            "code": "TR",
                                            "definition": "Transplant clinic",
                                            "display": "Transplant clinic",
                                        },
                                        {
                                            "code": "TRAVEL",
                                            "definition": "Travel and geographic medicine clinic",
                                            "display": "Travel and geographic medicine clinic",
                                        },
                                        {
                                            "code": "WND",
                                            "definition": "Wound clinic",
                                            "display": "Wound clinic",
                                        },
                                    ],
                                    "definition": "Outpatient facility",
                                    "display": "Outpatient facility",
                                },
                                {
                                    "code": "RTF",
                                    "concept": [
                                        {
                                            "code": "PRC",
                                            "definition": "Pain rehabilitation center",
                                            "display": "Pain rehabilitation center",
                                        },
                                        {
                                            "code": "SURF",
                                            "definition": "(X12N 324500000N)",
                                            "display": "Substance use rehabilitation facility",
                                        },
                                    ],
                                    "definition": "Residential treatment facility",
                                    "display": "Residential treatment facility",
                                },
                            ],
                            "definition": "A role of a place that further classifies the clinical setting (e.g., cardiology clinic, primary care clinic, rehabilitation hospital, skilled nursing facility) in which care is delivered during an encounter.",
                            "display": "DedicatedClinicalLocationRoleType",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_DedicatedNonClinicalLocationRoleType",
                            "concept": [
                                {
                                    "code": "DADDR",
                                    "definition": "Location address where medical supplies were transported to for use.",
                                    "display": "Delivery Address",
                                },
                                {
                                    "code": "MOBL",
                                    "concept": [
                                        {
                                            "code": "AMB",
                                            "definition": "Location (mobile) where healthcare service was delivered, identified specifically as an ambulance.",
                                            "display": "Ambulance",
                                        }
                                    ],
                                    "definition": "Location (mobile) where healthcare service was delivered.",
                                    "display": "Mobile Unit",
                                },
                                {
                                    "code": "PHARM",
                                    "definition": "Location where healthcare service was delivered, identified as a pharmacy.",
                                    "display": "Pharmacy",
                                    "property": [
                                        {"code": "child", "valueCode": "INPHARM"},
                                        {"code": "child", "valueCode": "OUTPHARM"},
                                    ],
                                },
                            ],
                            "definition": "A role of a place that further classifies a setting that is intended to house the provision of non-clinical services.",
                            "display": "DedicatedNonClinicalLocationRoleType",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                    ],
                    "definition": "A role of a place that further classifies a setting that is intended to house the provision of services.",
                    "display": "DedicatedServiceDeliveryLocationRoleType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_IncidentalServiceDeliveryLocationRoleType",
                    "concept": [
                        {
                            "code": "ACC",
                            "definition": "Location of an accident where healthcare service was delivered, such as a roadside.",
                            "display": "accident site",
                        },
                        {
                            "code": "COMM",
                            "concept": [
                                {
                                    "code": "CSC",
                                    "definition": "Description: A location that plays the role of delivering services which may include providing front-line services to the population of a defined geographic area such as: healthcare services and social services, preventive or curative, rehabilitation or reintegration.",
                                    "display": "community service center",
                                }
                            ],
                            "definition": "Community location where healthcare is delivered.",
                            "display": "Community Location",
                        },
                        {
                            "code": "PTRES",
                            "definition": "location where healthcare was delivered which is the residence of the Patient.",
                            "display": "Patient's Residence",
                        },
                        {
                            "code": "SCHOOL",
                            "definition": "Location where healthcare service was delivered, identified as a school or educational facility.",
                            "display": "school",
                        },
                        {
                            "code": "UPC",
                            "definition": "Description: A location that plays the role of delivering services which may include: social emergency services required for a young person as required under any jurisdictional youth laws, child placement, and family mediation in the defined geographical area the SDL is responsible for. It may provide expertise in a judiciary setting on child custody, adoption and biological history research.",
                            "display": "underage protection center",
                        },
                        {
                            "code": "WORK",
                            "definition": "Location where healthcare service was delivered, identified as a work place.",
                            "display": "work site",
                        },
                    ],
                    "definition": "IncidentalServiceDeliveryLocationRoleType",
                    "display": "IncidentalServiceDeliveryLocationRoleType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": "A role of a place that further classifies the setting (e.g., accident site, road side, work site, community location) in which services are delivered.",
            "display": "ServiceDeliveryLocationRoleType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ServiceDeliveryLocationRoleType

    A role of a place that further classifies the setting (e.g., accident site, road side, work site, community location) in which services are delivered.
    """

    underscore_specimen_role_type = CodeSystemConcept(
        {
            "code": "_SpecimenRoleType",
            "concept": [
                {
                    "code": "C",
                    "definition": "A specimen used for initial calibration settings of an instrument",
                    "display": "Calibrator",
                },
                {
                    "code": "G",
                    "definition": "A set of patient samples in which the individuals of the group may or may not be identified.",
                    "display": "Group",
                },
                {
                    "code": "L",
                    "definition": "Aliquots of individual specimens combined to form a single specimen representing all of the included individuals.",
                    "display": "Pool",
                },
                {
                    "code": "P",
                    "definition": "A specimen that has been collected from a patient.",
                    "display": "Patient",
                },
                {
                    "code": "Q",
                    "concept": [
                        {
                            "code": "B",
                            "definition": "Quality Control specimen submitted to the lab whose identity and composition is not known to the lab.",
                            "display": "Blind",
                        },
                        {
                            "code": "E",
                            "definition": "An electronically simulated QC specimen",
                            "display": "Electronic QC",
                        },
                        {
                            "code": "F",
                            "definition": "Specimen used for testing proficiency of an organization performing testing (how does this differ from O?)",
                            "display": "Filler Proficiency",
                        },
                        {
                            "code": "O",
                            "definition": "A specimen used for evaluation of operator proficiency (operator in what context?)",
                            "display": "Operator Proficiency",
                        },
                        {
                            "code": "V",
                            "definition": "A specimen used for periodic calibration checks of instruments",
                            "display": "Verifying",
                        },
                    ],
                    "definition": "A specimen specifically used to verify the sensitivity, specificity, accuracy or other perfomance parameter of a diagnostic test.",
                    "display": "Quality Control",
                },
                {
                    "code": "R",
                    "definition": "A portion of an original patent sample that is tested at the same time as the original sample",
                    "display": "Replicate",
                },
            ],
            "definition": "SpecimenRoleType",
            "display": "SpecimenRoleType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    SpecimenRoleType

    SpecimenRoleType
    """

    claim = CodeSystemConcept(
        {
            "code": "CLAIM",
            "definition": "A party that makes a claim for coverage under a policy.",
            "display": "claimant",
        }
    )
    """
    claimant

    A party that makes a claim for coverage under a policy.
    """

    community_laboratory = CodeSystemConcept(
        {
            "code": "communityLaboratory",
            "definition": "Community Laboratory",
            "display": "Community Laboratory",
        }
    )
    """
    Community Laboratory

    Community Laboratory
    """

    gt = CodeSystemConcept(
        {
            "code": "GT",
            "definition": "An individual or organization that makes or gives a promise, assurance, pledge to pay or has paid the healthcare service provider.",
            "display": "Guarantor",
        }
    )
    """
    Guarantor

    An individual or organization that makes or gives a promise, assurance, pledge to pay or has paid the healthcare service provider.
    """

    home_health = CodeSystemConcept(
        {"code": "homeHealth", "definition": "Home Health", "display": "Home Health"}
    )
    """
    Home Health

    Home Health
    """

    laboratory = CodeSystemConcept(
        {"code": "laboratory", "definition": "Laboratory", "display": "Laboratory"}
    )
    """
    Laboratory

    Laboratory
    """

    pathologist = CodeSystemConcept(
        {"code": "pathologist", "definition": "Pathologist", "display": "Pathologist"}
    )
    """
    Pathologist

    Pathologist
    """

    ph = CodeSystemConcept(
        {
            "code": "PH",
            "definition": "Policy holder for the insurance policy.",
            "display": "Policy Holder",
        }
    )
    """
    Policy Holder

    Policy holder for the insurance policy.
    """

    phlebotomist = CodeSystemConcept(
        {
            "code": "phlebotomist",
            "definition": "Phlebotomist",
            "display": "Phlebotomist",
        }
    )
    """
    Phlebotomist

    Phlebotomist
    """

    prog = CodeSystemConcept(
        {
            "code": "PROG",
            "definition": "A party that meets the eligibility criteria for coverage under a program.",
            "display": "program eligible",
        }
    )
    """
    program eligible

    A party that meets the eligibility criteria for coverage under a program.
    """

    pt = CodeSystemConcept(
        {
            "code": "PT",
            "definition": "The recipient for the service(s) and/or product(s) when they are not the covered party.",
            "display": "Patient",
        }
    )
    """
    Patient

    The recipient for the service(s) and/or product(s) when they are not the covered party.
    """

    subject = CodeSystemConcept(
        {"code": "subject", "definition": "Self", "display": "Self"}
    )
    """
    Self

    Self
    """

    third_party = CodeSystemConcept(
        {"code": "thirdParty", "definition": "Third Party", "display": "Third Party"}
    )
    """
    Third Party

    Third Party
    """

    dep = CodeSystemConcept(
        {"code": "DEP", "property": [{"code": "status", "valueCode": "retired"}]}
    )
    """
    None

    
    """

    depen = CodeSystemConcept(
        {
            "code": "DEPEN",
            "definition": "A party covered under a policy based on association with a subscriber.",
            "display": "dependent",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    dependent

    A party covered under a policy based on association with a subscriber.
    """

    fm = CodeSystemConcept(
        {
            "code": "FM",
            "definition": "A member of the covered party's family. This could be the spouse, a parent, a grand parent, a sibling, etc.",
            "display": "Family Member",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    Family Member

    A member of the covered party's family. This could be the spouse, a parent, a grand parent, a sibling, etc.
    """

    indiv = CodeSystemConcept(
        {
            "code": "INDIV",
            "definition": "A party covered under a policy as the policyholder.",
            "display": "individual",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    individual

    A party covered under a policy as the policyholder.
    """

    named = CodeSystemConcept(
        {
            "code": "NAMED",
            "definition": "A party to an insurance policy to whom the insurer agrees to indemnify for losses, provides benefits for, or renders services.",
            "display": "named insured",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    named insured

    A party to an insurance policy to whom the insurer agrees to indemnify for losses, provides benefits for, or renders services.
    """

    psychcf = CodeSystemConcept(
        {"code": "PSYCHCF", "property": [{"code": "status", "valueCode": "retired"}]}
    )
    """
    None

    
    """

    subscr = CodeSystemConcept(
        {
            "code": "SUBSCR",
            "definition": "A party covered under a policy based on association with a sponsor who is the policy holder, and whose association may provide for the eligibility of dependents for coverage",
            "display": "subscriber",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    subscriber

    A party covered under a policy based on association with a sponsor who is the policy holder, and whose association may provide for the eligibility of dependents for coverage
    """

    class Meta:
        resource = _resource
