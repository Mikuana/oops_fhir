from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ParticipationFunction"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ParticipationFunction:
    """
    v3 Code System ParticipationFunction

     This code is used to specify the exact function an actor had in a
service in all necessary detail. This domain may include local
extensions (CWE).

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ParticipationFunction
    """

    underscore_authorized_participation_function = CodeSystemConcept(
        {
            "code": "_AuthorizedParticipationFunction",
            "concept": [
                {
                    "code": "_AuthorizedReceiverParticipationFunction",
                    "concept": [
                        {
                            "code": "AUCG",
                            "definition": "Description:Caregiver authorized to receive patient health information.",
                            "display": "caregiver information receiver",
                        },
                        {
                            "code": "AULR",
                            "definition": "Description:Provider with legitimate relationship authorized to receive patient health information.",
                            "display": "legitimate relationship information receiver",
                        },
                        {
                            "code": "AUTM",
                            "definition": "Description:Member of care team authorized to receive patient health information.",
                            "display": "care team information receiver",
                        },
                        {
                            "code": "AUWA",
                            "definition": "Description:Entities within specified work area authorized to receive patient health information.",
                            "display": "work area information receiver",
                        },
                    ],
                    "definition": "This code is used to specify the exact function an actor is authorized to have as a receiver of information that is the subject of a consent directive or consent override.",
                    "display": "AuthorizedReceiverParticipationFunction",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_ConsenterParticipationFunction",
                    "concept": [
                        {
                            "code": "GRDCON",
                            "definition": "Description:Legal guardian of the subject of consent authorized to author a consent directive for the subject of consent.",
                            "display": "legal guardian consent author",
                        },
                        {
                            "code": "POACON",
                            "definition": "Description:Person authorized with healthcare power of attorney to author a  consent directive for the subject of consent.",
                            "display": "healthcare power of attorney consent author",
                        },
                        {
                            "code": "PRCON",
                            "definition": "Description:Personal representative of the subject of consent authorized to author a consent directive for the subject of consent.",
                            "display": "personal representative consent author",
                        },
                        {
                            "code": "PROMSK",
                            "definition": "Definition:Provider authorized to mask information to protect the patient, a third party, or to ensure that the provider has consulted with the patient prior to release of this information.",
                            "display": "authorized provider masking author",
                        },
                        {
                            "code": "SUBCON",
                            "definition": "Description:Subject of consent authorized to author a consent directive.",
                            "display": "subject of consent author",
                        },
                    ],
                    "definition": "This code is used to specify the exact function an actor is authorized to have in authoring a consent directive.",
                    "display": "ConsenterParticipationFunction",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_OverriderParticipationFunction",
                    "concept": [
                        {
                            "code": "AUCOV",
                            "definition": "Description:Entity authorized to override a consent directive.",
                            "display": "consent overrider",
                        },
                        {
                            "code": "AUEMROV",
                            "definition": "Description:Entity  authorized to override a consent directive or privacy policy in an emergency.",
                            "display": "emergency overrider",
                        },
                    ],
                    "definition": "This code is used to specify the exact function an actor is authorized to have in authoring a consent override.",
                    "display": "OverriderParticipationFunction",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": "This code is used to specify the exact function an actor is authorized to have in a service in all necessary detail.",
            "display": "AuthorizedParticipationFunction",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    AuthorizedParticipationFunction

    This code is used to specify the exact function an actor is authorized to have in a service in all necessary detail.
    """

    underscore_coverage_participation_function = CodeSystemConcept(
        {
            "code": "_CoverageParticipationFunction",
            "concept": [
                {
                    "code": "_PayorParticipationFunction",
                    "concept": [
                        {
                            "code": "CLMADJ",
                            "definition": "Definition: Manages all operations required to adjudicate fee for service claims or managed care encounter reports.",
                            "display": "claims adjudication",
                        },
                        {
                            "code": "ENROLL",
                            "definition": "Definition: Managing the enrollment of covered parties.",
                            "display": "enrollment broker",
                        },
                        {
                            "code": "FFSMGT",
                            "definition": "Definition: Managing all operations required to administer a fee for service or indemnity health plan including enrolling covered parties and providing customer service, provider contracting, claims payment, care management and utilization review.",
                            "display": "ffs management",
                        },
                        {
                            "code": "MCMGT",
                            "definition": "Definition: Managing all operations required to administer a managed care plan including enrolling covered parties and providing customer service,, provider contracting, claims payment, care management and utilization review.",
                            "display": "managed care management",
                        },
                        {
                            "code": "PROVMGT",
                            "definition": "Definition: Managing provider contracting, provider services, credentialing, profiling, performance measures, and ensuring network adequacy.",
                            "display": "provider management",
                        },
                        {
                            "code": "UMGT",
                            "definition": "Definition: Managing utilization of services by ensuring that providers adhere to, e.g., payeraTMs clinical protocols for medical appropriateness and standards of medical necessity.  May include management of authorizations for services and referrals.",
                            "display": "utilization management",
                        },
                    ],
                    "definition": "Definition: Set of codes indicating the manner in which payors participate in a policy or program.</",
                    "display": "PayorParticipationFunction",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_SponsorParticipationFunction",
                    "concept": [
                        {
                            "code": "FULINRD",
                            "definition": "Definition: Responsibility taken by a sponsor to contract with one or more underwriters for the assumption of full responsibility for the risk and administration of a policy or program.",
                            "display": "fully insured",
                        },
                        {
                            "code": "SELFINRD",
                            "definition": "Definition: Responsibility taken by a sponsor to organize the underwriting of risk and administration of a policy or program.",
                            "display": "self insured",
                        },
                    ],
                    "definition": "Definition: Set of codes indicating the manner in which sponsors participate in a policy or program. NOTE: use only when the Sponsor is not further specified with a SponsorRoleType as being either a fully insured sponsor or a self insured sponsor.",
                    "display": "SponsorParticipationFunction",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_UnderwriterParticipationFunction",
                    "concept": [
                        {
                            "code": "PAYORCNTR",
                            "definition": "Definition: Contracting for the provision and administration of health services to payors while retaining the risk for coverage.  Contracting may be for all provision and administration; or for provision of certain types of services; for provision of services by region; and by types of administration, e.g., claims adjudication, enrollment, provider management, and utilization management.  Typically done by underwriters for sponsors who need coverage provided to covered parties in multiple regions.  The underwriter may act as the payor in some, but not all of the regions in which coverage is provided.",
                            "display": "payor contracting",
                        },
                        {
                            "code": "REINS",
                            "definition": "Definition: Underwriting reinsurance for another underwriter for the policy or program.",
                            "display": "reinsures",
                        },
                        {
                            "code": "RETROCES",
                            "definition": "Definition: Underwriting reinsurance for another reinsurer.",
                            "display": "retrocessionaires",
                        },
                        {
                            "code": "SUBCTRT",
                            "definition": "Definition: Delegating risk for a policy or program to one or more subcontracting underwriters, e.g., a major health insurer may delegate risk for provision of coverage under a national health plan to other underwriters by region .",
                            "display": "subcontracting risk",
                        },
                        {
                            "code": "UNDERWRTNG",
                            "definition": "Definition: Provision of underwriting analysis for another underwriter without assumption of risk.",
                            "display": "underwriting",
                        },
                    ],
                    "definition": "Definition: Set of codes indicating the manner in which underwriters participate in a policy or program.",
                    "display": "UnderwriterParticipationFunction",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": "Definition: Set of codes indicating the manner in which sponsors, underwriters, and payers participate in a policy or program.",
            "display": "CoverageParticipationFunction",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    CoverageParticipationFunction

    Definition: Set of codes indicating the manner in which sponsors, underwriters, and payers participate in a policy or program.
    """

    admphys = CodeSystemConcept(
        {
            "code": "ADMPHYS",
            "definition": "A physician who admitted a patient to a hospital or other care unit that is the context of this service.",
            "display": "admitting physician",
        }
    )
    """
    admitting physician

    A physician who admitted a patient to a hospital or other care unit that is the context of this service.
    """

    anest = CodeSystemConcept(
        {
            "code": "ANEST",
            "definition": "In a typical anesthesia setting an anesthesiologist or anesthesia resident in charge of the anesthesia and life support, but only a witness to the surgical procedure itself.  To clarify responsibilities anesthesia should always be represented as a separate service related to the surgery.",
            "display": "anesthesist",
        }
    )
    """
    anesthesist

    In a typical anesthesia setting an anesthesiologist or anesthesia resident in charge of the anesthesia and life support, but only a witness to the surgical procedure itself.  To clarify responsibilities anesthesia should always be represented as a separate service related to the surgery.
    """

    anrs = CodeSystemConcept(
        {
            "code": "ANRS",
            "definition": "In a typical anesthesia setting the nurse principally assisting the anesthesiologist during the critical periods.",
            "display": "anesthesia nurse",
        }
    )
    """
    anesthesia nurse

    In a typical anesthesia setting the nurse principally assisting the anesthesiologist during the critical periods.
    """

    assembler = CodeSystemConcept(
        {
            "code": "ASSEMBLER",
            "definition": "A device that operates independently of an author on custodian's algorithms for data extraction of existing information for purpose of generating a new artifact.\n                           UsageConstraint: ASSEMBLER ParticipationFunction should be used with DEV (device) ParticipationType.",
            "display": "assembly software",
        }
    )
    """
    assembly software

    A device that operates independently of an author on custodian's algorithms for data extraction of existing information for purpose of generating a new artifact.
                           UsageConstraint: ASSEMBLER ParticipationFunction should be used with DEV (device) ParticipationType.
    """

    attphys = CodeSystemConcept(
        {
            "code": "ATTPHYS",
            "definition": "A physician who is primarily responsible for a patient during the hospitalization, which is the context of the service.",
            "display": "attending physician",
        }
    )
    """
    attending physician

    A physician who is primarily responsible for a patient during the hospitalization, which is the context of the service.
    """

    composer = CodeSystemConcept(
        {
            "code": "COMPOSER",
            "definition": "A device used by an author to record new information, which may also be used by the author to select existing information for aggregation with newly recorded information for the purpose of generating a new artifact.\n                           UsageConstraint: COMPOSER ParticipationFunction should be used with DEV (device) ParticipationType.\r\n\n                        \n                           Usage Note: This code will enable implementers to more specifically represent the manner in which a Device participated in and facilitated the generation of a CDA Clinical Document or a CDA Entry by the responsible Author, which is comprised of the Author's newly entered content, and may include the pre-existing content selected by the Author, for the purpose of establishing the provenance and accountability for these acts.",
            "display": "composer software",
        }
    )
    """
    composer software

    A device used by an author to record new information, which may also be used by the author to select existing information for aggregation with newly recorded information for the purpose of generating a new artifact.
                           UsageConstraint: COMPOSER ParticipationFunction should be used with DEV (device) ParticipationType.

                        
                           Usage Note: This code will enable implementers to more specifically represent the manner in which a Device participated in and facilitated the generation of a CDA Clinical Document or a CDA Entry by the responsible Author, which is comprised of the Author's newly entered content, and may include the pre-existing content selected by the Author, for the purpose of establishing the provenance and accountability for these acts.
    """

    disphys = CodeSystemConcept(
        {
            "code": "DISPHYS",
            "definition": "A physician who discharged a patient from a hospital or other care unit that is the context of this service.",
            "display": "discharging physician",
        }
    )
    """
    discharging physician

    A physician who discharged a patient from a hospital or other care unit that is the context of this service.
    """

    fasst = CodeSystemConcept(
        {
            "code": "FASST",
            "definition": "In a typical surgery setting the assistant facing the primary surgeon.  The first assistant performs parts of the operation and assists in others (e.g., incision, approach, electrocoutering, ligatures, sutures).",
            "display": "first assistant surgeon",
        }
    )
    """
    first assistant surgeon

    In a typical surgery setting the assistant facing the primary surgeon.  The first assistant performs parts of the operation and assists in others (e.g., incision, approach, electrocoutering, ligatures, sutures).
    """

    mdwf = CodeSystemConcept(
        {
            "code": "MDWF",
            "definition": "A person (usually female) helping a woman deliver a baby. Responsibilities vary locally, ranging from a mere optional assistant to a full required participant, responsible for (normal) births and pre- and post-natal care for both mother and baby.",
            "display": "midwife",
        }
    )
    """
    midwife

    A person (usually female) helping a woman deliver a baby. Responsibilities vary locally, ranging from a mere optional assistant to a full required participant, responsible for (normal) births and pre- and post-natal care for both mother and baby.
    """

    nasst = CodeSystemConcept(
        {
            "code": "NASST",
            "definition": "In a typical surgery setting the non-sterile nurse handles material supply from the stock, forwards specimen to pathology, and helps with other non-sterile tasks (e.g., phone calls, etc.).",
            "display": "nurse assistant",
        }
    )
    """
    nurse assistant

    In a typical surgery setting the non-sterile nurse handles material supply from the stock, forwards specimen to pathology, and helps with other non-sterile tasks (e.g., phone calls, etc.).
    """

    pcp = CodeSystemConcept(
        {
            "code": "PCP",
            "definition": "The healthcare provider that holds primary responsibility for the overall care of a patient.",
            "display": "primary care physician",
        }
    )
    """
    primary care physician

    The healthcare provider that holds primary responsibility for the overall care of a patient.
    """

    prisurg = CodeSystemConcept(
        {
            "code": "PRISURG",
            "definition": "In a typical surgery setting the primary performing surgeon.",
            "display": "primary surgeon",
        }
    )
    """
    primary surgeon

    In a typical surgery setting the primary performing surgeon.
    """

    reviewer = CodeSystemConcept(
        {
            "code": "REVIEWER",
            "definition": "A verifier who is accountable for reviewing and asserting that the verification of an Act complies with jurisdictional or organizational policy.\r\n\n                        \n                           UsageConstraint: UsageConstraint:  Specifies the exact function that an actor is authorized to have as a verifier of an Act.  Connotes that a specialized verifier asserts compliance for veracity of the review per jurisdictional or organizational policy.  E.g., The Provider who takes responsibility for authenticity of a record submitted to a payer.\r\n\n                        REVIEW ParticipationFunction should be used with VFR (verifier)",
            "display": "reviewer",
        }
    )
    """
    reviewer

    A verifier who is accountable for reviewing and asserting that the verification of an Act complies with jurisdictional or organizational policy.

                        
                           UsageConstraint: UsageConstraint:  Specifies the exact function that an actor is authorized to have as a verifier of an Act.  Connotes that a specialized verifier asserts compliance for veracity of the review per jurisdictional or organizational policy.  E.g., The Provider who takes responsibility for authenticity of a record submitted to a payer.

                        REVIEW ParticipationFunction should be used with VFR (verifier)
    """

    rndphys = CodeSystemConcept(
        {
            "code": "RNDPHYS",
            "definition": "A physician who made rounds on a patient in a hospital or other care center.",
            "display": "rounding physician",
        }
    )
    """
    rounding physician

    A physician who made rounds on a patient in a hospital or other care center.
    """

    sasst = CodeSystemConcept(
        {
            "code": "SASST",
            "definition": "In a typical surgery setting the assistant who primarily holds the hooks.",
            "display": "second assistant surgeon",
        }
    )
    """
    second assistant surgeon

    In a typical surgery setting the assistant who primarily holds the hooks.
    """

    snrs = CodeSystemConcept(
        {
            "code": "SNRS",
            "definition": "In a typical surgery setting the nurse in charge of the instrumentation.",
            "display": "scrub nurse",
        }
    )
    """
    scrub nurse

    In a typical surgery setting the nurse in charge of the instrumentation.
    """

    tasst = CodeSystemConcept(
        {
            "code": "TASST",
            "definition": "In a typical surgery setting there is rarely a third assistant (e.g., in some Hip operations the third assistant postures the affected leg).",
            "display": "third assistant",
        }
    )
    """
    third assistant

    In a typical surgery setting there is rarely a third assistant (e.g., in some Hip operations the third assistant postures the affected leg).
    """

    class Meta:
        resource = _resource
