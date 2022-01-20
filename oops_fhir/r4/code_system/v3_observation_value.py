from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ObservationValue"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ObservationValue:
    """
    v3 Code System ObservationValue

     This domain is the root domain to which all HL7-recognized value sets
for the Observation.value attribute will be linked when
Observation.value has a coded data type.  OpenIssue:  Description copied
from Concept Domain of same name.  Must be corrected..

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ObservationValue
    """

    underscore_act_coverage_assessment_observation_value = CodeSystemConcept(
        {
            "code": "_ActCoverageAssessmentObservationValue",
            "concept": [
                {
                    "code": "_ActFinancialStatusObservationValue",
                    "concept": [
                        {
                            "code": "ASSET",
                            "concept": [
                                {
                                    "code": "ANNUITY",
                                    "definition": "Indicator of annuity ownership or status as beneficiary.",
                                    "display": "annuity",
                                },
                                {
                                    "code": "PROP",
                                    "definition": "Indicator of real property ownership, e.g., deed or real estate contract.",
                                    "display": "real property",
                                },
                                {
                                    "code": "RETACCT",
                                    "definition": "Indicator of retirement investment account ownership.",
                                    "display": "retirement investment account",
                                },
                                {
                                    "code": "TRUST",
                                    "definition": "Indicator of status as trust beneficiary.",
                                    "display": "trust",
                                },
                            ],
                            "definition": "Codes specifying asset indicators used to assess or establish eligibility for coverage under a policy or program.",
                            "display": "asset",
                        },
                        {
                            "code": "INCOME",
                            "concept": [
                                {
                                    "code": "CHILD",
                                    "definition": "Indicator of child support payments received or provided.",
                                    "display": "child support",
                                },
                                {
                                    "code": "DISABL",
                                    "definition": "Indicator of disability income replacement payment.",
                                    "display": "disability pay",
                                },
                                {
                                    "code": "INVEST",
                                    "definition": "Indicator of investment income, e.g., dividend check, annuity payment; real estate rent, investment divestiture proceeds; trust or endowment check.",
                                    "display": "investment income",
                                },
                                {
                                    "code": "PAY",
                                    "definition": "Indicator of paid employment, e.g., letter of hire, contract, employer letter; copy of pay check or pay stub.",
                                    "display": "paid employment",
                                },
                                {
                                    "code": "RETIRE",
                                    "definition": "Indicator of retirement payment, e.g., pension check.",
                                    "display": "retirement pay",
                                },
                                {
                                    "code": "SPOUSAL",
                                    "definition": "Indicator of spousal or partner support payments received or provided; e.g., alimony payment; support stipulations in a divorce settlement.",
                                    "display": "spousal or partner support",
                                },
                                {
                                    "code": "SUPPLE",
                                    "definition": "Indicator of income supplement, e.g., gifting, parental income support; stipend, or grant.",
                                    "display": "income supplement",
                                },
                                {
                                    "code": "TAX",
                                    "definition": "Indicator of tax obligation or payment, e.g., statement of taxable income.",
                                    "display": "tax obligation",
                                },
                            ],
                            "definition": "Code specifying income indicators used to assess or establish eligibility for coverage under a policy or program; e.g., pay or pension check, child support payments received or provided, and taxes paid.",
                            "display": "income",
                        },
                        {
                            "code": "LIVEXP",
                            "concept": [
                                {
                                    "code": "CLOTH",
                                    "definition": "Indicator of clothing expenses.",
                                    "display": "clothing expense",
                                },
                                {
                                    "code": "FOOD",
                                    "definition": "Indicator of transportation expenses.",
                                    "display": "food expense",
                                },
                                {
                                    "code": "HEALTH",
                                    "definition": "Indicator of health expenses; including medication costs, health service costs, financial participations, and health coverage premiums.",
                                    "display": "health expense",
                                },
                                {
                                    "code": "HOUSE",
                                    "definition": "Indicator of housing expense, e.g., household appliances, fixtures, furnishings, and maintenance and repairs.",
                                    "display": "household expense",
                                },
                                {
                                    "code": "LEGAL",
                                    "definition": "Indicator of legal expenses.",
                                    "display": "legal expense",
                                },
                                {
                                    "code": "MORTG",
                                    "definition": "Indicator of mortgage amount, interest, and payments.",
                                    "display": "mortgage",
                                },
                                {
                                    "code": "RENT",
                                    "definition": "Indicator of rental or lease payments.",
                                    "display": "rent",
                                },
                                {
                                    "code": "SUNDRY",
                                    "definition": "Indicator of transportation expenses.",
                                    "display": "sundry expense",
                                },
                                {
                                    "code": "TRANS",
                                    "definition": "Indicator of transportation expenses, e.g., vehicle payments, vehicle insurance, vehicle fuel, and vehicle maintenance and repairs.",
                                    "display": "transportation expense",
                                },
                                {
                                    "code": "UTIL",
                                    "definition": "Indicator of transportation expenses.",
                                    "display": "utility expense",
                                },
                            ],
                            "definition": "Codes specifying living expense indicators used to assess or establish eligibility for coverage under a policy or program.",
                            "display": "living expense",
                        },
                    ],
                    "definition": "Code specifying financial indicators used to assess or establish eligibility for coverage under a policy or program; e.g., pay stub; tax or income document; asset document; living expenses.",
                    "display": "ActFinancialStatusObservationValue",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "ELSTAT",
                    "concept": [
                        {
                            "code": "ADOPT",
                            "definition": "Indicator of adoption.",
                            "display": "adoption document",
                        },
                        {
                            "code": "BTHCERT",
                            "definition": "Indicator of birth.",
                            "display": "birth certificate",
                        },
                        {
                            "code": "CCOC",
                            "definition": "Indicator of creditable coverage.",
                            "display": "creditable coverage document",
                        },
                        {
                            "code": "DRLIC",
                            "definition": "Indicator of driving status.",
                            "display": "driver license",
                        },
                        {
                            "code": "FOSTER",
                            "definition": "Indicator of foster child status.",
                            "display": "foster child document",
                        },
                        {
                            "code": "MEMBER",
                            "definition": "Indicator of status as covered member under a policy or program, e.g., member id card or coverage document.",
                            "display": "program or policy member",
                        },
                        {
                            "code": "MIL",
                            "definition": "Indicator of military status.",
                            "display": "military identification",
                        },
                        {
                            "code": "MRGCERT",
                            "definition": "Indicator of marriage status.",
                            "display": "marriage certificate",
                        },
                        {
                            "code": "PASSPORT",
                            "definition": "Indicator of citizenship.",
                            "display": "passport",
                        },
                        {
                            "code": "STUDENRL",
                            "definition": "Indicator of student status.",
                            "display": "student enrollment",
                        },
                    ],
                    "definition": "Code specifying eligibility indicators used to assess or establish eligibility for coverage under a policy or program eligibility status, e.g., certificates of creditable coverage; student enrollment; adoption, marriage or birth certificate.",
                    "display": "eligibility indicator",
                },
                {
                    "code": "HLSTAT",
                    "concept": [
                        {
                            "code": "DISABLE",
                            "definition": "Indication of disability.",
                            "display": "disabled",
                        },
                        {
                            "code": "DRUG",
                            "definition": "Indication of drug use.",
                            "display": "drug use",
                        },
                        {
                            "code": "IVDRG",
                            "definition": "Indication of IV drug use .",
                            "display": "IV drug use",
                        },
                        {
                            "code": "PGNT",
                            "definition": "Non-clinical report of pregnancy.",
                            "display": "pregnant",
                        },
                    ],
                    "definition": "Code specifying non-clinical indicators related to health status used to assess or establish eligibility for coverage under a policy or program, e.g., pregnancy, disability, drug use, mental health issues.",
                    "display": "health status",
                },
                {
                    "code": "LIVDEP",
                    "concept": [
                        {
                            "code": "RELDEP",
                            "definition": "Continued living in private residence requires functional and health care assistance from one or more relatives.",
                            "display": "relative dependent",
                        },
                        {
                            "code": "SPSDEP",
                            "definition": "Continued living in private residence requires functional and health care assistance from spouse or life partner.",
                            "display": "spouse dependent",
                        },
                        {
                            "code": "URELDEP",
                            "definition": "Continued living in private residence requires functional and health care assistance from one or more unrelated persons.",
                            "display": "unrelated person dependent",
                        },
                    ],
                    "definition": "Code specifying observations related to living dependency, such as dependent upon spouse for activities of daily living.",
                    "display": "living dependency",
                },
                {
                    "code": "LIVSIT",
                    "concept": [
                        {
                            "code": "ALONE",
                            "definition": "Living alone.  Maps to PD1-2   Living arrangement   (IS)   00742 [A]",
                            "display": "alone",
                        },
                        {
                            "code": "DEPCHD",
                            "definition": "Living with one or more dependent children requiring moderate supervision.",
                            "display": "dependent children",
                        },
                        {
                            "code": "DEPSPS",
                            "definition": "Living with disabled spouse requiring functional and health care assistance",
                            "display": "dependent spouse",
                        },
                        {
                            "code": "DEPYGCHD",
                            "definition": "Living with one or more dependent children requiring intensive supervision",
                            "display": "dependent young children",
                        },
                        {
                            "code": "FAM",
                            "definition": "Living with family. Maps to PD1-2   Living arrangement   (IS)   00742 [F]",
                            "display": "live with family",
                        },
                        {
                            "code": "RELAT",
                            "definition": "Living with one or more relatives. Maps to PD1-2   Living arrangement   (IS)   00742 [R]",
                            "display": "relative",
                        },
                        {
                            "code": "SPS",
                            "definition": "Living only with spouse or life partner. Maps to PD1-2   Living arrangement   (IS)   00742 [S]",
                            "display": "spouse only",
                        },
                        {
                            "code": "UNREL",
                            "definition": "Living with one or more unrelated persons.",
                            "display": "unrelated person",
                        },
                    ],
                    "definition": "Code specifying observations related to living situation for a person in a private residence.",
                    "display": "living situation",
                },
                {
                    "code": "SOECSTAT",
                    "concept": [
                        {
                            "code": "ABUSE",
                            "definition": "Indication of abuse victim.",
                            "display": "abuse victim",
                        },
                        {
                            "code": "HMLESS",
                            "definition": "Indication of status as homeless.",
                            "display": "homeless",
                        },
                        {
                            "code": "ILGIM",
                            "definition": "Indication of status as illegal immigrant.",
                            "display": "illegal immigrant",
                        },
                        {
                            "code": "INCAR",
                            "definition": "Indication of status as incarcerated.",
                            "display": "incarcerated",
                        },
                        {
                            "code": "PROB",
                            "definition": "Indication of probation status.",
                            "display": "probation",
                        },
                        {
                            "code": "REFUG",
                            "definition": "Indication of refugee status.",
                            "display": "refugee",
                        },
                        {
                            "code": "UNEMPL",
                            "definition": "Indication of unemployed status.",
                            "display": "unemployed",
                        },
                    ],
                    "definition": "Code specifying observations or indicators related to socio-economic status used to assess to assess for services, e.g., discharge planning, or to establish eligibility for coverage under a policy or program.",
                    "display": "socio economic status",
                },
            ],
            "definition": "Codes specify the category of observation, evidence, or document used to assess for services, e.g., discharge planning, or to establish eligibility for coverage under a policy or program. The type of evidence is coded as observation values.",
            "display": "ActCoverageAssessmentObservationValue",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActCoverageAssessmentObservationValue

    Codes specify the category of observation, evidence, or document used to assess for services, e.g., discharge planning, or to establish eligibility for coverage under a policy or program. The type of evidence is coded as observation values.
    """

    underscore_allergy_test_value = CodeSystemConcept(
        {
            "code": "_AllergyTestValue",
            "concept": [
                {
                    "code": "A0",
                    "definition": "Description:Patient exhibits no reaction to the challenge agent.",
                    "display": "no reaction",
                },
                {
                    "code": "A1",
                    "definition": "Description:Patient exhibits a minimal reaction to the challenge agent.",
                    "display": "minimal reaction",
                },
                {
                    "code": "A2",
                    "definition": "Description:Patient exhibits a mild reaction to the challenge agent.",
                    "display": "mild reaction",
                },
                {
                    "code": "A3",
                    "definition": "Description:Patient exhibits moderate reaction to the challenge agent.",
                    "display": "moderate reaction",
                },
                {
                    "code": "A4",
                    "definition": "Description:Patient exhibits a severe reaction to the challenge agent.",
                    "display": "severe reaction",
                },
            ],
            "definition": "Indicates the result of a particular allergy test.  E.g. Negative, Mild, Moderate, Severe",
            "display": "AllergyTestValue",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    AllergyTestValue

    Indicates the result of a particular allergy test.  E.g. Negative, Mild, Moderate, Severe
    """

    underscore_composite_measure_scoring = CodeSystemConcept(
        {
            "code": "_CompositeMeasureScoring",
            "concept": [
                {
                    "code": "ALLORNONESCR",
                    "definition": "Code specifying that the measure uses all-or-nothing scoring. All-or-nothing scoring places an individual in the numerator of the composite measure if and only if they are in the numerator of all component measures in which they are in the denominator.",
                    "display": "All-or-nothing Scoring",
                },
                {
                    "code": "LINEARSCR",
                    "definition": "Code specifying that the measure uses linear scoring. Linear scoring computes the fraction of component measures in which the individual appears in the numerator, giving equal weight to each component measure.",
                    "display": "Linear Scoring",
                },
                {
                    "code": "OPPORSCR",
                    "definition": "Code specifying that the measure uses opportunity-based scoring. In opportunity-based scoring the measure score is determined by combining the denominator and numerator of each component measure to determine an overall composite score.",
                    "display": "Opportunity Scoring",
                },
                {
                    "code": "WEIGHTSCR",
                    "definition": "Code specifying that the measure uses weighted scoring. Weighted scoring assigns a factor to each component measure to weight that measure's contribution to the overall score.",
                    "display": "Weighted Scoring",
                },
            ],
            "definition": "Observation values that communicate the method used in a quality measure to combine the component measure results included in an composite measure.",
            "display": "CompositeMeasureScoring",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    CompositeMeasureScoring

    Observation values that communicate the method used in a quality measure to combine the component measure results included in an composite measure.
    """

    underscore_coverage_limit_observation_value = CodeSystemConcept(
        {
            "code": "_CoverageLimitObservationValue",
            "concept": [
                {
                    "code": "_CoverageLevelObservationValue",
                    "concept": [
                        {
                            "code": "ADC",
                            "definition": "Description:Child over an age as specified by coverage policy or program, e.g., student, differently abled, and income dependent.",
                            "display": "adult child",
                        },
                        {
                            "code": "CHD",
                            "definition": "Description:Dependent biological, adopted, foster child as specified by coverage policy or program.",
                            "display": "child",
                        },
                        {
                            "code": "DEP",
                            "definition": "Description:Person requiring functional and/or financial assistance from another person as specified by coverage policy or program.",
                            "display": "dependent",
                        },
                        {
                            "code": "DP",
                            "definition": "Description:Persons registered as a family unit in a domestic partner registry as specified by law and by coverage policy or program.",
                            "display": "domestic partner",
                        },
                        {
                            "code": "ECH",
                            "definition": "Description:An individual employed by an employer who receive remuneration in wages, salary, commission, tips, piece-rates, or pay-in-kind through the employeraTMs payment system (i.e., not a contractor) as specified by coverage policy or program.",
                            "display": "employee",
                        },
                        {
                            "code": "FLY",
                            "definition": "Description:As specified by coverage policy or program.",
                            "display": "family coverage",
                        },
                        {
                            "code": "IND",
                            "definition": "Description:Person as specified by coverage policy or program.",
                            "display": "individual",
                        },
                        {
                            "code": "SSP",
                            "definition": "Description:A pair of people of the same gender who live together as a family as specified by coverage policy or program, e.g., Naomi and Ruth from the Book of Ruth; Socrates and Alcibiades",
                            "display": "same sex partner",
                        },
                    ],
                    "definition": "Description:Coded observation values for types of covered parties under a policy or program based on their personal relationships or employment status.",
                    "display": "CoverageLevelObservationValue",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                }
            ],
            "definition": "Description:Coded observation values for coverage limitations, for e.g., types of claims or types of parties covered under a policy or program.",
            "display": "CoverageLimitObservationValue",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    CoverageLimitObservationValue

    Description:Coded observation values for coverage limitations, for e.g., types of claims or types of parties covered under a policy or program.
    """

    underscore_criticality_observation_value = CodeSystemConcept(
        {
            "code": "_CriticalityObservationValue",
            "concept": [
                {
                    "code": "CRITH",
                    "definition": "Worst case result of a future exposure is assessed to be life-threatening or having high potential for organ system failure.",
                    "display": "high criticality",
                },
                {
                    "code": "CRITL",
                    "definition": "Worst case result of a future exposure is not assessed to be life-threatening or having high potential for organ system failure.",
                    "display": "low criticality",
                },
                {
                    "code": "CRITU",
                    "definition": "Unable to assess the worst case result of a future exposure.",
                    "display": "unable to assess criticality",
                },
            ],
            "definition": "A clinical judgment as to the worst case result of a future exposure (including substance administration). When the worst case result is assessed to have a life-threatening or organ system threatening potential, it is considered to be of high criticality.",
            "display": "CriticalityObservationValue",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    CriticalityObservationValue

    A clinical judgment as to the worst case result of a future exposure (including substance administration). When the worst case result is assessed to have a life-threatening or organ system threatening potential, it is considered to be of high criticality.
    """

    underscore_employment_status = CodeSystemConcept(
        {
            "code": "_EmploymentStatus",
            "concept": [
                {
                    "code": "Employed",
                    "definition": "Individuals who, during the last week: a) did any work for at least 1 hour as paid or unpaid employees of a business or government organization; worked in their own businesses, professions, or on their own farms; or b) were not working, but who have a job or business from which the individual was temporarily absent because of vacation, illness, bad weather, childcare problems, maternity or paternity leave, labor-management dispute, job training, or other family or personal reasons, regardless of whether or not they were paid for the time off or were seeking other jobs.",
                    "display": "Employed",
                },
                {
                    "code": "NotInLaborForce",
                    "definition": "Persons not classified as employed or unemployed, meaning those who have no job and are not looking for one.",
                    "display": "Not In Labor Force",
                },
                {
                    "code": "Unemployed",
                    "definition": "Persons who currently have no employment, but are available for work and have made specific efforts to find employment.",
                    "display": "Unemployed",
                },
            ],
            "definition": "Concepts representing whether a person does or does not currently have a job or is not currently in the labor pool seeking employment.",
            "display": "_EmploymentStatus",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    _EmploymentStatus

    Concepts representing whether a person does or does not currently have a job or is not currently in the labor pool seeking employment.
    """

    underscore_genetic_observation_value = CodeSystemConcept(
        {
            "code": "_GeneticObservationValue",
            "concept": [
                {
                    "code": "Homozygote",
                    "definition": "Description: An individual having different alleles at one or more loci regarding a specific character",
                    "display": "HOMO",
                }
            ],
            "definition": "Description: The domain contains genetic analysis specific observation values, e.g. Homozygote, Heterozygote, etc.",
            "display": "GeneticObservationValue",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    GeneticObservationValue

    Description: The domain contains genetic analysis specific observation values, e.g. Homozygote, Heterozygote, etc.
    """

    underscore_observation_measure_scoring = CodeSystemConcept(
        {
            "code": "_ObservationMeasureScoring",
            "concept": [
                {
                    "code": "COHORT",
                    "definition": "A measure in which either short-term cross-section or long-term longitudinal analysis is performed over a group of subjects defined by a set of common properties or defining characteristics (e.g., Male smokers between the ages of 40 and 50 years, exposure to treatment, exposure duration).",
                    "display": "cohort measure scoring",
                },
                {
                    "code": "CONTVAR",
                    "definition": "A measure score in which each individual value for the measure can fall anywhere along a continuous scale (e.g., mean time to thrombolytics which aggregates the time in minutes from a case presenting with chest pain to the time of administration of thrombolytics).",
                    "display": "continuous variable measure scoring",
                },
                {
                    "code": "PROPOR",
                    "definition": "A score derived by dividing the number of cases that meet a criterion for quality (the numerator) by the number of eligible cases within a given time frame (the denominator) where the numerator cases are a subset of the denominator cases (e.g., percentage of eligible women with a mammogram performed in the last year).",
                    "display": "proportion measure scoring",
                },
                {
                    "code": "RATIO",
                    "definition": "A score that may have a value of zero or greater that is derived by dividing a count of one type of data by a count of another type of data (e.g., the number of patients with central lines who develop infection divided by the number of central line days).",
                    "display": "ratio measure scoring",
                },
            ],
            "definition": "Observation values used to indicate the type of scoring (e.g. proportion, ratio) used by a health quality measure.",
            "display": "ObservationMeasureScoring",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ObservationMeasureScoring

    Observation values used to indicate the type of scoring (e.g. proportion, ratio) used by a health quality measure.
    """

    underscore_observation_measure_type = CodeSystemConcept(
        {
            "code": "_ObservationMeasureType",
            "concept": [
                {
                    "code": "COMPOSITE",
                    "definition": "A measure that is composed from one or more other measures and indicates an overall summary of those measures.",
                    "display": "composite measure type",
                },
                {
                    "code": "EFFICIENCY",
                    "definition": "A measure related to the efficiency of medical treatment.",
                    "display": "efficiency measure type",
                },
                {
                    "code": "EXPERIENCE",
                    "definition": "A measure related to the level of patient engagement or patient experience of care.",
                    "display": "experience measure type",
                },
                {
                    "code": "OUTCOME",
                    "concept": [
                        {
                            "code": "INTERM-OM",
                            "definition": "A measure that evaluates the change over time of a physiologic state observable that is associated with a specific long-term health outcome.",
                            "display": "intermediate clinical outcome measure",
                        },
                        {
                            "code": "PRO-PM",
                            "definition": "A measure that is a comparison of patient reported outcomes for a single or multiple patients collected via an instrument specifically designed to obtain input directly from patients.",
                            "display": "intermediate clinical outcome measure",
                        },
                    ],
                    "definition": "A measure that indicates the result of the performance (or non-performance) of a function or process.",
                    "display": "outcome measure type",
                },
                {
                    "code": "PROCESS",
                    "concept": [
                        {
                            "code": "APPROPRIATE",
                            "definition": "A measure that assesses the use of one or more processes where the expected health benefit exceeds the expected negative consequences.",
                            "display": "appropriate use process measure",
                        }
                    ],
                    "definition": "A measure which focuses on a process which leads to a certain outcome, meaning that a scientific basis exists for believing that the process, when executed well, will increase the probability of achieving a desired outcome.",
                    "display": "process measure type",
                },
                {
                    "code": "RESOURCE",
                    "definition": "A measure related to the extent of use of clinical resources or cost of care.",
                    "display": "resource use measure type",
                },
                {
                    "code": "STRUCTURE",
                    "definition": "A measure related to the structure of patient care.",
                    "display": "structure measure type",
                },
            ],
            "definition": "Observation values used to indicate what kind of health quality measure is used.",
            "display": "ObservationMeasureType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ObservationMeasureType

    Observation values used to indicate what kind of health quality measure is used.
    """

    underscore_observation_population_inclusion = CodeSystemConcept(
        {
            "code": "_ObservationPopulationInclusion",
            "concept": [
                {
                    "code": "DENEX",
                    "definition": "Patients who should be removed from the eMeasure population and denominator before determining if numerator criteria are met. Denominator exclusions are used in proportion and ratio measures to help narrow the denominator.",
                    "display": "denominator exclusions",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2013-07-26"},
                    ],
                },
                {
                    "code": "DENEXCEP",
                    "definition": "Denominator exceptions are those conditions that should remove a patient, procedure or unit of measurement from the denominator only if the numerator criteria are not met. Denominator exceptions allow for adjustment of the calculated score for those providers with higher risk populations. Denominator exceptions are used only in proportion eMeasures. They are not appropriate for ratio or continuous variable eMeasures.  Denominator exceptions allow for the exercise of clinical judgment and should be specifically defined where capturing the information in a structured manner fits the clinical workflow. Generic denominator exception reasons used in proportion eMeasures fall into three general categories:\r\n\n                        \n                           Medical reasons\n                           Patient reasons\n                           System reasons",
                    "display": "denominator exceptions",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2013-07-26"},
                    ],
                },
                {
                    "code": "DENOM",
                    "definition": "It can be the same as the initial patient population or a subset of the initial patient population to further constrain the population for the purpose of the eMeasure. Different measures within an eMeasure set may have different Denominators. Continuous Variable eMeasures do not have a Denominator, but instead define a Measure Population.",
                    "display": "denominator",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2013-07-26"},
                    ],
                },
                {
                    "code": "IP",
                    "concept": [
                        {
                            "code": "IPP",
                            "definition": "The initial patient population refers to all patients to be evaluated by a specific quality measure who share a common set of specified characteristics within a specific measurement set to which a given measure belongs. Details often include information based upon specific age groups, diagnoses, diagnostic and procedure codes, and enrollment periods.",
                            "display": "initial patient population",
                            "property": [
                                {"code": "status", "valueCode": "deprecated"},
                                {
                                    "code": "deprecationDate",
                                    "valueDateTime": "2013-07-26",
                                },
                            ],
                        }
                    ],
                    "definition": "The initial population refers to all entities to be evaluated by a specific quality measure who share a common set of specified characteristics within a specific measurement set to which a given measure belongs.",
                    "display": "initial population",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2013-07-26"},
                    ],
                },
                {
                    "code": "MSRPOPL",
                    "definition": "Measure population is used only in continuous variable eMeasures. It is a narrative description of the eMeasure population. \n(e.g., all patients seen in the Emergency Department during the measurement period).",
                    "display": "measure population",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2013-07-26"},
                    ],
                },
                {
                    "code": "NUMER",
                    "definition": "Numerators are used in proportion and ratio eMeasures. In proportion measures the numerator criteria are the processes or outcomes expected for each patient, procedure, or other unit of measurement defined in the denominator. In ratio measures the numerator is related, but not directly derived from the denominator (e.g., a numerator listing the number of central line blood stream infections and a denominator indicating the days per thousand of central line usage in a specific time period).",
                    "display": "numerator",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2013-07-26"},
                    ],
                },
                {
                    "code": "NUMEX",
                    "definition": "Numerator Exclusions are used only in ratio eMeasures to define instances that should not be included in the numerator data. (e.g., if the number of central line blood stream infections per 1000 catheter days were to exclude infections with a specific bacterium, that bacterium would be listed as a numerator exclusion.)",
                    "display": "numerator exclusions",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2013-07-26"},
                    ],
                },
            ],
            "definition": "Observation values used to assert various populations that a subject falls into.",
            "display": "ObservationPopulationInclusion",
            "property": [
                {"code": "status", "valueCode": "deprecated"},
                {"code": "deprecationDate", "valueDateTime": "2013-07-26"},
            ],
        }
    )
    """
    ObservationPopulationInclusion

    Observation values used to assert various populations that a subject falls into.
    """

    underscore_partial_completion_scale = CodeSystemConcept(
        {
            "code": "_PartialCompletionScale",
            "concept": [
                {
                    "code": "G",
                    "definition": "Value for Act.partialCompletionCode attribute that implies 81-99% completion",
                    "display": "Great extent",
                },
                {
                    "code": "LE",
                    "definition": "Value for Act.partialCompletionCode attribute that implies 61-80% completion",
                    "display": "Large extent",
                },
                {
                    "code": "ME",
                    "definition": "Value for Act.partialCompletionCode attribute that implies 41-60% completion",
                    "display": "Medium extent",
                },
                {
                    "code": "MI",
                    "definition": "Value for Act.partialCompletionCode attribute that implies 1-20% completion",
                    "display": "Minimal extent",
                },
                {
                    "code": "N",
                    "definition": "Value for Act.partialCompletionCode attribute that implies 0% completion",
                    "display": "None",
                },
                {
                    "code": "S",
                    "definition": "Value for Act.partialCompletionCode attribute that implies 21-40% completion",
                    "display": "Some extent",
                },
            ],
            "definition": "PartialCompletionScale",
            "display": "PartialCompletionScale",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    PartialCompletionScale

    PartialCompletionScale
    """

    underscore_security_observation_value = CodeSystemConcept(
        {
            "code": "_SecurityObservationValue",
            "concept": [
                {
                    "code": "_SECINTOBV",
                    "concept": [
                        {
                            "code": "_SECALTINTOBV",
                            "concept": [
                                {
                                    "code": "ABSTRED",
                                    "definition": "Security metadata observation values used to indicate the use of a more abstract version of the content, e.g., replacing exact value of an age or date field with a range, or remove the left digits of a credit card number or SSN.",
                                    "display": "abstracted",
                                },
                                {
                                    "code": "AGGRED",
                                    "definition": "Security metadata observation values used to indicate the use of an algorithmic combination of actual values with the result of an aggregate function, e.g., average, sum, or count in order to limit disclosure of an IT resource (data, information object, service, or system capability) to the minimum necessary.",
                                    "display": "aggregated",
                                },
                                {
                                    "code": "ANONYED",
                                    "definition": "Security metadata observation value conveying the alteration integrity of an IT resource (data, information object, service, or system capability) by used to indicate the mechanism by which software systems can strip portions of the resource that could allow the identification of the source of the information or the information subject.  No key to relink the data is retained.",
                                    "display": "anonymized",
                                },
                                {
                                    "code": "MAPPED",
                                    "definition": 'Security metadata observation value used to indicate that the IT resource semantic content has been transformed from one encoding to another.\r\n\n                        \n                           Usage Note: "MAP" code does not indicate the semantic fidelity of the transformed content.\r\n\n                        To indicate semantic fidelity for maps of HL7 to other code systems, this security alteration integrity observation may be further specified using an Act valued with Value Set: MapRelationship (2.16.840.1.113883.1.11.11052).\r\n\n                        Semantic fidelity of the mapped IT Resource may also be indicated using a SecurityIntegrityConfidenceObservation.',
                                    "display": "mapped",
                                },
                                {
                                    "code": "MASKED",
                                    "definition": 'Security metadata observation value conveying the alteration integrity of an IT resource (data, information object, service, or system capability) by indicating the mechanism by which software systems can make data unintelligible (that is, as unreadable and unusable by algorithmically transforming plaintext into ciphertext) such that it can only be accessed or used by authorized users.  An authorized user may be provided a key to decrypt per license or "shared secret".\r\n\n                        \n                           Usage Note: "MASKED" may be used, per applicable policy, as a flag to indicate to a user or receiver that some portion of an IT resource has been further encrypted, and may be accessed only by an authorized user or receiver to which a decryption key is provided.',
                                    "display": "masked",
                                },
                                {
                                    "code": "PSEUDED",
                                    "definition": "Security metadata observation value conveying the alteration integrity of an IT resource (data, information object, service, or system capability), by indicating the mechanism by which software systems can strip portions of the resource that could allow the identification of the source of the information or the information subject.  Custodian may retain a key to relink data necessary to reidentify the information subject.\r\n\n                        \n                           Rationale: Personal data which has been processed to make it impossible to know whose data it is. Used particularly for secondary use of health data. In some cases, it may be possible for authorized individuals to restore the identity of the individual, e.g.,for public health case management.  Based on ISO/TS 25237:2008 Health informaticsâ€”Pseudonymization",
                                    "display": "pseudonymized",
                                },
                                {
                                    "code": "REDACTED",
                                    "definition": 'Security metadata observation value used to indicate the mechanism by which software systems can filter an IT resource (data, information object, service, or system capability) to remove any portion of the resource that is not authorized to be access, used, or disclosed.\r\n\n                        \n                           Usage Note: "REDACTED" may be used, per applicable policy, as a flag to indicate to a user or receiver that some portion of an IT resource has filtered and not included in the content accessed or received.',
                                    "display": "redacted",
                                },
                                {
                                    "code": "SUBSETTED",
                                    "definition": "Metadata observation used to indicate that some information has been removed from the source object when the view this object contains was constructed because of configuration options when the view was created. The content may not be suitable for use as the basis of a record update\r\n\n                        \n                           Usage Note: This is not suitable to be used when information is removed for security reasons - see the code REDACTED for this use.",
                                    "display": "subsetted",
                                },
                                {
                                    "code": "SYNTAC",
                                    "definition": 'Security metadata observation value used to indicate that the IT resource syntax has been transformed from one syntactical representation to another.  \r\n\n                        \n                           Usage Note: "SYNTAC" code does not indicate the syntactical correctness of the syntactically transformed IT resource.',
                                    "display": "syntactic transform",
                                },
                                {
                                    "code": "TRSLT",
                                    "definition": 'Security metadata observation value used to indicate that the IT resource has been translated from one human language to another.  \r\n\n                        \n                           Usage Note: "TRSLT" does not indicate the fidelity of the translation or the languages translated.\r\n\n                        The fidelity of the IT Resource translation may be indicated using a SecurityIntegrityConfidenceObservation.\r\n\n                        To indicate languages, use the Value Set:HumanLanguage (2.16.840.1.113883.1.11.11526)',
                                    "display": "translated",
                                },
                                {
                                    "code": "VERSIONED",
                                    "definition": "Security metadata observation value conveying the alteration integrity of an IT resource (data, information object, service, or system capability)  which indicates that the resource only retains versions of an IT resource  for access and use per applicable policy\r\n\n                        \n                           Usage Note: When this code is used, expectation is that the system has removed historical versions of the data that falls outside the time period deemed to be the effective time of the applicable version.",
                                    "display": "versioned",
                                },
                            ],
                            "definition": "Abstract security metadata observation values used to indicate mechanism used for authorized alteration of an IT resource (data, information object, service, or system capability)",
                            "display": "alteration integrity",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_SECDATINTOBV",
                            "concept": [
                                {
                                    "code": "CRYTOHASH",
                                    "definition": "Security metadata observation value used to indicate the mechanism by which software systems can establish that data was not modified in transit.\r\n\n                        \n                           Rationale: This definition is intended to align with the ISO 22600-2 3.3.19 definition of cryptographic checkvalue: Information which is derived by performing a cryptographic transformation (see cryptography) on the data unit.  The derivation of the checkvalue may be performed in one or more steps and is a result of a mathematical function of the key and a data unit. It is usually used to check the integrity of a data unit.\r\n\n                        \n                           Examples: \n                        \r\n\n                        \n                           SHA-1\n                           SHA-2 (Secure Hash Algorithm)",
                                    "display": "cryptographic hash function",
                                },
                                {
                                    "code": "DIGSIG",
                                    "definition": "Security metadata observation value used to indicate the mechanism by which software systems use digital signature to establish that data has not been modified.  \r\n\n                        \n                           Rationale: This definition is intended to align with the ISO 22600-2 3.3.26 definition of digital signature:  Data appended to, or a cryptographic transformation (see cryptography) of, a data unit that allows a recipient of the data unit to prove the source and integrity of the data unit and protect against forgery e.g., by the recipient.",
                                    "display": "digital signature",
                                },
                            ],
                            "definition": "Abstract security observation values used to indicate data integrity metadata.\r\n\n                        \n                           Examples: Codes conveying the mechanism used to preserve the accuracy and consistency of an IT resource such as a digital signature and a cryptographic hash function.",
                            "display": "data integrity",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_SECINTCONOBV",
                            "concept": [
                                {
                                    "code": "HRELIABLE",
                                    "definition": "Security metadata observation value used to indicate that the veracity or trustworthiness of an IT resource (data, information object, service, or system capability) for a specified purpose of use is perceived to be or deemed by policy to be very high.",
                                    "display": "highly reliable",
                                },
                                {
                                    "code": "RELIABLE",
                                    "definition": "Security metadata observation value used to indicate that the veracity or trustworthiness of an IT resource (data, information object, service, or system capability) for a specified purpose of use is perceived to be or deemed by policy to be adequate.",
                                    "display": "reliable",
                                },
                                {
                                    "code": "UNCERTREL",
                                    "definition": "Security metadata observation value used to indicate that the veracity or trustworthiness of an IT resource (data, information object, service, or system capability) for a specified purpose of use is perceived to be or deemed by policy to be uncertain.",
                                    "display": "uncertain reliability",
                                },
                                {
                                    "code": "UNRELIABLE",
                                    "definition": "Security metadata observation value used to indicate that the veracity or trustworthiness of an IT resource (data, information object, service, or system capability) for a specified purpose of use is perceived to be or deemed by policy to be inadequate.",
                                    "display": "unreliable",
                                },
                            ],
                            "definition": "Abstract security observation value used to indicate integrity confidence metadata.\r\n\n                        \n                           Examples: Codes conveying the level of reliability and trustworthiness of an IT resource.",
                            "display": "integrity confidence",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_SECINTPRVOBV",
                            "concept": [
                                {
                                    "code": "_SECINTPRVABOBV",
                                    "concept": [
                                        {
                                            "code": "CLINAST",
                                            "definition": "Security provenance metadata observation value used to indicate that an IT resource (data, information object, service, or system capability) was asserted by a clinician.",
                                            "display": "clinician asserted",
                                        },
                                        {
                                            "code": "DEVAST",
                                            "definition": "Security provenance metadata observation value used to indicate that an IT resource (data, information object, service, or system capability) was asserted by a device.",
                                            "display": "device asserted",
                                        },
                                        {
                                            "code": "HCPAST",
                                            "definition": "Security provenance metadata observation value used to indicate that an IT resource (data, information object, service, or system capability) was asserted by a healthcare professional.",
                                            "display": "healthcare professional asserted",
                                        },
                                        {
                                            "code": "PACQAST",
                                            "definition": "Security provenance metadata observation value used to indicate that an IT resource (data, information object, service, or system capability) was asserted by a patient acquaintance.",
                                            "display": "patient acquaintance asserted",
                                        },
                                        {
                                            "code": "PATAST",
                                            "definition": "Security provenance metadata observation value used to indicate that an IT resource (data, information object, service, or system capability) was asserted by a patient.",
                                            "display": "patient asserted",
                                        },
                                        {
                                            "code": "PAYAST",
                                            "definition": "Security provenance metadata observation value used to indicate that an IT resource (data, information object, service, or system capability) was asserted by a payer.",
                                            "display": "payer asserted",
                                        },
                                        {
                                            "code": "PROAST",
                                            "definition": "Security provenance metadata observation value used to indicate that an IT resource (data, information object, service, or system capability) was asserted by a professional.",
                                            "display": "professional asserted",
                                        },
                                        {
                                            "code": "SDMAST",
                                            "definition": "Security provenance metadata observation value used to indicate that an IT resource (data, information object, service, or system capability) was asserted by a substitute decision maker.",
                                            "display": "substitute decision maker asserted",
                                        },
                                    ],
                                    "definition": "Abstract security provenance metadata observation value used to indicate the entity that asserted an IT resource (data, information object, service, or system capability).\r\n\n                        \n                           Examples: Codes conveying the provenance metadata about the entity asserting the resource.",
                                    "display": "provenance asserted by",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "_SECINTPRVRBOBV",
                                    "concept": [
                                        {
                                            "code": "CLINRPT",
                                            "definition": "Security provenance metadata observation value used to indicate that an IT resource (data, information object, service, or system capability) was reported by a clinician.",
                                            "display": "clinician reported",
                                        },
                                        {
                                            "code": "DEVRPT",
                                            "definition": "Security provenance metadata observation value used to indicate that an IT resource (data, information object, service, or system capability) was reported by a device.",
                                            "display": "device reported",
                                        },
                                        {
                                            "code": "HCPRPT",
                                            "definition": "Security provenance metadata observation value used to indicate that an IT resource (data, information object, service, or system capability) was reported by a healthcare professional.",
                                            "display": "healthcare professional reported",
                                        },
                                        {
                                            "code": "PACQRPT",
                                            "definition": "Security provenance metadata observation value used to indicate that an IT resource (data, information object, service, or system capability) was reported by a patient acquaintance.",
                                            "display": "patient acquaintance reported",
                                        },
                                        {
                                            "code": "PATRPT",
                                            "definition": "Security provenance metadata observation value used to indicate that an IT resource (data, information object, service, or system capability) was reported by a patient.",
                                            "display": "patient reported",
                                        },
                                        {
                                            "code": "PAYRPT",
                                            "definition": "Security provenance metadata observation value used to indicate that an IT resource (data, information object, service, or system capability) was reported by a payer.",
                                            "display": "payer reported",
                                        },
                                        {
                                            "code": "PRORPT",
                                            "definition": "Security provenance metadata observation value used to indicate that an IT resource (data, information object, service, or system capability) was reported by a professional.",
                                            "display": "professional reported",
                                        },
                                        {
                                            "code": "SDMRPT",
                                            "definition": "Security provenance metadata observation value used to indicate that an IT resource (data, information object, service, or system capability) was reported by a substitute decision maker.",
                                            "display": "substitute decision maker reported",
                                        },
                                    ],
                                    "definition": "Abstract security provenance metadata observation value used to indicate the entity that reported the resource (data, information object, service, or system capability).\r\n\n                        \n                           Examples: Codes conveying the provenance metadata about the entity reporting an IT resource.",
                                    "display": "provenance reported by",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                            ],
                            "definition": "Abstract security metadata observation value used to indicate the provenance of an IT resource (data, information object, service, or system capability).\r\n\n                        \n                           Examples: Codes conveying the provenance metadata about the entity reporting an IT resource.",
                            "display": "provenance",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                    ],
                    "definition": "Abstract security observation values used to indicate security integrity metadata.\r\n\n                        \n                           Examples: Codes conveying integrity status, integrity confidence, and provenance.",
                    "display": "security integrity",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "SECTRSTOBV",
                    "concept": [
                        {
                            "code": "TRSTACCRDOBV",
                            "definition": "Values for security trust accreditation metadata observation made about the formal declaration by an authority or neutral third party that validates the technical, security, trust, and business practice conformance of Trust Agents to facilitate security, interoperability, and trust among participants within a security domain or trust framework.",
                            "display": "trust accreditation observation",
                        },
                        {
                            "code": "TRSTAGREOBV",
                            "definition": "Values for security trust agreement metadata observation made about privacy and security requirements with which a security domain must comply. [ISO IEC 10181-1]\n[ISO IEC 10181-1]",
                            "display": "trust agreement observation",
                        },
                        {
                            "code": "TRSTCERTOBV",
                            "definition": "Values for security trust certificate metadata observation made about a set of security-relevant data issued by a security authority or trusted third party, together with security information which is used to provide the integrity and data origin authentication services for an IT resource (data, information object, service, or system capability). [Based on ISO IEC 10181-1]\r\n\n                        For example, a Certificate Policy (CP), which is a named set of rules that indicates the applicability of a certificate to a particular community and/or class of application with common security requirements.  A particular Certificate Policy might indicate the applicability of a type of certificate to the authentication of electronic data interchange transactions for the trading of goods within a given price range.  Another example is Cross Certification with Federal Bridge.",
                            "display": "trust certificate observation",
                        },
                        {
                            "code": "TRSTLOAOBV",
                            "concept": [
                                {
                                    "code": "LOAAN",
                                    "concept": [
                                        {
                                            "code": "LOAAN1",
                                            "definition": "Indicator of low digital quality or reliability of the digital reliability of the verification and validation process used to verify the claimed identity of an entity by securely associating an identifier and its authenticator. [Based on ISO 7498-2] \r\n\n                        The degree of confidence in the vetting process used to establish the identity of the individual to whom the credential was issued, and 2) the degree of confidence that the individual who uses the credential is the individual to whom the credential was issued. [OMB M-04-04 E-Authentication Guidance for Federal Agencies] \r\n\n                        Low authentication level of assurance indicates that the relying party may have little or no confidence in the asserted identity's validity. Level 1 requires little or no confidence in the asserted identity. No identity proofing is required at this level, but the authentication mechanism should provide some assurance that the same claimant is accessing the protected transaction or data. A wide range of available authentication technologies can be employed and any of the token methods of Levels 2, 3, or 4, including Personal Identification Numbers (PINs), may be used. To be authenticated, the claimant must prove control of the token through a secure authentication protocol. At Level 1, long-term shared authentication secrets may be revealed to verifiers.  Assertions issued about claimants as a result of a successful authentication are either cryptographically authenticated by relying parties (using approved methods) or are obtained directly from a trusted party via a secure authentication protocol.   [Summary of the technical requirements specified in NIST SP 800-63 for the four levels of assurance defined by the December 2003, the Office of Management and Budget (OMB) issued Memorandum M-04-04, E-Authentication Guidance for Federal Agencies.]",
                                            "display": "low authentication level of assurance",
                                        },
                                        {
                                            "code": "LOAAN2",
                                            "definition": "Indicator of basic digital quality or reliability of the digital reliability of the verification and validation process used to verify the claimed identity of an entity by securely associating an identifier and its authenticator. [Based on ISO 7498-2] \r\n\n                        The degree of confidence in the vetting process used to establish the identity of the individual to whom the credential was issued, and 2) the degree of confidence that the individual who uses the credential is the individual to whom the credential was issued. [OMB M-04-04 E-Authentication Guidance for Federal Agencies]\r\n\n                        Basic authentication level of assurance indicates that the relying party may have some confidence in the asserted identity's validity. Level 2 requires confidence that the asserted identity is accurate. Level 2 provides for single-factor remote network authentication, including identity-proofing requirements for presentation of identifying materials or information. A wide range of available authentication technologies can be employed, including any of the token methods of Levels 3 or 4, as well as passwords. Successful authentication requires that the claimant prove through a secure authentication protocol that the claimant controls the token.  Eavesdropper, replay, and online guessing attacks are prevented.  \nLong-term shared authentication secrets, if used, are never revealed to any party except the claimant and verifiers operated by the CSP; however, session (temporary) shared secrets may be provided to independent verifiers by the CSP. Approved cryptographic techniques are required. Assertions issued about claimants as a result of a successful authentication are either cryptographically authenticated by relying parties (using approved methods) or are obtained directly from a trusted party via a secure authentication protocol.   [Summary of the technical requirements specified in NIST SP 800-63 for the four levels of assurance defined by the December 2003, the Office of Management and Budget (OMB) issued Memorandum M-04-04, E-Authentication Guidance for Federal Agencies.]",
                                            "display": "basic authentication level of assurance",
                                        },
                                        {
                                            "code": "LOAAN3",
                                            "definition": 'Indicator of medium digital quality or reliability of the digital reliability of verification and validation of the process used to verify the claimed identity of an entity by securely associating an identifier and its authenticator. [Based on ISO 7498-2] \r\n\n                        The degree of confidence in the vetting process used to establish the identity of the individual to whom the credential was issued, and 2) the degree of confidence that the individual who uses the credential is the individual to whom the credential was issued. [OMB M-04-04 E-Authentication Guidance for Federal Agencies] \r\n\n                        Medium authentication level of assurance indicates that the relying party may have high confidence in the asserted identity\'s validity.  Level 3 is appropriate for transactions that need high confidence in the accuracy of the asserted identity. Level 3 provides multifactor remote network authentication. At this level, identity-proofing procedures require verification of identifying materials and information. Authentication is based on proof of possession of a key or password through a cryptographic protocol. Cryptographic strength mechanisms should protect the primary authentication token (a cryptographic key) against compromise by the protocol threats, including eavesdropper, replay, online guessing, verifier impersonation, and man-in-the-middle attacks. A minimum of two authentication factors is required. Three kinds of tokens may be used:\r\n\n                        \n                           "soft" cryptographic token, which has the key stored on a general-purpose computer, \n                           "hard" cryptographic token, which has the key stored on a special hardware device, and \n                           "one-time password" device token, which has symmetric key stored on a personal hardware device that is a cryptographic module validated at FIPS 140-2 Level 1 or higher. Validation testing of cryptographic modules and algorithms for conformance to Federal Information Processing Standard (FIPS) 140-2, Security Requirements for Cryptographic Modules, is managed by NIST.\n                        \n                        Authentication requires that the claimant prove control of the token through a secure authentication protocol. The token must be unlocked with a password or biometric representation, or a password must be used in a secure authentication protocol, to establish two-factor authentication. Long-term shared authentication secrets, if used, are never revealed to any party except the claimant and verifiers operated directly by the CSP; however, session (temporary) shared secrets may be provided to independent verifiers by the CSP. Approved cryptographic techniques are used for all operations.  Assertions issued about claimants as a result of a successful authentication are either cryptographically authenticated by relying parties (using approved methods) or are obtained directly from a trusted party via a secure authentication protocol.    [Summary of the technical requirements specified in NIST SP 800-63 for the four levels of assurance defined by the December 2003, the Office of Management and Budget (OMB) issued Memorandum M-04-04, E-Authentication Guidance for Federal Agencies.]',
                                            "display": "medium authentication level of assurance",
                                        },
                                        {
                                            "code": "LOAAN4",
                                            "definition": "Indicator of high digital quality or reliability of the digital reliability of the verification and validation process used to verify the claimed identity of an entity by securely associating an identifier and its authenticator. [Based on ISO 7498-2] \r\n\n                        The degree of confidence in the vetting process used to establish the identity of the individual to whom the credential was issued, and 2) the degree of confidence that the individual who uses the credential is the individual to whom the credential was issued. [OMB M-04-04 E-Authentication Guidance for Federal Agencies]\r\n\n                        High authentication level of assurance indicates that the relying party may have very high confidence in the asserted identity's validity. Level 4 is for transactions that need very high confidence in the accuracy of the asserted identity. Level 4 provides the highest practical assurance of remote network authentication. Authentication is based on proof of possession of a key through a cryptographic protocol. This level is similar to Level 3 except that only â€œhardâ€? cryptographic tokens are allowed, cryptographic module validation requirements are strengthened, and subsequent critical data transfers must be authenticated via a key that is bound to the authentication process. The token should be a hardware cryptographic module validated at FIPS 140-2 Level 2 or higher overall with at least FIPS 140-2 Level 3 physical security. This level requires a physical token, which cannot readily be copied, and operator authentication at Level 2 and higher, and ensures good, two-factor remote authentication.\r\n\n                        Level 4 requires strong cryptographic authentication of all parties and all sensitive data transfers between the parties. Either public key or symmetric key technology may be used. Authentication requires that the claimant prove through a secure authentication protocol that the claimant controls the token. Eavesdropper, replay, online guessing, verifier impersonation, and man-in-the-middle attacks are prevented. Long-term shared authentication secrets, if used, are never revealed to any party except the claimant and verifiers operated directly by the CSP; however, session (temporary) shared secrets may be provided to independent verifiers by the CSP. Strong approved cryptographic techniques are used for all operations. All sensitive data transfers are cryptographically authenticated using keys bound to the authentication process.   [Summary of the technical requirements specified in NIST SP 800-63 for the four levels of assurance defined by the December 2003, the Office of Management and Budget (OMB) issued Memorandum M-04-04, E-Authentication Guidance for Federal Agencies.]",
                                            "display": "high authentication level of assurance",
                                        },
                                    ],
                                    "definition": "The value assigned as the indicator of the digital quality or reliability of the verification and validation process used to verify the claimed identity of an entity by securely associating an identifier and its authenticator. [Based on ISO 7498-2]\r\n\n                        For example, the degree of confidence in the vetting process used to establish the identity of the individual to whom the credential was issued, and 2) the degree of confidence that the individual who uses the credential is the individual to whom the credential was issued. [OMB M-04-04 E-Authentication Guidance for Federal Agencies]",
                                    "display": "authentication level of assurance value",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "LOAAP",
                                    "concept": [
                                        {
                                            "code": "LOAAP1",
                                            "definition": "Indicator of the low digital quality or reliability of a defined sequence of messages between a Claimant and a Verifier that demonstrates that the Claimant has possession and control of a valid token to establish his/her identity, and optionally, demonstrates to the Claimant that he or she is communicating with the intended Verifier. [Based on NIST SP 800-63-2]\r\n\n                        Low authentication process level of assurance indicates that (1) long-term shared authentication secrets may be revealed to verifiers; and (2) assertions and assertion references require protection from manufacture/modification and reuse attacks.  [Summary of the technical requirements specified in NIST SP 800-63 for the four levels of assurance defined by the December 2003, the Office of Management and Budget (OMB) issued Memorandum M-04-04, E-Authentication Guidance for Federal Agencies.]",
                                            "display": "low authentication process level of assurance",
                                        },
                                        {
                                            "code": "LOAAP2",
                                            "definition": "Indicator of the basic digital quality or reliability of a defined sequence of messages between a Claimant and a Verifier that demonstrates that the Claimant has possession and control of a valid token to establish his/her identity, and optionally, demonstrates to the Claimant that he or she is communicating with the intended Verifier. [Based on NIST SP 800-63-2]\r\n\n                        Basic authentication process level of assurance indicates that long-term shared authentication secrets are never revealed to any other party except Credential Service Provider (CSP).  Sessions (temporary) shared secrets may be provided to independent verifiers by CSP. Long-term shared authentication secrets, if used, are never revealed to any other party except Verifiers operated by the Credential Service Provider (CSP); however, session (temporary) shared secrets may be provided to independent Verifiers by the CSP. In addition to Level 1 requirements, assertions are resistant to disclosure, redirection, capture and substitution attacks. Approved cryptographic techniques are required.  [Summary of the technical requirements specified in NIST SP 800-63 for the four levels of assurance defined by the December 2003, the Office of Management and Budget (OMB) issued Memorandum M-04-04, E-Authentication Guidance for Federal Agencies.]",
                                            "display": "basic authentication process level of assurance",
                                        },
                                        {
                                            "code": "LOAAP3",
                                            "definition": "Indicator of the medium digital quality or reliability of a defined sequence of messages between a Claimant and a Verifier that demonstrates that the Claimant has possession and control of a valid token to establish his/her identity, and optionally, demonstrates to the Claimant that he or she is communicating with the intended Verifier. [Based on NIST SP 800-63-2]\r\n\n                        Medium authentication process level of assurance indicates that the token can be unlocked with password, biometric, or uses a secure multi-token authentication protocol to establish two-factor authentication.  Long-term shared authentication secrets are never revealed to any party except the Claimant and Credential Service Provider (CSP).\r\n\n                        Authentication requires that the Claimant prove, through a secure authentication protocol, that he or she controls the token. The Claimant unlocks the token with a password or biometric, or uses a secure multi-token authentication protocol to establish two-factor authentication (through proof of possession of a physical or software token in combination with some memorized secret knowledge). Long-term shared authentication secrets, if used, are never revealed to any party except the Claimant and Verifiers operated directly by the CSP; however, session (temporary) shared secrets may be provided to independent Verifiers by the CSP. In addition to Level 2 requirements, assertions are protected against repudiation by the Verifier.",
                                            "display": "medium authentication process level of assurance",
                                        },
                                        {
                                            "code": "LOAAP4",
                                            "definition": "Indicator of the high digital quality or reliability of a defined sequence of messages between a Claimant and a Verifier that demonstrates that the Claimant has possession and control of a valid token to establish his/her identity, and optionally, demonstrates to the Claimant that he or she is communicating with the intended Verifier. [Based on NIST SP 800-63-2]\r\n\n                        High authentication process level of assurance indicates all sensitive data transfer are cryptographically authenticated using keys bound to the authentication process.  Level 4 requires strong cryptographic authentication of all communicating parties and all sensitive data transfers between the parties. Either public key or symmetric key technology may be used. Authentication requires that the Claimant prove through a secure authentication protocol that he or she controls the token. All protocol threats at Level 3 are required to be prevented at Level 4. Protocols shall also be strongly resistant to man-in-the-middle attacks. Long-term shared authentication secrets, if used, are never revealed to any party except the Claimant and Verifiers operated directly by the CSP; however, session (temporary) shared secrets may be provided to independent Verifiers by the CSP. Approved cryptographic techniques are used for all operations. All sensitive data transfers are cryptographically authenticated using keys bound to the authentication process.   [Summary of the technical requirements specified in NIST SP 800-63 for the four levels of assurance defined by the December 2003, the Office of Management and Budget (OMB) issued Memorandum M-04-04, E-Authentication Guidance for Federal Agencies.]",
                                            "display": "high authentication process level of assurance",
                                        },
                                    ],
                                    "definition": "The value assigned as the indicator of the digital quality or reliability of a defined sequence of messages between a Claimant and a Verifier that demonstrates that the Claimant has possession and control of a valid token to establish his/her identity, and optionally, demonstrates to the Claimant that he or she is communicating with the intended Verifier. [Based on NIST SP 800-63-2]",
                                    "display": "authentication process level of assurance value",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "LOAAS",
                                    "concept": [
                                        {
                                            "code": "LOAAS1",
                                            "definition": "Indicator of the low quality or reliability of the statement from a Verifier to a Relying Party (RP) that contains identity information about a Subscriber. Assertions may also contain verified attributes.\r\n\n                        Assertions and assertion references require protection from modification and reuse attacks.  [Summary of the technical requirements specified in NIST SP 800-63 for the four levels of assurance defined by the December 2003, the Office of Management and Budget (OMB) issued Memorandum M-04-04, E-Authentication Guidance for Federal Agencies.]",
                                            "display": "low assertion level of assurance",
                                        },
                                        {
                                            "code": "LOAAS2",
                                            "definition": "Indicator of the basic quality or reliability of the statement from a Verifier to a Relying Party (RP) that contains identity information about a Subscriber. Assertions may also contain verified attributes.\r\n\n                        Assertions are resistant to disclosure, redirection, capture and substitution attacks.  Approved cryptographic techniques are required for all assertion protocols.  [Summary of the technical requirements specified in NIST SP 800-63 for the four levels of assurance defined by the December 2003, the Office of Management and Budget (OMB) issued Memorandum M-04-04, E-Authentication Guidance for Federal Agencies.]",
                                            "display": "basic assertion level of assurance",
                                        },
                                        {
                                            "code": "LOAAS3",
                                            "definition": "Indicator of the medium quality or reliability of the statement from a Verifier to a Relying Party (RP) that contains identity information about a Subscriber. Assertions may also contain verified attributes.\r\n\n                        Assertions are protected against repudiation by the verifier.  [Summary of the technical requirements specified in NIST SP 800-63 for the four levels of assurance defined by the December 2003, the Office of Management and Budget (OMB) issued Memorandum M-04-04, E-Authentication Guidance for Federal Agencies.]",
                                            "display": "medium assertion level of assurance",
                                        },
                                        {
                                            "code": "LOAAS4",
                                            "definition": 'Indicator of the high quality or reliability of the statement from a Verifier to a Relying Party (RP) that contains identity information about a Subscriber. Assertions may also contain verified attributes.\r\n\n                        Strongly resistant to man-in-the-middle attacks. "Bearer" assertions are not used.  "Holder-of-key" assertions may be used. RP maintains records of the assertions.  [Summary of the technical requirements specified in NIST SP 800-63 for the four levels of assurance defined by the December 2003, the Office of Management and Budget (OMB) issued Memorandum M-04-04, E-Authentication Guidance for Federal Agencies.]',
                                            "display": "high assertion level of assurance",
                                        },
                                    ],
                                    "definition": "The value assigned as the indicator of the high quality or reliability of the statement from a Verifier to a Relying Party (RP) that contains identity information about a Subscriber. Assertions may also contain verified attributes.",
                                    "display": "assertion level of assurance value",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "LOACM",
                                    "concept": [
                                        {
                                            "code": "LOACM1",
                                            "definition": "Indicator of the low digital quality or reliability of the activities performed by the Credential Service Provider (CSP) subsequent to electronic authentication registration, identity proofing and issuance activities to manage and safeguard the integrity of an issued credential and its binding to an identity. Little or no confidence that an individual has maintained control over a token that has been entrusted to him or her and that that token has not been compromised. Characteristics include weak identity binding to tokens and plaintext passwords or secrets not transmitted across a network. [Electronic Authentication Guideline - Recommendations of the National Institute of Standards and Technology, NIST Special Publication 800-63-1, Dec 2011]",
                                            "display": "low token and credential management level of assurance",
                                        },
                                        {
                                            "code": "LOACM2",
                                            "definition": "Indicator of the basic digital quality or reliability of the activities performed by the Credential Service Provider (CSP) subsequent to electronic authentication registration, identity proofing and issuance activities to manage and safeguard the integrity of an issued credential and its binding to an identity.  Some confidence that an individual has maintained control over a token that has been entrusted to him or her and that that token has not been compromised. Characteristics include:  Verification must prove claimant controls the token; token resists online guessing, replay, session hijacking, and eavesdropping attacks; and  token is at least weakly resistant to man-in-the middle attacks. [Electronic Authentication Guideline - Recommendations of the National Institute of Standards and Technology, NIST Special Publication 800-63-1, Dec 2011]",
                                            "display": "basic token and credential management level of assurance",
                                        },
                                        {
                                            "code": "LOACM3",
                                            "definition": "Indicator of the medium digital quality or reliability of the activities performed by the Credential Service Provider (CSP) subsequent to electronic authentication registration, identity proofing and issuance activities to manage and safeguard the integrity of an issued credential and itâ€™s binding to an identity.  High confidence that an individual has maintained control over a token that has been entrusted to him or her and that that token has not been compromised. Characteristics  include: Ownership of token verifiable through security authentication protocol and credential management protects against verifier impersonation attacks. [Electronic Authentication Guideline - Recommendations of the National Institute of Standards and Technology, NIST Special Publication 800-63-1, Dec 2011]",
                                            "display": "medium token and credential management level of assurance",
                                        },
                                        {
                                            "code": "LOACM4",
                                            "definition": "Indicator of the high digital quality or reliability of the activities performed by the Credential Service Provider (CSP) subsequent to electronic authentication registration, identity proofing and issuance activities to manage and safeguard the integrity of an issued credential and itâ€™s binding to an identity.  Very high confidence that an individual has maintained control over a token that has been entrusted to him or her and that that token has not been compromised. Characteristics include: Verifier can prove control of token through a secure protocol; credential management supports strong cryptographic authentication of all communication parties. [Electronic Authentication Guideline - Recommendations of the National Institute of Standards and Technology, NIST Special Publication 800-63-1, Dec 2011]",
                                            "display": "high token and credential management level of assurance",
                                        },
                                    ],
                                    "definition": "Indicator of the digital quality or reliability of the activities performed by the Credential Service Provider (CSP) subsequent to electronic authentication registration, identity proofing and issuance activities to manage and safeguard the integrity of an issued credential and its binding to an identity. [Electronic Authentication Guideline - Recommendations of the National Institute of Standards and Technology, NIST Special Publication 800-63-1, Dec 2011]",
                                    "display": "token and credential management level of assurance value)",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "LOAID",
                                    "concept": [
                                        {
                                            "code": "LOAID1",
                                            "definition": "Indicator of low digital quality or reliability in the process of ascertaining that an individual is who he or she claims to be.  Requires that a continuity of identity be maintained but does not require identity proofing. [Based on Electronic Authentication Guideline - Recommendations of the National Institute of Standards and Technology, NIST Special Publication 800-63-1, Dec 2011]",
                                            "display": "low identity proofing level of assurance",
                                        },
                                        {
                                            "code": "LOAID2",
                                            "definition": "Indicator of some digital quality or reliability in the process of ascertaining that that an individual is who he or she claims to be. Requires identity proofing via presentation of identifying material or information. [Based on Electronic Authentication Guideline - Recommendations of the National Institute of Standards and Technology, NIST Special Publication 800-63-1, Dec 2011]",
                                            "display": "basic identity proofing level of assurance",
                                        },
                                        {
                                            "code": "LOAID3",
                                            "definition": "Indicator of high digital quality or reliability in the process of ascertaining that an individual is who he or she claims to be.  Requires identity proofing procedures for verification of identifying materials and information. [Based on Electronic Authentication Guideline - Recommendations of the National Institute of Standards and Technology, NIST Special Publication 800-63-1, Dec 2011]",
                                            "display": "medium identity proofing level of assurance",
                                        },
                                        {
                                            "code": "LOAID4",
                                            "definition": "Indicator of high digital quality or reliability in the process of ascertaining that an individual is who he or she claims to be.  Requires identity proofing procedures for verification of identifying materials and information. [Based on Electronic Authentication Guideline - Recommendations of the National Institute of Standards and Technology, NIST Special Publication 800-63-1, Dec 2011]",
                                            "display": "high identity proofing level of assurance",
                                        },
                                    ],
                                    "definition": "Indicator of the quality or reliability in the process of ascertaining that an individual is who he or she claims to be.",
                                    "display": "identity proofing level of assurance",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "LOANR",
                                    "concept": [
                                        {
                                            "code": "LOANR1",
                                            "definition": "Indicator of low digital quality or reliability in the process of establishing proof of delivery and proof of origin. [Based on ISO 7498-2]",
                                            "display": "low non-repudiation level of assurance",
                                        },
                                        {
                                            "code": "LOANR2",
                                            "definition": "Indicator of basic digital quality or reliability in the process of establishing proof of delivery and proof of origin. [Based on ISO 7498-2]",
                                            "display": "basic non-repudiation level of assurance",
                                        },
                                        {
                                            "code": "LOANR3",
                                            "definition": "Indicator of medium digital quality or reliability in the process of establishing proof of delivery and proof of origin. [Based on ISO 7498-2]",
                                            "display": "medium non-repudiation level of assurance",
                                        },
                                        {
                                            "code": "LOANR4",
                                            "definition": "Indicator of high digital quality or reliability in the process of establishing proof of delivery and proof of origin. [Based on ISO 7498-2]",
                                            "display": "high non-repudiation level of assurance",
                                        },
                                    ],
                                    "definition": "Indicator of the digital quality or reliability in the process of establishing proof of delivery and proof of origin. [Based on ISO 7498-2]",
                                    "display": "non-repudiation level of assurance value",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "LOARA",
                                    "concept": [
                                        {
                                            "code": "LOARA1",
                                            "definition": "Indicator of low digital quality or reliability of the information exchange between network-connected devices where the information cannot be reliably protected end-to-end by a single organizationâ€™s security controls. [Based on NIST SP 800-63-2]",
                                            "display": "low remote access level of assurance",
                                        },
                                        {
                                            "code": "LOARA2",
                                            "definition": "Indicator of basic digital quality or reliability of the information exchange between network-connected devices where the information cannot be reliably protected end-to-end by a single organizationâ€™s security controls. [Based on NIST SP 800-63-2]",
                                            "display": "basic remote access level of assurance",
                                        },
                                        {
                                            "code": "LOARA3",
                                            "definition": "Indicator of medium digital quality or reliability of the information exchange between network-connected devices where the information cannot be reliably protected end-to-end by a single organizationâ€™s security controls. [Based on NIST SP 800-63-2]",
                                            "display": "medium remote access level of assurance",
                                        },
                                        {
                                            "code": "LOARA4",
                                            "definition": "Indicator of high digital quality or reliability of the information exchange between network-connected devices where the information cannot be reliably protected end-to-end by a single organization's security controls. [Based on NIST SP 800-63-2]",
                                            "display": "high remote access level of assurance",
                                        },
                                    ],
                                    "definition": "Indicator of the digital quality or reliability of the information exchange between network-connected devices where the information cannot be reliably protected end-to-end by a single organizationâ€™s security controls. [Based on NIST SP 800-63-2]",
                                    "display": "remote access level of assurance value",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "LOATK",
                                    "concept": [
                                        {
                                            "code": "LOATK1",
                                            "definition": "Indicator of the low digital quality or reliability of single and multi-token authentication. Permits the use of any of the token methods of Levels 2, 3, or 4. [Electronic Authentication Guideline - Recommendations of the National Institute of Standards and Technology, NIST Special Publication 800-63-1, Dec 2011]",
                                            "display": "low token level of assurance",
                                        },
                                        {
                                            "code": "LOATK2",
                                            "definition": "Indicator of the basic digital quality or reliability of single and multi-token authentication. Requires single factor authentication using memorized secret tokens, pre-registered knowledge tokens, look-up secret tokens, out of band tokens, or single factor one-time password devices. [Electronic Authentication Guideline - Recommendations of the National Institute of Standards and Technology, NIST Special Publication 800-63-1, Dec 2011]",
                                            "display": "basic token level of assurance",
                                        },
                                        {
                                            "code": "LOATK3",
                                            "definition": "Indicator of the medium digital quality or reliability of single and multi-token authentication. Requires two authentication factors. Provides multi-factor remote network authentication. Permits multi-factor software cryptographic token. [Electronic Authentication Guideline - Recommendations of the National Institute of Standards and Technology, NIST Special Publication 800-63-1, Dec 2011]",
                                            "display": "medium token level of assurance",
                                        },
                                        {
                                            "code": "LOATK4",
                                            "definition": "Indicator of the high digital quality or reliability of single and multi-token authentication. Requires token that is a hardware cryptographic module validated at validated at Federal Information Processing Standard (FIPS) 140-2 Level 2 or higher overall with at least FIPS 140-2 Level 3 physical security. Level 4 token requirements can be met by using the PIV authentication key of a FIPS 201 compliant Personal Identity Verification (PIV) Card.  [Electronic Authentication Guideline - Recommendations of the National Institute of Standards and Technology, NIST Special Publication 800-63-1, Dec 2011]",
                                            "display": "high token level of assurance",
                                        },
                                    ],
                                    "definition": "Indicator of the digital quality or reliability of single and multi-token authentication. [Electronic Authentication Guideline - Recommendations of the National Institute of Standards and Technology, NIST Special Publication 800-63-1, Dec 2011]",
                                    "display": "token level of assurance value",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                            ],
                            "definition": "Values for security trust assurance metadata observation made about the digital quality or reliability of a trust assertion, activity, capability, information exchange, mechanism, process, or protocol.",
                            "display": "trust assurance observation",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "TRSTMECOBV",
                            "definition": "Values for security trust mechanism metadata observation made about a security architecture system component that supports enforcement of security policies.",
                            "display": "none supplied 6",
                        },
                    ],
                    "definition": "Observation value used to indicate aspects of trust applicable to an IT resource (data, information object, service, or system capability).",
                    "display": "security trust observation",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": "Observation values used to indicate security observation metadata.",
            "display": "SecurityObservationValue",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    SecurityObservationValue

    Observation values used to indicate security observation metadata.
    """

    underscore_severity_observation = CodeSystemConcept(
        {
            "code": "_SeverityObservation",
            "concept": [
                {
                    "code": "H",
                    "definition": "Indicates the condition may be life-threatening or has the potential to cause permanent injury.",
                    "display": "High",
                },
                {
                    "code": "L",
                    "definition": "Indicates the condition may result in some adverse consequences but is unlikely to substantially affect the situation of the subject.",
                    "display": "Low",
                },
                {
                    "code": "M",
                    "definition": "Indicates the condition may result in noticable adverse adverse consequences but is unlikely to be life-threatening or cause permanent injury.",
                    "display": "Moderate",
                },
            ],
            "definition": "Potential values for observations of severity.",
            "display": "SeverityObservation",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    SeverityObservation

    Potential values for observations of severity.
    """

    underscore_subject_body_position = CodeSystemConcept(
        {
            "code": "_SubjectBodyPosition",
            "concept": [
                {
                    "code": "LLD",
                    "definition": "Lying on the left side.",
                    "display": "left lateral decubitus",
                },
                {
                    "code": "PRN",
                    "definition": "Lying with the front or ventral surface downward; lying face down.",
                    "display": "prone",
                },
                {
                    "code": "RLD",
                    "definition": "Lying on the right side.",
                    "display": "right lateral decubitus",
                },
                {
                    "code": "SFWL",
                    "definition": "A semi-sitting position in bed with the head of the bed elevated approximately 45 degrees.",
                    "display": "Semi-Fowler's",
                },
                {
                    "code": "SIT",
                    "definition": "Resting the body on the buttocks, typically with upper torso erect or semi erect.",
                    "display": "sitting",
                },
                {
                    "code": "STN",
                    "definition": "To be stationary, upright, vertical, on one's legs.",
                    "display": "standing",
                },
                {
                    "code": "SUP",
                    "concept": [
                        {
                            "code": "RTRD",
                            "definition": "Lying on the back, on an inclined plane, typically about 30-45 degrees with head raised and feet lowered.",
                            "display": "reverse trendelenburg",
                        },
                        {
                            "code": "TRD",
                            "definition": "Lying on the back, on an inclined plane, typically about 30-45 degrees, with  head lowered and feet raised.",
                            "display": "trendelenburg",
                        },
                    ],
                    "definition": "supine",
                    "display": "supine",
                },
            ],
            "definition": "Contains codes for defining the observed, physical position of a subject, such as during an observation, assessment, collection of a specimen, etc.  ECG waveforms and vital signs, such as blood pressure, are two examples where a general, observed position typically needs to be noted.",
            "display": "_SubjectBodyPosition",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    _SubjectBodyPosition

    Contains codes for defining the observed, physical position of a subject, such as during an observation, assessment, collection of a specimen, etc.  ECG waveforms and vital signs, such as blood pressure, are two examples where a general, observed position typically needs to be noted.
    """

    underscore_verification_outcome_value = CodeSystemConcept(
        {
            "code": "_VerificationOutcomeValue",
            "concept": [
                {
                    "code": "ACT",
                    "definition": "Definition: Coverage is in effect for healthcare service(s) and/or product(s).",
                    "display": "active coverage",
                },
                {
                    "code": "ACTPEND",
                    "definition": "Definition: Coverage is in effect for healthcare service(s) and/or product(s) - Pending Investigation",
                    "display": "active - pending investigation",
                },
                {
                    "code": "ELG",
                    "definition": "Definition: Coverage is in effect for healthcare service(s) and/or product(s).",
                    "display": "eligible",
                },
                {
                    "code": "INACT",
                    "definition": "Definition: Coverage is not in effect for healthcare service(s) and/or product(s).",
                    "display": "inactive",
                },
                {
                    "code": "INPNDINV",
                    "definition": "Definition: Coverage is not in effect for healthcare service(s) and/or product(s) - Pending Investigation.",
                    "display": "inactive - pending investigation",
                },
                {
                    "code": "INPNDUPD",
                    "definition": "Definition: Coverage is not in effect for healthcare service(s) and/or product(s) - Pending Eligibility Update.",
                    "display": "inactive - pending eligibility update",
                },
                {
                    "code": "NELG",
                    "definition": "Definition: Coverage is not in effect for healthcare service(s) and/or product(s). May optionally include reasons for the ineligibility.",
                    "display": "not eligible",
                },
            ],
            "definition": "Values for observations of verification act results\r\n\n                        \n                           Examples: Verified, not verified, verified with warning.",
            "display": "verification outcome",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    verification outcome

    Values for observations of verification act results

                        
                           Examples: Verified, not verified, verified with warning.
    """

    underscore_work_schedule = CodeSystemConcept(
        {
            "code": "_WorkSchedule",
            "concept": [
                {
                    "code": "DS",
                    "definition": "A person who is scheduled for work during daytime hours (for example between 6am and 6pm) on a regular basis.",
                    "display": "daytime shift",
                },
                {
                    "code": "EMS",
                    "definition": "Consistent Early morning schedule of 13 hours or less per shift (between 2 am and 2 pm)",
                    "display": "early morning shift",
                },
                {
                    "code": "ES",
                    "definition": "A person who is scheduled for work during evening hours (for example between 2pm and midnight) on a regular basis.",
                    "display": "evening shift",
                },
                {
                    "code": "NS",
                    "definition": "Scheduled for work during nighttime hours (for example between 9pm and 8am) on a regular basis.",
                    "display": "night shift",
                },
                {
                    "code": "RSWN",
                    "definition": "Scheduled for work times that change periodically between days, and/or evenings, and includes some night shifts.",
                    "display": "rotating shift with nights",
                },
                {
                    "code": "RSWON",
                    "definition": "Scheduled for work days/times that change periodically between days, but does not include night or evening work.",
                    "display": "rotating shift without nights",
                },
                {
                    "code": "SS",
                    "definition": "Shift consisting of two distinct work periods each day that are separated by a break of a few hours (for example 2 to 4 hours)",
                    "display": "split shift",
                },
                {
                    "code": "VLS",
                    "definition": "Shifts of 17 or more hours.",
                    "display": "very long shift",
                },
                {
                    "code": "VS",
                    "definition": "Irregular, unpredictable hours scheduled on a short notice (for example, less than 2 day notice): inconsistent schedule, on-call, as needed, as available.",
                    "display": "variable shift",
                },
            ],
            "definition": "Concepts that describe an individual's typical arrangement of working hours for an occupation.",
            "display": "_WorkSchedule",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    _WorkSchedule

    Concepts that describe an individual's typical arrangement of working hours for an occupation.
    """

    underscore_annotation_value = CodeSystemConcept(
        {
            "code": "_AnnotationValue",
            "definition": "AnnotationValue",
            "display": "AnnotationValue",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "status", "valueCode": "retired"},
            ],
        }
    )
    """
    AnnotationValue

    AnnotationValue
    """

    underscore_common_clinical_observation_value = CodeSystemConcept(
        {
            "code": "_CommonClinicalObservationValue",
            "definition": "Description:Used in a patient care message to value simple clinical (non-lab) observations.",
            "display": "common clinical observation",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "status", "valueCode": "retired"},
            ],
        }
    )
    """
    common clinical observation

    Description:Used in a patient care message to value simple clinical (non-lab) observations.
    """

    underscore_individual_case_safety_report_value_domains = CodeSystemConcept(
        {
            "code": "_IndividualCaseSafetyReportValueDomains",
            "definition": "This domain is established as a parent to a variety of value domains being defined to support the communication of Individual Case Safety Reports to regulatory bodies. Arguably, this aggregation is not taxonomically pure, but the grouping will facilitate the management of these domains.",
            "display": "Individual Case Safety Report Value Domains",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "status", "valueCode": "retired"},
            ],
        }
    )
    """
    Individual Case Safety Report Value Domains

    This domain is established as a parent to a variety of value domains being defined to support the communication of Individual Case Safety Reports to regulatory bodies. Arguably, this aggregation is not taxonomically pure, but the grouping will facilitate the management of these domains.
    """

    underscore_indication_value = CodeSystemConcept(
        {
            "code": "_IndicationValue",
            "definition": "Indicates the specific observation result which is the reason for the action (prescription, lab test, etc.). E.g. Headache, Ear infection, planned diagnostic image (requiring contrast agent), etc.",
            "display": "IndicationValue",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "status", "valueCode": "retired"},
            ],
        }
    )
    """
    IndicationValue

    Indicates the specific observation result which is the reason for the action (prescription, lab test, etc.). E.g. Headache, Ear infection, planned diagnostic image (requiring contrast agent), etc.
    """

    class Meta:
        resource = _resource
