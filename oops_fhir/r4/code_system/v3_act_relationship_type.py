from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ActRelationshipType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ActRelationshipType:
    """
    v3 Code System ActRelationshipType

     The source is an excerpt from the target.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ActRelationshipType
    """

    art = CodeSystemConcept(
        {
            "code": "ART",
            "concept": [
                {
                    "code": "_ActClassTemporallyPertains",
                    "definition": "ActClassTemporallyPertains",
                    "display": "ActClassTemporallyPertains",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_ActRelationshipAccounting",
                    "concept": [
                        {
                            "code": "_ActRelationshipCostTracking",
                            "concept": [
                                {
                                    "code": "CHRG",
                                    "definition": "A relationship that provides an ability to associate a financial transaction (target) as a charge to a clinical act (source).  A clinical act may have a charge associated with the execution or delivery of the service.\r\n\n                        The financial transaction will define the charge (bill) for delivery or performance of the service.\r\n\n                        Charges and costs are distinct terms.  A charge defines what is charged or billed to another organization or entity within an organization.  The cost defines what it costs an organization to perform or deliver a service or product.",
                                    "display": "has charge",
                                },
                                {
                                    "code": "COST",
                                    "definition": "A relationship that provides an ability to associate a financial transaction (target) as a cost to a clinical act (source).  A clinical act may have an inherit cost associated with the execution or delivery of the service.\r\n\n                        The financial transaction will define the cost of delivery or performance of the service.\r\n\n                        Charges and costs are distinct terms.  A charge defines what is charged or billed to another organization or entity within an organization.  The cost defines what it costs an organization to perform or deliver a service or product.",
                                    "display": "has cost",
                                },
                            ],
                            "definition": "Expresses values for describing the relationship relationship between an InvoiceElement or InvoiceElementGroup and a billable act.",
                            "display": "ActRelationshipCostTracking",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_ActRelationshipPosting",
                            "concept": [
                                {
                                    "code": "CREDIT",
                                    "definition": "A credit relationship ties a financial transaction (target) to an account (source). A credit, once applied (posted), may have either a positive or negative effect on the account balance, depending on the type of account. An asset account credit will decrease the account balance. A non-asset account credit will decrease the account balance.",
                                    "display": "has credit",
                                },
                                {
                                    "code": "DEBIT",
                                    "definition": "A debit relationship ties a financial transaction (target) to an account (source).  A debit, once applied (posted), may have either a positive or negative effect on the account balance, depending on the type of account.  An asset account debit will increase the account balance.  A non-asset account debit will decrease the account balance.",
                                    "display": "has debit",
                                },
                            ],
                            "definition": "Expresses values for describing the relationship between a FinancialTransaction and an Account.",
                            "display": "ActRelationshipPosting",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                    ],
                    "definition": "Codes that describe the relationship between an Act and a financial instrument such as a financial transaction, account or invoice element.",
                    "display": "ActRelationshipAccounting",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_ActRelationshipConditional",
                    "concept": [
                        {
                            "code": "CIND",
                            "definition": "A contraindication is just a negation of a reason, i.e. it gives a condition under which the action is not to be done. Both, source and target can be any kind of service; target service is in criterion mood. How the strength of a contraindication is expressed (e.g., relative, absolute) is left as an open issue. The priorityNumber attribute could be used.",
                            "display": "has contra-indication",
                        },
                        {
                            "code": "PRCN",
                            "definition": "A requirement to be true before a service is performed. The target can be any service in criterion mood.  For multiple pre-conditions a conjunction attribute (AND, OR, XOR) is applicable.",
                            "display": "has pre-condition",
                        },
                        {
                            "code": "RSON",
                            "concept": [
                                {
                                    "code": "BLOCK",
                                    "definition": "Definition: The source act is performed to block the effects of the target act.  This act relationship should be used when describing near miss type incidents where potential harm could have occurred, but the action described in the source act blocked the potential harmful effects of the incident actually occurring.",
                                    "display": "blocks",
                                },
                                {
                                    "code": "DIAG",
                                    "definition": "Description: The source act is intended to help establish the presence of a (an adverse) situation described by the target act. This is not limited to diseases but can apply to any adverse situation or condition of medical or technical nature.",
                                    "display": "diagnoses",
                                },
                                {
                                    "code": "IMM",
                                    "concept": [
                                        {
                                            "code": "ACTIMM",
                                            "definition": "Description: The source act is intended to provide active immunity against the effects of the target act (the target act describes an infectious disease)",
                                            "display": "active immunization against",
                                        },
                                        {
                                            "code": "PASSIMM",
                                            "definition": "Description: The source act is intended to provide passive immunity against the effects of the target act (the target act describes an infectious disease).",
                                            "display": "passive immunization against",
                                        },
                                    ],
                                    "definition": "Description: The source act is intented to provide immunity against the effects of the target act (the target act describes an infectious disease)",
                                    "display": "immunization against",
                                },
                                {
                                    "code": "MITGT",
                                    "concept": [
                                        {
                                            "code": "RCVY",
                                            "definition": "Definition: The source act is performed to recover from the effects of the target act.",
                                            "display": "recovers",
                                        }
                                    ],
                                    "definition": "The source act removes or lessens the occurrence or effect of the target act.",
                                    "display": "mitigates",
                                },
                                {
                                    "code": "PRYLX",
                                    "definition": "Description: The source act is intended to reduce the risk of of an adverse situation to emerge as described by the target act. This is not limited to diseases but can apply to any adverse situation or condition of medical or technical nature.",
                                    "display": "prophylaxis of",
                                },
                                {
                                    "code": "TREAT",
                                    "concept": [
                                        {
                                            "code": "ADJUNCT",
                                            "definition": "Description: The source act is intended to offer an additional treatment for the management or cure of a pre-existing adverse situation described by the target act. This is not limited to diseases but can apply to any adverse situation or condition of medical or technical nature.  It is not a requirement that the non-adjunctive treatment is explicitly specified.",
                                            "display": "adjunctive treatment",
                                        },
                                        {
                                            "code": "MTREAT",
                                            "definition": "Description: The source act is intended to provide long term maintenance improvement or management of a pre-existing adverse situation described by the target act. This is not limited to diseases but can apply to any adverse situation or condition of medical or technical nature.",
                                            "display": "maintenance treatment",
                                        },
                                        {
                                            "code": "PALLTREAT",
                                            "definition": "Description: The source act is intended to provide palliation for the effects of the target act.",
                                            "display": "palliates",
                                        },
                                        {
                                            "code": "SYMP",
                                            "definition": "Description: The source act is intented to provide symptomatic relief for the effects of the target act.",
                                            "display": "symptomatic relief",
                                        },
                                    ],
                                    "definition": "Description: The source act is intended to improve a pre-existing adverse situation described by the target act. This is not limited to diseases but can apply to any adverse situation or condition of medical or technical nature.",
                                    "display": "treats",
                                },
                            ],
                            "definition": 'Description: The reason or rationale for a service. A reason link is weaker than a trigger, it only suggests that some service may be or might have been a reason for some action, but not that this reason requires/required the action to be taken. Also, as opposed to the trigger, there is no strong timely relation between the reason and the action.  As well as providing various types of information about the rationale for a service, the RSON act relationship is routinely used between a SBADM act and an OBS act to describe the indication for use of a medication.  Child concepts may be used to describe types of indication. \r\n\n                        \n                           Discussion: In prior releases, the code "SUGG" (suggests) was expressed as "an inversion of the reason link." That code has been retired in favor of the inversion indicator that is an attribute of ActRelationship.',
                            "display": "has reason",
                        },
                        {
                            "code": "TRIG",
                            "definition": "A pre-condition that if true should result in the source Act being executed.  The target is in typically in criterion mood.  When reported after the fact (i.e. the criterion has been met) it may be in Event mood.  A delay between the trigger and the triggered action can be specified.\r\n\n                        \n                           Discussion: This includes the concept of a  required act for a service or financial instrument such as an insurance plan or policy. In such cases, the trigger is the occurrence of a specific condition such as coverage limits being exceeded.",
                            "display": "has trigger",
                        },
                    ],
                    "definition": "Specifies under what circumstances (target Act) the source-Act may, must, must not or has occurred",
                    "display": "ActRelationshipConditional",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_ActRelationshipTemporallyPertains",
                    "concept": [
                        {
                            "code": "_ActRelationshipTemporallyPertainsApproximates",
                            "concept": [
                                {
                                    "code": "ENE",
                                    "concept": [
                                        {
                                            "code": "ECW",
                                            "concept": [
                                                {
                                                    "code": "CONCURRENT",
                                                    "definition": "A relationship in which the source act's effective time is the same as the target act's effective time.\r\n\n                        \n                           UsageNote: This code is reflexive.  Therefore its inverse code is itself.",
                                                    "display": "concurrent with",
                                                },
                                                {
                                                    "code": "SBSECWE",
                                                    "definition": "The source Act starts before the start of the target Act, and ends with the target Act.\r\n\n                        \n                           UsageNote: Inverse code is SASECWE",
                                                    "display": "starts before start of, ends with",
                                                },
                                            ],
                                            "definition": "A relationship in which the source act's effective time ends with the end of the target act's effective time.\r\n\n                        \n                           UsageNote: This code is reflexive.  Therefore its inverse code is itself.",
                                            "display": "ends concurrent with",
                                        }
                                    ],
                                    "definition": "A relationship in which the source act's effective time ends near the end of the target act's effective time. Near is defined separately as a time interval.\r\n\n                        \n                           Usage Note: Inverse code is ENS",
                                    "display": "ends near end",
                                },
                                {
                                    "code": "ENS",
                                    "concept": [
                                        {
                                            "code": "ECWS",
                                            "definition": 'The source Act ends when the target act starts (i.e. if we say "ActOne ECWS ActTwo", it means that ActOne ends when ActTwo starts, therefore ActOne is the source and ActTwo is the target).\r\n\n                        \n                           UsageNote: Inverse code is SCWE',
                                            "display": "ends concurrent with start of",
                                        }
                                    ],
                                    "definition": "A relationship in which the source act's effective time ends near the start of the target act's effective time. Near is defined separately as a time interval.\r\n\n                        \n                           Usage Note: Inverse code is ENE",
                                    "display": "ends near start",
                                },
                                {
                                    "code": "SNE",
                                    "concept": [
                                        {
                                            "code": "SCWE",
                                            "definition": 'The source Act starts when the target act ends (i.e. if we say "ActOne SCWE ActTwo", it means that ActOne starts when ActTwo ends, therefore ActOne is the source and ActTwo is the target).\r\n\n                        \n                           UsageNote: Inverse code is SBSECWS',
                                            "display": "starts concurrent with end of",
                                        }
                                    ],
                                    "definition": "A relationship in which the source act's effective time starts near the end of the target act's effective time. Near is defined separately as a time interval.\r\n\n                        \n                           Usage Note: Inverse code is SNS",
                                    "display": "starts near end",
                                },
                                {
                                    "code": "SNS",
                                    "concept": [
                                        {
                                            "code": "SCW",
                                            "concept": [
                                                {
                                                    "code": "SCWSEBE",
                                                    "definition": "The source Act starts with.the target Act and ends before the end of the target Act.\r\n\n                        \n                           UsageNote: Inverse code is SCWSEAE",
                                                    "display": "starts with. ends before end of",
                                                },
                                                {
                                                    "code": "SCWSEAE",
                                                    "definition": "The source Act starts with the target Act, and ends after the end of the target Act.",
                                                    "display": "starts with, ends after end of",
                                                },
                                            ],
                                            "definition": "A relationship in which the source act's effective time starts with the start of the target act's effective time.\r\n\n                        \n                           UsageNote: This code is reflexive.  Therefore its inverse code is itself.",
                                            "display": "starts concurrent with",
                                            "property": [
                                                {
                                                    "code": "child",
                                                    "valueCode": "CONCURRENT",
                                                }
                                            ],
                                        }
                                    ],
                                    "definition": "A relationship in which the source act's effective time starts near the start of the target act's effective time. Near is defined separately as a time interval.\r\n\n                        \n                           Usage Note: Inverse code is SNE",
                                    "display": "starts near start",
                                },
                            ],
                            "definition": "Abstract collector for ActRelationship types that relate two acts by their approximate timing.",
                            "display": "ActRelationshipTemporallyPertainsApproximates",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "EAS",
                            "concept": [
                                {
                                    "code": "EAE",
                                    "concept": [
                                        {
                                            "code": "SASEAE",
                                            "concept": [
                                                {
                                                    "code": "SBEEAE",
                                                    "concept": [
                                                        {
                                                            "code": "SASSBEEAS",
                                                            "definition": "The source Act start after the start of the target Act, and contains the end of the target Act.\r\n\n                        \n                           UsageNote: Inverse code is SBSEASEBE",
                                                            "display": "start after start of, contains end of",
                                                        },
                                                        {
                                                            "code": "SBSEAE",
                                                            "definition": "The source Act contains the time of the target Act.\r\n\n                        \n                           UsageNote: Inverse code is DURING",
                                                            "display": "contains time of",
                                                        },
                                                    ],
                                                    "definition": "The source Act contains the end of the target Act.\r\n\n                        \n                           UsageNote: Inverse code is EDU",
                                                    "display": "contains end of",
                                                    "property": [
                                                        {
                                                            "code": "child",
                                                            "valueCode": "SCWSEAE",
                                                        }
                                                    ],
                                                }
                                            ],
                                            "definition": "The source Act starts after start of the target Act and ends after end of the target Act.\r\n\n                        \n                           UsageNote: Inverse code is SBSEBE",
                                            "display": "starts after start of, ends after end of",
                                            "property": [
                                                {
                                                    "code": "child",
                                                    "valueCode": "SASSBEEAS",
                                                }
                                            ],
                                        }
                                    ],
                                    "definition": "A relationship in which the source act ends after the target act ends.\r\n\n                        \n                           UsageNote: Inverse code is EBE",
                                    "display": "ends after end of",
                                },
                                {
                                    "code": "SAS",
                                    "concept": [
                                        {
                                            "code": "SAE",
                                            "definition": "A relationship in which the source act starts after the target act ends.\r\n\n                        \n                           UsageNote: Inverse code is EBS",
                                            "display": "starts after end of",
                                        },
                                        {
                                            "code": "DURING",
                                            "definition": "A relationship in which the source act's effective time is wholly within the target act's effective time (including end points, as defined in the act's effective times)\r\n\n                        \n                           UsageNote: Inverse code is SBSEAE",
                                            "display": "occurs during",
                                        },
                                        {
                                            "code": "SASECWE",
                                            "definition": "The source Act starts after start of the target Act, and ends with the target Act.\r\n\n                        \n                           UsageNote: Inverse code is SBSECWE",
                                            "display": "starts after start of, ends with",
                                        },
                                    ],
                                    "definition": 'The source Act starts after the start of the target Act (i.e. if we say "ActOne SAS ActTwo", it means that ActOne starts after the start of ActTwo, therefore ActOne is the source and ActTwo is the target).\r\n\n                        \n                           UsageNote: Inverse code is SBS',
                                    "display": "starts after start of",
                                    "property": [
                                        {"code": "child", "valueCode": "SASEAE"}
                                    ],
                                },
                            ],
                            "definition": "A relationship in which the source act ends after the target act starts.\r\n\n                        \n                           UsageNote: Inverse code is SBE",
                            "display": "ends after start of",
                        },
                        {
                            "code": "EASORECWS",
                            "concept": [
                                {
                                    "code": "EAEORECW",
                                    "definition": "A relationship in which the source act's effective time ends after or concurrent with the end of the target act's effective time.\r\n\n                        \n                           Usage Note: Inverse code is EBEORECW",
                                    "display": "ends after or concurrent with end of",
                                    "property": [
                                        {"code": "child", "valueCode": "EAE"},
                                        {"code": "child", "valueCode": "ECW"},
                                    ],
                                }
                            ],
                            "definition": "A relationship in which the source act's effective time ends after or concurrent with the start of the target act's effective time.\r\n\n                        \n                           Usage Note: Inverse code is EBSORECWS",
                            "display": "ends after or concurrent with start of",
                            "property": [
                                {"code": "child", "valueCode": "EAS"},
                                {"code": "child", "valueCode": "ECWS"},
                            ],
                        },
                        {
                            "code": "INDEPENDENT",
                            "definition": "The source Act is independent of the time of the target Act.\r\n\n                        \n                           UsageNote: This code is reflexive.  Therefore its inverse code is itself.",
                            "display": "independent of time of",
                        },
                        {
                            "code": "SAEORSCWE",
                            "definition": "A relationship in which the source act's effective time starts after or concurrent with the end of the target act's effective time.\r\n\n                        \n                           Usage Note: Inverse code is SBEORSCWE",
                            "display": "starts after or concurrent with end of",
                            "property": [
                                {"code": "child", "valueCode": "SCWE"},
                                {"code": "child", "valueCode": "SAE"},
                            ],
                        },
                        {
                            "code": "SASORSCW",
                            "definition": "A relationship in which the source act's effective time starts after or concurrent with the start of the target act's effective time.\r\n\n                        \n                           Usage Note: Inverse code is SBSORSCW",
                            "display": "starts after or concurrent with start of",
                            "property": [
                                {"code": "child", "valueCode": "SAS"},
                                {"code": "child", "valueCode": "SCW"},
                            ],
                        },
                        {
                            "code": "SBEORSCWE",
                            "concept": [
                                {
                                    "code": "OVERLAP",
                                    "concept": [
                                        {
                                            "code": "EDU",
                                            "concept": [
                                                {
                                                    "code": "SBSEASEBE",
                                                    "definition": "The source Act contains the start of the target Act,  and ends before the end of the target Act.\r\n\n                        \n                           UsageNote: Inverse code is SASSBEEAS",
                                                    "display": "contains start of, ends before end of",
                                                }
                                            ],
                                            "definition": "A relationship in which the source act ends within the target act's effective time (including end points, as defined in the act's effective times)\r\n\n                        \n                           UsageNote: Inverse code is SBEEAE",
                                            "display": "ends during",
                                            "property": [
                                                {
                                                    "code": "child",
                                                    "valueCode": "SCWSEBE",
                                                }
                                            ],
                                        },
                                        {
                                            "code": "SBSEAS",
                                            "definition": "The source Act contains the start of the target Act.\r\n\n                        \n                           UsageNote: Inverse code is SDU",
                                            "display": "contains start of",
                                            "property": [
                                                {
                                                    "code": "child",
                                                    "valueCode": "SBSECWE",
                                                },
                                                {
                                                    "code": "child",
                                                    "valueCode": "SBSEASEBE",
                                                },
                                                {
                                                    "code": "child",
                                                    "valueCode": "SBSEAE",
                                                },
                                            ],
                                        },
                                        {
                                            "code": "SDU",
                                            "definition": "A relationship in which the source act starts within the target act's effective time (including end points, as defined in the act's effective times)\r\n\n                        \n                           UsageNote: Inverse code is SBSEAS",
                                            "display": "starts during",
                                            "property": [
                                                {
                                                    "code": "child",
                                                    "valueCode": "SASSBEEAS",
                                                }
                                            ],
                                        },
                                    ],
                                    "definition": "A relationship in which the source act's effective time overlaps the target act's effective time in any way.\r\n\n                        \n                           UsageNote: This code is reflexive.  Therefore its inverse code is itself.",
                                    "display": "overlaps with",
                                    "property": [
                                        {"code": "child", "valueCode": "ECW"},
                                        {"code": "child", "valueCode": "SBEEAE"},
                                        {"code": "child", "valueCode": "SCW"},
                                        {"code": "child", "valueCode": "SCWE"},
                                    ],
                                },
                                {
                                    "code": "SBE",
                                    "concept": [
                                        {
                                            "code": "EBE",
                                            "concept": [
                                                {
                                                    "code": "SBSEBE",
                                                    "concept": [
                                                        {
                                                            "code": "EBSORECWS",
                                                            "concept": [
                                                                {
                                                                    "code": "EBS",
                                                                    "definition": "A relationship in which the source act ends before the target act starts.\r\n\n                        \n                           UsageNote: Inverse code is SAE",
                                                                    "display": "ends before start of",
                                                                }
                                                            ],
                                                            "definition": "A relationship in which the source act's effective time ends before or concurrent with the start of the target act's effective time.\r\n\n                        \n                           Usage Note: Inverse code is EASORECWS",
                                                            "display": "ends before or concurrent with start of",
                                                            "property": [
                                                                {
                                                                    "code": "child",
                                                                    "valueCode": "ECWS",
                                                                }
                                                            ],
                                                        }
                                                    ],
                                                    "definition": "The source Act starts before the start of the target Act, and ends before the end of the target Act.\r\n\n                        \n                           UsageNote: Inverse code is SASEAE",
                                                    "display": "starts before start of, ends before end of",
                                                    "property": [
                                                        {
                                                            "code": "child",
                                                            "valueCode": "SBSEASEBE",
                                                        }
                                                    ],
                                                }
                                            ],
                                            "definition": 'The source Act ends before the end of the target Act (i.e. if we say "ActOne EBE ActTwo", it means that ActOne ends before the end of ActTwo, therefore ActOne is the source and ActTwo is the target).\r\n\n                        \n                           UsageNote: Inverse code is EAE',
                                            "display": "ends before end of",
                                        },
                                        {
                                            "code": "EBEORECW",
                                            "definition": "A relationship in which the source act's effective time ends before or concurrent with the end of the target act's effective time.\r\n\n                        \n                           Usage Note: Inverse code is EAEORECW",
                                            "display": "ends before or concurrent with end of",
                                            "property": [
                                                {"code": "child", "valueCode": "ECW"},
                                                {"code": "child", "valueCode": "EBE"},
                                            ],
                                        },
                                        {
                                            "code": "SBSORSCW",
                                            "concept": [
                                                {
                                                    "code": "SBS",
                                                    "definition": "A relationship in which the source act begins before the target act begins.\r\n\n                        \n                           UsageNote: Inverse code is SAS",
                                                    "display": "starts before start of",
                                                    "property": [
                                                        {
                                                            "code": "child",
                                                            "valueCode": "SBSEBE",
                                                        },
                                                        {
                                                            "code": "child",
                                                            "valueCode": "SBSEAS",
                                                        },
                                                    ],
                                                }
                                            ],
                                            "definition": "A relationship in which the source act's effective time starts before or concurrent with the start of the target act's effective time.\r\n\n                        \n                           Usage Note: Inverse code is SASORSCW",
                                            "display": "starts before or concurrent with start of",
                                            "property": [
                                                {"code": "child", "valueCode": "SCW"}
                                            ],
                                        },
                                    ],
                                    "definition": 'The source Act starts before the end of the target Act (i.e. if we say "ActOne SBE ActTwo", it means that ActOne starts before the end of ActTwo, therefore ActOne is the source and ActTwo is the target).\r\n\n                        \n                           UsageNote: Inverse code is EAS',
                                    "display": "starts before end of",
                                    "property": [
                                        {"code": "child", "valueCode": "SBSEASEBE"},
                                        {"code": "child", "valueCode": "SCWSEBE"},
                                    ],
                                },
                            ],
                            "definition": "A relationship in which the source act's effective time starts before or concurrent with the end of the target act's effective time.\r\n\n                        \n                           Usage Note: Inverse code is SAEORSCWE",
                            "display": "starts before or concurrent with end of",
                        },
                    ],
                    "definition": "Abstract collector for ActRelationhsip types that relate two acts by their timing.",
                    "display": "ActRelationshipTemporallyPertains",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "AUTH",
                    "definition": "A relationship in which the target act authorizes or certifies the source act.",
                    "display": "authorized by",
                },
                {
                    "code": "CAUS",
                    "definition": "Description: An assertion that an act was the cause of another act.This is stronger and more specific than the support link. The source (cause) is typically an observation, but may be any act, while the target may be any act.\r\n\n                        \n                           Examples:\n                        \r\n\n                        \n                           a growth of Staphylococcus aureus may be considered the cause of an abscess\n                           contamination of the infusion bag was deemed to be the cause of the infection that the patient experienced\n                           lack of staff on the shift was deemed to be a supporting factor (proximal factor) causing the patient safety incident where the patient fell out of bed because the  bed-sides had not been put up which caused the night patient to fall out of bed",
                    "display": "is etiology for",
                },
                {
                    "code": "COMP",
                    "concept": [
                        {
                            "code": "CTRLV",
                            "definition": "A relationship from an Act to a Control Variable.  For example, if a Device makes an Observation, this relates the Observation to its Control Variables documenting  the device's settings that influenced the observation.",
                            "display": "has control variable",
                        },
                        {
                            "code": "MBR",
                            "concept": [
                                {
                                    "code": "STEP",
                                    "concept": [
                                        {
                                            "code": "ARR",
                                            "definition": "The relationship that links to a Transportation Act (target) from another Act (source) indicating that the subject of the source Act entered into the source Act by means of the target Transportation act.",
                                            "display": "arrival",
                                        },
                                        {
                                            "code": "DEP",
                                            "definition": "The relationship that links to a Transportation Act (target) from another Act (source) indicating that the subject of the source Act departed from the source Act by means of the target Transportation act.",
                                            "display": "departure",
                                        },
                                    ],
                                    "definition": "A collection of sub-services as steps or subtasks performed for the source service. Services may be performed sequentially or concurrently.\r\n\n                        \n                           UsageNotes: Sequence of steps may be indicated by use of _ActRelationshipTemporallyPertains, as well as via  ActRelationship.sequenceNumber, ActRelationship.pauseQuantity, Target.priorityCode.\r\n\n                        \n                           OpenIssue: Need Additional guidelines on when each approach should be used.",
                                    "display": "has step",
                                }
                            ],
                            "definition": "The target Acts are aggregated by the source Act.  Target Acts may have independent existence, participate in multiple ActRelationships, and do not contribute to the meaning of the source.\r\n\n                        \n                           UsageNotes: This explicitly represents the conventional notion of aggregation.  The target Act is part of a collection of Acts (no implication is made of cardinality, a source of Acts may contain zero, one, or more member target Acts).\r\n\n                        It is expected that this will be primarily used with _ActClassRecordOrganizer, BATTERY, and LIST",
                            "display": "has member",
                        },
                        {
                            "code": "PART",
                            "definition": 'The source Act is a composite of the target Acts. The target Acts do not have an existence independent of the source Act.\r\n\n                        \n                           UsageNote: In UML 1.1, this is a "composition" defined as: \n                           "A form of aggregation with strong ownership and coincident lifetime as part of the whole. Parts with non-fixed multiplicity may be created after the composite itself, but once created they live and die with it (i.e., they share lifetimes). Such parts can also be explicitly removed before the death of the composite. Composition may be recursive."',
                            "display": "has part",
                        },
                    ],
                    "definition": "The target act is a component of the source act, with no semantics regarding composition or aggregation implied.",
                    "display": "has component",
                },
                {
                    "code": "COVBY",
                    "definition": "A relationship in which the source act is covered by or is under the authority of a target act.  A financial instrument such as an Invoice Element is covered by one or more specific instances of an Insurance Policy.",
                    "display": "covered by",
                },
                {
                    "code": "DRIV",
                    "definition": "Associates a derived Act with its input parameters. E.G., an anion-gap observation can be associated as being derived from given sodium-, (potassium-,), chloride-, and bicarbonate-observations. The narrative content (Act.text) of a source act is wholly machine-derived from the collection of target acts.",
                    "display": "is derived from",
                },
                {
                    "code": "ELNK",
                    "definition": "Expresses an association that links two instances of the same act over time, indicating that the instance are part of the same episode, e.g. linking two condition nodes for episode of illness; linking two encounters for episode of encounter.",
                    "display": "episodeLink",
                },
                {
                    "code": "EVID",
                    "definition": "Indicates that the target Act provides evidence in support of the action represented by the source Act. The target is not a 'reason' for the source act, but rather gives supporting information on why the source act is an appropriate course of action. Possible targets might be clinical trial results, journal articles, similar successful therapies, etc.\r\n\n                        \n                           Rationale: Provides a mechanism for conveying clinical justification for non-approved or otherwise non-traditional therapies.",
                    "display": "provides evidence for",
                },
                {
                    "code": "EXACBY",
                    "definition": 'Description:The source act is aggravated by the target act. (Example "chest pain" EXACBY "exercise")',
                    "display": "exacerbated by",
                },
                {
                    "code": "EXPL",
                    "definition": "This is the inversion of support.  Used to indicate that a given observation is explained by another observation or condition.",
                    "display": "has explanation",
                },
                {
                    "code": "INTF",
                    "definition": "the target act documents a set of circumstances (events, risks) which prevent successful completion, or degradation of quality of, the source Act.\r\n\n                        \n                           UsageNote: This provides the semantics to document barriers to care",
                    "display": "interfered by",
                },
                {
                    "code": "ITEMSLOC",
                    "definition": "Items located",
                    "display": "items located",
                },
                {
                    "code": "LIMIT",
                    "definition": "A relationship that limits or restricts the source act by the elements of the target act.  For example, an authorization may be limited by a financial amount (up to $500). Target Act must be in EVN.CRIT mood.",
                    "display": "limited by",
                },
                {
                    "code": "META",
                    "definition": 'Definition: Indicates that the attributes and associations of the target act provide metadata (for example, identifiers, authorship, etc.) for the source act.\r\n\n                        \n                           Constraint:  Source act must have either a mood code that is not "EVN" (event) or its "isCriterion" attribute must set to "true".  Target act must be an Act with a mood code of EVN and with isCriterionInd attribute set to "true".',
                    "display": "has metadata",
                },
                {
                    "code": "MFST",
                    "definition": "An assertion that a new observation may be the manifestation of another existing observation or action.  This assumption is attributed to the same actor who asserts the manifestation.  This is stronger and more specific than an inverted support link.  For example, an agitated appearance can be asserted to be the manifestation (effect) of a known hyperthyroxia.  This expresses that one might not have realized a symptom if it would not be a common manifestation of a known condition.  The target (cause) may be any service, while the source (manifestation) must be an observation.",
                    "display": "is manifestation of",
                },
                {
                    "code": "NAME",
                    "definition": 'Used to assign a "name" to a condition thread. Source is a condition node, target can be any service.',
                    "display": "assigns name",
                },
                {
                    "code": "OUTC",
                    "concept": [
                        {
                            "code": "_ActRelationsipObjective",
                            "concept": [
                                {
                                    "code": "OBJC",
                                    "definition": "A desired state that a service action aims to maintain.  E.g., keep systolic blood pressure between 90 and 110 mm Hg.  Source is an intervention service.  Target must be an observation in criterion mood.",
                                    "display": "has continuing objective",
                                },
                                {
                                    "code": "OBJF",
                                    "definition": "A desired outcome that a service action aims to meet finally.  Source is any service (typically an intervention).  Target must be an observation in criterion mood.",
                                    "display": "has final objective",
                                },
                            ],
                            "definition": "The target act is a desired outcome of the source act. Source is any act (typically an intervention). Target must be an observation in criterion mood.",
                            "display": "Act Relationsip Objective",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "GOAL",
                            "definition": "A goal that one defines given a patient's health condition.  Subsequently planned actions aim to meet that goal.  Source is an observation or condition node, target must be an observation in goal mood.",
                            "display": "has goal",
                        },
                        {
                            "code": "RISK",
                            "definition": "A noteworthy undesired outcome of a patient's condition that is either likely enough to become an issue or is less likely but dangerous enough to be addressed.",
                            "display": "has risk",
                        },
                    ],
                    "definition": 'An observation that should follow or does actually follow as a result or consequence of a condition or action (sometimes called "post-conditional".) Target must be an observation as a goal, risk or any criterion. For complex outcomes a conjunction attribute (AND, OR, XOR) can be used.  An outcome link is often inverted to describe an outcome assessment.',
                    "display": "has outcome",
                },
                {
                    "code": "PERT",
                    "definition": "This is a very unspecific relationship from one item of clinical information to another.  It does not judge about the role the pertinent information plays.",
                    "display": "has pertinent information",
                },
                {
                    "code": "PREV",
                    "definition": "A relationship in which the target act is a predecessor instance to the source act.  Generally each of these instances is similar, but no identical.  In healthcare coverage it is used to link a claim item to a previous claim item that might have claimed for the same set of services.",
                    "display": "has previous instance",
                },
                {
                    "code": "REFR",
                    "concept": [
                        {
                            "code": "USE",
                            "definition": 'Indicates that the source act makes use of (or will make use of) the information content of the target act.\r\n\n                        \n                           UsageNotes: A usage relationship only makes sense if the target act is authored and occurs independently of the source act.  Otherwise a simpler relationship such as COMP would be appropriate.\r\n\n                        \n                           Rationale: There is a need when defining a clinical trial protocol to indicate that the protocol makes use of other protocol or treatment specifications.  This is stronger than the assertion of "references".  References may exist without usage, and in a clinical trial protocol is common to assert both: what other specifications does this trial use and what other specifications does it merely reference.',
                            "display": "uses",
                        }
                    ],
                    "definition": "A relationship in which the target act is referred to by the source act.  This permits a simple reference relationship that distinguishes between the referent and the referee.",
                    "display": "refers to",
                },
                {
                    "code": "REFV",
                    "definition": 'Reference ranges are essentially descriptors of a class of result values assumed to be "normal", "abnormal", or "critical."  Those can vary by sex, age, or any other criterion. Source and target are observations, the target is in criterion mood.  This link type can act as a trigger in case of alarms being triggered by critical results.',
                    "display": "has reference values",
                },
                {
                    "code": "RELVBY",
                    "definition": 'Description:The source act is wholly or partially alleviated by the target act. (Example "chest pain" RELVBY "sublingual nitroglycerin administration")',
                    "display": "relieved by",
                },
                {
                    "code": "SEQL",
                    "concept": [
                        {
                            "code": "APND",
                            "definition": "An addendum (source) to an existing service object (target), containing supplemental information.  The addendum is itself an original service object linked to the supplemented service object.  The supplemented service object remains in place and its content and status are unaltered.",
                            "display": "is appendage",
                        },
                        {
                            "code": "BSLN",
                            "definition": "Indicates that the target observation(s) provide an initial reference for the source observation or observation group.\r\n\n                        \n                           UsageConstraints: Both source and target must be Observations or specializations thereof.",
                            "display": "has baseline",
                        },
                        {
                            "code": "COMPLY",
                            "definition": "Description:The source act complies with, adheres to, conforms to, or is permissible under (in whole or in part) the policy, contract, agreement, law, conformance criteria, certification guidelines or requirement conveyed by the target act.\r\n\n                        Examples for compliance relationships are: audits of adherence with a security policy, certificate of conformance to system certification requirements, or consent directive in compliance with or permissible under a privacy policy.",
                            "display": "complies with",
                        },
                        {
                            "code": "DOC",
                            "definition": "The source act documents the target act.",
                            "display": "documents",
                        },
                        {
                            "code": "FLFS",
                            "concept": [
                                {
                                    "code": "OCCR",
                                    "definition": 'The source act is a single occurrence of a repeatable target act. The source and target act can be in any mood on the "completion track" but the source act must be as far as or further along the track than the target act (i.e., the occurrence of an intent can be an event but not vice versa).',
                                    "display": "occurrence",
                                },
                                {
                                    "code": "OREF",
                                    "definition": "Relates either an appointment request or an appointment to the order for the service being scheduled.",
                                    "display": "references order",
                                },
                                {
                                    "code": "SCH",
                                    "definition": "Associates a specific time (and associated resources) with a scheduling request or other intent.",
                                    "display": "schedules request",
                                },
                            ],
                            "definition": "The source act fulfills (in whole or in part) the target act. Source act must be in a mood equal or more actual than the target act.",
                            "display": "fulfills",
                        },
                        {
                            "code": "GEN",
                            "definition": "The generalization relationship can be used to express categorical knowledge about services (e.g., amilorid, triamterene, and spironolactone have the common generalization potassium sparing diuretic).",
                            "display": "has generalization",
                        },
                        {
                            "code": "GEVL",
                            "definition": 'A goal-evaluation links an observation (intent or actual) to a goal to indicate that the observation evaluates the goal. Given the goal and the observation, a "goal distance" (e.g., goal to observation) can be "calculated" and need not be sent explicitly.',
                            "display": "evaluates (goal)",
                        },
                        {
                            "code": "INST",
                            "definition": 'Used to capture the link between a potential service ("master" or plan) and an actual service, where the actual service instantiates the potential service. The instantiation may override the master\'s defaults.',
                            "display": "instantiates (master)",
                        },
                        {
                            "code": "MOD",
                            "definition": "Definition: Used to link a newer version or 'snapshot' of a business object (source) to an older version or 'snapshot' of the same business object (target).\r\n\n                        \n                           Usage:The identifier of the Act should be the same for both source and target. If the identifiers are distinct, RPLC should be used instead.\r\n\n                        Name from source to target = \"modifiesPrior\"\r\n\n                        Name from target to source = \"modifiesByNew\"",
                            "display": "modifies",
                        },
                        {
                            "code": "MTCH",
                            "definition": 'A trigger-match links an actual service (e.g., an observation or procedure that took place) with a service in criterion mood.  For example if the trigger is "observation of pain" and pain is actually observed, and if that pain-observation caused the trigger to fire, that pain-observation can be linked with the trigger.',
                            "display": "matches (trigger)",
                        },
                        {
                            "code": "OPTN",
                            "definition": "A relationship between a source Act that provides more detailed properties to the target Act.\r\n\n                        The source act thus is a specialization of the target act, but instead of mentioning all the inherited properties it only mentions new property bindings or refinements.\r\n\n                        The typical use case is to specify certain alternative variants of one kind of Act. The priorityNumber attribute is used to weigh refinements as preferred over other alternative refinements.\r\n\n                        Example: several routing options for a drug are specified as one SubstanceAdministration for the general treatment with attached refinements for the various routing options.",
                            "display": "has option",
                        },
                        {
                            "code": "RCHAL",
                            "definition": "Description:A relationship in which the target act is carried out to determine whether an effect attributed to the source act can be recreated.",
                            "display": "re-challenge",
                        },
                        {
                            "code": "REV",
                            "definition": 'A relationship between a source Act that seeks to reverse or undo the action of the prior target Act.\r\n\n                        Example: A posted financial transaction (e.g., a debit transaction) was applied in error and must be reversed (e.g., by a credit transaction) the credit transaction is identified as an undo (or reversal) of the prior target transaction.\r\n\n                        Constraints: the "completion track" mood of the target Act must be equally or more "actual" than the source act. I.e., when the target act is EVN the source act can be EVN, or any INT. If the target act is INT, the source act can be INT.',
                            "display": "reverses",
                        },
                        {
                            "code": "RPLC",
                            "definition": "A replacement source act replaces an existing target act. The state of the target act being replaced becomes obselete, but the act is typically still retained in the system for historical reference.  The source and target must be of the same type.",
                            "display": "replaces",
                        },
                        {
                            "code": "SUCC",
                            "definition": "Definition:  A new act that carries forward the intention of the original act, but does not completely replace it.  The status of the predecessor act must be 'completed'.  The original act is the target act and the successor is the source act.",
                            "display": "succeeds",
                        },
                        {
                            "code": "UPDT",
                            "definition": "A condition thread relationship specifically links condition nodes together to form a condition thread. The source is the new condition node and the target links to the most recent node of the existing condition thread.",
                            "display": "updates (condition)",
                        },
                        {
                            "code": "XCRPT",
                            "concept": [
                                {
                                    "code": "VRXCRPT",
                                    "definition": "The source is a direct quote from the target.",
                                    "display": "Excerpt verbatim",
                                }
                            ],
                            "definition": "The source is an excerpt from the target.",
                            "display": "Excerpts",
                        },
                        {
                            "code": "XFRM",
                            "definition": "Used when the target Act is a transformation of the source Act. (For instance, used to show that a CDA document is a transformation of a DICOM SR document.)",
                            "display": "transformation",
                        },
                    ],
                    "definition": "An act relationship indicating that the source act follows the target act. The source act should in principle represent the same kind of act as the target. Source and target need not have the same mood code (mood will often differ). The target of a sequel is called antecedent. Examples for sequel relationships are: revision, transformation, derivation from a prototype (as a specialization is a derivation of a generalization), followup, realization, instantiation.",
                    "display": "is sequel",
                },
                {
                    "code": "SPRT",
                    "concept": [
                        {
                            "code": "SPRTBND",
                            "definition": 'A specialization of "has support" (SPRT), used to relate a secondary observation to a Region of Interest on a multidimensional observation, if the ROI specifies the true boundaries of the secondary observation as opposed to only marking the approximate area.  For example, if the start and end of an ST elevation episode is visible in an EKG, this relation would indicate the ROI bounds the  "ST elevation" observation -- the ROI defines the true beginning and ending of the episode.  Conversely, if a ROI simply contains ST elevation, but it does not define the bounds (start and end) of the episode, the more general "has support" relation is used.  Likewise, if a ROI on an image defines the true bounds of a "1st degree burn", the relation "has bounded support" is used; but if the ROI only points to the approximate area of the burn, the general "has support" relation is used.',
                            "display": "has bounded support",
                        }
                    ],
                    "definition": "Used to indicate that an existing service is suggesting evidence for a new observation. The assumption of support is attributed to the same actor who asserts the observation. Source must be an observation, target may be any service  (e.g., to indicate a status post).",
                    "display": "has support",
                },
                {
                    "code": "SUBJ",
                    "concept": [
                        {
                            "code": "QUALF",
                            "definition": "The target observation qualifies (refines) the semantics of the source observation.\r\n\n                        \n                           UsageNote: This is not intended to replace concept refinement and qualification via vocabulary.  It is used when there are multiple components which together provide the complete understanding of the source Act.",
                            "display": "has qualifier",
                        }
                    ],
                    "definition": 'Relates an Act to its subject Act that the first Act is primarily concerned with.\r\n\n                        Examples\r\n\n                        \n                           \n                              The first Act may be a ControlAct manipulating the subject Act \r\n\n                           \n                           \n                              The first act is a region of interest (ROI) that defines a region within the subject Act.\r\n\n                           \n                           \n                              The first act is a reporting or notification Act, that echos the subject Act for a specific new purpose.\r\n\n                           \n                        \n                        Constraints\r\n\n                        An Act may have multiple subject acts.\r\n\n                        Rationale\r\n\n                        The ActRelationshipType "has subject" is similar to the ParticipationType "subject", Acts that primarily operate on physical subjects use the Participation, those Acts that primarily operate on other Acts (other information) use the ActRelationship.',
                    "display": "has subject",
                },
                {
                    "code": "SUMM",
                    "definition": "An act that contains summary values for a list or set of subordinate acts.  For example, a summary of transactions for a particular accounting period.",
                    "display": "summarized by",
                },
                {
                    "code": "VALUE",
                    "definition": 'Description:Indicates that the target Act represents the result of the source observation Act.\r\n\n                        \n                           FormalConstraint: Source Act must be an Observation or specialization there-of. Source Act must not have the value attribute specified\r\n\n                        \n                           UsageNote: This relationship allows the result of an observation to be fully expressed as RIM acts as opposed to being embedded in the value attribute.  For example, sending a Document act as the result of an imaging observation, sending a list of Procedures and/or other acts as the result of a medical history observation.\r\n\n                        The valueNegationInd attribute on the source Act has the same semantics of "negated finding" when it applies to the target of a VALUE ActRelationship as it does to the value attribute.  On the other hand, if the ActRelationship.negationInd is true for a VALUE ActRelationship, that means the specified observation does not have the indicated value but does not imply a negated finding.  Because the semantics are extremely close, it is recommended that Observation.valueNegationInd be used, not ActRelationship.negationInd.\r\n\n                        \n                           OpenIssue: The implications of negationInd on ActRelationship and the valueNegationind on Observation.',
                    "display": "has value",
                },
            ],
            "definition": "Description: A directed association between a source Act and a target Act.\r\n\n                        \n                           Usage Note: This code should never be transmitted in an instance as the value of ActRelationship.typeCode (attribute)",
            "display": "act relationship type",
        }
    )
    """
    act relationship type

    Description: A directed association between a source Act and a target Act.

                        
                           Usage Note: This code should never be transmitted in an instance as the value of ActRelationship.typeCode (attribute)
    """

    cure = CodeSystemConcept(
        {
            "code": "CURE",
            "definition": "curative indication",
            "display": "curative indication",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    curative indication

    curative indication
    """

    cure_adj = CodeSystemConcept(
        {
            "code": "CURE.ADJ",
            "definition": "adjunct curative indication",
            "display": "adjunct curative indication",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    adjunct curative indication

    adjunct curative indication
    """

    mtgt_adj = CodeSystemConcept(
        {
            "code": "MTGT.ADJ",
            "definition": "adjunct mitigation",
            "display": "adjunct mitigation",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    adjunct mitigation

    adjunct mitigation
    """

    ract = CodeSystemConcept(
        {"code": "RACT", "property": [{"code": "status", "valueCode": "retired"}]}
    )
    """
    None

    
    """

    sugg = CodeSystemConcept(
        {"code": "SUGG", "property": [{"code": "status", "valueCode": "retired"}]}
    )
    """
    None

    
    """

    class Meta:
        resource = _resource
