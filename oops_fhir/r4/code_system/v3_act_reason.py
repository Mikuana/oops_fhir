from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ActReason"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ActReason:
    """
    v3 Code System ActReason

     A set of codes specifying the motivation, cause, or rationale of an
Act, when such rationale is not reasonably represented as an
ActRelationship of type "has reason" linking to another Act.  Examples:
Example reasons that might qualify for being coded in this field might
be: "routine requirement", "infectious disease reporting requirement",
"on patient request", "required by law".

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ActReason
    """

    underscore_act_accommodation_reason = CodeSystemConcept(
        {
            "code": "_ActAccommodationReason",
            "concept": [
                {
                    "code": "ACCREQNA",
                    "definition": "Accommodation requested is not available.",
                    "display": "Accommodation Requested Not Available",
                },
                {
                    "code": "FLRCNV",
                    "definition": "Accommodation is assigned for floor convenience.",
                    "display": "Floor Convenience",
                },
                {
                    "code": "MEDNEC",
                    "definition": "Required for medical reasons(s).",
                    "display": "Medical Necessity",
                },
                {
                    "code": "PAT",
                    "definition": "The Patient requested the action",
                    "display": "Patient request",
                },
            ],
            "definition": "Identifies the reason the patient is assigned to this accommodation type",
            "display": "ActAccommodationReason",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActAccommodationReason

    Identifies the reason the patient is assigned to this accommodation type
    """

    underscore_act_coverage_reason = CodeSystemConcept(
        {
            "code": "_ActCoverageReason",
            "concept": [
                {
                    "code": "_EligibilityActReasonCode",
                    "concept": [
                        {
                            "code": "_ActIneligibilityReason",
                            "concept": [
                                {
                                    "code": "COVSUS",
                                    "definition": "When a client has no contact with the health system for an extended period, coverage is suspended.  Client will be reinstated to original start date upon proof of identification, residency etc.\r\n\n                        Example: Coverage may be suspended during a strike situation, when employer benefits for employees are not covered (i.e. not in effect).",
                                    "display": "coverage suspended",
                                },
                                {
                                    "code": "DECSD",
                                    "definition": "Client deceased.",
                                    "display": "deceased",
                                },
                                {
                                    "code": "REGERR",
                                    "definition": "Client was registered in error.",
                                    "display": "registered in error",
                                },
                            ],
                            "definition": "Identifies the reason or rational for why a person is not eligibile for benefits under an insurance policy.\r\n\n                        Examples are client deceased & adopted client has been given a new policy identifier.",
                            "display": "ActIneligibilityReason",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_CoverageEligibilityReason",
                            "concept": [
                                {
                                    "code": "AGE",
                                    "definition": "A person becomes eligible for a program based on age.\r\n\n                        \n                           Example:  In the U.S., a person who is 65 years of age or older is eligible for Medicare.",
                                    "display": "age eligibility",
                                },
                                {
                                    "code": "CRIME",
                                    "definition": "A person becomes eligible for insurance or a program because of crime related health condition or injury. \r\n\n                        \n                           Example:  A person is a claimant under the U.S. Crime Victims Compensation program.",
                                    "display": "crime victim",
                                },
                                {
                                    "code": "DIS",
                                    "definition": "A person becomes a claimant under a disability income insurance policy or a disability rehabilitation program because of a health condition or injury which limits the person's ability to earn an income or function without institutionalization.",
                                    "display": "disability",
                                },
                                {
                                    "code": "EMPLOY",
                                    "definition": "A person becomes eligible for insurance provided as an employment benefit based on employment status.",
                                    "display": "employment benefit",
                                },
                                {
                                    "code": "FINAN",
                                    "definition": "A person becomes eligible for a program based on financial criteria.\r\n\n                        \n                           Example:  A person whose family income is below a financial threshold for eligibility for Medicaid or SCHIP.",
                                    "display": "financial eligibility",
                                },
                                {
                                    "code": "HEALTH",
                                    "definition": "A person becomes eligible for a program because of a qualifying health condition or injury. \r\n\n                        \n                           Examples:  A person is determined to have a qualifying health conditions include pregnancy, HIV/AIDs, tuberculosis, end stage renal disease, breast or cervical cancer, or other condition requiring specialized health services, hospice, institutional or community based care provided under a program",
                                    "display": "health status",
                                },
                                {
                                    "code": "MULTI",
                                    "definition": "A person becomes eligible for a program based on more than one criterion.\r\n\n                        \n                           Examples:  In the U.S., a child whose familiy income meets Medicaid financial thresholds and whose age is less than 18 is eligible for the Early and Periodic Screening, Diagnostic, and Treatment program (EPSDT).  A person whose family income meets Medicaid financial thresholds and whose age is 65 years or older is eligible for Medicaid and Medicare, and are referred to as dual eligibles.",
                                    "display": "multiple criteria eligibility",
                                },
                                {
                                    "code": "PNC",
                                    "definition": "A person becomes a claimant under a property and casualty insurance policy because of a related health condition or injury resulting from a circumstance covered under the terms of the policy. \r\n\n                        \n                           Example:  A person is a claimant under a homeowners insurance policy because of an injury sustained on the policyholderaTMs premises.",
                                    "display": "property and casualty condition",
                                },
                                {
                                    "code": "STATUTORY",
                                    "definition": "A person becomes eligible for a program based on statutory criteria.\r\n\n                        \n                           Examples:  A person is a member of an indigenous group, a veteran of military service, or  in the U.S., a recipient of adoption assistance and foster care under Title IV-E of the Social Security.",
                                    "display": "statutory eligibility",
                                },
                                {
                                    "code": "VEHIC",
                                    "definition": "A person becomes a claimant under a motor vehicle accident insurance because of a motor vehicle accident related health condition or injury.",
                                    "display": "motor vehicle accident victim",
                                },
                                {
                                    "code": "WORK",
                                    "definition": "A person becomes eligible for insurance or a program because of a work related health condition or injury. \r\n\n                        \n                           Example:  A person is a claimant under the U.S. Black Lung Program.",
                                    "display": "work related",
                                },
                            ],
                            "definition": "Definition: Identifies the reason or rational for why a person is eligibile for benefits under an insurance policy or progam. \r\n\n                        \n                           Examples:  A person is a claimant under an automobile insurance policy are client deceased & adopted client has been given a new policy identifier.  A new employee is eligible for health insurance as an employment benefit.  A person meets a government program eligibility criteria for financial, age or health status.",
                            "display": "CoverageEligibilityReason",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                    ],
                    "definition": "Identifies the reason or rational for why a person is eligibile for benefits under an insurance policy or progam. \r\n\n                        \n                           Examples:  A person is a claimant under an automobile insurance policy are client deceased & adopted client has been given a new policy identifier.  A new employee is eligible for health insurance as an employment benefit.  A person meets a government program eligibility criteria for financial, age or health status.",
                    "display": "EligibilityActReasonCode",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                }
            ],
            "definition": "Description:Codes used to specify reasons or criteria relating to coverage provided under a policy or program.  May be used to convey reasons pertaining to coverage contractual provisions, including criteria for eligibility, coverage limitations, coverage maximums, or financial participation required of covered parties.",
            "display": "ActCoverageReason",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActCoverageReason

    Description:Codes used to specify reasons or criteria relating to coverage provided under a policy or program.  May be used to convey reasons pertaining to coverage contractual provisions, including criteria for eligibility, coverage limitations, coverage maximums, or financial participation required of covered parties.
    """

    underscore_act_information_management_reason = CodeSystemConcept(
        {
            "code": "_ActInformationManagementReason",
            "concept": [
                {
                    "code": "_ActHealthInformationManagementReason",
                    "concept": [
                        {
                            "code": "_ActConsentInformationAccessOverrideReason",
                            "concept": [
                                {
                                    "code": "OVRER",
                                    "definition": "To perform one or more operations on information to which the patient has not consented by authorized entities for treating a condition which poses an immediate threat to the patient's health and which requires immediate medical intervention.\r\n\n                        \n                           Usage Notes: The patient is unable to provide consent, but the provider determines they have an urgent healthcare related reason to access the record.",
                                    "display": "emergency treatment override",
                                },
                                {
                                    "code": "OVRINCOMP",
                                    "definition": 'To perform one or more operations on information to which the patient has not consented because deemed incompetent to provide consent.\r\n\n                        \n                           Usage Note: Maps to v2 CON-16 Subject Competence Indicator (ID) 01791 Definition: Identifies whether the subject was deemed competent to provide consent. Refer to table HL7 Table 0136 - Yes/No Indicator and CON-23 Non-Subject Consenter Reason User-defined Table 0502 - Non-Subject Consenter Reason code NC "Subject is not competent to consent".',
                                    "display": "incompetency override",
                                },
                                {
                                    "code": "OVRPJ",
                                    "definition": "To perform one or more operations on information to which the patient declined to consent for providing health care.\r\n\n                        \n                           Usage Notes: The patient, while able to give consent, has not.  However the provider believes it is in the patient's interest to access the record without patient consent.",
                                    "display": "professional judgment override",
                                },
                                {
                                    "code": "OVRPS",
                                    "definition": "To perform one or more operations on information to which the patient has not consented for public safety reasons.\r\n\n                        \n                           Usage Notes: The patient, while able to give consent, has not.  However, the provider believes that access to masked patient information is justified because of concerns related to public safety.",
                                    "display": "public safety override",
                                },
                                {
                                    "code": "OVRTPS",
                                    "definition": "To perform one or more operations on information to which the patient has not consented for third party safety.  \r\n\n                        \n                           Usage Notes: The patient, while able to give consent, has not.  However, the provider believes that access to masked patient information is justified because of concerns related to the health and safety of one or more third parties.",
                                    "display": "third party safety override",
                                },
                            ],
                            "definition": "To perform one or more operations on information to which the patient has not consented as deemed necessary by authorized entities for providing care in the best interest of the patient; providing immediately needed health care for an emergent condition;  or for protecting public or third party safety.\r\n\n                        \n                           Usage Notes: Used to convey the reason that a provider or other entity may or has accessed personal healthcare information.  Typically, this involves overriding the subject's consent directives.",
                            "display": "ActConsentInformationAccessOverrideReason",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "PurposeOfUse",
                            "concept": [
                                {
                                    "code": "HMARKT",
                                    "definition": "To perform one or more operations on information for marketing services and products related to health care.",
                                    "display": "healthcare marketing",
                                },
                                {
                                    "code": "HOPERAT",
                                    "concept": [
                                        {
                                            "code": "CAREMGT",
                                            "definition": 'To perform analytics, evaluation and other secondary uses of treatment and healthcare related information to manage the quality, efficacy, patient safety, population health, and cost effectiveness of healthcare delivery. Explicitly excludes the use of information to organize the delivery of health care for care coordination and case management, or to provide healthcare treatment.\r\n\n                        \n                           Usage Note: The concept of care management is narrower than the list of activities related to more general organizational objectives such as provider profiling, education of healthcare and non-healthcare professionals; insurance underwriting, premium rating, reinsurance; organizational legal, medical review, auditing, compliance and fraud and abuse detection; business planning, development, and restructuring; fund-raising; and customer service.\r\n\n                        \n                           Map: Maps to ISO 14265 Classification Term "Health service management and quality assurance" described as "To inform persons or processes responsible for determining the availability, quality, safety, equity and cost-effectiveness of health care services." \r\n\n                        There is a semantic gap in concepts.  This classification term  is described as activities, i.e., "to inform persons" or "to inform processes" rather than the rationale for performing actions/operations on information related to the activity.',
                                            "display": "care management",
                                        },
                                        {
                                            "code": "DONAT",
                                            "definition": "To perform one or more operations on information used for cadaveric organ, eye or tissue donation.",
                                            "display": "donation",
                                        },
                                        {
                                            "code": "FRAUD",
                                            "definition": "To perform one or more operations on information used for fraud detection and prevention processes.",
                                            "display": "fraud",
                                        },
                                        {
                                            "code": "GOV",
                                            "definition": "To perform one or more operations on information used within government processes.",
                                            "display": "government",
                                        },
                                        {
                                            "code": "HACCRED",
                                            "definition": "To perform one or more operations on information for conducting activities related to meeting accreditation criteria.",
                                            "display": "health accreditation",
                                        },
                                        {
                                            "code": "HCOMPL",
                                            "definition": "To perform one or more operations on information used for conducting activities required to meet a mandate.",
                                            "display": "health compliance",
                                        },
                                        {
                                            "code": "HDECD",
                                            "definition": "To perform one or more operations on information used for handling deceased patient matters.",
                                            "display": "decedent",
                                        },
                                        {
                                            "code": "HDIRECT",
                                            "definition": "To perform one or more operation operations on information used to manage a patient directory.\r\n\n                        \n                           Examples: \n                        \r\n\n                        \n                           facility\n                           enterprise\n                           payer\n                           health information exchange patient directory",
                                            "display": "directory",
                                        },
                                        {
                                            "code": "HDM",
                                            "definition": 'To perform one or more actions on information used for conducting administrative and contractual activities by or on behalf of organizational entities responsible for delivery of  an individual\'s benefits in a healthcare program, health plan or insurance.   Explicitly excludes the use of information to organize the delivery of health care for care coordination and case management, or to provide healthcare treatment.\n\r\n\n                        \n                           Usage Note: Examples of activities conducted under this purpose of use: provider profiling, risk adjustment, underwriting, fraud and abuse, quality improvement population health and care management. Aligns with HIPAA Operation POU minus coordination of care or other treatment related activities. Similar to the description in SAMHSA Confidentiality of Substance Use Disorder Patient Records Supplemental notice of proposed rulemaking.\r\n\n                        \n                           Map: Maps to ISO 14265 Classification Term  "Administration of care for an individual subject of care" described as "To inform persons or processes responsible for enabling the availability of resources or funding or permissions for providing health care services to the subject of care."\r\n\n                        However, this classification term is described as activities, i.e., "to inform persons" or "to inform processes" rather than the rationale for performing actions/operations on information related to the activity.',
                                            "display": "healthcare delivery management",
                                        },
                                        {
                                            "code": "HLEGAL",
                                            "definition": "To perform one or more operations on information for conducting activities required by legal proceeding.",
                                            "display": "legal",
                                        },
                                        {
                                            "code": "HOUTCOMS",
                                            "definition": "To perform one or more operations on information used for assessing results and comparative effectiveness achieved by health care practices and interventions.",
                                            "display": "health outcome measure",
                                        },
                                        {
                                            "code": "HPRGRP",
                                            "definition": "To perform one or more operations on information used for conducting activities to meet program accounting requirements.",
                                            "display": "health program reporting",
                                        },
                                        {
                                            "code": "HQUALIMP",
                                            "definition": "To perform one or more operations on information used for conducting administrative activities to improve health care quality.",
                                            "display": "health quality improvement",
                                        },
                                        {
                                            "code": "HSYSADMIN",
                                            "concept": [
                                                {
                                                    "code": "LABELING",
                                                    "definition": "To perform one or more operations on information to assign, persist, and manage labels to healthcare data to characterize various aspects, such as its security classification, sensitivity, compartment, integrity, and provenance; applicable privacy, consent, security, provenance, and trust policies; and handling caveats such as purpose of use, obligations, and refrain policies.\r\n\n                        Label management includes classification of target data by constructing and binding of a label set per applicable policies, security policy information file semantics, and classification guides.  Label management also includes process and procedures for subsequent revision of a label for, e.g., reclassification, downgrading classification, and declassification.\r\n\n                        Label revisions may be triggered by, e.g., expiry of classification period; changes in applicable policy, e.g., revocation of a consent directive; or changes in the governing policy domain in which the data is relocated or a copy of the data is sent.  If a label is revised, an audit log should be kept and the provenance of the label changes should be tracked.",
                                                    "display": "labeling",
                                                },
                                                {
                                                    "code": "METAMGT",
                                                    "definition": "To perform one or more operations on information to assign, persist, and manage metadata to healthcare data to characterize various aspects used for its indexing, discovery, retrieval, and processing by systems, applications, and end users.  For example, master index identifier, media type, and location.",
                                                    "display": "metadata management",
                                                },
                                            ],
                                            "definition": "To perform one or more operations on information to administer the electronic systems used for the delivery of health care.",
                                            "display": "health system administration",
                                        },
                                        {
                                            "code": "MEMADMIN",
                                            "definition": "To perform one or more operations on information to administer health care coverage to an enrollee under a policy or program.",
                                            "display": "member administration",
                                        },
                                        {
                                            "code": "MILCDM",
                                            "definition": "To perform one or more operations on information for conducting activities required by military processes, procedures, policies, or law.",
                                            "display": "military command",
                                        },
                                        {
                                            "code": "PATADMIN",
                                            "definition": "To perform one or more operations on information used for operational activities conducted to administer the delivery of health care to a patient.",
                                            "display": "patient administration",
                                        },
                                        {
                                            "code": "PATSFTY",
                                            "definition": "To perform one or more operations on information in processes related to ensuring the safety of health care.",
                                            "display": "patient safety",
                                        },
                                        {
                                            "code": "PERFMSR",
                                            "definition": "To perform one or more operations on information used for monitoring performance of recommended health care practices and interventions.",
                                            "display": "performance measure",
                                        },
                                        {
                                            "code": "RECORDMGT",
                                            "definition": "To perform one or more operations on information used within the health records management process.",
                                            "display": "records management",
                                        },
                                        {
                                            "code": "SYSDEV",
                                            "concept": [
                                                {
                                                    "code": "HTEST",
                                                    "definition": "To perform one or more operations on information that is simulated or synthetic health data used for testing system capabilities outside of a production or operational system environment.\r\n\n                        \n                           Usage Note: Data marked with a HTEST security label enables an access control system to permit interfacing systems or end users provisioned with a clearance, which includes a HTEST purpose of use attribute, to test, verify, or validate that a system or application will operate in production as intended based on design specifications.",
                                                    "display": "test health data",
                                                }
                                            ],
                                            "definition": "To perform one or more operations on information to design, develop, implement, test, or deploy a healthcare system or application.",
                                            "display": "system development",
                                        },
                                        {
                                            "code": "TRAIN",
                                            "definition": "To perform one or more operations on information used in training and education.",
                                            "display": "training",
                                        },
                                    ],
                                    "definition": "To perform one or more operations on information used for conducting administrative and contractual activities related to the provision of health care.",
                                    "display": "healthcare operations",
                                },
                                {
                                    "code": "HPAYMT",
                                    "concept": [
                                        {
                                            "code": "CLMATTCH",
                                            "definition": "To perform one or more operations on information for provision of additional clinical evidence in support of a request for coverage or payment for health services.",
                                            "display": "claim attachment",
                                        },
                                        {
                                            "code": "COVAUTH",
                                            "definition": "To perform one or more operations on information for conducting prior authorization or predetermination of coverage for services.",
                                            "display": "coverage authorization",
                                        },
                                        {
                                            "code": "COVERAGE",
                                            "concept": [
                                                {
                                                    "code": "ELIGDTRM",
                                                    "definition": "To perform one or more operations on information used for conducting eligibility determination for coverage in a program or policy.  May entail review of financial status or disability assessment.",
                                                    "display": "eligibility determination",
                                                },
                                                {
                                                    "code": "ELIGVER",
                                                    "definition": "To perform one or more operations on information used for conducting eligibility verification of coverage in a program or policy.  May entail provider contacting coverage source (e.g., government health program such as workers compensation or health plan) for confirmation of enrollment, eligibility for specific services, and any applicable copays.",
                                                    "display": "eligibility verification",
                                                },
                                                {
                                                    "code": "ENROLLM",
                                                    "definition": "To perform one or more operations on information used for enrolling a covered party in a program or policy.  May entail recording of covered party's and any dependent's demographic information and benefit choices.",
                                                    "display": "enrollment",
                                                },
                                                {
                                                    "code": "MILDCRG",
                                                    "definition": "To perform one or more operations on information for the process of releasing military personnel from their service obligations, which may include determining service merit, discharge benefits, and disability assessment.",
                                                    "display": "military discharge",
                                                },
                                            ],
                                            "definition": "To perform one or more operations on information for conducting activities related to coverage under a program or policy.",
                                            "display": "coverage under policy or program",
                                        },
                                        {
                                            "code": "REMITADV",
                                            "definition": "To perform one or more operations on information about the amount remitted for a health care claim.",
                                            "display": "remittance advice",
                                        },
                                    ],
                                    "definition": "To perform one or more operations on information for conducting financial or contractual activities related to payment for provision of health care.",
                                    "display": "healthcare payment",
                                },
                                {
                                    "code": "HRESCH",
                                    "concept": [
                                        {
                                            "code": "BIORCH",
                                            "definition": "To perform one or more operations on information for conducting scientific investigations to obtain health care knowledge. Use of the data must be related to specified biomedical basic or applied research.  For example, research on rare plants to determine whether biologic properties may be useful for pharmaceutical development. May be used in combination with clinical trial and other healthcare research purposes of use.",
                                            "display": "biomedical research",
                                        },
                                        {
                                            "code": "CLINTRCH",
                                            "concept": [
                                                {
                                                    "code": "CLINTRCHNPC",
                                                    "definition": "To perform one or more operations on information for conducting scientific investigations in accordance with clinical trial protocols to obtain health care knowledge without provision of patient care. May be post-coordinated or used with other purposes of use such as disease, discipline, specialty, population origins or ancestry, translational healthcare research. For example, a clinical trial conducted on laboratory specimens collected from a specified patient population.",
                                                    "display": "clinical trial research without patient care",
                                                },
                                                {
                                                    "code": "CLINTRCHPC",
                                                    "definition": 'To perform one or more operations on information for conducting scientific investigations with patient care in accordance with clinical trial protocols to obtain health care knowledge. May be post-coordinated or used with other purposes of use such as disease, discipline, specialty, population origins or ancestry, translational healthcare research. For example, an "off-label" drug used for cancer therapy administer to a specified patient population.',
                                                    "display": "clinical trial research with patient care",
                                                },
                                                {
                                                    "code": "PRECLINTRCH",
                                                    "definition": "To perform one or more operations on information in preparation for conducting scientific investigation to obtain health care knowledge, such as research on animals or review of patient health records, to determine the feasibility of a clinical trial study; assist with protocol design; or in preparation for institutional review board or ethics committee approval process.  May be post-coordinated or used with other purposes of use such as disease, discipline, specialty, population origins or ancestry, translational healthcare research.",
                                                    "display": "preclinical trial research",
                                                },
                                            ],
                                            "definition": "To perform one or more operations on information for conducting scientific investigations in accordance with clinical trial protocols to obtain health care knowledge.",
                                            "display": "clinical trial research",
                                        },
                                        {
                                            "code": "DSRCH",
                                            "definition": "To perform one or more operations on information for conducting scientific investigations to obtain health care knowledge. Use of the data must be related to specified conditions, diagnosis, or disease healthcare research.  For example, conducting cancer research by testing reaction of tumor cells to certain biologics. May be used in combination with clinical trial and other healthcare research purposes of use.",
                                            "display": "disease specific healthcare research",
                                        },
                                        {
                                            "code": "POARCH",
                                            "definition": "To perform one or more operations on information, including genealogical pedigrees, historical records, surveys, family health data, health records, and genetic information, for conducting scientific investigations to obtain health care knowledge. Use of the data must be related to population origins and/or ancestry healthcare research.  For example, gathering genetic specimens from a specific population in order to determine the ancestry and population origins of that group. May be used in combination with clinical trial and other healthcare research purposes of use.",
                                            "display": "population origins or ancestry healthcare research",
                                        },
                                        {
                                            "code": "TRANSRCH",
                                            "definition": 'To perform one or more operations on information for conducting scientific investigations to obtain health care knowledge related to evidence based medicine during the course of providing healthcare treatment.  Sometimes referred to as "bench to bedside", which is the iterative feedback loop between healthcare research and clinical trials with input from information collected in the course of routine provision of healthcare. For example, by extending a patient encounter to conduct a survey related to a research topic such as attitudes about use of a wellness device that a patient agreed to use. May be used in combination with clinical trial and other healthcare research purposes of use.',
                                            "display": "translational healthcare research",
                                        },
                                    ],
                                    "definition": "To perform one or more operations on information for conducting scientific investigations to obtain health care knowledge.  Use of the data iincludes basic and applied research such as biomedical, population origin or ancestry, translational research, and disease, discipline, specialty specific healthcare research and clinical trial research.",
                                    "display": "healthcare research",
                                },
                                {
                                    "code": "PATRQT",
                                    "concept": [
                                        {
                                            "code": "FAMRQT",
                                            "definition": "To perform one or more operations on information in response to a request by a family member authorized by the patient.",
                                            "display": "family requested",
                                        },
                                        {
                                            "code": "PWATRNY",
                                            "definition": "To perform one or more operations on information in response to a request by a person appointed as the patient's legal representative.",
                                            "display": "power of attorney",
                                        },
                                        {
                                            "code": "SUPNWK",
                                            "definition": "To perform one or more operations on information in response to a request by a person authorized by the patient.",
                                            "display": "support network",
                                        },
                                    ],
                                    "definition": "To perform one or more operations on information in response to a patient's request.",
                                    "display": "patient requested",
                                },
                                {
                                    "code": "PUBHLTH",
                                    "concept": [
                                        {
                                            "code": "DISASTER",
                                            "definition": "To perform one or more operations on information used for provision of immediately needed health care to a population of living subjects located in a disaster zone.",
                                            "display": "disaster",
                                        },
                                        {
                                            "code": "THREAT",
                                            "definition": "To perform one or more operations on information used to prevent injury or disease to living subjects who may be the target of violence.",
                                            "display": "threat",
                                        },
                                    ],
                                    "definition": "To perform one or more operations on information for conducting public health activities, such as the reporting of notifiable conditions.",
                                    "display": "public health",
                                },
                                {
                                    "code": "TREAT",
                                    "concept": [
                                        {
                                            "code": "CLINTRL",
                                            "definition": "To perform health care as part of the clinical trial protocol.",
                                            "display": "clinical trial",
                                        },
                                        {
                                            "code": "COC",
                                            "definition": 'To perform one or more actions on information in order to organize the provision and case management of an individual????????s healthcare, including: Monitoring a person\'s goals, needs, and preferences; acting as the communication link between two or more participants concerned with a person\'s health and wellness; organizing and facilitating care activities and promoting self-management by advocating for, empowering, and educating a person; and ensuring safe, appropriate, non-duplicative, and effective integrated care.\r\n\n                        \n                           Usage Note: Use when describing these functions: 1. Monitoring a person????????s goals, needs, and preferences.   2. Acting as the communication link between two or more participants concerned with a person\'s health and wellness.  3. Organizing and facilitating care activities and promoting self-management by advocating for, empowering, and educating a person.  4. Ensuring safe, appropriate, non-duplicative, and effective integrated care.\r\n\n                        The goal is to clearly differentiate this type of coordination of care from HIPAA Operations by specifying that these actions on information are undertaken in the provision of healthcare treatment.\r\n\n                        For similar uses of this concept, see SAMHSA Confidentiality of Substance Use Disorder Patient Records Supplemental notice of proposed rulemaking, which differentiates concepts of care coordination and case management for the provision of treatment as specifically distinct from activities related to health care delivery management and the operations of organizational entities involved in the delivery of healthcare.\r\n\n                        \n                           Map: Maps to ISO 14265 Classification Terms: "Support of care activities within the provider organisation for an individual subject of care" described as "To inform persons or processes enabling others to provide health care services to the subject of care."  "Subject of Care Uses" described as "To inform the subject of care in support of his or her own interests."',
                                            "display": "coordination of care",
                                        },
                                        {
                                            "code": "ETREAT",
                                            "concept": [
                                                {
                                                    "code": "BTG",
                                                    "definition": 'To perform policy override operations on information for provision of immediately needed health care for an emergent condition affecting potential harm, death or patient safety by end users who are not provisioned for this purpose of use.  Includes override of organizational provisioning policies and may include override of subject of care consent directive restricting access.\r\n\n                        \n                           Map: Partially Maps to ISO 14265 Classification Term "Emergency care provision to an individual subject of care" described as "To inform persons needing to provide health care services to the subject of care urgently, possibly needing to over-ride the  policies and consents pertaining to Purpose 1 above." Purpose 1 is equivalent to HL7 treatment purpose of use: "Clinical care provision to an individual subject of care" described as "To inform persons or processes responsible for providing health care services to the subject of care."\nThe ISO description conflates both of the proposed specializations of HL7 ETREAT: break the glass and the typically broader access to health information normally available to providers who are provisioned for emergency workflows on a regular basis, e.g., Emergency Room providers. Examples of greater access than is normally accessible by providers based on the need to know are access to sensitive information for which access typically requires a patient\'s consent.  This is not an override of a patient\'s dissent to disclose sensitive information in cases where the applicable policy waives the need for that consent to access this information. In US, Title 38 Section 7332 and 42 CFR Part 2 both permit emergency access without the need to override a patient\'s consent directive; rather, this access is a limitation to the patient\'s right to dissent from disclosure.',
                                                    "display": "break the glass",
                                                },
                                                {
                                                    "code": "ERTREAT",
                                                    "definition": 'To perform one or more operations on information for provision of immediately needed health care for an emergent condition in an emergency room or similar emergent care context by end users provisioned for this purpose, which does not constitute as policy override such as in a "Break the Glass" purpose of use.\r\n\n                        Map:Partially Maps to ISO 14265 Classification Term "Emergency care provision to an individual subject of care" described as "To inform persons needing to provide health care services to the subject of care urgently, possibly needing to over-ride the  policies and consents pertaining to Purpose 1 above." Purpose 1 is equivalent to HL7 treatment purpose of use: "Clinical care provision to an individual subject of care" described as "To inform persons or processes responsible for providing health care services to the subject of care."\r\n\n                        The ISO description conflates both of the proposed specializations of HL7 ETREAT: break the glass and the typically broader access to health information normally available to providers who are provisioned for emergency workflows on a regular basis, e.g., Emergency Room providers. Examples of greater access than is normally accessible by providers based on the need to know are access to sensitive information for which access typically requires a patient\'s consent.  This is not an override of a patient\'s dissent to disclose sensitive information in cases where the applicable policy waives the need for that consent to access this information. In US, Title 38 Section 7332 and 42 CFR Part 2 both permit emergency access without the need to override a patient\'s consent directive; rather, this access is a limitation to the patient\'s right to dissent from disclosure. \r\n\n                        There is a semantic gap in concepts.  This classification term is described as activities ???????to inform persons?????? rather than the rationale for performing actions/operations on information related to the activity.',
                                                    "display": "emergency room treatment",
                                                },
                                            ],
                                            "definition": "To perform one or more operations on information for provision of immediately needed health care for an emergent condition.",
                                            "display": "Emergency Treatment",
                                        },
                                        {
                                            "code": "POPHLTH",
                                            "definition": "To perform one or more operations on information for provision of health care to a population of living subjects, e.g., needle exchange program.",
                                            "display": "population health",
                                        },
                                    ],
                                    "definition": "To perform one or more operations on information for provision of health care.",
                                    "display": "treatment",
                                },
                            ],
                            "definition": "Reason for performing one or more operations on information, which may be permitted by source system's security policy in accordance with one or more privacy policies and consent directives.\r\n\n                        \n                           Usage Notes: The rationale or purpose for an act relating to the management of personal health information, such as collecting personal health information for research or public health purposes.",
                            "display": "purpose of use",
                        },
                    ],
                    "definition": "Description:The rationale or purpose for an act relating to health information management, such as archiving information for the purpose of complying with an organization policy or jurisdictional law relating to  data retention.",
                    "display": "ActHealthInformationManagementReason",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_ActInformationPrivacyReason",
                    "concept": [
                        {
                            "code": "MARKT",
                            "definition": "Description:",
                            "display": "marketing",
                        },
                        {
                            "code": "OPERAT",
                            "concept": [
                                {
                                    "code": "LEGAL",
                                    "definition": "Definition:To provide information as a result of a subpoena.",
                                    "display": "subpoena",
                                },
                                {
                                    "code": "ACCRED",
                                    "definition": "Description:Operational activities conducted for the purposes of meeting of criteria defined by an accrediting entity for an activity, product, or service",
                                    "display": "accreditation",
                                },
                                {
                                    "code": "COMPL",
                                    "definition": "Description:Operational activities required to meet a mandate related to an activity, product, or service",
                                    "display": "compliance",
                                },
                                {
                                    "code": "ENADMIN",
                                    "definition": "Description:Operational activities conducted to administer information relating to entities involves with an activity, product, or service",
                                    "display": "entity administration",
                                },
                                {
                                    "code": "OUTCOMS",
                                    "definition": "Description:Operational activities conducted for the purposes of assessing the results of an activity, product, or service",
                                    "display": "outcome measure",
                                },
                                {
                                    "code": "PRGRPT",
                                    "definition": "Description:Operational activities conducted to meet program accounting requirements related to an activity, product, or service",
                                    "display": "program reporting",
                                },
                                {
                                    "code": "QUALIMP",
                                    "definition": "Description:Operational activities conducted for the purposes of improving the quality of an activity, product, or service",
                                    "display": "quality improvement",
                                },
                                {
                                    "code": "SYSADMN",
                                    "definition": "Description:Operational activities conducted to administer the electronic systems used for an activity, product, or service",
                                    "display": "system administration",
                                },
                            ],
                            "definition": "Description:Administrative and contractual processes required to support an activity, product, or service",
                            "display": "operations",
                        },
                        {
                            "code": "PAYMT",
                            "definition": "Description:Administrative, financial, and contractual processes related to payment for an activity, product, or service",
                            "display": "payment",
                        },
                        {
                            "code": "RESCH",
                            "definition": "Description:Investigative activities conducted for the purposes of obtaining knowledge",
                            "display": "research",
                        },
                        {
                            "code": "SRVC",
                            "definition": "Description:Provision of a service, product, or capability to an individual or organization",
                            "display": "service",
                        },
                    ],
                    "definition": "Description:The rationale or purpose for an act relating to the management of personal information, such as disclosing personal tax information for the purpose of complying with a court order.",
                    "display": "ActInformationPrivacyReason",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": "Description:The rationale or purpose for an act relating to information management, such as archiving information for the purpose of complying with an enterprise data retention policy.",
            "display": "ActInformationManagementReason",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActInformationManagementReason

    Description:The rationale or purpose for an act relating to information management, such as archiving information for the purpose of complying with an enterprise data retention policy.
    """

    underscore_act_invalid_reason = CodeSystemConcept(
        {
            "code": "_ActInvalidReason",
            "concept": [
                {
                    "code": "ADVSTORAGE",
                    "concept": [
                        {
                            "code": "COLDCHNBRK",
                            "definition": "Description: Cold chain was not maintained for the substance.",
                            "display": "cold chain break",
                        }
                    ],
                    "definition": "Description: Storage conditions caused the substance to be ineffective.",
                    "display": "adverse storage condition",
                },
                {
                    "code": "EXPLOT",
                    "definition": "Description: The lot from which the substance was drawn was expired.",
                    "display": "expired lot",
                },
                {
                    "code": "OUTSIDESCHED",
                    "definition": "The substance was administered outside of the recommended schedule or practice.",
                    "display": "administered outside recommended schedule or practice",
                },
                {
                    "code": "PRODRECALL",
                    "definition": "Description: The substance was recalled by the manufacturer.",
                    "display": "product recall",
                },
            ],
            "definition": "Description: Types of reasons why a substance is invalid for use.",
            "display": "ActInvalidReason",
        }
    )
    """
    ActInvalidReason

    Description: Types of reasons why a substance is invalid for use.
    """

    underscore_act_invoice_cancel_reason = CodeSystemConcept(
        {
            "code": "_ActInvoiceCancelReason",
            "concept": [
                {
                    "code": "INCCOVPTY",
                    "definition": "The covered party (patient) specified with the Invoice is not correct.",
                    "display": "incorrect covered party as patient",
                },
                {
                    "code": "INCINVOICE",
                    "definition": "The billing information, specified in the Invoice Elements, is not correct.  This could include incorrect costing for items included in the Invoice.",
                    "display": "incorrect billing",
                },
                {
                    "code": "INCPOLICY",
                    "definition": "The policy specified with the Invoice is not correct.  For example, it may belong to another Adjudicator or Covered Party.",
                    "display": "incorrect policy",
                },
                {
                    "code": "INCPROV",
                    "definition": "The provider specified with the Invoice is not correct.",
                    "display": "incorrect provider",
                },
            ],
            "definition": "Domain specifies the codes used to describe reasons why a Provider is cancelling an Invoice or Invoice Grouping.",
            "display": "ActInvoiceCancelReason",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActInvoiceCancelReason

    Domain specifies the codes used to describe reasons why a Provider is cancelling an Invoice or Invoice Grouping.
    """

    underscore_act_no_immunization_reason = CodeSystemConcept(
        {
            "code": "_ActNoImmunizationReason",
            "concept": [
                {
                    "code": "IMMUNE",
                    "definition": "Definition:Testing has shown that the patient already has immunity to the agent targeted by the immunization.",
                    "display": "immunity",
                },
                {
                    "code": "MEDPREC",
                    "definition": "Definition:The patient currently has a medical condition for which the vaccine is contraindicated or for which precaution is warranted.",
                    "display": "medical precaution",
                },
                {
                    "code": "OSTOCK",
                    "definition": "Definition:There was no supply of the product on hand to perform the service.",
                    "display": "product out of stock",
                },
                {
                    "code": "PATOBJ",
                    "definition": "Definition:The patient or their guardian objects to receiving the vaccine.",
                    "display": "patient objection",
                },
                {
                    "code": "PHILISOP",
                    "definition": "Definition:The patient or their guardian objects to receiving the vaccine because of philosophical beliefs.",
                    "display": "philosophical objection",
                },
                {
                    "code": "RELIG",
                    "definition": "Definition:The patient or their guardian objects to receiving the vaccine on religious grounds.",
                    "display": "religious objection",
                },
                {
                    "code": "VACEFF",
                    "definition": "Definition:The intended vaccine has expired or is otherwise believed to no longer be effective.\r\n\n                        \n                           Example:Due to temperature exposure.",
                    "display": "vaccine efficacy concerns",
                },
                {
                    "code": "VACSAF",
                    "definition": "Definition:The patient or their guardian objects to receiving the vaccine because of concerns over its safety.",
                    "display": "vaccine safety concerns",
                },
            ],
            "definition": "A coded description of the reason for why a patient did not receive a scheduled immunization.\r\n\n                        (important for public health strategy",
            "display": "ActNoImmunizationReason",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActNoImmunizationReason

    A coded description of the reason for why a patient did not receive a scheduled immunization.

                        (important for public health strategy
    """

    underscore_act_supply_fulfillment_refusal_reason = CodeSystemConcept(
        {
            "code": "_ActSupplyFulfillmentRefusalReason",
            "concept": [
                {
                    "code": "FRR01",
                    "definition": "Definition:The order has been stopped by the prescriber but this fact has not necessarily captured electronically.\r\n\n                        \n                           Example:A verbal stop, a fax, etc.",
                    "display": "order stopped",
                },
                {
                    "code": "FRR02",
                    "definition": "Definition:Order has not been fulfilled within a reasonable amount of time, and may not be current.",
                    "display": "stale-dated order",
                },
                {
                    "code": "FRR03",
                    "definition": "Definition:Data needed to safely act on the order which was expected to become available independent of the order is not yet available\r\n\n                        \n                           Example:Lab results, diagnostic imaging, etc.",
                    "display": "incomplete data",
                },
                {
                    "code": "FRR04",
                    "definition": "Definition:Product not available or manufactured. Cannot supply.",
                    "display": "product unavailable",
                },
                {
                    "code": "FRR05",
                    "definition": "Definition:The dispenser has ethical, religious or moral objections to fulfilling the order/dispensing the product.",
                    "display": "ethical/religious",
                },
                {
                    "code": "FRR06",
                    "definition": "Definition:Fulfiller not able to provide appropriate care associated with fulfilling the order.\r\n\n                        \n                           Example:Therapy requires ongoing monitoring by fulfiller and fulfiller will be ending practice, leaving town, unable to schedule necessary time, etc.",
                    "display": "unable to provide care",
                },
            ],
            "definition": 'Indicates why a fulfiller refused to fulfill a supply order, and considered it important to notify other providers of their decision.  E.g. "Suspect fraud", "Possible abuse", "Contraindicated".\r\n\n                        (used when capturing \'refusal to fill\' annotations)',
            "display": "ActSupplyFulfillmentRefusalReason",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActSupplyFulfillmentRefusalReason

    Indicates why a fulfiller refused to fulfill a supply order, and considered it important to notify other providers of their decision.  E.g. "Suspect fraud", "Possible abuse", "Contraindicated".

                        (used when capturing 'refusal to fill' annotations)
    """

    underscore_clinical_research_event_reason = CodeSystemConcept(
        {
            "code": "_ClinicalResearchEventReason",
            "concept": [
                {
                    "code": "RET",
                    "definition": "Definition:The event occurred so that a test or observation performed at a prior event could be performed again due to conditions set forth in the protocol.",
                    "display": "retest",
                },
                {
                    "code": "SCH",
                    "definition": "Definition:The event occurred due to it being scheduled in the research protocol.",
                    "display": "scheduled",
                },
                {
                    "code": "TRM",
                    "definition": "Definition:The event occurred in order to terminate the subject's participation in the study.",
                    "display": "termination",
                },
                {
                    "code": "UNS",
                    "definition": "Definition:The event that occurred was initiated by a study participant (e.g. the subject or the investigator), and did not occur for protocol reasons.",
                    "display": "unscheduled",
                },
            ],
            "definition": "Definition:Specifies the reason that an event occurred in a clinical research study.",
            "display": "ClinicalResearchEventReason",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ClinicalResearchEventReason

    Definition:Specifies the reason that an event occurred in a clinical research study.
    """

    underscore_clinical_research_observation_reason = CodeSystemConcept(
        {
            "code": "_ClinicalResearchObservationReason",
            "concept": [
                {
                    "code": "NPT",
                    "definition": "Definition:The observation or test was neither defined or scheduled in the study protocol.",
                    "display": "non-protocol",
                },
                {
                    "code": "PPT",
                    "definition": "Definition:The observation or test occurred due to it being defined in the research protocol, and during an activity or event that was scheduled in the protocol.",
                    "display": "per protocol",
                },
                {
                    "code": "UPT",
                    "definition": ":The observation or test occurred as defined in the research protocol, but at a point in time not specified in the study protocol.",
                    "display": "per definition",
                },
            ],
            "definition": "Definition:SSpecifies the reason that a test was performed or observation collected in a clinical research study.\r\n\n                        \n                           Note:This set of codes are not strictly reasons, but are used in the currently Normative standard.  Future revisions of the specification will model these as ActRelationships and thes codes may subsequently be retired.  Thus, these codes should not be used for new specifications.",
            "display": "ClinicalResearchObservationReason",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ClinicalResearchObservationReason

    Definition:SSpecifies the reason that a test was performed or observation collected in a clinical research study.

                        
                           Note:This set of codes are not strictly reasons, but are used in the currently Normative standard.  Future revisions of the specification will model these as ActRelationships and thes codes may subsequently be retired.  Thus, these codes should not be used for new specifications.
    """

    underscore_combined_pharmacy_order_suspend_reason_code = CodeSystemConcept(
        {
            "code": "_CombinedPharmacyOrderSuspendReasonCode",
            "concept": [
                {
                    "code": "ALTCHOICE",
                    "definition": "Description:This therapy has been ordered as a backup to a preferred therapy.  This order will be released when and if the preferred therapy is unsuccessful.",
                    "display": "try another treatment first",
                },
                {
                    "code": "CLARIF",
                    "definition": "Description:Clarification is required before the order can be acted upon.",
                    "display": "prescription requires clarification",
                },
                {
                    "code": "DRUGHIGH",
                    "definition": "Description:The current level of the medication in the patient's system is too high.  The medication is suspended to allow the level to subside to a safer level.",
                    "display": "drug level too high",
                },
                {
                    "code": "HOSPADM",
                    "definition": "Description:The patient has been admitted to a care facility and their community medications are suspended until hospital discharge.",
                    "display": "admission to hospital",
                },
                {
                    "code": "LABINT",
                    "definition": "Description:The therapy would interfere with a planned lab test and the therapy is being withdrawn until the test is completed.",
                    "display": "lab interference issues",
                },
                {
                    "code": "NON-AVAIL",
                    "definition": "Description:Patient not available for a period of time due to a scheduled therapy, leave of absence or other reason.",
                    "display": "patient not-available",
                },
                {
                    "code": "PREG",
                    "definition": "Description:The patient is pregnant or breast feeding.  The therapy will be resumed when the pregnancy is complete and the patient is no longer breastfeeding.",
                    "display": "parent is pregnant/breast feeding",
                },
                {
                    "code": "SALG",
                    "definition": "Description:The patient is believed to be allergic to a substance that is part of the therapy and the therapy is being temporarily withdrawn to confirm.",
                    "display": "allergy",
                },
                {
                    "code": "SDDI",
                    "definition": "Description:The drug interacts with a short-term treatment that is more urgently required.  This order will be resumed when the short-term treatment is complete.",
                    "display": "drug interacts with another drug",
                },
                {
                    "code": "SDUPTHER",
                    "definition": "Description:Another short-term co-occurring therapy fulfills the same purpose as this therapy.  This therapy will be resumed when the co-occuring therapy is complete.",
                    "display": "duplicate therapy",
                },
                {
                    "code": "SINTOL",
                    "definition": "Description:The patient is believed to have an intolerance to a substance that is part of the therapy and the therapy is being temporarily withdrawn to confirm.",
                    "display": "suspected intolerance",
                },
                {
                    "code": "SURG",
                    "definition": "Description:The drug is contraindicated for patients receiving surgery and the patient is scheduled to be admitted for surgery in the near future.  The drug will be resumed when the patient has sufficiently recovered from the surgery.",
                    "display": "patient scheduled for surgery",
                },
                {
                    "code": "WASHOUT",
                    "definition": "Description:The patient was previously receiving a medication contraindicated with the current medication.  The current medication will remain on hold until the prior medication has been cleansed from their system.",
                    "display": "waiting for old drug to wash out",
                },
            ],
            "definition": "Description:Indicates why the prescription should be suspended.",
            "display": "CombinedPharmacyOrderSuspendReasonCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    CombinedPharmacyOrderSuspendReasonCode

    Description:Indicates why the prescription should be suspended.
    """

    underscore_control_act_nullification_reason_code = CodeSystemConcept(
        {
            "code": "_ControlActNullificationReasonCode",
            "concept": [
                {
                    "code": "ALTD",
                    "definition": "Description:The decision on which the recorded information was based was changed before the decision had an effect.\r\n\n                        \n                           Example:Aborted prescription before patient left office, released prescription before suspend took effect.",
                    "display": "altered decision",
                },
                {
                    "code": "EIE",
                    "definition": "Description:The information was recorded incorrectly or was recorded in the wrong record.",
                    "display": "entered in error",
                },
                {
                    "code": "NORECMTCH",
                    "definition": "Description: There is no match for the record in the database.",
                    "display": "no record match",
                },
            ],
            "definition": "Description:Identifies reasons for nullifying (retracting) a particular control act.",
            "display": "ControlActNullificationReasonCode",
        }
    )
    """
    ControlActNullificationReasonCode

    Description:Identifies reasons for nullifying (retracting) a particular control act.
    """

    underscore_control_act_nullification_refusal_reason_type = CodeSystemConcept(
        {
            "code": "_ControlActNullificationRefusalReasonType",
            "concept": [
                {
                    "code": "INRQSTATE",
                    "definition": "The record is already in the requested state.",
                    "display": "in requested state",
                },
                {
                    "code": "NOMATCH",
                    "concept": [
                        {
                            "code": "NOPRODMTCH",
                            "definition": "Description: There is no match for the product in the master file repository.",
                            "display": "no product match",
                        },
                        {
                            "code": "NOSERMTCH",
                            "definition": "Description: There is no match for the service in the master file repository.",
                            "display": "no service match",
                        },
                        {
                            "code": "NOVERMTCH",
                            "definition": "Description: There is no match for the record and version.",
                            "display": "no version match",
                        },
                    ],
                    "definition": "Description: There is no match.",
                    "display": "no match",
                    "property": [{"code": "child", "valueCode": "NORECMTCH"}],
                },
                {
                    "code": "NOPERM",
                    "concept": [
                        {
                            "code": "NOUSERPERM",
                            "definition": "Definition:The user does not have permission",
                            "display": "no user permission",
                        },
                        {
                            "code": "NOAGNTPERM",
                            "definition": "Description: The agent does not have permission.",
                            "display": "no agent permission",
                        },
                        {
                            "code": "NOUSRPERM",
                            "definition": "Description: The user does not have permission.",
                            "display": "no user permission",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                    ],
                    "definition": "Description: There is no permission.",
                    "display": "no permission",
                },
                {
                    "code": "WRNGVER",
                    "definition": "Description: The record and version requested to update is not the current version.",
                    "display": "wrong version",
                },
            ],
            "definition": "Description: Reasons to refuse a transaction to be undone.",
            "display": "ControlActNullificationRefusalReasonType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ControlActNullificationRefusalReasonType

    Description: Reasons to refuse a transaction to be undone.
    """

    underscore_control_act_reason = CodeSystemConcept(
        {
            "code": "_ControlActReason",
            "concept": [
                {
                    "code": "_MedicationOrderAbortReasonCode",
                    "concept": [
                        {
                            "code": "DISCONT",
                            "definition": "Description:The medication is no longer being manufactured or is otherwise no longer available.",
                            "display": "product discontinued",
                        },
                        {
                            "code": "INEFFECT",
                            "definition": "Description:The therapy has been found to not have the desired therapeutic benefit on the patient.",
                            "display": "ineffective",
                        },
                        {
                            "code": "MONIT",
                            "definition": "Description:Monitoring the patient while taking the medication, the decision has been made that the therapy is no longer appropriate.",
                            "display": "response to monitoring",
                        },
                        {
                            "code": "NOREQ",
                            "definition": "Description:The underlying condition has been resolved or has evolved such that a different treatment is no longer needed.",
                            "display": "no longer required for treatment",
                        },
                        {
                            "code": "NOTCOVER",
                            "definition": "Description:The product does not have (or no longer has) coverage under the patientaTMs insurance policy.",
                            "display": "not covered",
                        },
                        {
                            "code": "PREFUS",
                            "definition": "Description:The patient refused to take the product.",
                            "display": "patient refuse",
                        },
                        {
                            "code": "RECALL",
                            "definition": "Description:The manufacturer or other agency has requested that stocks of a medication be removed from circulation.",
                            "display": "product recalled",
                        },
                        {
                            "code": "REPLACE",
                            "concept": [
                                {
                                    "code": "DOSECHG",
                                    "definition": "Description:The medication is being re-prescribed at a different dosage.",
                                    "display": "change in medication/dose",
                                }
                            ],
                            "definition": "Description:Item in current order is no longer in use as requested and a new one has/will be created to replace it.",
                            "display": "change in order",
                        },
                        {
                            "code": "REPLACEFIX",
                            "definition": "Description:Current order was issued with incorrect data and a new order has/will be created to replace it.",
                            "display": "error in order",
                        },
                        {
                            "code": "UNABLE",
                            "definition": "Description:<The patient is not (or is no longer) able to use the medication in a manner prescribed.\r\n\n                        \n                           Example:CanaTMt swallow.",
                            "display": "unable to use",
                        },
                    ],
                    "definition": "Description:Indicates the reason the medication order should be aborted.",
                    "display": "medication order abort reason",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_MedicationOrderReleaseReasonCode",
                    "concept": [
                        {
                            "code": "HOLDDONE",
                            "definition": "Definition:The original reason for suspending the medication has ended.",
                            "display": "suspend reason no longer applies",
                        },
                        {
                            "code": "HOLDINAP",
                            "definition": "Definition:",
                            "display": "suspend reason inappropriate",
                        },
                    ],
                    "definition": "Definition:A collection of concepts that indicate why the prescription should be released from suspended state.",
                    "display": "medication order release reason",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_ModifyPrescriptionReasonType",
                    "concept": [
                        {
                            "code": "ADMINERROR",
                            "definition": "Order was created with incorrect data and is changed to reflect the intended accuracy of the order.",
                            "display": "administrative error in order",
                        },
                        {
                            "code": "CLINMOD",
                            "definition": "Order is changed based on a clinical reason.",
                            "display": "clinical modification",
                        },
                    ],
                    "definition": "Types of reason why a prescription is being changed.",
                    "display": "ModifyPrescriptionReasonType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_PharmacySupplyEventAbortReason",
                    "concept": [
                        {
                            "code": "CONTRA",
                            "definition": "Definition:Contraindication identified",
                            "display": "contraindication",
                        },
                        {
                            "code": "FOABORT",
                            "definition": "Definition:Order to be fulfilled was aborted",
                            "display": "order aborted",
                        },
                        {
                            "code": "FOSUSP",
                            "definition": "Definition:Order to be fulfilled was suspended",
                            "display": "order suspended",
                        },
                        {
                            "code": "NOPICK",
                            "definition": "Definition:Patient did not come to get medication",
                            "display": "not picked up",
                        },
                        {
                            "code": "PATDEC",
                            "definition": "Definition:Patient changed their mind regarding obtaining medication",
                            "display": "patient changed mind",
                        },
                        {
                            "code": "QUANTCHG",
                            "definition": "Definition:Patient requested a revised quantity of medication",
                            "display": "change supply quantity",
                        },
                    ],
                    "definition": "Definition:Identifies why the dispense event was not completed.",
                    "display": "PharmacySupplyEventAbortReason",
                },
                {
                    "code": "_PharmacySupplyEventStockReasonCode",
                    "concept": [
                        {
                            "code": "FLRSTCK",
                            "definition": "Definition:The bulk supply is issued to replenish a ward for local dispensing.  (Includes both mobile and fixed-location ward stocks.)",
                            "display": "floor stock",
                        },
                        {
                            "code": "LTC",
                            "definition": "Definition:The bulk supply will be administered within a long term care facility.",
                            "display": "long term care use",
                        },
                        {
                            "code": "OFFICE",
                            "definition": "Definition:The bulk supply is intended for general clinician office use.",
                            "display": "office use",
                        },
                        {
                            "code": "PHARM",
                            "definition": "Definition:The bulk supply is being transferred to another dispensing facility to.\r\n\n                        \n                           Example:Alleviate a temporary shortage.",
                            "display": "pharmacy transfer",
                        },
                        {
                            "code": "PROG",
                            "definition": "Definition:The bulk supply is intended for dispensing according to a specific program.\r\n\n                        \n                           Example:Mass immunization.",
                            "display": "program use",
                        },
                    ],
                    "definition": 'Definition:A collection of concepts that indicates the reason for a "bulk supply" of medication.',
                    "display": "pharmacy supply event stock reason",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_PharmacySupplyRequestRenewalRefusalReasonCode",
                    "concept": [
                        {
                            "code": "ALREADYRX",
                            "definition": "Definition:Patient has already been given a new (renewal) prescription.",
                            "display": "new prescription exists",
                        },
                        {
                            "code": "FAMPHYS",
                            "definition": "Definition:Request for further authorization must be done through patient's family physician.",
                            "display": "family physician must authorize further fills",
                        },
                        {
                            "code": "MODIFY",
                            "definition": "Definition:Therapy has been changed and new prescription issued",
                            "display": "modified prescription exists",
                        },
                        {
                            "code": "NEEDAPMT",
                            "definition": "Definition:Patient must see prescriber prior to further fills.",
                            "display": "patient must make appointment",
                        },
                        {
                            "code": "NOTAVAIL",
                            "definition": "Definition:Original prescriber is no longer available to prescribe and no other prescriber has taken responsibility for the patient.",
                            "display": "prescriber not available",
                        },
                        {
                            "code": "NOTPAT",
                            "definition": "Definition:Patient no longer or has never been under this prescribers care.",
                            "display": "patient no longer in this practice",
                        },
                        {
                            "code": "ONHOLD",
                            "definition": "Definition:This medication is on hold.",
                            "display": "medication on hold",
                        },
                        {
                            "code": "PRNA",
                            "definition": "Description:This product is not available or manufactured.",
                            "display": "product not available",
                        },
                        {
                            "code": "STOPMED",
                            "definition": "Renewing or original prescriber informed patient to stop using the medication.",
                            "display": "prescriber stopped medication for patient",
                        },
                        {
                            "code": "TOOEARLY",
                            "definition": "Definition:The patient should have medication remaining.",
                            "display": "too early",
                        },
                    ],
                    "definition": "Definition:A collection of concepts that identifies why a renewal prescription has been refused.",
                    "display": "pharmacy supply request renewal refusal reason",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "DISCONT"},
                    ],
                },
                {
                    "code": "_SupplyOrderAbortReasonCode",
                    "concept": [
                        {
                            "code": "IMPROV",
                            "definition": "Definition:The patient's medical condition has nearly abated.",
                            "display": "condition improved",
                        },
                        {
                            "code": "INTOL",
                            "definition": "Description:The patient has an intolerance to the medication.",
                            "display": "intolerance",
                        },
                        {
                            "code": "NEWSTR",
                            "definition": "Definition:The current medication will be replaced by a new strength of the same medication.",
                            "display": "new strength",
                        },
                        {
                            "code": "NEWTHER",
                            "definition": "Definition:A new therapy will be commenced when current supply exhausted.",
                            "display": "new therapy",
                        },
                    ],
                    "definition": "Definition:A collection of concepts that indicates why the prescription should no longer be allowed to be dispensed (but can still administer what is already being dispensed).",
                    "display": "supply order abort reason",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": "Identifies why a specific query, request, or other trigger event occurred.",
            "display": "ControlActReason",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ControlActReason

    Identifies why a specific query, request, or other trigger event occurred.
    """

    underscore_generic_update_reason_code = CodeSystemConcept(
        {
            "code": "_GenericUpdateReasonCode",
            "concept": [
                {
                    "code": "CHGDATA",
                    "definition": "Description:Information has changed since the record was created.",
                    "display": "information change",
                },
                {
                    "code": "FIXDATA",
                    "definition": "Description:Previously recorded information was erroneous and is being corrected.",
                    "display": "error correction",
                },
                {
                    "code": "MDATA",
                    "definition": "Information is combined into the record.",
                    "display": "merge data",
                },
                {
                    "code": "NEWDATA",
                    "definition": "Description:New information has become available to supplement the record.",
                    "display": "new information",
                },
                {
                    "code": "UMDATA",
                    "definition": "Information is separated from the record.",
                    "display": "unmerge data",
                },
            ],
            "definition": "Description:Identifies why a change is being made to a  record.",
            "display": "GenericUpdateReasonCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    GenericUpdateReasonCode

    Description:Identifies why a change is being made to a  record.
    """

    underscore_patient_profile_query_reason_code = CodeSystemConcept(
        {
            "code": "_PatientProfileQueryReasonCode",
            "concept": [
                {
                    "code": "ADMREV",
                    "definition": "Definition: To evaluate for service authorization, payment, reporting, or performance/outcome measures.",
                    "display": "administrative review",
                },
                {
                    "code": "PATCAR",
                    "definition": "Definition:To obtain records as part of patient care.",
                    "display": "patient care",
                },
                {
                    "code": "PATREQ",
                    "definition": "Definition:Patient requests information from their profile.",
                    "display": "patient request query",
                },
                {
                    "code": "PRCREV",
                    "definition": "Definition:To evaluate the provider's current practice for professional-improvement reasons.",
                    "display": "practice review",
                },
                {
                    "code": "REGUL",
                    "definition": "Description:Review for the purpose of regulatory compliance.",
                    "display": "regulatory review",
                },
                {
                    "code": "RSRCH",
                    "definition": "Definition:To provide research data, as authorized by the patient.",
                    "display": "research",
                },
                {
                    "code": "VALIDATION",
                    "definition": "Description:To validate the patient's record.\r\n\n                        \n                           Example:Merging or unmerging records.",
                    "display": "validation review",
                },
            ],
            "definition": "Definition:A collection of concepts identifying why the patient's profile is being queried.",
            "display": "patient profile query reason",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "child", "valueCode": "LEGAL"},
            ],
        }
    )
    """
    patient profile query reason

    Definition:A collection of concepts identifying why the patient's profile is being queried.
    """

    underscore_pharmacy_supply_request_fulfiller_revision_refusal_reason_code = CodeSystemConcept(
        {
            "code": "_PharmacySupplyRequestFulfillerRevisionRefusalReasonCode",
            "concept": [
                {
                    "code": "LOCKED",
                    "definition": "Definition:The prescription may not be reassigned from the original pharmacy.",
                    "display": "locked",
                },
                {
                    "code": "UNKWNTARGET",
                    "definition": "Definition:The target facility does not recognize the dispensing facility.",
                    "display": "unknown target",
                },
            ],
            "definition": "Definition:Indicates why the request to transfer a prescription from one dispensing facility to another has been refused.",
            "display": "PharmacySupplyRequestFulfillerRevisionRefusalReasonCode",
            "property": [{"code": "child", "valueCode": "NOUSERPERM"}],
        }
    )
    """
    PharmacySupplyRequestFulfillerRevisionRefusalReasonCode

    Definition:Indicates why the request to transfer a prescription from one dispensing facility to another has been refused.
    """

    underscore_refusal_reason_code = CodeSystemConcept(
        {
            "code": "_RefusalReasonCode",
            "definition": "Description: Identifies why a request to add (or activate) a record is being refused.  Examples include the receiving system not able to match the identifier and find that record in the receiving system, having no permission, or a detected issue exists which precludes the requested action.",
            "display": "RefusalReasonCode",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "child", "valueCode": "NOMATCH"},
                {"code": "child", "valueCode": "NOPERM"},
            ],
        }
    )
    """
    RefusalReasonCode

    Description: Identifies why a request to add (or activate) a record is being refused.  Examples include the receiving system not able to match the identifier and find that record in the receiving system, having no permission, or a detected issue exists which precludes the requested action.
    """

    underscore_scheduling_act_reason = CodeSystemConcept(
        {
            "code": "_SchedulingActReason",
            "concept": [
                {
                    "code": "BLK",
                    "definition": "The time slots previously allocated are now blocked and no longer available for booking Appointments",
                    "display": "Unexpected Block (of Schedule)",
                },
                {
                    "code": "DEC",
                    "definition": "The Patient is deceased",
                    "display": "Patient Deceased",
                },
                {
                    "code": "FIN",
                    "definition": "Patient unable to pay and not covered by insurance",
                    "display": "No Financial Backing",
                },
                {
                    "code": "MED",
                    "definition": "The medical condition of the Patient has changed",
                    "display": "Medical Status Altered",
                },
                {
                    "code": "MTG",
                    "definition": "The Physician is in a meeting.  For example, he/she may request administrative time to talk to family after appointment",
                    "display": "In an outside meeting",
                },
                {
                    "code": "PHY",
                    "definition": "The Physician requested the action",
                    "display": "Physician request",
                },
            ],
            "definition": "Reasons for cancelling or rescheduling an Appointment",
            "display": "SchedulingActReason",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "child", "valueCode": "PAT"},
            ],
        }
    )
    """
    SchedulingActReason

    Reasons for cancelling or rescheduling an Appointment
    """

    underscore_status_revision_refusal_reason_code = CodeSystemConcept(
        {
            "code": "_StatusRevisionRefusalReasonCode",
            "concept": [
                {
                    "code": "FILLED",
                    "definition": "Ordered quantity has already been completely fulfilled.",
                    "display": "fully filled",
                }
            ],
            "definition": "Indicates why the act revision (status update) is being refused.",
            "display": "StatusRevisionRefusalReasonCode",
            "property": [
                {"code": "child", "valueCode": "NORECMTCH"},
                {"code": "child", "valueCode": "INRQSTATE"},
                {"code": "child", "valueCode": "NOUSERPERM"},
            ],
        }
    )
    """
    StatusRevisionRefusalReasonCode

    Indicates why the act revision (status update) is being refused.
    """

    underscore_substance_administration_permission_refusal_reason_code = CodeSystemConcept(
        {
            "code": "_SubstanceAdministrationPermissionRefusalReasonCode",
            "concept": [
                {
                    "code": "PATINELIG",
                    "definition": "Definition:Patient not eligible for drug",
                    "display": "patient not eligible",
                },
                {
                    "code": "PROTUNMET",
                    "definition": "Definition:Patient does not meet required protocol",
                    "display": "protocol not met",
                },
                {
                    "code": "PROVUNAUTH",
                    "definition": "Definition:Provider is not authorized to prescribe or dispense",
                    "display": "provider not authorized",
                },
            ],
            "definition": "Definition:Indicates why the requested authorization to prescribe or dispense a medication has been refused.",
            "display": "SubstanceAdministrationPermissionRefusalReasonCode",
            "property": [{"code": "child", "valueCode": "NOUSERPERM"}],
        }
    )
    """
    SubstanceAdministrationPermissionRefusalReasonCode

    Definition:Indicates why the requested authorization to prescribe or dispense a medication has been refused.
    """

    underscore_substance_admin_substitution_not_allowed_reason = CodeSystemConcept(
        {
            "code": "_SubstanceAdminSubstitutionNotAllowedReason",
            "concept": [
                {
                    "code": "ALGINT",
                    "definition": "Definition: Patient has had a prior allergic intolerance response to alternate product or one of its components.",
                    "display": "allergy intolerance",
                },
                {
                    "code": "COMPCON",
                    "definition": "Definition: Patient has compliance issues with medication such as differing appearance, flavor, size, shape or consistency.",
                    "display": "compliance concern",
                },
                {
                    "code": "THERCHAR",
                    "definition": "The prescribed product has specific clinical release or other therapeutic characteristics not shared by other substitutable medications.",
                    "display": "therapeutic characteristics",
                },
                {
                    "code": "TRIAL",
                    "definition": "Definition: The specific manufactured drug is part of a clinical trial.",
                    "display": "clinical trial drug",
                },
            ],
            "definition": "Reasons why substitution of a substance administration request is not permitted.",
            "display": "SubstanceAdminSubstitutionNotAllowedReason",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "child", "valueCode": "PAT"},
            ],
        }
    )
    """
    SubstanceAdminSubstitutionNotAllowedReason

    Reasons why substitution of a substance administration request is not permitted.
    """

    underscore_substance_admin_substitution_reason = CodeSystemConcept(
        {
            "code": "_SubstanceAdminSubstitutionReason",
            "concept": [
                {
                    "code": "CT",
                    "definition": "Indicates that the decision to substitute or to not substitute was driven by a desire to maintain consistency with a pre-existing therapy.  I.e. The performer provided the same item/service as had been previously provided rather than providing exactly what was ordered, or rather than substituting with a lower-cost equivalent.",
                    "display": "continuing therapy",
                },
                {
                    "code": "FP",
                    "definition": "Indicates that the decision to substitute or to not substitute was driven by a policy expressed within the formulary.",
                    "display": "formulary policy",
                },
                {
                    "code": "OS",
                    "definition": "In the case of 'substitution', indicates that the substitution occurred because the ordered item was not in stock.  In the case of 'no substitution', indicates that a cheaper equivalent was not substituted because it was not in stock.",
                    "display": "out of stock",
                },
                {
                    "code": "RR",
                    "definition": "Indicates that the decision to substitute or to not substitute was driven by a jurisdictional regulatory requirement mandating or prohibiting substitution.",
                    "display": "regulatory requirement",
                },
            ],
            "definition": "SubstanceAdminSubstitutionReason",
            "display": "SubstanceAdminSubstitutionReason",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    SubstanceAdminSubstitutionReason

    SubstanceAdminSubstitutionReason
    """

    underscore_transfer_act_reason = CodeSystemConcept(
        {
            "code": "_TransferActReason",
            "concept": [
                {
                    "code": "ER",
                    "definition": "Moved to an error in placing the patient in the original location.",
                    "display": "Error",
                },
                {
                    "code": "RQ",
                    "definition": "Moved at the request of the patient.",
                    "display": "Request",
                },
            ],
            "definition": "The explanation for why a patient is moved from one location to another within the organization",
            "display": "TransferActReason",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    TransferActReason

    The explanation for why a patient is moved from one location to another within the organization
    """

    underscore_act_billable_service_reason = CodeSystemConcept(
        {
            "code": "_ActBillableServiceReason",
            "concept": [
                {
                    "code": "_ActBillableClinicalServiceReason",
                    "definition": "Reason for Clinical Service being performed.\r\n\n                        This domain excludes reasons specified by diagnosed conditions.\r\n\n                        Examples of values from this domain include duplicate therapy and fraudulent prescription.",
                    "display": "ActBillableClinicalServiceReason",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "status", "valueCode": "retired"},
                    ],
                }
            ],
            "definition": "Definition: This domain is used to document reasons for providing a billable service; the billable services may include both clinical services and social services.",
            "display": "ActBillableServiceReason",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "status", "valueCode": "retired"},
            ],
        }
    )
    """
    ActBillableServiceReason

    Definition: This domain is used to document reasons for providing a billable service; the billable services may include both clinical services and social services.
    """

    bonus = CodeSystemConcept(
        {"code": "BONUS", "property": [{"code": "status", "valueCode": "retired"}]}
    )
    """
    None

    
    """

    chd = CodeSystemConcept(
        {
            "code": "CHD",
            "definition": "Description:The level of coverage under the policy or program is available only to children",
            "display": "Children only",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    Children only

    Description:The level of coverage under the policy or program is available only to children
    """

    dep = CodeSystemConcept(
        {
            "code": "DEP",
            "definition": "Description:The level of coverage under the policy or program is available only to a subscriber's dependents.",
            "display": "Dependents only",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    Dependents only

    Description:The level of coverage under the policy or program is available only to a subscriber's dependents.
    """

    ech = CodeSystemConcept(
        {
            "code": "ECH",
            "definition": "Description:The level of coverage under the policy or program is available to an employee and his or her children.",
            "display": "Employee and children",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    Employee and children

    Description:The level of coverage under the policy or program is available to an employee and his or her children.
    """

    edu = CodeSystemConcept(
        {"code": "EDU", "property": [{"code": "status", "valueCode": "retired"}]}
    )
    """
    None

    
    """

    emp = CodeSystemConcept(
        {
            "code": "EMP",
            "definition": "Description:The level of coverage under the policy or program is available only to an employee.",
            "display": "Employee only",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    Employee only

    Description:The level of coverage under the policy or program is available only to an employee.
    """

    esp = CodeSystemConcept(
        {
            "code": "ESP",
            "definition": "Description:The level of coverage under the policy or program is available to an employee and his or her spouse.",
            "display": "Employee and spouse",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    Employee and spouse

    Description:The level of coverage under the policy or program is available to an employee and his or her spouse.
    """

    fam = CodeSystemConcept(
        {
            "code": "FAM",
            "definition": "Description:The level of coverage under the policy or program is available to a subscriber's family.",
            "display": "Family",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    Family

    Description:The level of coverage under the policy or program is available to a subscriber's family.
    """

    ind = CodeSystemConcept(
        {
            "code": "IND",
            "definition": "Description:The level of coverage under the policy or program is available to an individual.",
            "display": "Individual",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    Individual

    Description:The level of coverage under the policy or program is available to an individual.
    """

    invoice = CodeSystemConcept(
        {"code": "INVOICE", "property": [{"code": "status", "valueCode": "retired"}]}
    )
    """
    None

    
    """

    proa = CodeSystemConcept(
        {"code": "PROA", "property": [{"code": "status", "valueCode": "retired"}]}
    )
    """
    None

    
    """

    recov = CodeSystemConcept(
        {"code": "RECOV", "property": [{"code": "status", "valueCode": "retired"}]}
    )
    """
    None

    
    """

    retro = CodeSystemConcept(
        {"code": "RETRO", "property": [{"code": "status", "valueCode": "retired"}]}
    )
    """
    None

    
    """

    spc = CodeSystemConcept(
        {
            "code": "SPC",
            "definition": "Description:The level of coverage under the policy or program is available to a subscriber's spouse and children",
            "display": "Spouse and children",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    Spouse and children

    Description:The level of coverage under the policy or program is available to a subscriber's spouse and children
    """

    spo = CodeSystemConcept(
        {
            "code": "SPO",
            "definition": "Description:The level of coverage under the policy or program is available only to a subscribers spouse",
            "display": "Spouse only",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    Spouse only

    Description:The level of coverage under the policy or program is available only to a subscribers spouse
    """

    tran = CodeSystemConcept(
        {"code": "TRAN", "property": [{"code": "status", "valueCode": "retired"}]}
    )
    """
    None

    
    """

    class Meta:
        resource = _resource
