from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3RoleClass"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3RoleClass:
    """
    v3 Code System RoleClass

     Codes for the Role class hierarchy.  The values in this hierarchy,
represent a Role which is an association or relationship between two
entities - the entity that plays the role and the entity that scopes the
role.  Roles names are derived from the name of the playing entity in
that role. The role hierarchy stems from three core concepts, or
abstract domains:    RoleClassOntological  is an abstract domain that
collects roles in which the playing entity is defined or specified by
the scoping entity.   RoleClassPartitive  collects roles in which the
playing entity is in some sense a "part" of the scoping entity.
RoleClassAssociative  collects all of the remaining forms of association
between the playing entity and the scoping entity. This set of roles is
further partitioned between:    RoleClassPassive  which are roles in
which the playing entity is used, known, treated, handled, built, or
destroyed, etc. under the auspices of the scoping entity. The playing
entity is passive in these roles in that the role exists without an
agreement from the playing entity.   RoleClassMutualRelationship  which
are relationships based on mutual behavior of the two entities. The
basis of these relationship may be formal agreements or they may bede
facto  behavior.  Thus, this sub-domain is further divided into:
RoleClassRelationshipFormal  in which the relationship is formally
defined, frequently by a contract or agreement.   Personal relationship
which inks two people in a personal relationship. The hierarchy
discussed above is represented In the current vocabulary tables as a set
of abstract domains, with the exception of the  "Personal relationship"
which is a leaf concept.  OpenIssue:  Description copied from Concept
Domain of same name.  Must be verified.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-RoleClass
    """

    rol = CodeSystemConcept(
        {
            "code": "ROL",
            "concept": [
                {
                    "code": "_RoleClassAssociative",
                    "concept": [
                        {
                            "code": "_RoleClassMutualRelationship",
                            "concept": [
                                {
                                    "code": "_RoleClassRelationshipFormal",
                                    "concept": [
                                        {
                                            "code": "AFFL",
                                            "definition": "Player of the Affiliate role has a business/professional relationship with scoper.  Player and scoper may be persons or organization.  The Affiliate relationship does not imply membership in a group, nor does it exist for resource scheduling purposes.\r\n\n                        \n                           Example: A healthcare provider is affiliated with another provider as a business associate.",
                                            "display": "affiliate",
                                        },
                                        {
                                            "code": "AGNT",
                                            "concept": [
                                                {
                                                    "code": "ASSIGNED",
                                                    "concept": [
                                                        {
                                                            "code": "COMPAR",
                                                            "definition": "An Entity that is authorized to issue or instantiate permissions, privileges, credentials or other formal/legal authorizations.",
                                                            "display": "commissioning party",
                                                        },
                                                        {
                                                            "code": "SGNOFF",
                                                            "definition": "The role of a person (player) who is the officer or signature authority for of a scoping entity, usually an organization (scoper).",
                                                            "display": "signing authority or officer",
                                                        },
                                                    ],
                                                    "definition": "An agent role in which the agent is an Entity acting in the employ of an organization.  The focus is on functional role on behalf of the organization, unlike the Employee role where the focus is on the 'Human Resources' relationship between the employee and the organization.",
                                                    "display": "assigned entity",
                                                },
                                                {
                                                    "code": "CON",
                                                    "concept": [
                                                        {
                                                            "code": "ECON",
                                                            "definition": "An entity to be contacted in the event of an emergency.",
                                                            "display": "emergency contact",
                                                        },
                                                        {
                                                            "code": "NOK",
                                                            "definition": "An individual designated for notification as the next of kin for a given entity.",
                                                            "display": "next of kin",
                                                        },
                                                    ],
                                                    "definition": "A person or an organization (player) which provides or receives information regarding another entity (scoper).  Examples; patient NOK and emergency contacts; guarantor contact; employer contact.",
                                                    "display": "contact",
                                                },
                                                {
                                                    "code": "GUARD",
                                                    "definition": "Guardian of a ward",
                                                    "display": "guardian",
                                                },
                                            ],
                                            "definition": "An entity (player) that acts or is authorized to act on behalf of another entity (scoper).",
                                            "display": "agent",
                                        },
                                        {
                                            "code": "CIT",
                                            "definition": "Citizen of apolitical entity",
                                            "display": "citizen",
                                        },
                                        {
                                            "code": "COVPTY",
                                            "concept": [
                                                {
                                                    "code": "CLAIM",
                                                    "definition": 'Description: A role played by a party making a claim for coverage under a policy or program.  A claimant must be either a person or organization, or a group of persons or organizations.  A claimant is not a named insured or a program eligible.\r\n\n                        \n                           Discussion: With respect to liability insurance such as property and casualty insurance, a claimant must file a claim requesting indemnification for a loss that the claimant considers covered under the policy of a named insured.  The claims adjuster for the policy underwriter will review the claim to determine whether the loss meets the benefit coverage criteria under a policy, and base any indemnification or coverage payment on that review.  If a third party is liable in whole or part for the loss, the underwriter may pursue third party liability recovery.  A claimant may be involved in civil or criminal legal proceedings involving claims against a defendant party that is indemnified by an insurance policy or to protest the finding of a claims adjustor. With respect to life insurance, a beneficiary designated by a named insured becomes a claimant of the proceeds of coverage, as in the case of a life insurance policy.  However, a claimant for coverage under life insurance is not necessarily a designated beneficiary.\r\n\n                        \n                           Note: A claimant is not a named insured.  However, a named insured may make a claim under a policy, e.g., an insured driver may make a claim for an injury under his or her comprehensive automobile insurance policy.  Similarly, a program eligible may make a claim under program, e.g., an unemployed worker may claim benefits under an unemployment insurance program, but parties playing these covered party role classes are not, for purposes of this vocabulary and in an effort to clearly distinguish role classes, considered claimants.\r\n\n                        In the case of a named insured making a claim, a role type code INSCLM (insured claimant) subtypes the class to indicate that either a named insured or an individual insured has filed a claim for a loss.  In the case of a program eligible, a role type code INJWKR (injured worker) subtypes the class to indicate that the covered party in a workers compensation program is an injured worker, and as such, has filed a "claim" under the program for benefits.  Likewise, a covered role type code UNEMP (unemployed worker) subtypes the program eligible class to indicate that the covered party in an unemployment insurance program has filed a claim for unemployment benefits.\r\n\n                        \n                           Example: A claimant under automobile policy that is not the named insured.',
                                                    "display": "claimant",
                                                },
                                                {
                                                    "code": "NAMED",
                                                    "concept": [
                                                        {
                                                            "code": "DEPEN",
                                                            "definition": "Description: A role played by a person covered under a policy or program based on an association with a subscriber, which is recognized by the policy holder.\r\n\n                        \n                           Note:  The party playing the role of a dependent is not a claimant in the sense conveyed by the RoleClassCoveredParty CLAIM (claimant).  However, a dependent may make a claim under a policy, e.g., a dependent under a health insurance policy may become the claimant for coverage under that policy for wellness examines or if injured and there is no liable third party.  In the case of a dependent making a claim, a role type code INSCLM (insured claimant) subtypes the class to indicate that the dependent has filed a claim for services covered under the health insurance policy.\r\n\n                        \n                           Example: The dependent has an association with the subscriber such as a financial dependency or personal relationship such as that of a spouse, or a natural or adopted child.  The policy holder may be required by law to recognize certain associations or may have discretion about the associations.  For example, a policy holder may dictate the criteria for the dependent status of adult children who are students, such as requiring full time enrollment, or may recognize domestic partners as dependents.  Under certain circumstances, the dependent may be under the indirect authority of a responsible party acting as a surrogate for the subscriber, for example, if the subscriber is differently abled or deceased, a guardian ad Lidem or estate executor may be appointed to assume the subscriberaTMs legal standing in the relationship with the dependent.",
                                                            "display": "dependent",
                                                        },
                                                        {
                                                            "code": "INDIV",
                                                            "definition": "Description: A role played by a party covered under a policy as the policy holder.  An individual may be either a person or an organization.\r\n\n                        \n                           Note: The party playing the role of an individual insured is not a claimant in the sense conveyed by the RoleClassCoveredParty CLAIM (claimant).  However, a named insured may make a claim under a policy, e.g., a party that is the named insured and policy holder under a comprehensive automobile insurance policy may become the claimant for coverage under that policy if injured in an automobile accident and there is no liable third party.  In the case of an individual insured making a claim, a role type code INSCLM (insured claimant) subtypes the class to indicate that an individual insured has filed a claim for a loss.\r\n\n                        \n                           Example: The individual insured under a comprehensive automobile, disability, or property and casualty policy that is the policy holder.",
                                                            "display": "individual",
                                                        },
                                                        {
                                                            "code": "SUBSCR",
                                                            "definition": "Description: A role played by a person covered under a policy based on association with a sponsor who is the policy holder, and whose association may provide for the eligibility of dependents for coverage.\r\n\n                        \n                           Discussion: The policy holder holds the contract with the policy or program underwriter.  The subscriber holds a certificate of coverage under the contract.  In legal proceedings concerning the policy or program, the terms of the contract takes precedence over the terms of the certificate of coverage if there are any inconsistencies.\r\n\n                        \n                           Note: The party playing the role of a subscriber is not a claimant in the sense conveyed by the RoleClassCoveredParty CLAIM (claimant).  However, a subscriber may make a claim under a policy, e.g., a subscriber under a health insurance policy may become the claimant for coverage under that policy for wellness examines or if injured and there is no liable third party.  In the case of a subscriber making a claim, a role type code INSCLM (insured claimant) subtypes the class to indicate that the subscriber has filed a claim for services covered under the health insurance policy.\r\n\n                        \n                           Example: An employee or a member of an association.",
                                                            "display": "subscriber",
                                                        },
                                                    ],
                                                    "definition": "Description: A role played by a party to an insurance policy to which the insurer agrees to indemnify for losses, provides benefits for, or renders services.  A named insured may be either a person, non-person living subject, or an organization, or a group of persons, non-person living subjects, or organizations.\r\n\n                        \n                           Discussion: The coded concept NAMED should not be used where a more specific child concept in this Specializable value set applies.  In some cases, the named insured may not be the policy holder, e.g., where a policy holder purchases life insurance policy in which another party is the named insured and the policy holder is the beneficiary of the policy.\r\n\n                        \n                           Note: The party playing the role of a named insured is not a claimant in the sense conveyed by the RoleClassCoveredParty CLAIM (claimant).  However, a named insured may make a claim under a policy, e.g., e.g., a party that is the named insured and policy holder under a comprehensive automobile insurance policy may become the claimant for coverage under that policy e.g., if injured in an automobile accident and there is no liable third party.  In the case of a named insured making a claim, a role type code INSCLM (insured claimant) subtypes the class to indicate that a named insured has filed a claim for a loss.\r\n\n                        \n                           Example: The named insured under a comprehensive automobile, disability, or property and casualty policy that is the named insured and may or may not be the policy holder.",
                                                    "display": "named insured",
                                                },
                                                {
                                                    "code": "PROG",
                                                    "definition": 'Description: A role played by a party that meets the eligibility criteria for coverage under a program.  A program eligible may be either a person, non-person living subject, or an organization, or a group of persons, non-person living subjects, or organizations.\r\n\n                        \n                           Discussion: A program as typically government administered coverage for parties determined eligible under the terms of the program.\r\n\n                        \n                           Note: The party playing a program eligible is not a claimant in the sense conveyed by the RoleClassCoveredParty CLAIM (claimant).  However a program eligible may make a claim under program, e.g., an unemployed worker may claim benefits under an unemployment insurance program, but parties playing these covered party role classes are not, for purposes of this vocabulary and in an effort to clearly distinguish role classes, considered claimants.\r\n\n                        In the case of a program eligible, a role type code INJWKR (injured worker) subtypes the class to indicate that the covered party in a workers compensation program is an injured worker, and as such, has filed a "claim" under the program for benefits.  Likewise, a covered role type code UNEMP (unemployed worker) subtypes the program eligible class to indicate that the covered party in an unemployment insurance program has filed a claim for unemployment benefits.\r\n\n                        \n                           Example: A party meeting eligibility criteria related to health or financial status, e.g., in the U.S., persons meeting health, demographic, or financial criteria established by state and federal law are eligible for Medicaid.',
                                                    "display": "program eligible",
                                                },
                                            ],
                                            "definition": "A role class played by a person who receives benefit coverage under the terms of a particular insurance policy.  The underwriter of that policy is the scoping entity.  The covered party receives coverage because of some contractual or other relationship with the holder of that policy.\r\n\n                        \n                           Discussion:This reason for coverage is captured in 'Role.code' and a relationship link with type code of indirect authority should be included using the policy holder role as the source, and the covered party role as the target.\r\n\n                        Note that a particular policy may cover several individuals one of whom may be, but need not be, the policy holder.  Thus the notion of covered party is a role that is distinct from that of the policy holder.",
                                            "display": "covered party",
                                        },
                                        {
                                            "code": "CRINV",
                                            "definition": "A role played by a provider, always a person, who has agency authority from a Clinical Research Sponsor to direct the conduct of a clinical research trial or study on behalf of the sponsor.",
                                            "display": "clinical research investigator",
                                        },
                                        {
                                            "code": "CRSPNSR",
                                            "definition": "A role played by an entity, usually an organization, that is the sponsor of a clinical research trial or study.  The sponsor commissions the study, bears the expenses, is responsible for satisfying all legal requirements concerning subject safety and privacy, and is generally responsible for collection, storage and analysis of the data generated during the trial.  No scoper is necessary, as a clinical research sponsor undertakes the role on its own authority and declaration. Clinical research sponsors are usually educational or other research organizations, government agencies or biopharmaceutical companies.",
                                            "display": "clinical research sponsor",
                                        },
                                        {
                                            "code": "EMP",
                                            "concept": [
                                                {
                                                    "code": "MIL",
                                                    "definition": "A role played by a member of a military service. Scoper is the military service (e.g. Army, Navy, Air Force, etc.) or, more specifically, the unit (e.g. Company C, 3rd Battalion, 4th Division, etc.)",
                                                    "display": "military person",
                                                }
                                            ],
                                            "definition": "A relationship between a person or organization and a person or organization formed for the purpose of exchanging work for compensation.  The purpose of the role is to identify the type of relationship the employee has to the employer, rather than the nature of the work actually performed.  (Contrast with AssignedEntity.)",
                                            "display": "employee",
                                        },
                                        {
                                            "code": "GUAR",
                                            "definition": "A person or organization (player) that serves as a financial guarantor for another person or organization (scoper).",
                                            "display": "guarantor",
                                        },
                                        {
                                            "code": "INVSBJ",
                                            "concept": [
                                                {
                                                    "code": "CASEBJ",
                                                    "definition": "A person, non-person living subject, or place that is the subject of an investigation related to a notifiable condition (health circumstance that is reportable within the applicable public health jurisdiction)",
                                                    "display": "Case Subject",
                                                },
                                                {
                                                    "code": "RESBJ",
                                                    "definition": "Definition:Specifies the administrative functionality within a formal experimental design for which the ResearchSubject role was established.\r\n\n                        \n                           Examples: Screening - role is used for pre-enrollment evaluation portion of the design; enrolled - role is used for subjects admitted to the experimental portion of the design.",
                                                    "display": "research subject",
                                                },
                                            ],
                                            "definition": "An entity that is the subject of an investigation. This role is scoped by the party responsible for the investigation.",
                                            "display": "Investigation Subject",
                                        },
                                        {
                                            "code": "LIC",
                                            "concept": [
                                                {
                                                    "code": "NOT",
                                                    "definition": "notary public",
                                                    "display": "notary public",
                                                },
                                                {
                                                    "code": "PROV",
                                                    "definition": "An Entity (player) that is authorized to provide health care services by some authorizing agency (scoper).",
                                                    "display": "healthcare provider",
                                                },
                                            ],
                                            "definition": "A relationship in which the scoper certifies the player ( e. g. a medical care giver, a medical device or a provider organization) to perform certain activities that fall under the jurisdiction of the scoper (e.g., a health authority licensing healthcare providers, a medical quality authority certifying healthcare professionals).",
                                            "display": "licensed entity",
                                        },
                                        {
                                            "code": "PAT",
                                            "definition": "A Role of a LivingSubject (player) as an actual or potential recipient of health care services from a healthcare provider organization (scoper).\r\n\n                        \n                           Usage Note: Communication about relationships between patients and specific healthcare practitioners (people) is not done via scoper.  Instead this is generally done using the CareProvision act.  This allows linkage between patient and a particular healthcare practitioner role and also allows description of the type of care involved in the relationship.",
                                            "display": "patient",
                                        },
                                        {
                                            "code": "PAYEE",
                                            "definition": "The role of an organization or individual designated to receive payment for a claim against a particular coverage. The scoping entity is the organization that is the submitter of the invoice in question.",
                                            "display": "payee",
                                        },
                                        {
                                            "code": "PAYOR",
                                            "definition": "The role of an organization that undertakes to accept claims invoices, assess the coverage or payments due for those invoices and pay to the designated payees for those invoices.  This role may be either the underwriter or a third-party organization authorized by the underwriter.  The scoping entity is the organization that underwrites the claimed coverage.",
                                            "display": "invoice payor",
                                        },
                                        {
                                            "code": "POLHOLD",
                                            "definition": "A role played by a person or organization that holds an insurance policy.  The underwriter of that policy is the scoping entity.\r\n\n                        \n                           Discussion:The identifier of the policy is captured in 'Role.id' when the Role is a policy holder.\r\n\n                        A particular policy may cover several individuals one of whom may be, but need not be, the policy holder.  Thus the notion of covered party is a role that is distinct from that of the policy holder.",
                                            "display": "policy holder",
                                        },
                                        {
                                            "code": "QUAL",
                                            "definition": "An entity (player) that has been recognized as having certain training/experience or other characteristics that would make said entity an appropriate performer for a certain activity. The scoper is an organization that educates or qualifies entities.",
                                            "display": "qualified entity",
                                        },
                                        {
                                            "code": "SPNSR",
                                            "definition": "A role played by an entity, usually an organization that is the sponsor of an insurance plan or a health program. A sponsor is the party that is ultimately accountable for the coverage by employment contract or by law.  A sponsor can be an employer, union, government agency, or association.  Fully insured sponsors establish the terms of the plan and contract with health insurance plans to assume the risk and to administer the plan.  Self-insured sponsors delegate coverage administration, but not risk, to third-party administrators.  Program sponsors designate services to be covered in accordance with statute.   Program sponsors may administer the coverage themselves, delegate coverage administration, but not risk to third-party administrators, or contract with health insurance plans to assume the risk and administrator a program. Sponsors qualify individuals who may become \r\n\n                        \n                           \n                              a policy holder of the plan;\r\n\n                           \n                           \n                              where the sponsor is the policy holder, who may become a subscriber or a dependent to a policy under the plan; or\r\n\n                           \n                           \n                              where the sponsor is a government agency, who may become program eligibles under a program. \r\n\n                           \n                        \n                        The sponsor role may be further qualified by the SponsorRole.code.  Entities playing the sponsor role may also play the role of a Coverage Administrator.\r\n\n                        \n                           Example: An employer, union, government agency, or association.",
                                            "display": "coverage sponsor",
                                        },
                                        {
                                            "code": "STD",
                                            "definition": "A role played by an individual who is a student of a school, which is the scoping entity.",
                                            "display": "student",
                                        },
                                        {
                                            "code": "UNDWRT",
                                            "definition": "A role played by a person or an organization.  It is the party that \r\n\n                        \n                           \n                              accepts fiscal responsibility for insurance plans and the policies created under those plans;\r\n\n                           \n                           \n                              administers and accepts fiscal responsibility for a program that provides coverage for services to eligible individuals; and/or\r\n\n                           \n                           \n                              has the responsibility to assess the merits of each risk and decide a suitable premium for accepting all or part of the risk.  If played by an organization, this role may be further specified by an appropriate RoleCode.\r\n\n                           \n                        \n                        \n                           Example:\n                        \r\n\n                        \n                           \n                              A health insurer; \r\n\n                           \n                           \n                              Medicaid Program;\r\n\n                           \n                           \n                              Lloyd's of London",
                                            "display": "underwriter",
                                        },
                                    ],
                                    "definition": "A relationship between two entities that is formally recognized, frequently by a contract or similar agreement.",
                                    "display": "RoleClassRelationshipFormal",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "CAREGIVER",
                                    "definition": "A person responsible for the primary care of a patient at home.",
                                    "display": "caregiver",
                                },
                                {
                                    "code": "PRS",
                                    "definition": "Links two entities with classCode PSN (person) in a personal relationship. The character of the relationship must be defined by a PersonalRelationshipRoleType code. The player and scoper are determined by PersonalRelationshipRoleType code as well.",
                                    "display": "personal relationship",
                                },
                                {
                                    "code": "SELF",
                                    "definition": 'The "same" roleclass asserts an identity between playing and scoping entities: that they are in fact instances of the same entity and, in the case of discrepancies (e.g different DOB, gender), that one or both are in error.\r\n\n                        \n                           Usage:\n                        \r\n\n                        playing and scoping entities must have same classcode, but need not have identical attributes or values. \r\n\n                        \n                           Example: \n                        \r\n\n                        a provider registry maintains sets of conflicting demographic data for what is reported to be the same individual.',
                                    "display": "self",
                                    "property": [
                                        {"code": "status", "valueCode": "retired"}
                                    ],
                                },
                            ],
                            "definition": "A relationship that is based on mutual behavior of the two Entities as being related. The basis of such relationship may be agreements (e.g., spouses, contract parties) or they may be de facto behavior (e.g. friends) or may be an incidental involvement with each other (e.g. parties over a dispute, siblings, children).",
                            "display": "RoleClassMutualRelationship",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_RoleClassPassive",
                            "concept": [
                                {
                                    "code": "ACCESS",
                                    "definition": "A role in which the playing entity (material) provides access to another entity. The principal use case is intravenous (or other bodily) access lines that preexist and need to be referred to for medication routing instructions.",
                                    "display": "access",
                                },
                                {
                                    "code": "ADJY",
                                    "concept": [
                                        {
                                            "code": "CONC",
                                            "concept": [
                                                {
                                                    "code": "BOND",
                                                    "definition": "A connection between two atoms of a molecule.\r\n\n                        \n                           Examples: double bond between first and second C in ethane, peptide bond between two amino-acid, disulfide bridge between two proteins, chelate and ion associations, even the much weaker van-der-Waals bonds can be considered molecular bonds.\r\n\n                        \n                           UsageConstraints: See connection and adjacency for the assignment of player and scoper.",
                                                    "display": "molecular bond",
                                                },
                                                {
                                                    "code": "CONY",
                                                    "definition": "A connection between two regional parts.\r\n\n                        \n                           Examples:  the connection between ascending aorta and the aortic arc, connection between descending colon and sigmoid.\r\n\n                        \n                           UsageConstraints: See connection and adjacency for the assignment of player and scoper.",
                                                    "display": "continuity",
                                                },
                                            ],
                                            "definition": "An adjacency of two Entities held together by a bond which attaches to each of the two entities. \r\n\n                        \n                           Examples: biceps brachii muscle connected to the radius bone, port 3 on a network switch connected to port 5 on a patch panel.\r\n\n                        \n                           UsageConstraints: See Adjacency for the assignment of scoper (larger, more central) and player (smaller, more distant).",
                                            "display": "connection",
                                        }
                                    ],
                                    "definition": "A physical association whereby two Entities are in some (even lose) spatial relationship with each other such that they touch each other in some way.\r\n\n                        \n                           Examples: the colon is connected (and therefore adjacent) to the jejunum; the colon is adjacent to the liver (even if not actually connected.)\r\n\n                        \n                           UsageConstraints: Adjacency is in principle a symmetrical connection, but scoper and player of the role should, where applicable, be assigned to have scoper be the larger, more central Entity and player the smaller, more distant, appendage.",
                                    "display": "adjacency",
                                },
                                {
                                    "code": "ADMM",
                                    "definition": "A material (player) that can be administered to an Entity (scoper).",
                                    "display": "Administerable Material",
                                },
                                {
                                    "code": "BIRTHPL",
                                    "definition": "Relates a place (playing Entity) as the location where a living subject (scoping Entity) was born.",
                                    "display": "birthplace",
                                },
                                {
                                    "code": "DEATHPLC",
                                    "definition": "Definition: Relates a place (playing Entity) as the location where a living subject (scoping Entity) died.",
                                    "display": "place of death",
                                },
                                {
                                    "code": "DST",
                                    "concept": [
                                        {
                                            "code": "RET",
                                            "definition": "Material (player) sold by a retailer (scoper), who also give advice to prospective buyers.",
                                            "display": "retailed material",
                                        }
                                    ],
                                    "definition": "A material (player) distributed by a distributor (scoper) who functions between a manufacturer and a buyer or retailer.",
                                    "display": "distributed material",
                                },
                                {
                                    "code": "EXLOC",
                                    "concept": [
                                        {
                                            "code": "SDLOC",
                                            "concept": [
                                                {
                                                    "code": "DSDLOC",
                                                    "definition": 'A role of a place (player) that is intended to house the provision of services. Scoper is the Entity (typically Organization) that provides these services. This is not synonymous with "ownership."',
                                                    "display": "dedicated service delivery location",
                                                },
                                                {
                                                    "code": "ISDLOC",
                                                    "definition": "A role played by a place at which health care services may be provided without prior designation or authorization.",
                                                    "display": "incidental service delivery location",
                                                },
                                            ],
                                            "definition": "A role played by a place at which services may be provided.",
                                            "display": "service delivery location",
                                        }
                                    ],
                                    "definition": "A role played by a place at which the location of an event may be recorded.",
                                    "display": "event location",
                                },
                                {
                                    "code": "EXPR",
                                    "definition": 'A role played by an entity that has been exposed to a person or animal suffering a contagious disease, or with a location from which a toxin has been distributed.  The player of the role is normally a person or animal, but it is possible that other entity types could become exposed.  The role is scoped by the source of the exposure, and it is quite possible for a person playing the role of exposed party to also become the scoper a role played by another person.  That is to say, once a person has become infected, it is possible, perhaps likely, for that person to infect others.\r\n\n                        Management of exposures and tracking exposed parties is a key function within public health, and within most public health contexts - exposed parties are known as "contacts."',
                                    "display": "exposed entity",
                                },
                                {
                                    "code": "HLD",
                                    "definition": "Entity that is currently in the possession of a holder (scoper), who holds, or uses it, usually based on some agreement with the owner.",
                                    "display": "held entity",
                                },
                                {
                                    "code": "HLTHCHRT",
                                    "definition": "The role of a material (player) that is the physical health chart belonging to an organization (scoper).",
                                    "display": "health chart",
                                },
                                {
                                    "code": "IDENT",
                                    "definition": "A role in which the scoping entity designates an identifier for a playing entity.",
                                    "display": "identified entity",
                                },
                                {
                                    "code": "MANU",
                                    "concept": [
                                        {
                                            "code": "THER",
                                            "definition": "A manufactured material (player) that is used for its therapeutic properties.  The manufacturer is the scoper.",
                                            "display": "therapeutic agent",
                                        }
                                    ],
                                    "definition": "Scoped by the manufacturer",
                                    "display": "manufactured product",
                                },
                                {
                                    "code": "MNT",
                                    "definition": "An entity (player) that is maintained by another entity (scoper).  This is typical role held by durable equipment. The scoper assumes responsibility for proper operation, quality, and safety.",
                                    "display": "maintained entity",
                                },
                                {
                                    "code": "OWN",
                                    "definition": "An Entity (player) for which someone (scoper) is granted by law the right to call the material (player) his own.  This entitles the scoper to make decisions about the disposition of that material.",
                                    "display": "owned entity",
                                },
                                {
                                    "code": "RGPR",
                                    "definition": "A product regulated by some governmentatl orgnization.  The role is played by Material and scoped by Organization.\r\n\n                        Rationale: To support an entity clone used to identify the NDC number for a drug product.",
                                    "display": "regulated product",
                                },
                                {
                                    "code": "TERR",
                                    "definition": 'Relates a place entity (player) as the region over which the scoper (typically an Organization) has certain authority (jurisdiction). For example, the Calgary Regional Health Authority (scoper) has authority over the territory "Region 4 of Alberta" (player) in matters of health.',
                                    "display": "territory of authority",
                                },
                                {
                                    "code": "USED",
                                    "definition": "Description:An entity (player) that is used by another entity (scoper)",
                                    "display": "used entity",
                                },
                                {
                                    "code": "WRTE",
                                    "definition": "A role a product plays when a guarantee is given to the purchaser by the seller (scoping entity) stating that the product is reliable and free from known defects and that the seller will repair or replace defective parts within a given time limit and under certain conditions.",
                                    "display": "warranted product",
                                },
                            ],
                            "definition": "An association for a playing Entity that is used, known, treated, handled, built, or destroyed, etc. under the auspices of the scoping Entity. The playing Entity is passive in these roles (even though it may be active in other roles), in the sense that the kinds of things done to it in this role happen without an agreement from the playing Entity.",
                            "display": "RoleClassPassive",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                    ],
                    "definition": "A general association between two entities that is neither partitive nor ontological.",
                    "display": "RoleClassAssociative",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_RoleClassOntological",
                    "concept": [
                        {
                            "code": "EQUIV",
                            "concept": [
                                {
                                    "code": "SAME",
                                    "definition": 'The "same" role asserts an identity between playing and scoping entities, i.e., that they are in fact two records of the same entity instance, and, in the case of discrepancies (e.g different DOB, gender), that one or both are in error.\r\n\n                        \n                           Usage:\n                        \r\n\n                        playing and scoping entities must have same classCode, but need not have identical attributes or values.\r\n\n                        \n                           Example: \n                        \r\n\n                        a provider registry maintains sets of conflicting demographic data for what is reported to be the same individual.',
                                    "display": "same",
                                },
                                {
                                    "code": "SUBY",
                                    "definition": "Relates a prevailing record of an Entity (scoper) with another record (player) that it subsumes.\r\n\n                        \n                           Examples: Show a correct new Person object (scoper) that subsumes one or more duplicate Person objects that had accidentally been created for the same physical person.\r\n\n                        \n                           Constraints: Both the player and scoper must have the same classCode.",
                                    "display": "subsumed by",
                                },
                            ],
                            "definition": 'Description: Specifies the player Entity (the equivalent Entity) as an Entity that is considered to be equivalent to a reference Entity (scoper).  The equivalence is in principle a symmetric relationship, however, it is expected that the scoper is a reference entity which serves as reference entity for multiple different equivalent entities. \r\n\n                        \n                           Examples: An innovator\'s medicine formulation is the reference for "generics", i.e., formulations manufactured differently but having been proven to be biologically equivalent to the reference medicine. Another example is a reference ingredient that serves as basis for quantity specifications (basis of strength, e.g., metoprolol succinate specified in terms of metoprolol tartrate.)',
                            "display": "equivalent entity",
                        },
                        {
                            "code": "GEN",
                            "concept": [
                                {
                                    "code": "GRIC",
                                    "definition": "A special link between pharmaceuticals indicating that the target (scoper) is a generic for the source (player).",
                                    "display": "has generic",
                                }
                            ],
                            "definition": "Relates a specialized material concept (player) to its generalization (scoper).",
                            "display": "has generalization",
                        },
                        {
                            "code": "INST",
                            "definition": "An individual piece of material (player) instantiating a class of material (scoper).",
                            "display": "instance",
                        },
                        {
                            "code": "SUBS",
                            "definition": "An entity that subsumes the identity of another.  Used in the context of merging documented entity instances. Both the player and scoper must have the same classCode.\r\n\n                        The use of this code is deprecated in favor of the term SUBY which is its inverse and is more ontologically correct.",
                            "display": "subsumer",
                            "property": [
                                {"code": "status", "valueCode": "retired"},
                                {
                                    "code": "deprecationDate",
                                    "valueDateTime": "2011-12-01",
                                },
                            ],
                        },
                    ],
                    "definition": 'A relationship in which the scoping Entity defines or specifies what the playing Entity is.  Thus, the player\'s "being" (Greek: ontos) is specified.',
                    "display": "RoleClassOntological",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_RoleClassPartitive",
                    "concept": [
                        {
                            "code": "CONT",
                            "definition": "Relates a material as the content (player) to a container (scoper).  Unlike ingredients, the content and a container remain separate (not mixed) and the content can be removed from the container.  A content is not part of an empty container.",
                            "display": "content",
                        },
                        {
                            "code": "EXPAGTCAR",
                            "concept": [
                                {
                                    "code": "EXPVECTOR",
                                    "definition": "Description: A vector is a living subject that carries an exposure agent.  The vector does not cause the disease itself, but exposes targets to the exposure agent.  A mosquito carrying malaria is an example of a vector.  The scoper of the role must be the exposure agent (e.g., pathogen).",
                                    "display": "exposure vector",
                                },
                                {
                                    "code": "FOMITE",
                                    "definition": "Description: A fomite is a non-living entity that is capable of conveying exposure agent from one entity to another.  A doorknob contaminated with a Norovirus is an example of a fomite.  Anyone touching the doorknob would be exposed to the virus.  The scoper of the role must be the exposure agent (e.g., pathogen).",
                                    "display": "fomite",
                                },
                            ],
                            "definition": "An exposure agent carrier is an entity that is capable of conveying an exposure agent from one entity to another.  The scoper of the role must be the exposure agent (e.g., pathogen).",
                            "display": "exposure agent carrier",
                        },
                        {
                            "code": "INGR",
                            "concept": [
                                {
                                    "code": "ACTI",
                                    "concept": [
                                        {
                                            "code": "ACTIB",
                                            "definition": 'Description:  Active ingredient, where the ingredient substance (player) is itself the "basis of strength", i.e., where the Role.quantity specifies exactly the quantity of the player substance in the medicine formulation. \r\n\n                        \n                           Examples: Lopressor 50 mg actually contains 50 mg of metoprolol succinate, even though the active moiety is metoprolol,  but also: Tenormin 50 mg contain 50 mg of atenolol, as free base, i.e., where the active ingredient atenolol is also the active moiety.',
                                            "display": "active ingredient - basis of strength",
                                        },
                                        {
                                            "code": "ACTIM",
                                            "definition": 'Description: Active ingredient, where not the ingredient substance (player), but itaTMs active moiety is the "basis of strength", i.e., where the Role.quantity specifies the quantity of the player substance\'s active moiety in the medicine formulation.\r\n\n                        \n                           Examples: 1 mL of Betopic 5mg/mL eye drops contains 5.6 mg betaxolol hydrochloride equivalent to betaxolol base 5 mg.',
                                            "display": "active ingredient - moiety is basis of strength",
                                        },
                                        {
                                            "code": "ACTIR",
                                            "definition": 'Description: Active ingredient, where not the ingredient substance (player) but another reference substance with the same active moiety, is the "basis of strength", i.e., where the Role.quantity specifies the quantity of a reference substance, similar but different from the player substance\'s in the medicine formulation.\r\n\n                        \n                           Examples: Toprol-XL 50 mg contains 47.5 mg of metoprolol succinate equivalent to 50 mg of metoprolol tartrate.',
                                            "display": "active ingredient - reference substance is basis of strength",
                                        },
                                    ],
                                    "definition": "Definition: a therapeutically active ingredient (player) in a mixture (scoper), where the mixture is typically a manufactured pharmaceutical.  It is unknown if the quantity of such an ingredient is expressed precisely in terms of the playing ingredient substance, or, if it is specified in terms of a closely related substance (active moiety or reference substance).",
                                    "display": "active ingredient",
                                },
                                {
                                    "code": "ADJV",
                                    "definition": "A component (player) added to enhance the action of an active ingredient (scoper) (in the manner of a catalyst) but which has no active effect in and of itself.  Such ingredients are significant in defining equivalence of products in a way that inactive ingredients are not.",
                                    "display": "adjuvant",
                                },
                                {
                                    "code": "ADTV",
                                    "definition": "An ingredient (player)  that is added to a base (scoper), that amounts to a minor part of the overall mixture.",
                                    "display": "additive",
                                },
                                {
                                    "code": "BASE",
                                    "definition": "A base ingredient (player) is what comprises the major part of a mixture (scoper). E.g., Water in most i.v. solutions, or Vaseline in salves. Among all ingredients of a material, there should be only one base. A base substance can, in turn, be a mixture.",
                                    "display": "base",
                                },
                                {
                                    "code": "CNTM",
                                    "definition": "An ingredient whose presence is not intended but may not be reasonably avoided given the circumstances of the mixture's nature or origin.",
                                    "display": "contaminant ingredient",
                                },
                                {
                                    "code": "IACT",
                                    "concept": [
                                        {
                                            "code": "COLR",
                                            "definition": "A substance (player) influencing the optical aspect of material (scoper).",
                                            "display": "color additive",
                                        },
                                        {
                                            "code": "FLVR",
                                            "definition": "A substance (player) added to a mixture (scoper) to make it taste a certain way.  In food the use is obvious, in pharmaceuticals flavors can hide disgusting taste of the active ingredient (important in pediatric treatments).",
                                            "display": "flavor additive",
                                        },
                                        {
                                            "code": "PRSV",
                                            "definition": "A substance (player) added to a mixture (scoper) to prevent microorganisms (fungi, bacteria) to spoil the mixture.",
                                            "display": "preservative",
                                        },
                                        {
                                            "code": "STBL",
                                            "definition": "A stabilizer (player) added to a mixture (scoper) in order to prevent the molecular disintegration of the main substance.",
                                            "display": "stabilizer",
                                        },
                                    ],
                                    "definition": "An ingredient which is not considered therapeutically active, e.g., colors, flavors, stabilizers, or preservatives, fillers, or structural components added to an active ingredient in order to facilitate administration of the active ingredient but without being considered therapeutically active. An inactive ingredient need not be biologically inert, e.g., might be active as an allergen or might have a pleasant taste, but is not an essential constituent delivering the therapeutic effect.",
                                    "display": "inactive ingredient",
                                },
                                {
                                    "code": "MECH",
                                    "definition": "An ingredient (player) of a medication (scoper) that is inseparable from the active ingredients, but has no intended chemical or pharmaceutical effect itself, but which may have some systemic effect on the patient.\r\n\n                        An example is a collagen matrix used as a base for transplanting skin cells.  The collagen matrix can be left permanently in the graft site.  Because it is of bovine origin, the patient may exhibit allergies or may have cultural objections to its use.",
                                    "display": "mechanical ingredient",
                                },
                            ],
                            "definition": "Relates a component (player) to a mixture (scoper). E.g., Glucose and Water are ingredients of D5W, latex may be an ingredient in a tracheal tube.",
                            "display": "ingredient",
                        },
                        {
                            "code": "LOCE",
                            "concept": [
                                {
                                    "code": "STOR",
                                    "definition": "Relates an entity (player) (e.g. a device) to a location (scoper) at which it is normally found or stored when not used.",
                                    "display": "stored entity",
                                }
                            ],
                            "definition": "Relates an entity (player) to a location (scoper) at which it is present in some way. This presence may be limited in time.",
                            "display": "located entity",
                        },
                        {
                            "code": "MBR",
                            "definition": "A role played by an entity that is a member of a group.  The group provides the scope for this role.\r\n\n                        Among other uses, groups as used in insurance (groups of covered individuals) and in scheduling where resources may be grouped for scheduling and logistical purposes.",
                            "display": "member",
                        },
                        {
                            "code": "PART",
                            "concept": [
                                {
                                    "code": "ACTM",
                                    "definition": "The molecule or ion that is responsible for the intended pharmacological action of the drug substance, excluding those appended or associated parts of the molecule that make the molecule an ester, salt (including a salt with hydrogen or coordination bonds), or other noncovalent derivative (such as a complex, chelate, or clathrate).\r\n\n                        Examples: heparin-sodium and heparin-potassium have the same active moiety, heparin; the active moiety of morphine-hydrochloride is morphine.",
                                    "display": "active moiety",
                                }
                            ],
                            "definition": "Definition:  an association between two Entities where the playing Entity (the part) is a component of the whole (scoper) in the sense of an integral structural component, that is distinct from other parts in the same whole, has a distinct function in the whole, and, as an effect, the full integrity of the whole depends (to some degree) on the presence of this part, even though the part may often be separable from the whole.\r\n\n                        \n                           Discussion: Part is defined in opposition to (a) ingredient (not separable), (b) content (not a functional component), and (c) member (not functionally distinct from other members).",
                            "display": "part",
                        },
                        {
                            "code": "SPEC",
                            "concept": [
                                {
                                    "code": "ALQT",
                                    "definition": "A portion (player) of an original or source specimen (scoper) used for testing or transportation.",
                                    "display": "aliquot",
                                },
                                {
                                    "code": "ISLT",
                                    "definition": "A microorganism that has been isolated from other microorganisms or a source matrix.",
                                    "display": "isolate",
                                },
                            ],
                            "definition": "A role played by a material entity that is a specimen for an act. It is scoped by the source of the specimen.",
                            "display": "specimen",
                        },
                    ],
                    "definition": 'An association between two Entities where the playing Entity is considered in some way "part" of the scoping Entity, e.g., as a member, component, ingredient, or content. Being "part" in the broadest sense of the word can mean anything from being an integral structural component to a mere incidental temporary association of a playing Entity with a (generally larger) scoping Entity.',
                    "display": "RoleClassPartitive",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": "Corresponds to the Role class",
            "display": "role",
        }
    )
    """
    role

    Corresponds to the Role class
    """

    child = CodeSystemConcept(
        {
            "code": "CHILD",
            "definition": "The player of the role is a child of the scoping entity, in a generic sense.",
            "display": "child",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    child

    The player of the role is a child of the scoping entity, in a generic sense.
    """

    cred = CodeSystemConcept(
        {
            "code": "CRED",
            "definition": "A role played by an entity that receives credentials from the scoping entity.",
            "display": "credentialed entity",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    credentialed entity

    A role played by an entity that receives credentials from the scoping entity.
    """

    nurprac = CodeSystemConcept(
        {
            "code": "NURPRAC",
            "definition": "nurse practitioner",
            "display": "nurse practitioner",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    nurse practitioner

    nurse practitioner
    """

    nurs = CodeSystemConcept(
        {
            "code": "NURS",
            "definition": "nurse",
            "display": "nurse",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    nurse

    nurse
    """

    pa = CodeSystemConcept(
        {
            "code": "PA",
            "definition": "physician assistant",
            "display": "physician assistant",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    physician assistant

    physician assistant
    """

    phys = CodeSystemConcept(
        {
            "code": "PHYS",
            "definition": "physician",
            "display": "physician",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    physician

    physician
    """

    class Meta:
        resource = _resource
