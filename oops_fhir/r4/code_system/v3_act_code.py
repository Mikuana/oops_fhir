from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ActCode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ActCode:
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

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ActCode
    """

    underscore_act_account_code = CodeSystemConcept(
        {
            "code": "_ActAccountCode",
            "concept": [
                {
                    "code": "ACCTRECEIVABLE",
                    "definition": "An account for collecting charges, reversals, adjustments and payments, including deductibles, copayments, coinsurance (financial transactions) credited or debited to the account receivable account for a patient's encounter.",
                    "display": "account receivable",
                },
                {"code": "CASH", "definition": "Cash", "display": "Cash"},
                {
                    "code": "CC",
                    "concept": [
                        {
                            "code": "AE",
                            "definition": "American Express",
                            "display": "American Express",
                        },
                        {
                            "code": "DN",
                            "definition": "Diner's Club",
                            "display": "Diner's Club",
                        },
                        {
                            "code": "DV",
                            "definition": "Discover Card",
                            "display": "Discover Card",
                        },
                        {
                            "code": "MC",
                            "definition": "Master Card",
                            "display": "Master Card",
                        },
                        {"code": "V", "definition": "Visa", "display": "Visa"},
                    ],
                    "definition": "Description: Types of advance payment to be made on a plastic card usually issued by a financial institution used of purchasing services and/or products.",
                    "display": "credit card",
                },
                {
                    "code": "PBILLACCT",
                    "definition": "An account representing charges and credits (financial transactions) for a patient's encounter.",
                    "display": "patient billing account",
                },
            ],
            "definition": "An account represents a grouping of financial transactions that are tracked and reported together with a single balance. \t \tExamples of account codes (types) are Patient billing accounts (collection of charges), Cost centers; Cash.",
            "display": "ActAccountCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActAccountCode

    An account represents a grouping of financial transactions that are tracked and reported together with a single balance. 	 	Examples of account codes (types) are Patient billing accounts (collection of charges), Cost centers; Cash.
    """

    underscore_act_adjudication_code = CodeSystemConcept(
        {
            "code": "_ActAdjudicationCode",
            "concept": [
                {
                    "code": "_ActAdjudicationGroupCode",
                    "concept": [
                        {
                            "code": "CONT",
                            "definition": "Transaction counts and value totals by Contract Identifier.",
                            "display": "contract",
                        },
                        {
                            "code": "DAY",
                            "definition": "Transaction counts and value totals for each calendar day within the date range specified.",
                            "display": "day",
                        },
                        {
                            "code": "LOC",
                            "definition": "Transaction counts and value totals by service location (e.g clinic).",
                            "display": "location",
                        },
                        {
                            "code": "MONTH",
                            "definition": "Transaction counts and value totals for each calendar month within the date range specified.",
                            "display": "month",
                        },
                        {
                            "code": "PERIOD",
                            "definition": "Transaction counts and value totals for the date range specified.",
                            "display": "period",
                        },
                        {
                            "code": "PROV",
                            "definition": "Transaction counts and value totals by Provider Identifier.",
                            "display": "provider",
                        },
                        {
                            "code": "WEEK",
                            "definition": "Transaction counts and value totals for each calendar week within the date range specified.",
                            "display": "week",
                        },
                        {
                            "code": "YEAR",
                            "definition": "Transaction counts and value totals for each calendar year within the date range specified.",
                            "display": "year",
                        },
                    ],
                    "definition": "Catagorization of grouping criteria for the associated transactions and/or summary (totals, subtotals).",
                    "display": "ActAdjudicationGroupCode",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "AA",
                    "concept": [
                        {
                            "code": "ANF",
                            "definition": "The invoice element has been accepted for payment but one or more adjustment(s) have been made to one or more invoice element line items (component charges) without changing the amount.  \r\n\n                        Invoice element can be reversed (nullified).  \r\n\n                        Recommend that the invoice element is saved for DUR (Drug Utilization Reporting).",
                            "display": "adjudicated with adjustments and no financial impact",
                        }
                    ],
                    "definition": "The invoice element has been accepted for payment but one or more adjustment(s) have been made to one or more invoice element line items (component charges).  \r\n\n                        Also includes the concept 'Adjudicate as zero' and items not covered under a particular Policy.  \r\n\n                        Invoice element can be reversed (nullified).  \r\n\n                        Recommend that the invoice element is saved for DUR (Drug Utilization Reporting).",
                    "display": "adjudicated with adjustments",
                },
                {
                    "code": "AR",
                    "definition": "The invoice element has passed through the adjudication process but payment is refused due to one or more reasons.\r\n\n                        Includes items such as patient not covered, or invoice element is not constructed according to payer rules (e.g. 'invoice submitted too late').\r\n\n                        If one invoice element line item in the invoice element structure is rejected, the remaining line items may not be adjudicated and the complete group is treated as rejected.\r\n\n                        A refused invoice element can be forwarded to the next payer (for Coordination of Benefits) or modified and resubmitted to refusing payer.\r\n\n                        Invoice element cannot be reversed (nullified) as there is nothing to reverse.  \r\n\n                        Recommend that the invoice element is not saved for DUR (Drug Utilization Reporting).",
                    "display": "adjudicated as refused",
                },
                {
                    "code": "AS",
                    "definition": "The invoice element was/will be paid exactly as submitted, without financial adjustment(s).\r\n\n                        If the dollar amount stays the same, but the billing codes have been amended or financial adjustments have been applied through the adjudication process, the invoice element is treated as \"Adjudicated with Adjustment\".\r\n\n                        If information items are included in the adjudication results that do not affect the monetary amounts paid, then this is still Adjudicated as Submitted (e.g. 'reached Plan Maximum on this Claim').  \r\n\n                        Invoice element can be reversed (nullified).  \r\n\n                        Recommend that the invoice element is saved for DUR (Drug Utilization Reporting).",
                    "display": "adjudicated as submitted",
                },
            ],
            "definition": "Includes coded responses that will occur as a result of the adjudication of an electronic invoice at a summary level and provides guidance on interpretation of the referenced adjudication results.",
            "display": "ActAdjudicationCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActAdjudicationCode

    Includes coded responses that will occur as a result of the adjudication of an electronic invoice at a summary level and provides guidance on interpretation of the referenced adjudication results.
    """

    underscore_act_adjudication_result_action_code = CodeSystemConcept(
        {
            "code": "_ActAdjudicationResultActionCode",
            "concept": [
                {
                    "code": "DISPLAY",
                    "definition": "The adjudication result associated is to be displayed to the receiver of the adjudication result.",
                    "display": "Display",
                },
                {
                    "code": "FORM",
                    "definition": "The adjudication result associated is to be printed on the specified form, which is then provided to the covered party.",
                    "display": "Print on Form",
                },
            ],
            "definition": "Actions to be carried out by the recipient of the Adjudication Result information.",
            "display": "ActAdjudicationResultActionCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActAdjudicationResultActionCode

    Actions to be carried out by the recipient of the Adjudication Result information.
    """

    underscore_act_billable_modifier_code = CodeSystemConcept(
        {
            "code": "_ActBillableModifierCode",
            "concept": [
                {
                    "code": "CPTM",
                    "definition": "Description:CPT modifier codes are found in Appendix A of CPT 2000 Standard Edition.",
                    "display": "CPT modifier codes",
                },
                {
                    "code": "HCPCSA",
                    "definition": "Description:HCPCS Level II (HCFA-assigned) and Carrier-assigned (Level III) modifiers are reported in Appendix A of CPT 2000 Standard Edition and in the Medicare Bulletin.",
                    "display": "HCPCS Level II and Carrier-assigned",
                },
            ],
            "definition": "Definition:An identifying modifier code for healthcare interventions or procedures.",
            "display": "ActBillableModifierCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActBillableModifierCode

    Definition:An identifying modifier code for healthcare interventions or procedures.
    """

    underscore_act_billing_arrangement_code = CodeSystemConcept(
        {
            "code": "_ActBillingArrangementCode",
            "concept": [
                {
                    "code": "BLK",
                    "definition": "A billing arrangement where a Provider charges a lump sum to provide a prescribed group (volume) of services to a single patient which occur over a period of time.  Services included in the block may vary.  \r\n\n                        This billing arrangement is also known as Program of Care for some specific Payors and Program Fees for other Payors.",
                    "display": "block funding",
                },
                {
                    "code": "CAP",
                    "definition": "A billing arrangement where the payment made to a Provider is determined by analyzing one or more demographic attributes about the persons/patients who are enrolled with the Provider (in their practice).",
                    "display": "capitation funding",
                },
                {
                    "code": "CONTF",
                    "definition": "A billing arrangement where a Provider charges a lump sum to provide a particular volume of one or more interventions/procedures or groups of interventions/procedures.",
                    "display": "contract funding",
                },
                {
                    "code": "FINBILL",
                    "definition": "A billing arrangement where a Provider charges for non-clinical items.  This includes interest in arrears, mileage, etc.  Clinical content is not \tincluded in Invoices submitted with this type of billing arrangement.",
                    "display": "financial",
                },
                {
                    "code": "ROST",
                    "definition": "A billing arrangement where funding is based on a list of individuals registered as patients of the Provider.",
                    "display": "roster funding",
                },
                {
                    "code": "SESS",
                    "definition": "A billing arrangement where a Provider charges a sum to provide a group (volume) of interventions/procedures to one or more patients within a defined period of time, typically on the same date.  Interventions/procedures included in the session may vary.",
                    "display": "sessional funding",
                },
                {
                    "code": "FFS",
                    "concept": [
                        {
                            "code": "FFPS",
                            "definition": "A first fill where the quantity supplied is less than one full repetition of the ordered amount. (e.g. If the order was 90 tablets, 3 refills, a partial fill might be for only 30 tablets.) and also where the strength supplied is less than the ordered strength (e.g. 10mg for an order of 50mg where a subsequent fill will dispense 40mg tablets)",
                            "display": "first fill, part fill, partial strength",
                        },
                        {
                            "code": "FFCS",
                            "definition": "A first fill where the quantity supplied is equal to one full repetition of the ordered amount. (e.g. If the order was 90 tablets, 3 refills, a complete fill would be for the full 90 tablets) and also where the strength supplied is less than the ordered strength (e.g. 10mg for an order of 50mg where a subsequent fill will dispense 40mg tablets).",
                            "display": "first fill complete, partial strength",
                        },
                        {
                            "code": "TFS",
                            "definition": "A fill where a small portion is provided to allow for determination of the therapy effectiveness and patient tolerance and also where the strength supplied is less than the ordered strength (e.g. 10mg for an order of 50mg where a subsequent fill will dispense 40mg tablets).",
                            "display": "trial fill partial strength",
                        },
                    ],
                    "definition": "A billing arrangement where a Provider charges a separate fee for each intervention/procedure/event or product.\r\n\n                        Fee for Service is used when an individual intervention/procedure/event is used for billing purposes.  In other words, fees are associated with the  intervention/procedure/event.  For example, a specific CCI (Canadian Classification of Interventions) code has an associated fee and is used for billing purposes.",
                    "display": "fee for service",
                    "property": [{"code": "status", "valueCode": "retired"}],
                },
            ],
            "definition": "The type of provision(s)  made for reimbursing for the deliver of healthcare services and/or goods provided by a Provider, over a specified period.",
            "display": "ActBillingArrangementCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActBillingArrangementCode

    The type of provision(s)  made for reimbursing for the deliver of healthcare services and/or goods provided by a Provider, over a specified period.
    """

    underscore_act_bounded_roicode = CodeSystemConcept(
        {
            "code": "_ActBoundedROICode",
            "concept": [
                {
                    "code": "ROIFS",
                    "definition": 'A fully specified bounded Region of Interest (ROI) delineates a ROI in which only those dimensions participate that are specified by boundary criteria, whereas all other dimensions are excluded.  For example a ROI to mark an episode of "ST elevation" in a subset of the EKG leads V2, V3, and V4 would include 4 boundaries, one each for time, V2, V3, and V4.',
                    "display": "fully specified ROI",
                },
                {
                    "code": "ROIPS",
                    "definition": "A partially specified bounded Region of Interest (ROI) specifies a ROI in which at least all values in the dimensions specified by the boundary criteria participate. For example, if an episode of ventricular fibrillations (VFib) is observed, it usually doesn't make sense to exclude any EKG leads from the observation and the partially specified ROI would contain only one boundary for time indicating the time interval where VFib was observed.",
                    "display": "partially specified ROI",
                },
            ],
            "definition": "Type of bounded ROI.",
            "display": "ActBoundedROICode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActBoundedROICode

    Type of bounded ROI.
    """

    underscore_act_care_provision_code = CodeSystemConcept(
        {
            "code": "_ActCareProvisionCode",
            "concept": [
                {
                    "code": "_ActCredentialedCareCode",
                    "concept": [
                        {
                            "code": "_ActCredentialedCareProvisionPersonCode",
                            "concept": [
                                {
                                    "code": "CACC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified anatomic pathology and clinical pathology care",
                                },
                                {
                                    "code": "CAIC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified allergy and immunology care",
                                },
                                {
                                    "code": "CAMC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified aerospace medicine care",
                                },
                                {
                                    "code": "CANC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified anesthesiology care",
                                },
                                {
                                    "code": "CAPC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified anatomic pathology care",
                                },
                                {
                                    "code": "CBGC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified clinical biochemical genetics care",
                                },
                                {
                                    "code": "CCCC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified clinical cytogenetics care",
                                },
                                {
                                    "code": "CCGC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified clinical genetics (M.D.) care",
                                },
                                {
                                    "code": "CCPC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified clinical pathology care",
                                },
                                {
                                    "code": "CCSC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified colon and rectal surgery care",
                                },
                                {
                                    "code": "CDEC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified dermatology care",
                                },
                                {
                                    "code": "CDRC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified diagnostic radiology care",
                                },
                                {
                                    "code": "CEMC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified emergency medicine care",
                                },
                                {
                                    "code": "CFPC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified family practice care",
                                },
                                {
                                    "code": "CIMC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified internal medicine care",
                                },
                                {
                                    "code": "CMGC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified clinical molecular genetics care",
                                },
                                {
                                    "code": "CNEC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board",
                                    "display": "certified neurology care",
                                },
                                {
                                    "code": "CNMC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified nuclear medicine care",
                                },
                                {
                                    "code": "CNQC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified neurology with special qualifications in child neurology care",
                                },
                                {
                                    "code": "CNSC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified neurological surgery care",
                                },
                                {
                                    "code": "COGC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified obstetrics and gynecology care",
                                },
                                {
                                    "code": "COMC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified occupational medicine care",
                                },
                                {
                                    "code": "COPC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified ophthalmology care",
                                },
                                {
                                    "code": "COSC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified orthopaedic surgery care",
                                },
                                {
                                    "code": "COTC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified otolaryngology care",
                                },
                                {
                                    "code": "CPEC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified pediatrics care",
                                },
                                {
                                    "code": "CPGC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified Ph.D. medical genetics care",
                                },
                                {
                                    "code": "CPHC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified public health and general preventive medicine care",
                                },
                                {
                                    "code": "CPRC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified physical medicine and rehabilitation care",
                                },
                                {
                                    "code": "CPSC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified plastic surgery care",
                                },
                                {
                                    "code": "CPYC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified psychiatry care",
                                },
                                {
                                    "code": "CROC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified radiation oncology care",
                                },
                                {
                                    "code": "CRPC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified radiological physics care",
                                },
                                {
                                    "code": "CSUC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified surgery care",
                                },
                                {
                                    "code": "CTSC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified thoracic surgery care",
                                },
                                {
                                    "code": "CURC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified urology care",
                                },
                                {
                                    "code": "CVSC",
                                    "definition": "Description:Scope of responsibility taken on for specialty care as defined by the respective Specialty Board.",
                                    "display": "certified vascular surgery care",
                                },
                                {
                                    "code": "LGPC",
                                    "definition": "Description:Scope of responsibility taken-on for physician care of a patient as defined by a governmental licensing agency.",
                                    "display": "licensed general physician care",
                                },
                            ],
                            "definition": "Description:The type and scope of legal and/or professional responsibility taken-on by the performer of the Act for a specific subject of care as described by an agency for credentialing individuals.",
                            "display": "act credentialed care provision peron",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_ActCredentialedCareProvisionProgramCode",
                            "concept": [
                                {
                                    "code": "AALC",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the respective accreditation agency.",
                                    "display": "accredited assisted living care",
                                },
                                {
                                    "code": "AAMC",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the respective accreditation agency.",
                                    "display": "accredited ambulatory care",
                                },
                                {
                                    "code": "ABHC",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the respective accreditation agency.",
                                    "display": "accredited behavioral health care",
                                },
                                {
                                    "code": "ACAC",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the respective accreditation agency.",
                                    "display": "accredited critical access hospital care",
                                },
                                {
                                    "code": "ACHC",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the respective accreditation agency.",
                                    "display": "accredited hospital care",
                                },
                                {
                                    "code": "AHOC",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the respective accreditation agency.",
                                    "display": "accredited home care",
                                },
                                {
                                    "code": "ALTC",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the respective accreditation agency.",
                                    "display": "accredited long term care",
                                },
                                {
                                    "code": "AOSC",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the respective accreditation agency.",
                                    "display": "accredited office-based surgery care",
                                },
                                {
                                    "code": "CACS",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified acute coronary syndrome care",
                                },
                                {
                                    "code": "CAMI",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified acute myocardial infarction care",
                                },
                                {
                                    "code": "CAST",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified asthma care",
                                },
                                {
                                    "code": "CBAR",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified bariatric surgery care",
                                },
                                {
                                    "code": "CCAD",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified coronary artery disease care",
                                },
                                {
                                    "code": "CCAR",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified cardiac care",
                                },
                                {
                                    "code": "CDEP",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified depression care",
                                },
                                {
                                    "code": "CDGD",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified digestive/gastrointestinal disorders care",
                                },
                                {
                                    "code": "CDIA",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified diabetes care",
                                },
                                {
                                    "code": "CEPI",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified epilepsy care",
                                },
                                {
                                    "code": "CFEL",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified frail elderly care",
                                },
                                {
                                    "code": "CHFC",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified heart failure care",
                                },
                                {
                                    "code": "CHRO",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified high risk obstetrics care",
                                },
                                {
                                    "code": "CHYP",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified hyperlipidemia care",
                                },
                                {
                                    "code": "CMIH",
                                    "definition": "Description:.",
                                    "display": "certified migraine headache care",
                                },
                                {
                                    "code": "CMSC",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified multiple sclerosis care",
                                },
                                {
                                    "code": "COJR",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified orthopedic joint replacement care",
                                },
                                {
                                    "code": "CONC",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified oncology care",
                                },
                                {
                                    "code": "COPD",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified chronic obstructive pulmonary disease care",
                                },
                                {
                                    "code": "CORT",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified organ transplant care",
                                },
                                {
                                    "code": "CPAD",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified parkinsons disease care",
                                },
                                {
                                    "code": "CPND",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified pneumonia disease care",
                                },
                                {
                                    "code": "CPST",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified primary stroke center care",
                                },
                                {
                                    "code": "CSDM",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified stroke disease management care",
                                },
                                {
                                    "code": "CSIC",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified sickle cell care",
                                },
                                {
                                    "code": "CSLD",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified sleep disorders care",
                                },
                                {
                                    "code": "CSPT",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified spine treatment care",
                                },
                                {
                                    "code": "CTBU",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified trauma/burn center care",
                                },
                                {
                                    "code": "CVDC",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified vascular diseases care",
                                },
                                {
                                    "code": "CWMA",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified wound management care",
                                },
                                {
                                    "code": "CWOH",
                                    "definition": "Description:Scope of responsibility taken on by an organization for care of a patient as defined by the disease management certification agency.",
                                    "display": "certified women's health care",
                                },
                            ],
                            "definition": "Description:The type and scope of legal and/or professional responsibility taken-on by the performer of the Act for a specific subject of care as described by an agency for credentialing programs within organizations.",
                            "display": "act credentialed care provision program",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                    ],
                    "definition": "Description:The type and scope of legal and/or professional responsibility taken-on by the performer of the Act for a specific subject of care as described by a credentialing agency, i.e. government or non-government agency. Failure in executing this Act may result in loss of credential to the person or organization who participates as performer of the Act. Excludes employment agreements.\r\n\n                        \n                           Example:Hospital license; physician license; clinic accreditation.",
                    "display": "act credentialed care",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_ActEncounterCode",
                    "concept": [
                        {
                            "code": "AMB",
                            "definition": "A comprehensive term for health care provided in a healthcare facility (e.g. a practitioneraTMs office, clinic setting, or hospital) on a nonresident basis. The term ambulatory usually implies that the patient has come to the location and is not assigned to a bed. Sometimes referred to as an outpatient encounter.",
                            "display": "ambulatory",
                        },
                        {
                            "code": "EMER",
                            "definition": "A patient encounter that takes place at a dedicated healthcare service delivery location where the patient receives immediate evaluation and treatment, provided until the patient can be discharged or responsibility for the patient's care is transferred elsewhere (for example, the patient could be admitted as an inpatient or transferred to another facility.)",
                            "display": "emergency",
                        },
                        {
                            "code": "FLD",
                            "definition": "A patient encounter that takes place both outside a dedicated service delivery location and outside a patient's residence. Example locations might include an accident site and at a supermarket.",
                            "display": "field",
                        },
                        {
                            "code": "HH",
                            "definition": "Healthcare encounter that takes place in the residence of the patient or a designee",
                            "display": "home health",
                        },
                        {
                            "code": "IMP",
                            "concept": [
                                {
                                    "code": "ACUTE",
                                    "definition": "An acute inpatient encounter.",
                                    "display": "inpatient acute",
                                },
                                {
                                    "code": "NONAC",
                                    "definition": "Any category of inpatient encounter except 'acute'",
                                    "display": "inpatient non-acute",
                                },
                            ],
                            "definition": "A patient encounter where a patient is admitted by a hospital or equivalent facility, assigned to a location where patients generally stay at least overnight and provided with room, board, and continuous nursing service.",
                            "display": "inpatient encounter",
                        },
                        {
                            "code": "OBSENC",
                            "definition": "An encounter where the patient usually will start in different encounter, such as one in the emergency department (EMER) but then transition to this type of encounter because they require a significant period of treatment and monitoring to determine whether or not their condition warrants an inpatient admission or discharge. In the majority of cases the decision about admission or discharge will occur within a time period determined by local, regional or national regulation, often between 24 and 48 hours.",
                            "display": "observation encounter",
                        },
                        {
                            "code": "PRENC",
                            "definition": "A patient encounter where patient is scheduled or planned to receive service delivery in the future, and the patient is given a pre-admission account number. When the patient comes back for subsequent service, the pre-admission encounter is selected and is encapsulated into the service registration, and a new account number is generated.\r\n\n                        \n                           Usage Note: This is intended to be used in advance of encounter types such as ambulatory, inpatient encounter, virtual, etc.",
                            "display": "pre-admission",
                        },
                        {
                            "code": "SS",
                            "definition": "An encounter where the patient is admitted to a health care facility for a predetermined length of time, usually less than 24 hours.",
                            "display": "short stay",
                        },
                        {
                            "code": "VR",
                            "definition": "A patient encounter where the patient and the practitioner(s) are not in the same physical location. Examples include telephone conference, email exchange, robotic surgery, and televideo conference.",
                            "display": "virtual",
                        },
                    ],
                    "definition": "Domain provides codes that qualify the ActEncounterClass (ENC)",
                    "display": "ActEncounterCode",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_ActMedicalServiceCode",
                    "concept": [
                        {
                            "code": "ALC",
                            "definition": "Provision of Alternate Level of Care to a patient in an acute bed.  Patient is waiting for placement in a long-term care facility and is unable to return home.",
                            "display": "Alternative Level of Care",
                        },
                        {
                            "code": "CARD",
                            "definition": "Provision of diagnosis and treatment of diseases and disorders affecting the heart",
                            "display": "Cardiology",
                        },
                        {
                            "code": "CHR",
                            "definition": "Provision of recurring care for chronic illness.",
                            "display": "Chronic",
                        },
                        {
                            "code": "DNTL",
                            "definition": "Provision of treatment for oral health and/or dental surgery.",
                            "display": "Dental",
                        },
                        {
                            "code": "DRGRHB",
                            "definition": "Provision of treatment for drug abuse.",
                            "display": "Drug Rehab",
                        },
                        {
                            "code": "GENRL",
                            "definition": "General care performed by a general practitioner or family doctor as a responsible provider for a patient.",
                            "display": "General",
                        },
                        {
                            "code": "MED",
                            "definition": "Provision of diagnostic and/or therapeutic treatment.",
                            "display": "Medical",
                        },
                        {
                            "code": "OBS",
                            "definition": "Provision of care of women during pregnancy, childbirth and immediate postpartum period.  Also known as Maternity.",
                            "display": "Obstetrics",
                        },
                        {
                            "code": "ONC",
                            "definition": "Provision of treatment and/or diagnosis related to tumors and/or cancer.",
                            "display": "Oncology",
                        },
                        {
                            "code": "PALL",
                            "definition": "Provision of care for patients who are living or dying from an advanced illness.",
                            "display": "Palliative",
                        },
                        {
                            "code": "PED",
                            "definition": "Provision of diagnosis and treatment of diseases and disorders affecting children.",
                            "display": "Pediatrics",
                        },
                        {
                            "code": "PHAR",
                            "definition": "Pharmaceutical care performed by a pharmacist.",
                            "display": "Pharmaceutical",
                        },
                        {
                            "code": "PHYRHB",
                            "definition": "Provision of treatment for physical injury.",
                            "display": "Physical Rehab",
                        },
                        {
                            "code": "PSYCH",
                            "definition": "Provision of treatment of psychiatric disorder relating to mental illness.",
                            "display": "Psychiatric",
                        },
                        {
                            "code": "SURG",
                            "definition": "Provision of surgical treatment.",
                            "display": "Surgical",
                        },
                    ],
                    "definition": "General category of medical service provided to the patient during their encounter.",
                    "display": "ActMedicalServiceCode",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": "Description:The type and scope of responsibility taken-on by the performer of the Act for a specific subject of care.",
            "display": "act care provision",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    act care provision

    Description:The type and scope of responsibility taken-on by the performer of the Act for a specific subject of care.
    """

    underscore_act_claim_attachment_category_code = CodeSystemConcept(
        {
            "code": "_ActClaimAttachmentCategoryCode",
            "concept": [
                {
                    "code": "AUTOATTCH",
                    "definition": "Description: Automobile Information Attachment",
                    "display": "auto attachment",
                },
                {
                    "code": "DOCUMENT",
                    "definition": "Description: Document Attachment",
                    "display": "document",
                },
                {
                    "code": "HEALTHREC",
                    "definition": "Description: Health Record Attachment",
                    "display": "health record",
                },
                {
                    "code": "IMG",
                    "definition": "Description: Image Attachment",
                    "display": "image attachment",
                },
                {
                    "code": "LABRESULTS",
                    "definition": "Description: Lab Results Attachment",
                    "display": "lab results",
                },
                {
                    "code": "MODEL",
                    "definition": "Description: Digital Model Attachment",
                    "display": "model",
                },
                {
                    "code": "WIATTCH",
                    "definition": "Description: Work Injury related additional Information Attachment",
                    "display": "work injury report attachment",
                },
                {
                    "code": "XRAY",
                    "definition": "Description: Digital X-Ray Attachment",
                    "display": "x-ray",
                },
            ],
            "definition": "Description: Coded types of attachments included to support a healthcare claim.",
            "display": "ActClaimAttachmentCategoryCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActClaimAttachmentCategoryCode

    Description: Coded types of attachments included to support a healthcare claim.
    """

    underscore_act_consent_type = CodeSystemConcept(
        {
            "code": "_ActConsentType",
            "concept": [
                {
                    "code": "ICOL",
                    "definition": "Definition: Consent to have healthcare information collected in an electronic health record.  This entails that the information may be used in analysis, modified, updated.",
                    "display": "information collection",
                },
                {
                    "code": "IDSCL",
                    "definition": "Definition: Consent to have collected healthcare information disclosed.",
                    "display": "information disclosure",
                },
                {
                    "code": "INFA",
                    "concept": [
                        {
                            "code": "INFAO",
                            "definition": 'Definition: Consent to access or "read" only, which entails that the information is not to be copied, screen printed, saved, emailed, stored, re-disclosed or altered in any way.  This level ensures that data which is masked or to which access is restricted will not be.\r\n\n                        \n                           Example: Opened and then emailed or screen printed for use outside of the consent directive purpose.',
                            "display": "access only",
                        },
                        {
                            "code": "INFASO",
                            "definition": "Definition: Consent to access and save only, which entails that access to the saved copy will remain locked.",
                            "display": "access and save only",
                        },
                    ],
                    "definition": "Definition: Consent to access healthcare information.",
                    "display": "information access",
                },
                {
                    "code": "IRDSCL",
                    "definition": "Definition: Information re-disclosed without the patient's consent.",
                    "display": "information redisclosure",
                },
                {
                    "code": "RESEARCH",
                    "concept": [
                        {
                            "code": "RSDID",
                            "definition": "Definition: Consent to have de-identified healthcare information in an electronic health record that is accessed for research purposes, but without consent to re-identify the information under any circumstance.",
                            "display": "de-identified information access",
                        },
                        {
                            "code": "RSREID",
                            "definition": "Definition: Consent to have de-identified healthcare information in an electronic health record that is accessed for research purposes re-identified under specific circumstances outlined in the consent.\r\n\n                        \n                           Example:: Where there is a need to inform the subject of potential health issues.",
                            "display": "re-identifiable information access",
                        },
                    ],
                    "definition": "Definition: Consent to have healthcare information in an electronic health record accessed for research purposes.",
                    "display": "research information access",
                },
            ],
            "definition": "Definition: The type of consent directive, e.g., to consent or dissent to collect, access, or use in specific ways within an EHRS or for health information exchange; or to disclose  health information  for purposes such as research.",
            "display": "ActConsentType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActConsentType

    Definition: The type of consent directive, e.g., to consent or dissent to collect, access, or use in specific ways within an EHRS or for health information exchange; or to disclose  health information  for purposes such as research.
    """

    underscore_act_container_registration_code = CodeSystemConcept(
        {
            "code": "_ActContainerRegistrationCode",
            "concept": [
                {
                    "code": "ID",
                    "definition": "Used by one system to inform another that it has received a container.",
                    "display": "Identified",
                },
                {
                    "code": "IP",
                    "definition": "Used by one system to inform another that the container is in position for specimen transfer (e.g., container removal from track, pipetting, etc.).",
                    "display": "In Position",
                },
                {
                    "code": "L",
                    "definition": "Used by one system to inform another that the container has been released from that system.",
                    "display": "Left Equipment",
                },
                {
                    "code": "M",
                    "definition": "Used by one system to inform another that the container did not arrive at its next expected location.",
                    "display": "Missing",
                },
                {
                    "code": "O",
                    "definition": "Used by one system to inform another that the specific container is being processed by the equipment. It is useful as a response to a query about Container Status, when the specific step of the process is not relevant.",
                    "display": "In Process",
                },
                {
                    "code": "R",
                    "definition": "Status is used by one system to inform another that the processing has been completed, but the container has not been released from that system.",
                    "display": "Process Completed",
                },
                {
                    "code": "X",
                    "definition": "Used by one system to inform another that the container is no longer available within the scope of the system (e.g., tube broken or discarded).",
                    "display": "Container Unavailable",
                },
            ],
            "definition": "Constrains the ActCode to the domain of Container Registration",
            "display": "ActContainerRegistrationCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActContainerRegistrationCode

    Constrains the ActCode to the domain of Container Registration
    """

    underscore_act_control_variable = CodeSystemConcept(
        {
            "code": "_ActControlVariable",
            "concept": [
                {
                    "code": "AUTO",
                    "definition": "Specifies whether or not automatic repeat testing is to be initiated on specimens.",
                    "display": "auto-repeat permission",
                },
                {
                    "code": "ENDC",
                    "definition": "A baseline value for the measured test that is inherently contained in the diluent.  In the calculation of the actual result for the measured test, this baseline value is normally considered.",
                    "display": "endogenous content",
                },
                {
                    "code": "REFLEX",
                    "definition": "Specifies whether or not further testing may be automatically or manually initiated on specimens.",
                    "display": "reflex permission",
                },
            ],
            "definition": "An observation form that determines parameters or attributes of an Act. Examples are the settings of a ventilator machine as parameters of a ventilator treatment act; the controls on dillution factors of a chemical analyzer as a parameter of a laboratory observation act; the settings of a physiologic measurement assembly (e.g., time skew) or the position of the body while measuring blood pressure.\r\n\n                        Control variables are forms of observations because just as with clinical observations, the Observation.code determines the parameter and the Observation.value assigns the value. While control variables sometimes can be observed (by noting the control settings or an actually measured feedback loop) they are not primary observations, in the sense that a control variable without a primary act is of no use (e.g., it makes no sense to record a blood pressure position without recording a blood pressure, whereas it does make sense to record a systolic blood pressure without a diastolic blood pressure).",
            "display": "ActControlVariable",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActControlVariable

    An observation form that determines parameters or attributes of an Act. Examples are the settings of a ventilator machine as parameters of a ventilator treatment act; the controls on dillution factors of a chemical analyzer as a parameter of a laboratory observation act; the settings of a physiologic measurement assembly (e.g., time skew) or the position of the body while measuring blood pressure.

                        Control variables are forms of observations because just as with clinical observations, the Observation.code determines the parameter and the Observation.value assigns the value. While control variables sometimes can be observed (by noting the control settings or an actually measured feedback loop) they are not primary observations, in the sense that a control variable without a primary act is of no use (e.g., it makes no sense to record a blood pressure position without recording a blood pressure, whereas it does make sense to record a systolic blood pressure without a diastolic blood pressure).
    """

    underscore_act_coverage_confirmation_code = CodeSystemConcept(
        {
            "code": "_ActCoverageConfirmationCode",
            "concept": [
                {
                    "code": "_ActCoverageAuthorizationConfirmationCode",
                    "concept": [
                        {
                            "code": "AUTH",
                            "definition": "Authorization approved and funds have been set aside to pay for specified healthcare service(s) and/or product(s) within defined criteria for the authorization.",
                            "display": "Authorized",
                        },
                        {
                            "code": "NAUTH",
                            "definition": "Authorization for specified healthcare service(s) and/or product(s) denied.",
                            "display": "Not Authorized",
                        },
                    ],
                    "definition": "Indication of authorization for healthcare service(s) and/or product(s).  If authorization is approved, funds are set aside.",
                    "display": "ActCoverageAuthorizationConfirmationCode",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_ActCoverageEligibilityConfirmationCode",
                    "concept": [
                        {
                            "code": "ELG",
                            "definition": "Insurance coverage is in effect for healthcare service(s) and/or product(s).",
                            "display": "Eligible",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                        {
                            "code": "NELG",
                            "definition": "Insurance coverage is not in effect for healthcare service(s) and/or product(s). May optionally include reasons for the ineligibility.",
                            "display": "Not Eligible",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                    ],
                    "definition": "Indication of eligibility coverage for healthcare service(s) and/or product(s).",
                    "display": "ActCoverageEligibilityConfirmationCode",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "status", "valueCode": "retired"},
                    ],
                },
            ],
            "definition": "Response to an insurance coverage eligibility query or authorization request.",
            "display": "ActCoverageConfirmationCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActCoverageConfirmationCode

    Response to an insurance coverage eligibility query or authorization request.
    """

    underscore_act_coverage_limit_code = CodeSystemConcept(
        {
            "code": "_ActCoverageLimitCode",
            "concept": [
                {
                    "code": "_ActCoverageQuantityLimitCode",
                    "concept": [
                        {
                            "code": "COVPRD",
                            "definition": "Codes representing the time period during which coverage is available; or financial participation requirements are in effect.",
                            "display": "coverage period",
                        },
                        {
                            "code": "LFEMX",
                            "definition": "Definition: Maximum amount paid by payer or covered party; or maximum number of services or products covered under the policy or program during a covered party's lifetime.",
                            "display": "life time maximum",
                        },
                        {
                            "code": "NETAMT",
                            "definition": "Maximum net amount that will be covered for the product or service specified.",
                            "display": "Net Amount",
                        },
                        {
                            "code": "PRDMX",
                            "definition": "Definition: Maximum amount paid by payer or covered party; or maximum number of services/products covered under the policy or program by time period specified by the effective time on the act.",
                            "display": "period maximum",
                        },
                        {
                            "code": "UNITPRICE",
                            "definition": "Maximum unit price that will be covered for the authorized product or service.",
                            "display": "Unit Price",
                        },
                        {
                            "code": "UNITQTY",
                            "definition": "Maximum number of items that will be covered of the product or service specified.",
                            "display": "Unit Quantity",
                        },
                    ],
                    "definition": "Maximum amount paid or maximum number of services/products covered; or maximum amount or number covered during a specified time period under the policy or program.",
                    "display": "ActCoverageQuantityLimitCode",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "COVMX",
                    "definition": "Definition: Codes representing the maximum coverate or financial participation requirements.",
                    "display": "coverage maximum",
                    "property": [
                        {"code": "child", "valueCode": "LFEMX"},
                        {"code": "child", "valueCode": "PRDMX"},
                    ],
                },
                {
                    "code": "_ActCoveredPartyLimitCode",
                    "definition": "Codes representing the types of covered parties that may receive covered benefits under a policy or program.",
                    "display": "ActCoveredPartyLimitCode",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "status", "valueCode": "retired"},
                    ],
                },
            ],
            "definition": "Criteria that are applicable to the authorized coverage.",
            "display": "ActCoverageLimitCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActCoverageLimitCode

    Criteria that are applicable to the authorized coverage.
    """

    underscore_act_coverage_type_code = CodeSystemConcept(
        {
            "code": "_ActCoverageTypeCode",
            "concept": [
                {
                    "code": "_ActInsurancePolicyCode",
                    "concept": [
                        {
                            "code": "EHCPOL",
                            "definition": "Private insurance policy that provides coverage in addition to other policies (e.g. in addition to a Public Healthcare insurance policy).",
                            "display": "extended healthcare",
                        },
                        {
                            "code": "HSAPOL",
                            "definition": "Insurance policy that provides for an allotment of funds replenished on a periodic (e.g. annual) basis. The use of the funds under this policy is at the \tdiscretion of the covered party.",
                            "display": "health spending account",
                        },
                        {
                            "code": "AUTOPOL",
                            "concept": [
                                {
                                    "code": "COL",
                                    "definition": "Definition: An automobile insurance policy under which the insurance company will cover the cost of damages to an automobile owned by the named insured that are caused by accident or intentionally by another party.",
                                    "display": "collision coverage policy",
                                },
                                {
                                    "code": "UNINSMOT",
                                    "definition": "Definition: An automobile insurance policy under which the insurance company will indemnify a loss for which another motorist is liable if that motorist is unable to pay because he or she is uninsured.  Coverage under the policy applies to bodily injury damages only.  Injuries to the covered party caused by a hit-and-run driver are also covered.",
                                    "display": "uninsured motorist policy",
                                },
                            ],
                            "definition": "Insurance policy for injuries sustained in an automobile accident.  Will also typically covered non-named parties to the policy, such as pedestrians \tand passengers.",
                            "display": "automobile",
                        },
                        {
                            "code": "PUBLICPOL",
                            "concept": [
                                {
                                    "code": "DENTPRG",
                                    "definition": "Definition: A public or government health program that administers and funds coverage for dental care to assist program eligible who meet financial and health status criteria.",
                                    "display": "dental program",
                                },
                                {
                                    "code": "DISEASEPRG",
                                    "concept": [
                                        {
                                            "code": "CANPRG",
                                            "definition": "Definition: A program that provides low-income, uninsured, and underserved women access to timely, high-quality screening and diagnostic services, to detect breast and cervical cancer at the earliest stages.\r\n\n                        \n                           Example: To improve women's access to screening for breast and cervical cancers, Congress passed the Breast and Cervical Cancer Mortality Prevention Act of 1990, which guided CDC in creating the National Breast and Cervical Cancer Early Detection Program (NBCCEDP), which  provides access to critical breast and cervical cancer screening services for underserved women in the United States.  An estimated 7 to 10% of U.S. women of screening age are eligible to receive NBCCEDP services. Federal guidelines establish an eligibility baseline to direct services to uninsured and underinsured women at or below 250% of federal poverty level; ages 18 to 64 for cervical screening; ages 40 to 64 for breast screening.",
                                            "display": "women's cancer detection program",
                                        },
                                        {
                                            "code": "ENDRENAL",
                                            "definition": "Definition: A public or government program that administers publicly funded coverage of kidney dialysis and kidney transplant services.\r\n\n                        Example: In the U.S., the Medicare End-stage Renal Disease program (ESRD), the National Kidney Foundation (NKF) American Kidney Fund (AKF) The Organ Transplant Fund.",
                                            "display": "end renal program",
                                        },
                                        {
                                            "code": "HIVAIDS",
                                            "definition": "Definition: Government administered and funded HIV-AIDS program for beneficiaries meeting financial and health status criteria.  Administration, funding levels, eligibility criteria, covered benefits, provider types, and financial participation are typically set by a regulatory process.  Payer responsibilities for administering the program may be delegated to contractors.\r\n\n                        \n                           Example: In the U.S., the Ryan White program, which is administered by the Health Resources and Services Administration.",
                                            "display": "HIV-AIDS program",
                                        },
                                    ],
                                    "definition": "Definition: A public or government health program that administers and funds coverage for health and social services to assist program eligible who meet financial and health status criteria related to a particular disease.\r\n\n                        \n                           Example: Reproductive health, sexually transmitted disease, and end renal disease programs.",
                                    "display": "public health program",
                                },
                                {
                                    "code": "MANDPOL",
                                    "definition": "mandatory health program",
                                    "display": "mandatory health program",
                                },
                                {
                                    "code": "MENTPRG",
                                    "definition": "Definition: Government administered and funded mental health program for beneficiaries meeting financial and mental health status criteria.  Administration, funding levels, eligibility criteria, covered benefits, provider types, and financial participation are typically set by a regulatory process.  Payer responsibilities for administering the program may be delegated to contractors.\r\n\n                        \n                           Example: In the U.S., states receive funding for substance use programs from the Substance Abuse Mental Health Administration (SAMHSA).",
                                    "display": "mental health program",
                                },
                                {
                                    "code": "SAFNET",
                                    "definition": "Definition: Government administered and funded program to support provision of care to underserved populations through safety net clinics.\r\n\n                        \n                           Example: In the U.S., safety net providers such as federally qualified health centers (FQHC) receive funding under PHSA Section 330 grants administered by the Health Resources and Services Administration.",
                                    "display": "safety net clinic program",
                                },
                                {
                                    "code": "SUBPRG",
                                    "definition": "Definition: Government administered and funded substance use program for beneficiaries meeting financial, substance use behavior, and health status criteria.  Beneficiaries may be required to enroll as a result of legal proceedings.  Administration, funding levels, eligibility criteria, covered benefits, provider types, and financial participation are typically set by a regulatory process.  Payer responsibilities for administering the program may be delegated to contractors.\r\n\n                        \n                           Example: In the U.S., states receive funding for substance use programs from the Substance Abuse Mental Health Administration (SAMHSA).",
                                    "display": "substance use program",
                                },
                                {
                                    "code": "SUBSIDIZ",
                                    "concept": [
                                        {
                                            "code": "SUBSIDMC",
                                            "definition": "Definition: A government health program that provides coverage through managed care contracts for health services to persons meeting eligibility criteria such as income, location of residence, access to other coverages, health condition, and age, the cost of which is to some extent subsidized by public funds. \r\n\n                        \n                           Discussion: The structure and business processes for underwriting and administering a subsidized managed care program is further specified by the Underwriter and Payer Role.class and Role.code.",
                                            "display": "subsidized managed care program",
                                        },
                                        {
                                            "code": "SUBSUPP",
                                            "definition": "Definition: A government health program that provides coverage for health services to persons meeting eligibility criteria for a supplemental health policy or program such as income, location of residence, access to other coverages, health condition, and age, the cost of which is to some extent subsidized by public funds.\r\n\n                        \n                           Example:  Supplemental health coverage program may cover the cost of a health program or policy financial participations, such as the copays and the premiums, and may provide coverage for services in addition to those covered under the supplemented health program or policy.  In the U.S., Medicaid programs may pay the premium for a covered party who is also covered under the  Medicare program or a private health policy.\r\n\n                        \n                           Discussion: The structure and business processes for underwriting and administering a subsidized supplemental retiree health program is further specified by the Underwriter and Payer Role.class and Role.code.",
                                            "display": "subsidized supplemental health program",
                                        },
                                    ],
                                    "definition": "Definition: A government health program that provides coverage for health services to persons meeting eligibility criteria such as income, location of residence, access to other coverages, health condition, and age, the cost of which is to some extent subsidized by public funds.",
                                    "display": "subsidized health program",
                                },
                            ],
                            "definition": "Insurance policy funded by a public health system such as a provincial or national health plan.  Examples include BC MSP (British Columbia \tMedical Services Plan) OHIP (Ontario Health Insurance Plan), NHS (National Health Service).",
                            "display": "public healthcare",
                        },
                        {
                            "code": "WCBPOL",
                            "definition": "Insurance policy for injuries sustained in the work place or in the course of employment.",
                            "display": "worker's compensation",
                        },
                    ],
                    "definition": "Set of codes indicating the type of insurance policy or other source of funds to cover healthcare costs.",
                    "display": "ActInsurancePolicyCode",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_ActInsuranceTypeCode",
                    "concept": [
                        {
                            "code": "_ActHealthInsuranceTypeCode",
                            "concept": [
                                {
                                    "code": "DENTAL",
                                    "definition": "Definition: A health insurance policy that that covers benefits for dental services.",
                                    "display": "dental care policy",
                                },
                                {
                                    "code": "DISEASE",
                                    "definition": "Definition: A health insurance policy that covers benefits for healthcare services provided for named conditions under the policy, e.g., cancer, diabetes, or HIV-AIDS.",
                                    "display": "disease specific policy",
                                },
                                {
                                    "code": "DRUGPOL",
                                    "definition": "Definition: A health insurance policy that covers benefits for prescription drugs, pharmaceuticals, and supplies.",
                                    "display": "drug policy",
                                },
                                {
                                    "code": "HIP",
                                    "definition": "Definition: A health insurance policy that covers healthcare benefits by protecting covered parties from medical expenses arising from health conditions, sickness, or accidental injury as well as preventive care. Health insurance policies explicitly exclude coverage for losses insured under a disability policy, workers' compensation program, liability insurance (including automobile insurance); or for medical expenses, coverage for on-site medical clinics or for limited dental or vision benefits when these are provided under a separate policy.\r\n\n                        \n                           Discussion: Health insurance policies are offered by health insurance plans that typically reimburse providers for covered services on a fee-for-service basis, that is, a fee that is the allowable amount that a provider may charge.  This is in contrast to managed care plans, which typically prepay providers a per-member/per-month amount or capitation as reimbursement for all covered services rendered.  Health insurance plans include indemnity and healthcare services plans.",
                                    "display": "health insurance plan policy",
                                },
                                {
                                    "code": "LTC",
                                    "definition": "Definition: An insurance policy that covers benefits for long-term care services people need when they no longer can care for themselves. This may be due to an accident, disability, prolonged illness or the simple process of aging. Long-term care services assist with activities of daily living including:\r\n\n                        \n                           \n                              Help at home with day-to-day activities, such as cooking, cleaning, bathing and dressing\r\n\n                           \n                           \n                              Care in the community, such as in an adult day care facility\r\n\n                           \n                           \n                              Supervised care provided in an assisted living facility\r\n\n                           \n                           \n                              Skilled care provided in a nursing home",
                                    "display": "long term care policy",
                                },
                                {
                                    "code": "MCPOL",
                                    "concept": [
                                        {
                                            "code": "POS",
                                            "definition": "Definition: A policy for a health plan that has features of both an HMO and a FFS plan.  Like an HMO, a POS plan encourages the use its HMO network to maintain discounted fees with participating providers, but recognizes that sometimes covered parties want to choose their own provider.  The POS plan allows a covered party to use providers who are not part of the HMO network (non-participating providers).  However, there is a greater cost associated with choosing these non-network providers. A covered party will usually pay deductibles and coinsurances that are substantially higher than the payments when he or she uses a plan provider. Use of non-participating providers often requires the covered party to pay the provider directly and then to file a claim for reimbursement, like in an FFS plan.",
                                            "display": "point of service policy",
                                        },
                                        {
                                            "code": "HMO",
                                            "definition": "Definition: A policy for a health plan that provides coverage for health care only through contracted or employed physicians and hospitals located in particular geographic or service areas.  HMOs emphasize prevention and early detection of illness. Eligibility to enroll in an HMO is determined by where a covered party lives or works.",
                                            "display": "health maintenance organization policy",
                                        },
                                        {
                                            "code": "PPO",
                                            "definition": 'Definition: A network-based, managed care plan that allows a covered party to choose any health care provider. However, if care is received from a "preferred" (participating in-network) provider, there are generally higher benefit coverage and lower deductibles.',
                                            "display": "preferred provider organization policy",
                                        },
                                    ],
                                    "definition": "Definition: Government mandated program providing coverage, disability income, and vocational rehabilitation for injuries sustained in the work place or in the course of employment.  Employers may either self-fund the program, purchase commercial coverage, or pay a premium to a government entity that administers the program.  Employees may be required to pay premiums toward the cost of coverage as well.\r\n\n                        Managed care policies specifically exclude coverage for losses insured under a disability policy, workers' compensation program, liability insurance (including automobile insurance); or for medical expenses, coverage for on-site medical clinics or for limited dental or vision benefits when these are provided under a separate policy.\r\n\n                        \n                           Discussion: Managed care policies are offered by managed care plans that contract with selected providers or health care organizations to provide comprehensive health care at a discount to covered parties and coordinate the financing and delivery of health care. Managed care uses medical protocols and procedures agreed on by the medical profession to be cost effective, also known as medical practice guidelines. Providers are typically reimbursed for covered services by a capitated amount on a per member per month basis that may reflect difference in the health status and level of services anticipated to be needed by the member.",
                                    "display": "managed care policy",
                                },
                                {
                                    "code": "MENTPOL",
                                    "definition": "Definition: A health insurance policy that covers benefits for mental health services and prescriptions.",
                                    "display": "mental health policy",
                                },
                                {
                                    "code": "SUBPOL",
                                    "definition": "Definition: A health insurance policy that covers benefits for substance use services.",
                                    "display": "substance use policy",
                                },
                                {
                                    "code": "VISPOL",
                                    "definition": "Definition: Set of codes for a policy that provides coverage for health care expenses arising from vision services.\r\n\n                        A health insurance policy that covers benefits for vision care services, prescriptions, and products.",
                                    "display": "vision care policy",
                                },
                            ],
                            "definition": "Definition: Set of codes indicating the type of health insurance policy that covers health services provided to covered parties.  A health insurance policy is a written contract for insurance between the insurance company and the policyholder, and contains pertinent facts about the policy owner (the policy holder), the health insurance coverage, the insured subscribers and dependents, and the insurer.  Health insurance is typically administered in accordance with a plan, which specifies (1) the type of health services and health conditions that will be covered under what circumstances (e.g., exclusion of a pre-existing condition, service must be deemed medically necessary; service must not be experimental; service must provided in accordance with a protocol; drug must be on a formulary; service must be prior authorized; or be a referral from a primary care provider); (2) the type and affiliation of providers (e.g., only allopathic physicians, only in network, only providers employed by an HMO); (3) financial participations required of covered parties (e.g., co-pays, coinsurance, deductibles, out-of-pocket); and (4) the manner in which services will be paid (e.g., under indemnity or fee-for-service health plans, the covered party typically pays out-of-pocket and then file a claim for reimbursement, while health plans that have contractual relationships with providers, i.e., network providers, typically do not allow the providers to bill the covered party for the cost of the service until after filing a claim with the payer and receiving reimbursement).",
                            "display": "ActHealthInsuranceTypeCode",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True},
                                {"code": "child", "valueCode": "EHCPOL"},
                                {"code": "child", "valueCode": "HSAPOL"},
                                {"code": "child", "valueCode": "POS"},
                            ],
                        },
                        {
                            "code": "DIS",
                            "definition": "Definition: An insurance policy that provides a regular payment to compensate for income lost due to the covered party's inability to work because of illness or injury.",
                            "display": "disability insurance policy",
                        },
                        {
                            "code": "EWB",
                            "definition": "Definition: An insurance policy under a benefit plan run by an employer or employee organization for the purpose of providing benefits other than pension-related to employees and their families. Typically provides health-related benefits, benefits for disability, disease or unemployment, or day care and scholarship benefits, among others.  An employer sponsored health policy includes coverage of health care expenses arising from sickness or accidental injury, coverage for on-site medical clinics or for dental or vision benefits, which are typically provided under a separate policy.  Coverage excludes health care expenses covered by accident or disability, workers' compensation, liability or automobile insurance.",
                            "display": "employee welfare benefit plan policy",
                        },
                        {
                            "code": "FLEXP",
                            "definition": "Definition:  An insurance policy that covers qualified benefits under a Flexible Benefit plan such as group medical insurance, long and short term disability income insurance, group term life insurance for employees only up to $50,000 face amount, specified disease coverage such as a cancer policy, dental and/or vision insurance, hospital indemnity insurance, accidental death and dismemberment insurance, a medical expense reimbursement plan and a dependent care reimbursement plan.\r\n\n                        \n                            Discussion: See UnderwriterRoleTypeCode flexible benefit plan which is defined as a benefit plan that allows employees to choose from several life, health, disability, dental, and other insurance plans according to their individual needs. Also known as cafeteria plans.  Authorized under Section 125 of the Revenue Act of 1978.",
                            "display": "flexible benefit plan policy",
                        },
                        {
                            "code": "LIFE",
                            "concept": [
                                {
                                    "code": "ANNU",
                                    "definition": "Definition: A policy that, after an initial premium or premiums, pays out a sum at pre-determined intervals.\r\n\n                        For example, a policy holder may pay $10,000, and in return receive $150 each month until he dies; or $1,000 for each of 14 years or death benefits if he dies before the full term of the annuity has elapsed.",
                                    "display": "annuity policy",
                                },
                                {
                                    "code": "TLIFE",
                                    "definition": "Definition: Life insurance under which the benefit is payable only if the insured dies during a specified period. If an insured dies during that period, the beneficiary receives the death payments. If the insured survives, the policy ends and the beneficiary receives nothing.",
                                    "display": "term life insurance policy",
                                },
                                {
                                    "code": "ULIFE",
                                    "definition": "Definition: Life insurance under which the benefit is payable upon the insuredaTMs death or diagnosis of a terminal illness.  If an insured dies during that period, the beneficiary receives the death payments. If the insured survives, the policy ends and the beneficiary receives nothing",
                                    "display": "universal life insurance policy",
                                },
                            ],
                            "definition": "Definition: A policy under which the insurer agrees to pay a sum of money upon the occurrence of the covered partys death. In return, the policyholder agrees to pay a stipulated amount called a premium at regular intervals.  Life insurance indemnifies the beneficiary for the loss of the insurable interest that a beneficiary has in the life of a covered party.  For persons related by blood, a substantial interest established through love and affection, and for all other persons, a lawful and substantial economic interest in having the life of the insured continue. An insurable interest is required when purchasing life insurance on another person. Specific exclusions are often written into the contract to limit the liability of the insurer; for example claims resulting from suicide or relating to war, riot and civil commotion.\r\n\n                        \n                           Discussion:A life insurance policy may be used by the covered party as a source of health care coverage in the case of  a viatical settlement, which is the sale of a life insurance policy by the policy owner, before the policy matures. Such a sale, at a price discounted from the face amount of the policy but usually in excess of the premiums paid or current cash surrender value, provides the seller an immediate cash settlement. Generally, viatical settlements involve insured individuals with a life expectancy of less than two years. In countries without state-subsidized healthcare and high healthcare costs (e.g. United States), this is a practical way to pay extremely high health insurance premiums that severely ill people face. Some people are also familiar with life settlements, which are similar transactions but involve insureds with longer life expectancies (two to fifteen years).",
                            "display": "life insurance policy",
                        },
                        {
                            "code": "PNC",
                            "definition": 'Definition: A type of insurance that covers damage to or loss of the policyholderaTMs property by providing payments for damages to property damage or the injury or death of living subjects.  The terms "casualty" and "liability" insurance are often used interchangeably. Both cover the policyholder\'s legal liability for damages caused to other persons and/or their property.',
                            "display": "property and casualty insurance policy",
                        },
                        {
                            "code": "REI",
                            "definition": "Definition: An agreement between two or more insurance companies by which the risk of loss is proportioned. Thus the risk of loss is spread and a disproportionately large loss under a single policy does not fall on one insurance company. Acceptance by an insurer, called a reinsurer, of all or part of the risk of loss of another insurance company.\r\n\n                        \n                           Discussion: Reinsurance is a means by which an insurance company can protect itself against the risk of losses with other insurance companies. Individuals and corporations obtain insurance policies to provide protection for various risks (hurricanes, earthquakes, lawsuits, collisions, sickness and death, etc.). Reinsurers, in turn, provide insurance to insurance companies.\r\n\n                        For example, an HMO may purchase a reinsurance policy to protect itself from losing too much money from one insured's particularly expensive health care costs. An insurance company issuing an automobile liability policy, with a limit of $100,000 per accident may reinsure its liability in excess of $10,000. A fire insurance company which issues a large policy generally reinsures a portion of the risk with one or several other companies. Also called risk control insurance or stop-loss insurance.",
                            "display": "reinsurance policy",
                        },
                        {
                            "code": "SURPL",
                            "definition": "Definition: \n                        \r\n\n                        \n                           \n                              A risk or part of a risk for which there is no normal insurance market available.\r\n\n                           \n                           \n                              Insurance written by unauthorized insurance companies. Surplus lines insurance is insurance placed with unauthorized insurance companies through licensed surplus lines agents or brokers.",
                            "display": "surplus line insurance policy",
                        },
                        {
                            "code": "UMBRL",
                            "definition": "Definition: A form of insurance protection that provides additional liability coverage after the limits of your underlying policy are reached. An umbrella liability policy also protects you (the insured) in many situations not covered by the usual liability policies.",
                            "display": "umbrella liability insurance policy",
                        },
                    ],
                    "definition": "Definition: Set of codes indicating the type of insurance policy.  Insurance, in law and economics, is a form of risk management primarily used to hedge against the risk of potential financial loss. Insurance is defined as the equitable transfer of the risk of a potential loss, from one entity to another, in exchange for a premium and duty of care. A policy holder is an individual or an organization enters into a contract with an underwriter which stipulates that, in exchange for payment of a sum of money (a premium), one or more covered parties (insureds) is guaranteed compensation for losses resulting from certain perils under specified conditions.  The underwriter analyzes the risk of loss, makes a decision as to whether the risk is insurable, and prices the premium accordingly.  A policy provides benefits that indemnify or cover the cost of a loss incurred by a covered party, and may include coverage for services required to remediate a loss.  An insurance policy contains pertinent facts about the policy holder, the insurance coverage, the covered parties, and the insurer.  A policy may include exemptions and provisions specifying the extent to which the indemnification clause cannot be enforced for intentional tortious conduct of a covered party, e.g., whether the covered parties are jointly or severably insured.\r\n\n                        \n                           Discussion: In contrast to programs, an insurance policy has one or more policy holders, who own the policy.  The policy holder may be the covered party, a relative of the covered party, a partnership, or a corporation, e.g., an employer.  A subscriber of a self-insured health insurance policy is a policy holder.  A subscriber of an employer sponsored health insurance policy is holds a certificate of coverage, but is not a policy holder; the policy holder is the employer.  See CoveredRoleType.",
                    "display": "ActInsuranceTypeCode",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "AUTOPOL"},
                    ],
                },
                {
                    "code": "_ActProgramTypeCode",
                    "concept": [
                        {
                            "code": "CHAR",
                            "definition": "Definition: A program that covers the cost of services provided directly to a beneficiary who typically has no other source of coverage without charge.",
                            "display": "charity program",
                        },
                        {
                            "code": "CRIME",
                            "definition": "Definition: A program that covers the cost of services provided to crime victims for injuries or losses related to the occurrence of a crime.",
                            "display": "crime victim program",
                        },
                        {
                            "code": "EAP",
                            "definition": "Definition: An employee assistance program is run by an employer or employee organization for the purpose of providing benefits and covering all or part of the cost for employees to receive counseling, referrals, and advice in dealing with stressful issues in their lives. These may include substance abuse, bereavement, marital problems, weight issues, or general wellness issues.  The services are usually provided by a third-party, rather than the company itself, and the company receives only summary statistical data from the service provider. Employee's names and services received are kept confidential.",
                            "display": "employee assistance program",
                        },
                        {
                            "code": "GOVEMP",
                            "definition": "Definition: A set of codes used to indicate a government program that is an organized structure for administering and funding coverage of a benefit package for covered parties meeting eligibility criteria, typically related to employment, health and financial status. Government programs are established or permitted by legislation with provisions for ongoing government oversight.  Regulation mandates the structure of the program, the manner in which it is funded and administered, covered benefits, provider types, eligibility criteria and financial participation. A government agency is charged with implementing the program in accordance to the regulation\r\n\n                        \n                           Example: Federal employee health benefit program in the U.S.",
                            "display": "government employee health program",
                        },
                        {
                            "code": "HIRISK",
                            "definition": 'Definition: A government program that provides health coverage to individuals who are considered medically uninsurable or high risk, and who have been denied health insurance due to a serious health condition. In certain cases, it also applies to those who have been quoted very high premiums a" again, due to a serious health condition.  The pool charges premiums for coverage.  Because the pool covers high-risk people, it incurs a higher level of claims than premiums can cover. The insurance industry pays into the pool to make up the difference and help it remain viable.',
                            "display": "high risk pool program",
                        },
                        {
                            "code": "IND",
                            "definition": "Definition: Services provided directly and through contracted and operated indigenous peoples health programs.\r\n\n                        \n                           Example: Indian Health Service in the U.S.",
                            "display": "indigenous peoples health program",
                        },
                        {
                            "code": "MILITARY",
                            "definition": "Definition: A government program that provides coverage for health services to military personnel, retirees, and dependents.  A covered party who is a subscriber can choose from among Fee-for-Service (FFS) plans, and their Preferred Provider Organizations (PPO), or Plans offering a Point of Service (POS) Product, or Health Maintenance Organizations.\r\n\n                        \n                           Example: In the U.S., TRICARE, CHAMPUS.",
                            "display": "military health program",
                        },
                        {
                            "code": "RETIRE",
                            "definition": "Definition: A government mandated program with specific eligibility requirements based on premium contributions made during employment, length of employment, age, and employment status, e.g., being retired, disabled, or a dependent of a covered party under this program.   Benefits typically include ambulatory, inpatient, and long-term care, such as hospice care, home health care and respite care.",
                            "display": "retiree health program",
                        },
                        {
                            "code": "SOCIAL",
                            "definition": "Definition: A social service program funded by a public or governmental entity.\r\n\n                        \n                           Example: Programs providing habilitation, food, lodging, medicine, transportation, equipment, devices, products, education, training, counseling, alteration of living or work space, and other resources to persons meeting eligibility criteria.",
                            "display": "social service program",
                        },
                        {
                            "code": "VET",
                            "definition": "Definition: Services provided directly and through contracted and operated veteran health programs.",
                            "display": "veteran health program",
                        },
                    ],
                    "definition": "Definition: A set of codes used to indicate coverage under a program.  A program is an organized structure for administering and funding coverage of a benefit package for covered parties meeting eligibility criteria, typically related to employment, health, financial, and demographic status. Programs are typically established or permitted by legislation with provisions for ongoing government oversight.  Regulations may mandate the structure of the program, the manner in which it is funded and administered, covered benefits, provider types, eligibility criteria and financial participation. A government agency may be charged with implementing the program in accordance to the regulation.  Risk of loss under a program in most cases would not meet what an underwriter would consider an insurable risk, i.e., the risk is not random in nature, not financially measurable, and likely requires subsidization with government funds.\r\n\n                        \n                           Discussion: Programs do not have policy holders or subscribers.  Program eligibles are enrolled based on health status, statutory eligibility, financial status, or age.  Program eligibles who are covered parties under the program may be referred to as members, beneficiaries, eligibles, or recipients.  Programs risk are underwritten by not for profit organizations such as governmental entities, and the beneficiaries typically do not pay for any or some portion of the cost of coverage.  See CoveredPartyRoleType.",
                    "display": "ActProgramTypeCode",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "PUBLICPOL"},
                        {"code": "child", "valueCode": "WCBPOL"},
                    ],
                },
            ],
            "definition": "Definition: Set of codes indicating the type of insurance policy or program that pays for the cost of benefits provided to covered parties.",
            "display": "ActCoverageTypeCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActCoverageTypeCode

    Definition: Set of codes indicating the type of insurance policy or program that pays for the cost of benefits provided to covered parties.
    """

    underscore_act_detected_issue_management_code = CodeSystemConcept(
        {
            "code": "_ActDetectedIssueManagementCode",
            "concept": [
                {
                    "code": "_ActAdministrativeDetectedIssueManagementCode",
                    "concept": [
                        {
                            "code": "_AuthorizationIssueManagementCode",
                            "concept": [
                                {
                                    "code": "EMAUTH",
                                    "concept": [
                                        {
                                            "code": "21",
                                            "definition": "Description: Indicates that the permissions have been externally verified and the request should be processed.",
                                            "display": "authorization confirmed",
                                        }
                                    ],
                                    "definition": "Used to temporarily override normal authorization rules to gain access to data in a case of emergency. Use of this override code will typically be monitored, and a procedure to verify its proper use may be triggered when used.",
                                    "display": "emergency authorization override",
                                }
                            ],
                            "definition": "Authorization Issue Management Code",
                            "display": "Authorization Issue Management Code",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        }
                    ],
                    "definition": "Codes dealing with the management of Detected Issue observations for the administrative and patient administrative acts domains.",
                    "display": "ActAdministrativeDetectedIssueManagementCode",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "1",
                    "concept": [
                        {
                            "code": "19",
                            "definition": "Consulted other supplier/pharmacy, therapy confirmed",
                            "display": "Consulted Supplier",
                        },
                        {
                            "code": "2",
                            "definition": "Assessed patient, therapy is appropriate",
                            "display": "Assessed Patient",
                        },
                        {
                            "code": "22",
                            "definition": "Description: The patient has the appropriate indication or diagnosis for the action to be taken.",
                            "display": "appropriate indication or diagnosis",
                        },
                        {
                            "code": "23",
                            "definition": "Description: It has been confirmed that the appropriate pre-requisite therapy has been tried.",
                            "display": "prior therapy documented",
                        },
                        {
                            "code": "3",
                            "definition": "Patient gave adequate explanation",
                            "display": "Patient Explanation",
                        },
                        {
                            "code": "4",
                            "definition": "Consulted other supply source, therapy still appropriate",
                            "display": "Consulted Other Source",
                        },
                        {
                            "code": "5",
                            "concept": [
                                {
                                    "code": "6",
                                    "definition": "Consulted prescriber and recommended change, prescriber declined",
                                    "display": "Prescriber Declined Change",
                                }
                            ],
                            "definition": "Consulted prescriber, therapy confirmed",
                            "display": "Consulted Prescriber",
                        },
                        {
                            "code": "7",
                            "definition": "Concurrent therapy triggering alert is no longer on-going or planned",
                            "display": "Interacting Therapy No Longer Active/Planned",
                        },
                    ],
                    "definition": "Confirmed drug therapy appropriate",
                    "display": "Therapy Appropriate",
                },
                {
                    "code": "14",
                    "concept": [
                        {
                            "code": "15",
                            "definition": "Patient's existing supply was lost/wasted",
                            "display": "Replacement",
                        },
                        {
                            "code": "16",
                            "definition": "Supply date is due to patient vacation",
                            "display": "Vacation Supply",
                        },
                        {
                            "code": "17",
                            "definition": "Supply date is intended to carry patient over weekend",
                            "display": "Weekend Supply",
                        },
                        {
                            "code": "18",
                            "definition": "Supply is intended for use during a leave of absence from an institution.",
                            "display": "Leave of Absence",
                        },
                        {
                            "code": "20",
                            "definition": "Description: Supply is different than expected as an additional quantity has been supplied in a separate dispense.",
                            "display": "additional quantity on separate dispense",
                        },
                    ],
                    "definition": "Confirmed supply action appropriate",
                    "display": "Supply Appropriate",
                },
                {
                    "code": "8",
                    "concept": [
                        {
                            "code": "10",
                            "definition": "Provided education or training to the patient on appropriate therapy use",
                            "display": "Provided Patient Education",
                        },
                        {
                            "code": "11",
                            "definition": "Instituted an additional therapy to mitigate potential negative effects",
                            "display": "Added Concurrent Therapy",
                        },
                        {
                            "code": "12",
                            "definition": "Suspended existing therapy that triggered interaction for the duration of this therapy",
                            "display": "Temporarily Suspended Concurrent Therapy",
                        },
                        {
                            "code": "13",
                            "definition": "Aborted existing therapy that triggered interaction.",
                            "display": "Stopped Concurrent Therapy",
                        },
                        {
                            "code": "9",
                            "definition": "Arranged to monitor patient for adverse effects",
                            "display": "Instituted Ongoing Monitoring Program",
                        },
                    ],
                    "definition": "Order is performed as issued, but other action taken to mitigate potential adverse effects",
                    "display": "Other Action Taken",
                },
            ],
            "definition": "Codes dealing with the management of Detected Issue observations",
            "display": "ActDetectedIssueManagementCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActDetectedIssueManagementCode

    Codes dealing with the management of Detected Issue observations
    """

    underscore_act_exposure_code = CodeSystemConcept(
        {
            "code": "_ActExposureCode",
            "concept": [
                {
                    "code": "CHLDCARE",
                    "definition": "Description: Exposure participants' interaction occurred in a child care setting",
                    "display": "Day care - Child care Interaction",
                },
                {
                    "code": "CONVEYNC",
                    "definition": "Description: An interaction where the exposure participants traveled in/on the same vehicle (not necessarily concurrently, e.g. both are passengers of the same plane, but on different flights of that plane).",
                    "display": "Common Conveyance Interaction",
                },
                {
                    "code": "HLTHCARE",
                    "definition": "Description: Exposure participants' interaction occurred during the course of health care delivery or in a health care delivery setting, but did not involve the direct provision of care (e.g. a janitor cleaning a patient's hospital room).",
                    "display": "Health Care Interaction - Not Patient Care",
                },
                {
                    "code": "HOMECARE",
                    "definition": "Description: Exposure interaction occurred in context of one providing care for the other, i.e. a babysitter providing care for a child, a home-care aide providing assistance to a paraplegic.",
                    "display": "Care Giver Interaction",
                },
                {
                    "code": "HOSPPTNT",
                    "definition": "Description: Exposure participants' interaction occurred when both were patients being treated in the same (acute) health care delivery facility.",
                    "display": "Hospital Patient Interaction",
                },
                {
                    "code": "HOSPVSTR",
                    "definition": "Description: Exposure participants' interaction occurred when one visited the other who was a patient being treated in a health care delivery facility.",
                    "display": "Hospital Visitor Interaction",
                },
                {
                    "code": "HOUSEHLD",
                    "definition": "Description: Exposure interaction occurred in context of domestic interaction, i.e. both participants reside in the same household.",
                    "display": "Household Interaction",
                },
                {
                    "code": "INMATE",
                    "definition": "Description: Exposure participants' interaction occurred in the course of one or both participants being incarcerated at a correctional facility",
                    "display": "Inmate Interaction",
                },
                {
                    "code": "INTIMATE",
                    "definition": "Description: Exposure interaction was intimate, i.e. participants are intimate companions (e.g. spouses, domestic partners).",
                    "display": "Intimate Interaction",
                },
                {
                    "code": "LTRMCARE",
                    "definition": "Description: Exposure participants' interaction occurred in the course of one or both participants being resident at a long term care facility (second participant may be a visitor, worker, resident or a physical place or object within the facility).",
                    "display": "Long Term Care Facility Interaction",
                },
                {
                    "code": "PLACE",
                    "definition": "Description: An interaction where the exposure participants were both present in the same location/place/space.",
                    "display": "Common Space Interaction",
                },
                {
                    "code": "PTNTCARE",
                    "definition": "Description: Exposure participants' interaction occurred during the course of  health care delivery by a provider (e.g. a physician treating a patient in her office).",
                    "display": "Health Care Interaction - Patient Care",
                },
                {
                    "code": "SCHOOL2",
                    "definition": "Description: Exposure participants' interaction occurred in an academic setting (e.g., participants are fellow students, or student and teacher).",
                    "display": "School Interaction",
                },
                {
                    "code": "SOCIAL2",
                    "definition": "Description: An interaction where the exposure participants are social associates or members of the same extended family",
                    "display": "Social/Extended Family Interaction",
                },
                {
                    "code": "SUBSTNCE",
                    "definition": "Description: An interaction where the exposure participants shared or co-used a common substance (e.g. drugs, needles, or common food item).",
                    "display": "Common Substance Interaction",
                },
                {
                    "code": "TRAVINT",
                    "definition": "Description: An interaction where the exposure participants traveled together in/on the same vehicle/trip (e.g. concurrent co-passengers).",
                    "display": "Common Travel Interaction",
                },
                {
                    "code": "WORK2",
                    "definition": "Description: Exposure interaction occurred in a work setting, i.e. participants are co-workers.",
                    "display": "Work Interaction",
                },
            ],
            "definition": 'Concepts that identify the type or nature of exposure interaction.  Examples include "household", "care giver", "intimate partner", "common space", "common substance", etc. to further describe the nature of interaction.',
            "display": "ActExposureCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActExposureCode

    Concepts that identify the type or nature of exposure interaction.  Examples include "household", "care giver", "intimate partner", "common space", "common substance", etc. to further describe the nature of interaction.
    """

    underscore_act_financial_transaction_code = CodeSystemConcept(
        {
            "code": "_ActFinancialTransactionCode",
            "concept": [
                {
                    "code": "CHRG",
                    "definition": "A type of transaction that represents a charge for a service or product.  Expressed in monetary terms.",
                    "display": "Standard Charge",
                },
                {
                    "code": "REV",
                    "definition": "A type of transaction that represents a reversal of a previous charge for a service or product. Expressed in monetary terms.  It has the opposite effect of a standard charge.",
                    "display": "Standard Charge Reversal",
                },
            ],
            "definition": "ActFinancialTransactionCode",
            "display": "ActFinancialTransactionCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActFinancialTransactionCode

    ActFinancialTransactionCode
    """

    underscore_act_incident_code = CodeSystemConcept(
        {
            "code": "_ActIncidentCode",
            "concept": [
                {
                    "code": "MVA",
                    "definition": "Incident or accident as the result of a motor vehicle accident",
                    "display": "Motor vehicle accident",
                },
                {
                    "code": "SCHOOL",
                    "definition": "Incident or accident is the result of a school place accident.",
                    "display": "School Accident",
                },
                {
                    "code": "SPT",
                    "definition": "Incident or accident is the result of a sporting accident.",
                    "display": "Sporting Accident",
                },
                {
                    "code": "WPA",
                    "definition": "Incident or accident is the result of a work place accident",
                    "display": "Workplace accident",
                },
            ],
            "definition": "Set of codes indicating the type of incident or accident.",
            "display": "ActIncidentCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActIncidentCode

    Set of codes indicating the type of incident or accident.
    """

    underscore_act_information_access_code = CodeSystemConcept(
        {
            "code": "_ActInformationAccessCode",
            "concept": [
                {
                    "code": "ACADR",
                    "definition": "Description: Provide consent to collect, use, disclose, or access adverse drug reaction information for a patient.",
                    "display": "adverse drug reaction access",
                },
                {
                    "code": "ACALL",
                    "definition": "Description: Provide consent to collect, use, disclose, or access all information for a patient.",
                    "display": "all access",
                },
                {
                    "code": "ACALLG",
                    "definition": "Description: Provide consent to collect, use, disclose, or access allergy information for a patient.",
                    "display": "allergy access",
                },
                {
                    "code": "ACCONS",
                    "definition": "Description: Provide consent to collect, use, disclose, or access informational consent information for a patient.",
                    "display": "informational consent access",
                },
                {
                    "code": "ACDEMO",
                    "definition": "Description: Provide consent to collect, use, disclose, or access demographics information for a patient.",
                    "display": "demographics access",
                },
                {
                    "code": "ACDI",
                    "definition": "Description: Provide consent to collect, use, disclose, or access diagnostic imaging information for a patient.",
                    "display": "diagnostic imaging access",
                },
                {
                    "code": "ACIMMUN",
                    "definition": "Description: Provide consent to collect, use, disclose, or access immunization information for a patient.",
                    "display": "immunization access",
                },
                {
                    "code": "ACLAB",
                    "definition": "Description: Provide consent to collect, use, disclose, or access lab test result information for a patient.",
                    "display": "lab test result access",
                },
                {
                    "code": "ACMED",
                    "definition": "Description: Provide consent to collect, use, disclose, or access medical condition information for a patient.",
                    "display": "medication access",
                },
                {
                    "code": "ACMEDC",
                    "definition": "Definition: Provide consent to view or access medical condition information for a patient.",
                    "display": "medical condition access",
                },
                {
                    "code": "ACMEN",
                    "definition": "Description:Provide consent to collect, use, disclose, or access mental health information for a patient.",
                    "display": "mental health access",
                },
                {
                    "code": "ACOBS",
                    "definition": "Description: Provide consent to collect, use, disclose, or access common observation information for a patient.",
                    "display": "common observations access",
                },
                {
                    "code": "ACPOLPRG",
                    "definition": "Description: Provide consent to collect, use, disclose, or access coverage policy or program for a patient.",
                    "display": "policy or program information access",
                },
                {
                    "code": "ACPROV",
                    "definition": "Description: Provide consent to collect, use, disclose, or access provider information for a patient.",
                    "display": "provider information access",
                },
                {
                    "code": "ACPSERV",
                    "definition": "Description: Provide consent to collect, use, disclose, or access professional service information for a patient.",
                    "display": "professional service access",
                },
                {
                    "code": "ACSUBSTAB",
                    "definition": "Description:Provide consent to collect, use, disclose, or access substance abuse information for a patient.",
                    "display": "substance abuse access",
                },
            ],
            "definition": "Description: The type of health information to which the subject of the information or the subject's delegate consents or dissents.",
            "display": "ActInformationAccessCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActInformationAccessCode

    Description: The type of health information to which the subject of the information or the subject's delegate consents or dissents.
    """

    underscore_act_information_access_context_code = CodeSystemConcept(
        {
            "code": "_ActInformationAccessContextCode",
            "concept": [
                {
                    "code": "INFAUT",
                    "concept": [
                        {
                            "code": "INFCON",
                            "definition": "Authorization to collect, access, use, or disclose specified patient health information as explicitly consented to by the subject of the information or the subject's representative.",
                            "display": "after explicit consent",
                        }
                    ],
                    "definition": "Authorization to collect, access, use, or disclose specified patient health information in accordance with jurisdictional law, organizational policy, or a patient's consent directive, which may be implied, deemed, opt-in, opt-out, or explicit.",
                    "display": "authorized information transfer",
                },
                {
                    "code": "INFCRT",
                    "definition": "Authorization to collect, access, use, or disclose specified patient health information in accordance with judicial system protocol, such as in the case of a subpoena or court order.",
                    "display": "only on court order",
                },
                {
                    "code": "INFDNG",
                    "definition": "Authorization to collect, access, use, or disclose specified patient health information where deemed necessary to avert potential danger to other persons in accordance with jurisdictional law, organizational policy, or standards of practice.  For example, disclosure about a person threatening violence.",
                    "display": "only if danger to others",
                },
                {
                    "code": "INFEMER",
                    "definition": "Authorization to collect, access, use, or disclose specified patient health information in accordance with emergency information transfer protocol dictated by jurisdictional law, organization policy, or standards of practice. For example, sharing of health information during disaster response.",
                    "display": "only in an emergency",
                },
                {
                    "code": "INFPWR",
                    "definition": "Authorization to collect, access, use, or disclose specified patient health information necessary to avert potential public welfare risk in accordance with jurisdictional law, organizational policy, or standards of practice.  For example, reporting that a person is a victim of abuse or demonstrating suicidal tendencies.",
                    "display": "only if public welfare risk",
                },
                {
                    "code": "INFREG",
                    "definition": "Authorization to collect, access, use, or disclose specified patient health information for public health, welfare, and safety purposes in accordance with jurisdictional law, organizational policy, or standards of practice.  For example, public health reporting of notifiable conditions.",
                    "display": "regulatory information transfer",
                },
            ],
            "definition": "Concepts conveying the context in which authorization given under jurisdictional law, by organizational policy, or by a patient consent directive permits the collection, access, use or disclosure of specified patient health information.",
            "display": "ActInformationAccessContextCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActInformationAccessContextCode

    Concepts conveying the context in which authorization given under jurisdictional law, by organizational policy, or by a patient consent directive permits the collection, access, use or disclosure of specified patient health information.
    """

    underscore_act_information_category_code = CodeSystemConcept(
        {
            "code": "_ActInformationCategoryCode",
            "concept": [
                {
                    "code": "ALLCAT",
                    "definition": "Description: All patient information.",
                    "display": "all categories",
                },
                {
                    "code": "ALLGCAT",
                    "definition": "Definition:All information pertaining to a patient's allergy and intolerance records.",
                    "display": "allergy category",
                },
                {
                    "code": "ARCAT",
                    "definition": "Description: All information pertaining to a patient's adverse drug reactions.",
                    "display": "adverse drug reaction category",
                },
                {
                    "code": "COBSCAT",
                    "definition": "Definition:All information pertaining to a patient's common observation records (height, weight, blood pressure, temperature, etc.).",
                    "display": "common observation category",
                },
                {
                    "code": "DEMOCAT",
                    "definition": "Definition:All information pertaining to a patient's demographics (such as name, date of birth, gender, address, etc).",
                    "display": "demographics category",
                },
                {
                    "code": "DICAT",
                    "definition": "Definition:All information pertaining to a patient's diagnostic image records (orders & results).",
                    "display": "diagnostic image category",
                },
                {
                    "code": "IMMUCAT",
                    "definition": "Definition:All information pertaining to a patient's vaccination records.",
                    "display": "immunization category",
                },
                {
                    "code": "LABCAT",
                    "definition": "Description: All information pertaining to a patient's lab test records (orders & results)",
                    "display": "lab test category",
                },
                {
                    "code": "MEDCCAT",
                    "definition": "Definition:All information pertaining to a patient's medical condition records.",
                    "display": "medical condition category",
                },
                {
                    "code": "MENCAT",
                    "definition": "Description: All information pertaining to a patient's mental health records.",
                    "display": "mental health category",
                },
                {
                    "code": "PSVCCAT",
                    "definition": "Definition:All information pertaining to a patient's professional service records (such as smoking cessation, counseling, medication review, mental health).",
                    "display": "professional service category",
                },
                {
                    "code": "RXCAT",
                    "definition": "Definition:All information pertaining to a patient's medication records (orders, dispenses and other active medications).",
                    "display": "medication category",
                },
            ],
            "definition": "Definition:Indicates the set of information types which may be manipulated or referenced, such as for recommending access restrictions.",
            "display": "ActInformationCategoryCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActInformationCategoryCode

    Definition:Indicates the set of information types which may be manipulated or referenced, such as for recommending access restrictions.
    """

    underscore_act_invoice_element_code = CodeSystemConcept(
        {
            "code": "_ActInvoiceElementCode",
            "concept": [
                {
                    "code": "_ActInvoiceAdjudicationPaymentCode",
                    "concept": [
                        {
                            "code": "_ActInvoiceAdjudicationPaymentGroupCode",
                            "concept": [
                                {
                                    "code": "ALEC",
                                    "definition": "Payment initiated by the payor as the result of adjudicating a submitted invoice that arrived to the payor from an electronic source that did not provide a conformant set of HL7 messages (e.g. web claim submission).",
                                    "display": "alternate electronic",
                                },
                                {
                                    "code": "BONUS",
                                    "definition": "Bonus payments based on performance, volume, etc. as agreed to by the payor.",
                                    "display": "bonus",
                                },
                                {
                                    "code": "CFWD",
                                    "definition": "An amount still owing to the payor but the payment is 0$ and this cannot be settled until a future payment is made.",
                                    "display": "carry forward adjusment",
                                },
                                {
                                    "code": "EDU",
                                    "definition": "Fees deducted on behalf of a payee for tuition and continuing education.",
                                    "display": "education fees",
                                },
                                {
                                    "code": "EPYMT",
                                    "definition": "Fees deducted on behalf of a payee for charges based on a shorter payment frequency (i.e. next day versus biweekly payments.",
                                    "display": "early payment fee",
                                },
                                {
                                    "code": "GARN",
                                    "definition": "Fees deducted on behalf of a payee for charges based on a per-transaction or time-period (e.g. monthly) fee.",
                                    "display": "garnishee",
                                },
                                {
                                    "code": "INVOICE",
                                    "definition": "Payment is based on a payment intent for a previously submitted Invoice, based on formal adjudication results..",
                                    "display": "submitted invoice",
                                },
                                {
                                    "code": "PINV",
                                    "definition": "Payment initiated by the payor as the result of adjudicating a paper (original, may have been faxed) invoice.",
                                    "display": "paper invoice",
                                },
                                {
                                    "code": "PPRD",
                                    "definition": "An amount that was owed to the payor as indicated, by a carry forward adjusment, in a previous payment advice",
                                    "display": "prior period adjustment",
                                },
                                {
                                    "code": "PROA",
                                    "definition": "Professional association fee that is collected by the payor from the practitioner/provider on behalf of the association",
                                    "display": "professional association deduction",
                                },
                                {
                                    "code": "RECOV",
                                    "definition": "Retroactive adjustment such as fee rate adjustment due to contract negotiations.",
                                    "display": "recovery",
                                },
                                {
                                    "code": "RETRO",
                                    "definition": "Bonus payments based on performance, volume, etc. as agreed to by the payor.",
                                    "display": "retro adjustment",
                                },
                                {
                                    "code": "TRAN",
                                    "definition": "Fees deducted on behalf of a payee for charges based on a per-transaction or time-period (e.g. monthly) fee.",
                                    "display": "transaction fee",
                                },
                            ],
                            "definition": "Codes representing adjustments to a Payment Advice such as retroactive, clawback, garnishee, etc.",
                            "display": "ActInvoiceAdjudicationPaymentGroupCode",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_ActInvoiceAdjudicationPaymentSummaryCode",
                            "concept": [
                                {
                                    "code": "INVTYPE",
                                    "definition": "Transaction counts and value totals by invoice type (e.g. RXDINV - Pharmacy Dispense)",
                                    "display": "invoice type",
                                },
                                {
                                    "code": "PAYEE",
                                    "definition": "Transaction counts and value totals by each instance of an invoice payee.",
                                    "display": "payee",
                                },
                                {
                                    "code": "PAYOR",
                                    "definition": "Transaction counts and value totals by each instance of an invoice payor.",
                                    "display": "payor",
                                },
                                {
                                    "code": "SENDAPP",
                                    "definition": "Transaction counts and value totals by each instance of a messaging application on a single processor. It is a registered identifier known to the receivers.",
                                    "display": "sending application",
                                },
                            ],
                            "definition": "Codes representing a grouping of invoice elements (totals, sub-totals), reported through a Payment Advice or a Statement of Financial Activity (SOFA).  The code can represent summaries by day, location, payee, etc.",
                            "display": "ActInvoiceAdjudicationPaymentSummaryCode",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True},
                                {"code": "child", "valueCode": "CONT"},
                                {"code": "child", "valueCode": "DAY"},
                                {"code": "child", "valueCode": "LOC"},
                                {"code": "child", "valueCode": "MONTH"},
                                {"code": "child", "valueCode": "PERIOD"},
                                {"code": "child", "valueCode": "PROV"},
                                {"code": "child", "valueCode": "WEEK"},
                                {"code": "child", "valueCode": "YEAR"},
                            ],
                        },
                    ],
                    "definition": "Codes representing a grouping of invoice elements (totals, sub-totals), reported through a Payment Advice or a Statement of Financial Activity (SOFA).  The code can represent summaries by day, location, payee and other cost elements such as bonus, retroactive adjustment and transaction fees.",
                    "display": "ActInvoiceAdjudicationPaymentCode",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_ActInvoiceDetailCode",
                    "concept": [
                        {
                            "code": "_ActInvoiceDetailClinicalProductCode",
                            "concept": [
                                {
                                    "code": "UNSPSC",
                                    "definition": "Description:United Nations Standard Products and Services Classification, managed by Uniform Code Council (UCC): www.unspsc.org",
                                    "display": "United Nations Standard Products and Services Classification",
                                }
                            ],
                            "definition": "An identifying data string for healthcare products.",
                            "display": "ActInvoiceDetailClinicalProductCode",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_ActInvoiceDetailDrugProductCode",
                            "concept": [
                                {
                                    "code": "GTIN",
                                    "definition": "Description:Global Trade Item Number is an identifier for trade items developed by GS1 (comprising the former EAN International and Uniform Code Council).",
                                    "display": "Global Trade Item Number",
                                },
                                {
                                    "code": "UPC",
                                    "definition": "Description:Universal Product Code is one of a wide variety of bar code languages widely used in the United States and Canada for items in stores.",
                                    "display": "Universal Product Code",
                                },
                            ],
                            "definition": "An identifying data string for A substance used as a medication or in the preparation of medication.",
                            "display": "ActInvoiceDetailDrugProductCode",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_ActInvoiceDetailGenericCode",
                            "concept": [
                                {
                                    "code": "_ActInvoiceDetailGenericAdjudicatorCode",
                                    "concept": [
                                        {
                                            "code": "COIN",
                                            "definition": "That portion of the eligible charges which a covered party must pay for each service and/or product. It is a percentage of the eligible amount for the service/product that is typically charged after the covered party has met the policy deductible.  This amount represents the covered party's coinsurance that is applied to a particular adjudication result. It is expressed as a negative dollar amount in adjudication results.",
                                            "display": "coinsurance",
                                        },
                                        {
                                            "code": "COPAYMENT",
                                            "definition": "That portion of the eligible charges which a covered party must pay for each service and/or product. It is a defined amount per service/product of the eligible amount for the service/product. This amount represents the covered party's copayment that is applied to a particular adjudication result. It is expressed as a negative dollar amount in adjudication results.",
                                            "display": "patient co-pay",
                                        },
                                        {
                                            "code": "DEDUCTIBLE",
                                            "definition": "That portion of the eligible charges which a covered party must pay in a particular period (e.g. annual) before the benefits are payable by the adjudicator. This amount represents the covered party's deductible that is applied to a particular adjudication result. It is expressed as a negative dollar amount in adjudication results.",
                                            "display": "deductible",
                                        },
                                        {
                                            "code": "PAY",
                                            "definition": "The guarantor, who may be the patient, pays the entire charge for a service. Reasons for such action may include: there is no insurance coverage for the service (e.g. cosmetic surgery); the patient wishes to self-pay for the service; or the insurer denies payment for the service due to contractual provisions such as the need for prior authorization.",
                                            "display": "payment",
                                        },
                                        {
                                            "code": "SPEND",
                                            "definition": "That total amount of the eligible charges which a covered party must periodically pay for services and/or products prior to the Medicaid program providing any coverage. This amount represents the covered party's spend down that is applied to a particular adjudication result. It is expressed as a negative dollar amount in adjudication results",
                                            "display": "spend down",
                                        },
                                        {
                                            "code": "COINS",
                                            "definition": "The covered party pays a percentage of the cost of covered services.",
                                            "display": "co-insurance",
                                            "property": [
                                                {
                                                    "code": "status",
                                                    "valueCode": "retired",
                                                }
                                            ],
                                        },
                                    ],
                                    "definition": "The billable item codes to identify adjudicator specified components to the total billing of a claim.",
                                    "display": "ActInvoiceDetailGenericAdjudicatorCode",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "_ActInvoiceDetailGenericModifierCode",
                                    "concept": [
                                        {
                                            "code": "AFTHRS",
                                            "definition": "Premium paid on service fees in compensation for practicing outside of normal working hours.",
                                            "display": "non-normal hours",
                                        },
                                        {
                                            "code": "ISOL",
                                            "definition": "Premium paid on service fees in compensation for practicing in a remote location.",
                                            "display": "isolation allowance",
                                        },
                                        {
                                            "code": "OOO",
                                            "definition": "Premium paid on service fees in compensation for practicing at a location other than normal working location.",
                                            "display": "out of office",
                                        },
                                    ],
                                    "definition": "The billable item codes to identify modifications to a billable item charge. As for example after hours increase in the office visit fee.",
                                    "display": "ActInvoiceDetailGenericModifierCode",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "_ActInvoiceDetailGenericProviderCode",
                                    "concept": [
                                        {
                                            "code": "CANCAPT",
                                            "definition": "A charge to compensate the provider when a patient cancels an appointment with insufficient time for the provider to make another appointment with another patient.",
                                            "display": "cancelled appointment",
                                        },
                                        {
                                            "code": "DSC",
                                            "definition": "A reduction in the amount charged as a percentage of the amount. For example a 5% discount for volume purchase.",
                                            "display": "discount",
                                        },
                                        {
                                            "code": "ESA",
                                            "definition": "A premium on a service fee is requested because, due to extenuating circumstances, the service took an extraordinary amount of time or supplies.",
                                            "display": "extraordinary service assessment",
                                        },
                                        {
                                            "code": "FFSTOP",
                                            "definition": "Under agreement between the parties (payor and provider), a guaranteed level of income is established for the provider over a specific, pre-determined period of time. The normal course of business for the provider is submission of fee-for-service claims. Should the fee-for-service income during the specified period of time be less than the agreed to amount, a top-up amount is paid to the provider equal to the difference between the fee-for-service total and the guaranteed income amount for that period of time. The details of the agreement may specify (or not) a requirement for repayment to the payor in the event that the fee-for-service income exceeds the guaranteed amount.",
                                            "display": "fee for service top off",
                                        },
                                        {
                                            "code": "FNLFEE",
                                            "definition": "Anticipated or actual final fee associated with treating a patient.",
                                            "display": "final fee",
                                        },
                                        {
                                            "code": "FRSTFEE",
                                            "definition": "Anticipated or actual initial fee associated with treating a patient.",
                                            "display": "first fee",
                                        },
                                        {
                                            "code": "MARKUP",
                                            "definition": "An increase in the amount charged as a percentage of the amount. For example, 12% markup on product cost.",
                                            "display": "markup or up-charge",
                                        },
                                        {
                                            "code": "MISSAPT",
                                            "definition": "A charge to compensate the provider when a patient does not show for an appointment.",
                                            "display": "missed appointment",
                                        },
                                        {
                                            "code": "PERFEE",
                                            "definition": "Anticipated or actual periodic fee associated with treating a patient. For example, expected billing cycle such as monthly, quarterly. The actual period (e.g. monthly, quarterly) is specified in the unit quantity of the Invoice Element.",
                                            "display": "periodic fee",
                                        },
                                        {
                                            "code": "PERMBNS",
                                            "definition": "The amount for a performance bonus that is being requested from a payor for the performance of certain services (childhood immunizations, influenza immunizations, mammograms, pap smears) on a sliding scale. That is, for 90% of childhood immunizations to a maximum of $2200/yr. An invoice is created at the end of the service period (one year) and a code is submitted indicating the percentage achieved and the dollar amount claimed.",
                                            "display": "performance bonus",
                                        },
                                        {
                                            "code": "RESTOCK",
                                            "definition": "A charge is requested because the patient failed to pick up the item and it took an amount of time to return it to stock for future use.",
                                            "display": "restocking fee",
                                        },
                                        {
                                            "code": "TRAVEL",
                                            "definition": "A charge to cover the cost of travel time and/or cost in conjuction with providing a service or product. It may be charged per kilometer or per hour based on the effective agreement.",
                                            "display": "travel",
                                        },
                                        {
                                            "code": "URGENT",
                                            "definition": "Premium paid on service fees in compensation for providing an expedited response to an urgent situation.",
                                            "display": "urgent",
                                        },
                                    ],
                                    "definition": "The billable item codes to identify provider supplied charges or changes to the total billing of a claim.",
                                    "display": "ActInvoiceDetailGenericProviderCode",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "_ActInvoiceDetailTaxCode",
                                    "concept": [
                                        {
                                            "code": "FST",
                                            "definition": "Federal tax on transactions such as the Goods and Services Tax (GST)",
                                            "display": "federal sales tax",
                                        },
                                        {
                                            "code": "HST",
                                            "definition": "Joint Federal/Provincial Sales Tax",
                                            "display": "harmonized sales Tax",
                                        },
                                        {
                                            "code": "PST",
                                            "definition": "Tax levied by the provincial or state jurisdiction such as Provincial Sales Tax",
                                            "display": "provincial/state sales tax",
                                        },
                                    ],
                                    "definition": "The billable item codes to identify modifications to a billable item charge by a tax factor applied to the amount. As for example 7% provincial sales tax.",
                                    "display": "ActInvoiceDetailTaxCode",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                            ],
                            "definition": "The detail item codes to identify charges or changes to the total billing of a claim due to insurance rules and payments.",
                            "display": "ActInvoiceDetailGenericCode",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_ActInvoiceDetailPreferredAccommodationCode",
                            "concept": [
                                {
                                    "code": "_ActEncounterAccommodationCode",
                                    "concept": [
                                        {
                                            "code": "_HL7AccommodationCode",
                                            "concept": [
                                                {
                                                    "code": "I",
                                                    "definition": "Accommodations used in the care of diseases that are transmitted through casual contact or respiratory transmission.",
                                                    "display": "Isolation",
                                                },
                                                {
                                                    "code": "P",
                                                    "definition": "Accommodations in which there is only 1 bed.",
                                                    "display": "Private",
                                                },
                                                {
                                                    "code": "S",
                                                    "definition": "Uniquely designed and elegantly decorated accommodations with many amenities available for an additional charge.",
                                                    "display": "Suite",
                                                },
                                                {
                                                    "code": "SP",
                                                    "definition": "Accommodations in which there are 2 beds.",
                                                    "display": "Semi-private",
                                                },
                                                {
                                                    "code": "W",
                                                    "definition": "Accommodations in which there are 3 or more beds.",
                                                    "display": "Ward",
                                                },
                                            ],
                                            "definition": "Description:Accommodation type. In Intent mood, represents the accommodation type requested. In Event mood, represents accommodation assigned/used. In Definition mood, represents the available accommodation type.",
                                            "display": "HL7AccommodationCode",
                                            "property": [
                                                {
                                                    "code": "notSelectable",
                                                    "valueBoolean": True,
                                                }
                                            ],
                                        }
                                    ],
                                    "definition": "Accommodation type.  In Intent mood, represents the accommodation type requested.  In Event mood, represents accommodation assigned/used.  In Definition mood, represents the available accommodation type.",
                                    "display": "ActEncounterAccommodationCode",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                }
                            ],
                            "definition": "An identifying data string for medical facility accommodations.",
                            "display": "ActInvoiceDetailPreferredAccommodationCode",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_ActInvoiceDetailClinicalServiceCode",
                            "definition": "An identifying data string for healthcare procedures.",
                            "display": "ActInvoiceDetailClinicalServiceCode",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True},
                                {"code": "status", "valueCode": "retired"},
                            ],
                        },
                    ],
                    "definition": 'Codes representing a service or product that is being invoiced (billed).  The code can represent such concepts as "office visit", "drug X", "wheelchair" and other billable items such as taxes, service charges and discounts.',
                    "display": "ActInvoiceDetailCode",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_ActInvoiceGroupCode",
                    "concept": [
                        {
                            "code": "_ActInvoiceInterGroupCode",
                            "concept": [
                                {
                                    "code": "CPNDDRGING",
                                    "definition": "A grouping of invoice element groups and details including the ones specifying the compound ingredients being invoiced. It may also contain generic detail items such as markup.",
                                    "display": "compound drug invoice group",
                                },
                                {
                                    "code": "CPNDINDING",
                                    "definition": "A grouping of invoice element details including the one specifying an ingredient drug being invoiced. It may also contain generic detail items such as tax or markup.",
                                    "display": "compound ingredient invoice group",
                                },
                                {
                                    "code": "CPNDSUPING",
                                    "definition": "A grouping of invoice element groups and details including the ones specifying the compound supplies being invoiced. It may also contain generic detail items such as markup.",
                                    "display": "compound supply invoice group",
                                },
                                {
                                    "code": "DRUGING",
                                    "definition": "A grouping of invoice element details including the one specifying the drug being invoiced. It may also contain generic detail items such as markup.",
                                    "display": "drug invoice group",
                                },
                                {
                                    "code": "FRAMEING",
                                    "definition": "A grouping of invoice element details including the ones specifying the frame fee and the frame dispensing cost that are being invoiced.",
                                    "display": "frame invoice group",
                                },
                                {
                                    "code": "LENSING",
                                    "definition": "A grouping of invoice element details including the ones specifying the lens fee and the lens dispensing cost that are being invoiced.",
                                    "display": "lens invoice group",
                                },
                                {
                                    "code": "PRDING",
                                    "definition": "A grouping of invoice element details including the one specifying the product (good or supply) being invoiced. It may also contain generic detail items such as tax or discount.",
                                    "display": "product invoice group",
                                },
                            ],
                            "definition": "Type of invoice element that is used to assist in describing an Invoice that is either submitted for adjudication or for which is returned on adjudication results.\r\n\n                        Invoice elements of this type signify a grouping of one or more children (detail) invoice elements.  They do not have intrinsic costing associated with them, but merely reflect the sum of all costing for it's immediate children invoice elements.\r\n\n                        The domain is only specified for an intermediate invoice element group (non-root or non-top level) for an Invoice.",
                            "display": "ActInvoiceInterGroupCode",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_ActInvoiceRootGroupCode",
                            "concept": [
                                {
                                    "code": "CPINV",
                                    "definition": "Clinical product invoice where the Invoice Grouping contains one or more billable item and is supported by clinical product(s).\r\n\n                        For example, a crutch or a wheelchair.",
                                    "display": "clinical product invoice",
                                },
                                {
                                    "code": "CSINV",
                                    "definition": "Clinical Services Invoice which can be used to describe a single service, multiple services or repeated services.\r\n\n                        [1] Single Clinical services invoice where the Invoice Grouping contains one billable item and is supported by one clinical service.\r\n\n                        For example, a single service for an office visit or simple clinical procedure (e.g. knee mobilization).\r\n\n                        [2] Multiple Clinical services invoice where the Invoice Grouping contains more than one billable item, supported by one or more clinical services.  The services can be distinct and over multiple dates, but for the same patient. This type of invoice includes a series of treatments which must be adjudicated together.\r\n\n                        For example, an adjustment and ultrasound for a chiropractic session where fees are associated for each of the services and adjudicated (invoiced) together.\r\n\n                        [3] Repeated Clinical services invoice where the Invoice Grouping contains one or more billable item, supported by the same clinical service repeated over a period of time.\r\n\n                        For example, the same Chiropractic adjustment (service or treatment) delivered on 3 separate occasions over a period of time at the discretion of the provider (e.g. month).",
                                    "display": "clinical service invoice",
                                },
                                {
                                    "code": "CSPINV",
                                    "definition": "A clinical Invoice Grouping consisting of one or more services and one or more product.  Billing for these service(s) and product(s) are supported by multiple clinical billable events (acts).\r\n\n                        All items in the Invoice Grouping must be adjudicated together to be acceptable to the Adjudicator.\r\n\n                        For example , a brace (product) invoiced together with the fitting (service).",
                                    "display": "clinical service and product",
                                },
                                {
                                    "code": "FININV",
                                    "definition": "Invoice Grouping without clinical justification.  These will not require identification of participants and associations from a clinical context such as patient and provider.\r\n\n                        Examples are interest charges and mileage.",
                                    "display": "financial invoice",
                                },
                                {
                                    "code": "OHSINV",
                                    "definition": "A clinical Invoice Grouping consisting of one or more oral health services. Billing for these service(s) are supported by multiple clinical billable events (acts).\r\n\n                        All items in the Invoice Grouping must be adjudicated together to be acceptable to the Adjudicator.",
                                    "display": "oral health service",
                                },
                                {
                                    "code": "PAINV",
                                    "definition": "HealthCare facility preferred accommodation invoice.",
                                    "display": "preferred accommodation invoice",
                                },
                                {
                                    "code": "RXCINV",
                                    "definition": "Pharmacy dispense invoice for a compound.",
                                    "display": "Rx compound invoice",
                                },
                                {
                                    "code": "RXDINV",
                                    "definition": "Pharmacy dispense invoice not involving a compound",
                                    "display": "Rx dispense invoice",
                                },
                                {
                                    "code": "SBFINV",
                                    "definition": "Clinical services invoice where the Invoice Group contains one billable item for multiple clinical services in one or more sessions.",
                                    "display": "sessional or block fee invoice",
                                },
                                {
                                    "code": "VRXINV",
                                    "definition": "Vision dispense invoice for up to 2 lens (left and right), frame and optional discount.  Eye exams are invoiced as a clinical service invoice.",
                                    "display": "vision dispense invoice",
                                },
                            ],
                            "definition": "Type of invoice element that is used to assist in describing an Invoice that is either submitted for adjudication or for which is returned on adjudication results.\r\n\n                        Invoice elements of this type signify a grouping of one or more children (detail) invoice elements.  They do not have intrinsic costing associated with them, but merely reflect the sum of all costing for it's immediate children invoice elements.\r\n\n                        Codes from this domain reflect the type of Invoice such as Pharmacy Dispense, Clinical Service and Clinical Product.  The domain is only specified for the root (top level) invoice element group for an Invoice.",
                            "display": "ActInvoiceRootGroupCode",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                    ],
                    "definition": "Type of invoice element that is used to assist in describing an Invoice that is either submitted for adjudication or for which is returned on adjudication results.\r\n\n                        Invoice elements of this type signify a grouping of one or more children (detail) invoice elements.  They do not have intrinsic costing associated with them, but merely reflect the sum of all costing for it's immediate children invoice elements.",
                    "display": "ActInvoiceGroupCode",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": "Type of invoice element that is used to assist in describing an Invoice that is either submitted for adjudication or for which is returned on adjudication results.",
            "display": "ActInvoiceElementCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActInvoiceElementCode

    Type of invoice element that is used to assist in describing an Invoice that is either submitted for adjudication or for which is returned on adjudication results.
    """

    underscore_act_invoice_element_summary_code = CodeSystemConcept(
        {
            "code": "_ActInvoiceElementSummaryCode",
            "concept": [
                {
                    "code": "_InvoiceElementAdjudicated",
                    "concept": [
                        {
                            "code": "ADNFPPELAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were adjudicated as payable prior to the specified time period (based on adjudication date), subsequently cancelled in the specified period and submitted electronically.",
                            "display": "adjud. nullified prior-period electronic amount",
                        },
                        {
                            "code": "ADNFPPELCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were adjudicated as payable prior to the specified time period (based on adjudication date), subsequently cancelled in the specified period and submitted electronically.",
                            "display": "adjud. nullified prior-period electronic count",
                        },
                        {
                            "code": "ADNFPPMNAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were adjudicated as payable prior to the specified time period (based on adjudication date), subsequently cancelled in the specified period and submitted manually.",
                            "display": "adjud. nullified prior-period manual amount",
                        },
                        {
                            "code": "ADNFPPMNCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were adjudicated as payable prior to the specified time period (based on adjudication date), subsequently cancelled in the specified period and submitted manually.",
                            "display": "adjud. nullified prior-period manual count",
                        },
                        {
                            "code": "ADNFSPELAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were adjudicated as payable during the specified time period (based on adjudication date), subsequently nullified in the specified period and submitted electronically.",
                            "display": "adjud. nullified same-period electronic amount",
                        },
                        {
                            "code": "ADNFSPELCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were adjudicated as payable during the specified time period (based on adjudication date), subsequently nullified in the specified period and submitted electronically.",
                            "display": "adjud. nullified same-period electronic count",
                        },
                        {
                            "code": "ADNFSPMNAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were adjudicated as payable during the specified time period (based on adjudication date), subsequently cancelled in the specified period and submitted manually.",
                            "display": "adjud. nullified same-period manual amount",
                        },
                        {
                            "code": "ADNFSPMNCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were adjudicated as payable during the specified time period (based on adjudication date), subsequently cancelled in the specified period and submitted manually.",
                            "display": "adjud. nullified same-period manual count",
                        },
                        {
                            "code": "ADNPPPELAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were adjudicated as payable prior to the specified time period (based on adjudication date) that do not match a specified payee (e.g. pay patient) and submitted electronically.",
                            "display": "adjud. non-payee payable prior-period electronic amount",
                        },
                        {
                            "code": "ADNPPPELCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were adjudicated as payable prior to the specified time period (based on adjudication date) that do not match a specified payee (e.g. pay patient) and submitted electronically.",
                            "display": "adjud. non-payee payable prior-period electronic count",
                        },
                        {
                            "code": "ADNPPPMNAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were adjudicated as payable prior to the specified time period (based on adjudication date) that do not match a specified payee (e.g. pay patient) and submitted manually.",
                            "display": "adjud. non-payee payable prior-period manual amount",
                        },
                        {
                            "code": "ADNPPPMNCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were adjudicated as payable prior to the specified time period (based on adjudication date) that do not match a specified payee (e.g. pay patient) and submitted manually.",
                            "display": "adjud. non-payee payable prior-period manual count",
                        },
                        {
                            "code": "ADNPSPELAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were adjudicated as payable during the specified time period (based on adjudication date) that do not match a specified payee (e.g. pay patient) and submitted electronically.",
                            "display": "adjud. non-payee payable same-period electronic amount",
                        },
                        {
                            "code": "ADNPSPELCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were adjudicated as payable during the specified time period (based on adjudication date) that do not match a specified payee (e.g. pay patient) and submitted electronically.",
                            "display": "adjud. non-payee payable same-period electronic count",
                        },
                        {
                            "code": "ADNPSPMNAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were adjudicated as payable during the specified time period (based on adjudication date) that do not match a specified payee (e.g. pay patient) and submitted manually.",
                            "display": "adjud. non-payee payable same-period manual amount",
                        },
                        {
                            "code": "ADNPSPMNCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were adjudicated as payable during the specified time period (based on adjudication date) that do not match a specified payee (e.g. pay patient) and submitted manually.",
                            "display": "adjud. non-payee payable same-period manual count",
                        },
                        {
                            "code": "ADPPPPELAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were adjudicated as payable prior to the specified time period (based on adjudication date) that match a specified payee (e.g. pay provider) and submitted electronically.",
                            "display": "adjud. payee payable prior-period electronic amount",
                        },
                        {
                            "code": "ADPPPPELCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were adjudicated as payable prior to the specified time period (based on adjudication date) that match a specified payee (e.g. pay provider) and submitted electronically.",
                            "display": "adjud. payee payable prior-period electronic count",
                        },
                        {
                            "code": "ADPPPPMNAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were adjudicated as payable prior to the specified time period (based on adjudication date) that match a specified payee (e.g. pay provider) and submitted manually.",
                            "display": "adjud. payee payable prior-period manual amout",
                        },
                        {
                            "code": "ADPPPPMNCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were adjudicated as payable prior to the specified time period (based on adjudication date) that match a specified payee (e.g. pay provider) and submitted manually.",
                            "display": "adjud. payee payable prior-period manual count",
                        },
                        {
                            "code": "ADPPSPELAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were adjudicated as payable during the specified time period (based on adjudication date) that match a specified payee (e.g. pay provider) and submitted electronically.",
                            "display": "adjud. payee payable same-period electronic amount",
                        },
                        {
                            "code": "ADPPSPELCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were adjudicated as payable during the specified time period (based on adjudication date) that match a specified payee (e.g. pay provider) and submitted electronically.",
                            "display": "adjud. payee payable same-period electronic count",
                        },
                        {
                            "code": "ADPPSPMNAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were adjudicated as payable during the specified time period (based on adjudication date) that match a specified payee (e.g. pay provider) and submitted manually.",
                            "display": "adjud. payee payable same-period manual amount",
                        },
                        {
                            "code": "ADPPSPMNCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were adjudicated as payable during the specified time period (based on adjudication date) that match a specified payee (e.g. pay provider) and submitted manually.",
                            "display": "adjud. payee payable same-period manual count",
                        },
                        {
                            "code": "ADRFPPELAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were adjudicated as refused prior to the specified time period (based on adjudication date) and submitted electronically.",
                            "display": "adjud. refused prior-period electronic amount",
                        },
                        {
                            "code": "ADRFPPELCT",
                            "definition": "Identifies the  total number of all  Invoice Groupings that were adjudicated as refused prior to the specified time period (based on adjudication date) and submitted electronically.",
                            "display": "adjud. refused prior-period electronic count",
                        },
                        {
                            "code": "ADRFPPMNAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were adjudicated as refused prior to the specified time period (based on adjudication date) and submitted manually.",
                            "display": "adjud. refused prior-period manual amount",
                        },
                        {
                            "code": "ADRFPPMNCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were adjudicated as refused prior to the specified time period (based on adjudication date) and submitted manually.",
                            "display": "adjud. refused prior-period manual count",
                        },
                        {
                            "code": "ADRFSPELAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were adjudicated as refused during the specified time period (based on adjudication date) and submitted electronically.",
                            "display": "adjud. refused same-period electronic amount",
                        },
                        {
                            "code": "ADRFSPELCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were adjudicated as refused during the specified time period (based on adjudication date) and submitted electronically.",
                            "display": "adjud. refused same-period electronic count",
                        },
                        {
                            "code": "ADRFSPMNAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were adjudicated as refused during the specified time period (based on adjudication date) and submitted manually.",
                            "display": "adjud. refused same-period manual amount",
                        },
                        {
                            "code": "ADRFSPMNCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were adjudicated as refused during the specified time period (based on adjudication date) and submitted manually.",
                            "display": "adjud. refused same-period manual count",
                        },
                    ],
                    "definition": "Total counts and total net amounts adjudicated for all  Invoice Groupings that were adjudicated within a time period based on the adjudication date of the Invoice Grouping.",
                    "display": "InvoiceElementAdjudicated",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_InvoiceElementPaid",
                    "concept": [
                        {
                            "code": "PDNFPPELAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were paid prior to the specified time period (based on payment date), subsequently nullified in the specified period and submitted electronically.",
                            "display": "paid nullified prior-period electronic amount",
                        },
                        {
                            "code": "PDNFPPELCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were paid prior to the specified time period (based on payment date), subsequently nullified in the specified period and submitted electronically.",
                            "display": "paid nullified prior-period electronic count",
                        },
                        {
                            "code": "PDNFPPMNAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were paid prior to the specified time period (based on payment date), subsequently nullified in the specified period and submitted manually.",
                            "display": "paid nullified prior-period manual amount",
                        },
                        {
                            "code": "PDNFPPMNCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were paid prior to the specified time period (based on payment date), subsequently nullified in the specified period and submitted manually.",
                            "display": "paid nullified prior-period manual count",
                        },
                        {
                            "code": "PDNFSPELAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were paid during the specified time period (based on payment date), subsequently nullified in the specified period and submitted electronically.",
                            "display": "paid nullified same-period electronic amount",
                        },
                        {
                            "code": "PDNFSPELCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were paid during the specified time period (based on payment date), subsequently cancelled in the specified period and submitted electronically.",
                            "display": "paid nullified same-period electronic count",
                        },
                        {
                            "code": "PDNFSPMNAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were paid during the specified time period (based on payment date), subsequently nullified in the specified period and submitted manually.",
                            "display": "paid nullified same-period manual amount",
                        },
                        {
                            "code": "PDNFSPMNCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were paid during the specified time period (based on payment date), subsequently nullified in the specified period and submitted manually.",
                            "display": "paid nullified same-period manual count",
                        },
                        {
                            "code": "PDNPPPELAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were paid prior to the specified time period (based on payment date) that do not match a specified payee (e.g. pay patient) and submitted electronically.",
                            "display": "paid non-payee payable prior-period electronic amount",
                        },
                        {
                            "code": "PDNPPPELCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were paid prior to the specified time period (based on payment date) that do not match a specified payee (e.g. pay patient) and submitted electronically.",
                            "display": "paid non-payee payable prior-period electronic count",
                        },
                        {
                            "code": "PDNPPPMNAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were paid prior to the specified time period (based on payment date) that do not match a specified payee (e.g. pay patient) and submitted manually.",
                            "display": "paid non-payee payable prior-period manual amount",
                        },
                        {
                            "code": "PDNPPPMNCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were paid prior to the specified time period (based on payment date) that do not match a specified payee (e.g. pay patient) and submitted manually.",
                            "display": "paid non-payee payable prior-period manual count",
                        },
                        {
                            "code": "PDNPSPELAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were paid during the specified time period (based on payment date) that do not match a specified payee (e.g. pay patient) and submitted electronically.",
                            "display": "paid non-payee payable same-period electronic amount",
                        },
                        {
                            "code": "PDNPSPELCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were paid during the specified time period (based on payment date) that do not match a specified payee (e.g. pay patient) and submitted electronically.",
                            "display": "paid non-payee payable same-period electronic count",
                        },
                        {
                            "code": "PDNPSPMNAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were paid during the specified time period (based on payment date) that do not match a specified payee (e.g. pay patient) and submitted manually.",
                            "display": "paid non-payee payable same-period manual amount",
                        },
                        {
                            "code": "PDNPSPMNCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were paid during the specified time period (based on payment date) that do not match a specified payee (e.g. pay patient) and submitted manually.",
                            "display": "paid non-payee payable same-period manual count",
                        },
                        {
                            "code": "PDPPPPELAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were paid prior to the specified time period (based on payment date) that match a specified payee (e.g. pay provider) and submitted electronically.",
                            "display": "paid payee payable prior-period electronic amount",
                        },
                        {
                            "code": "PDPPPPELCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were paid prior to the specified time period (based on payment date) that match a specified payee (e.g. pay provider) and submitted electronically.",
                            "display": "paid payee payable prior-period electronic count",
                        },
                        {
                            "code": "PDPPPPMNAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were paid prior to the specified time period (based on payment date) that match a specified payee (e.g. pay provider) and submitted manually.",
                            "display": "paid payee payable prior-period manual amount",
                        },
                        {
                            "code": "PDPPPPMNCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were paid prior to the specified time period (based on payment date) that match a specified payee (e.g. pay provider) and submitted manually.",
                            "display": "paid payee payable prior-period manual count",
                        },
                        {
                            "code": "PDPPSPELAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were paid during the specified time period (based on payment date) that match a specified payee (e.g. pay provider) and submitted electronically.",
                            "display": "paid payee payable same-period electronic amount",
                        },
                        {
                            "code": "PDPPSPELCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were paid during the specified time period (based on payment date) that match a specified payee (e.g. pay provider) and submitted electronically.",
                            "display": "paid payee payable same-period electronic count",
                        },
                        {
                            "code": "PDPPSPMNAT",
                            "definition": "Identifies the total net amount of all  Invoice Groupings that were paid during the specified time period (based on payment date) that match a specified payee (e.g. pay provider) and submitted manually.",
                            "display": "paid payee payable same-period manual amount",
                        },
                        {
                            "code": "PDPPSPMNCT",
                            "definition": "Identifies the total number of all  Invoice Groupings that were paid during the specified time period (based on payment date) that match a specified payee (e.g. pay provider) and submitted manually.",
                            "display": "paid payee payable same-period manual count",
                        },
                    ],
                    "definition": "Total counts and total net amounts paid for all  Invoice Groupings that were paid within a time period based on the payment date.",
                    "display": "InvoiceElementPaid",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_InvoiceElementSubmitted",
                    "concept": [
                        {
                            "code": "SBBLELAT",
                            "definition": "Identifies the total net amount billed for all submitted Invoice Groupings within a time period and submitted electronically.  Adjudicated invoice elements are included.",
                            "display": "submitted billed electronic amount",
                        },
                        {
                            "code": "SBBLELCT",
                            "definition": "Identifies the total number of submitted Invoice Groupings within a time period and submitted electronically.  Adjudicated invoice elements are included.",
                            "display": "submitted billed electronic count",
                        },
                        {
                            "code": "SBNFELAT",
                            "definition": "Identifies the total net amount billed for all submitted  Invoice Groupings that were nullified within a time period and submitted electronically.  Adjudicated invoice elements are included.",
                            "display": "submitted nullified electronic amount",
                        },
                        {
                            "code": "SBNFELCT",
                            "definition": "Identifies the total number of submitted  Invoice Groupings that were nullified within a time period and submitted electronically.  Adjudicated invoice elements are included.",
                            "display": "submitted cancelled electronic count",
                        },
                        {
                            "code": "SBPDELAT",
                            "definition": "Identifies the total net amount billed for all submitted  Invoice Groupings that are pended or held by the payor, within a time period and submitted electronically.  Adjudicated invoice elements are not included.",
                            "display": "submitted pending electronic amount",
                        },
                        {
                            "code": "SBPDELCT",
                            "definition": "Identifies the total number of submitted  Invoice Groupings that are pended or held by the payor, within a time period and submitted electronically.  Adjudicated invoice elements are not included.",
                            "display": "submitted pending electronic count",
                        },
                    ],
                    "definition": "Total counts and total net amounts billed for all Invoice Groupings that were submitted within a time period.  Adjudicated invoice elements are included.",
                    "display": "InvoiceElementSubmitted",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": "Identifies the different types of summary information that can be reported by queries dealing with Statement of Financial Activity (SOFA).  The summary information is generally used to help resolve balance discrepancies between providers and payors.",
            "display": "ActInvoiceElementSummaryCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActInvoiceElementSummaryCode

    Identifies the different types of summary information that can be reported by queries dealing with Statement of Financial Activity (SOFA).  The summary information is generally used to help resolve balance discrepancies between providers and payors.
    """

    underscore_act_invoice_override_code = CodeSystemConcept(
        {
            "code": "_ActInvoiceOverrideCode",
            "concept": [
                {
                    "code": "COVGE",
                    "definition": "Insurance coverage problems have been encountered. Additional explanation information to be supplied.",
                    "display": "coverage problem",
                },
                {
                    "code": "EFORM",
                    "definition": "Electronic form with supporting or additional information to follow.",
                    "display": "electronic form to follow",
                },
                {
                    "code": "FAX",
                    "definition": "Fax with supporting or additional information to follow.",
                    "display": "fax to follow",
                },
                {
                    "code": "GFTH",
                    "definition": "The medical service was provided to a patient in good faith that they had medical coverage, although no evidence of coverage was available before service was rendered.",
                    "display": "good faith indicator",
                },
                {
                    "code": "LATE",
                    "definition": "Knowingly over the payor's published time limit for this invoice possibly due to a previous payor's delays in processing. Additional reason information will be supplied.",
                    "display": "late invoice",
                },
                {
                    "code": "MANUAL",
                    "definition": "Manual review of the invoice is requested.  Additional information to be supplied.  This may be used in the case of an appeal.",
                    "display": "manual review",
                },
                {
                    "code": "OOJ",
                    "definition": "The medical service and/or product was provided to a patient that has coverage in another jurisdiction.",
                    "display": "out of jurisdiction",
                },
                {
                    "code": "ORTHO",
                    "definition": "The service provided is required for orthodontic purposes. If the covered party has orthodontic coverage, then the service may be paid.",
                    "display": "orthodontic service",
                },
                {
                    "code": "PAPER",
                    "definition": "Paper documentation (or other physical format) with supporting or additional information to follow.",
                    "display": "paper documentation to follow",
                },
                {
                    "code": "PIE",
                    "definition": "Public Insurance has been exhausted.  Invoice has not been sent to Public Insuror and therefore no Explanation Of Benefits (EOB) is provided with this Invoice submission.",
                    "display": "public insurance exhausted",
                },
                {
                    "code": "PYRDELAY",
                    "definition": "Allows provider to explain lateness of invoice to a subsequent payor.",
                    "display": "delayed by a previous payor",
                },
                {
                    "code": "REFNR",
                    "definition": "Rules of practice do not require a physician's referral for the provider to perform a billable service.",
                    "display": "referral not required",
                },
                {
                    "code": "REPSERV",
                    "definition": "The same service was delivered within a time period that would usually indicate a duplicate billing.  However, the repeated service is a medical \tnecessity and therefore not a duplicate.",
                    "display": "repeated service",
                },
                {
                    "code": "UNRELAT",
                    "definition": "The service provided is not related to another billed service. For example, 2 unrelated services provided on the same day to the same patient which may normally result in a refused payment for one of the items.",
                    "display": "unrelated service",
                },
                {
                    "code": "VERBAUTH",
                    "definition": "The provider has received a verbal permission from an authoritative source to perform the service or supply the item being invoiced.",
                    "display": "verbal authorization",
                },
            ],
            "definition": "Includes coded responses that will occur as a result of the adjudication of an electronic invoice at a summary level and provides guidance on interpretation of the referenced adjudication results.",
            "display": "ActInvoiceOverrideCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActInvoiceOverrideCode

    Includes coded responses that will occur as a result of the adjudication of an electronic invoice at a summary level and provides guidance on interpretation of the referenced adjudication results.
    """

    underscore_act_list_code = CodeSystemConcept(
        {
            "code": "_ActListCode",
            "concept": [
                {
                    "code": "_ActObservationList",
                    "concept": [
                        {
                            "code": "CARELIST",
                            "definition": "List of acts representing a care plan.  The acts can be in a varierty of moods including event (EVN) to record acts that have been carried out as part of the care plan.",
                            "display": "care plan",
                        },
                        {
                            "code": "CONDLIST",
                            "concept": [
                                {
                                    "code": "INTOLIST",
                                    "definition": "List of intolerance observations.",
                                    "display": "intolerance list",
                                },
                                {
                                    "code": "PROBLIST",
                                    "definition": "List of problem observations.",
                                    "display": "problem list",
                                },
                                {
                                    "code": "RISKLIST",
                                    "definition": "List of risk factor observations.",
                                    "display": "risk factors",
                                },
                            ],
                            "definition": "List of condition observations.",
                            "display": "condition list",
                        },
                        {
                            "code": "GOALLIST",
                            "definition": "List of observations in goal mood.",
                            "display": "goal list",
                        },
                    ],
                    "definition": "ActObservationList",
                    "display": "ActObservationList",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_ActTherapyDurationWorkingListCode",
                    "concept": [
                        {
                            "code": "_ActMedicationTherapyDurationWorkingListCode",
                            "concept": [
                                {
                                    "code": "ACU",
                                    "definition": "Definition:A list of medications which the patient is only expected to consume for the duration of the current order or limited set of orders and which is not expected to be renewed.",
                                    "display": "short term/acute",
                                },
                                {
                                    "code": "CHRON",
                                    "definition": "Definition:A list of medications which are expected to be continued beyond the present order and which the patient should be assumed to be taking unless explicitly stopped.",
                                    "display": "continuous/chronic",
                                },
                                {
                                    "code": "ONET",
                                    "definition": "Definition:A list of medications which the patient is intended to be administered only once.",
                                    "display": "one time",
                                },
                                {
                                    "code": "PRN",
                                    "definition": "Definition:A list of medications which the patient will consume intermittently based on the behavior of the condition for which the medication is indicated.",
                                    "display": "as needed",
                                },
                            ],
                            "definition": 'Definition:A collection of concepts that identifies different types of \'duration-based\' mediation working lists.\r\n\n                        \n                           Examples:"Continuous/Chronic" "Short-Term" and "As Needed"',
                            "display": "act medication therapy duration working list",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        }
                    ],
                    "definition": 'Codes used to identify different types of \'duration-based\' working lists.  Examples include "Continuous/Chronic", "Short-Term" and "As-Needed".',
                    "display": "ActTherapyDurationWorkingListCode",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "MEDLIST",
                    "concept": [
                        {
                            "code": "CURMEDLIST",
                            "definition": "List of current medications.",
                            "display": "current medication list",
                        },
                        {
                            "code": "DISCMEDLIST",
                            "definition": "List of discharge medications.",
                            "display": "discharge medication list",
                        },
                        {
                            "code": "HISTMEDLIST",
                            "definition": "Historical list of medications.",
                            "display": "medication history",
                        },
                    ],
                    "definition": "List of medications.",
                    "display": "medication list",
                },
            ],
            "definition": "Provides codes associated with ActClass value of LIST (working list)",
            "display": "ActListCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActListCode

    Provides codes associated with ActClass value of LIST (working list)
    """

    underscore_act_monitoring_protocol_code = CodeSystemConcept(
        {
            "code": "_ActMonitoringProtocolCode",
            "concept": [
                {
                    "code": "CTLSUB",
                    "definition": "A monitoring program that focuses on narcotics and/or commonly abused substances that are subject to legal restriction.",
                    "display": "Controlled Substance",
                },
                {
                    "code": "INV",
                    "definition": "Definition:A monitoring program that focuses on a drug which is under investigation and has not received regulatory approval for the condition being investigated",
                    "display": "investigational",
                },
                {
                    "code": "LU",
                    "definition": "Description:A drug that can be prescribed (and reimbursed) only if it meets certain criteria.",
                    "display": "limited use",
                },
                {
                    "code": "OTC",
                    "definition": "Medicines designated in this way may be supplied for patient use without a prescription.  The exact form of categorisation will vary in different realms.",
                    "display": "non prescription medicine",
                },
                {
                    "code": "RX",
                    "definition": "Some form of prescription is required before the related medicine can be supplied for a patient.  The exact form of regulation will vary in different realms.",
                    "display": "prescription only medicine",
                },
                {
                    "code": "SA",
                    "definition": "Definition:A drug that requires prior approval (to be reimbursed) before being dispensed",
                    "display": "special authorization",
                },
                {
                    "code": "SAC",
                    "definition": "Description:A drug that requires special access permission to be prescribed and dispensed.",
                    "display": "special access",
                },
            ],
            "definition": "Identifies types of monitoring programs",
            "display": "ActMonitoringProtocolCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActMonitoringProtocolCode

    Identifies types of monitoring programs
    """

    underscore_act_non_observation_indication_code = CodeSystemConcept(
        {
            "code": "_ActNonObservationIndicationCode",
            "concept": [
                {
                    "code": "IND01",
                    "definition": "Description:Contrast agent required for imaging study.",
                    "display": "imaging study requiring contrast",
                },
                {
                    "code": "IND02",
                    "definition": "Description:Provision of prescription or direction to consume a product for purposes of bowel clearance in preparation for a colonoscopy.",
                    "display": "colonoscopy prep",
                },
                {
                    "code": "IND03",
                    "definition": "Description:Provision of medication as a preventative measure during a treatment or other period of increased risk.",
                    "display": "prophylaxis",
                },
                {
                    "code": "IND04",
                    "definition": "Description:Provision of medication during pre-operative phase; e.g., antibiotics before dental surgery or bowel prep before colon surgery.",
                    "display": "surgical prophylaxis",
                },
                {
                    "code": "IND05",
                    "definition": "Description:Provision of medication for pregnancy --e.g., vitamins, antibiotic treatments for vaginal tract colonization, etc.",
                    "display": "pregnancy prophylaxis",
                },
            ],
            "definition": "Description:Concepts representing indications (reasons for clinical action) other than diagnosis and symptoms.",
            "display": "ActNonObservationIndicationCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActNonObservationIndicationCode

    Description:Concepts representing indications (reasons for clinical action) other than diagnosis and symptoms.
    """

    underscore_act_observation_verification_type = CodeSystemConcept(
        {
            "code": "_ActObservationVerificationType",
            "concept": [
                {
                    "code": "VFPAPER",
                    "definition": "Definition:Indicates that the paper version of the record has, should be or is being verified against the electronic version.",
                    "display": "verify paper",
                }
            ],
            "definition": "Identifies the type of verification investigation being undertaken with respect to the subject of the verification activity.\r\n\n                        \n                           Examples:\n                        \r\n\n                        \n                           \n                              Verification of eligibility for coverage under a policy or program - aka enrolled/covered by a policy or program\r\n\n                           \n                           \n                              Verification of record - e.g., person has record in an immunization registry\r\n\n                           \n                           \n                              Verification of enumeration - e.g. NPI\r\n\n                           \n                           \n                              Verification of Board Certification - provider specific\r\n\n                           \n                           \n                              Verification of Certification - e.g. JAHCO, NCQA, URAC\r\n\n                           \n                           \n                              Verification of Conformance - e.g. entity use with HIPAA, conformant to the CCHIT EHR system criteria\r\n\n                           \n                           \n                              Verification of Provider Credentials\r\n\n                           \n                           \n                              Verification of no adverse findings - e.g. on National Provider Data Bank, Health Integrity Protection Data Base (HIPDB)",
            "display": "act observation verification",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    act observation verification

    Identifies the type of verification investigation being undertaken with respect to the subject of the verification activity.


                           Examples:




                              Verification of eligibility for coverage under a policy or program - aka enrolled/covered by a policy or program



                              Verification of record - e.g., person has record in an immunization registry



                              Verification of enumeration - e.g. NPI



                              Verification of Board Certification - provider specific



                              Verification of Certification - e.g. JAHCO, NCQA, URAC



                              Verification of Conformance - e.g. entity use with HIPAA, conformant to the CCHIT EHR system criteria



                              Verification of Provider Credentials



                              Verification of no adverse findings - e.g. on National Provider Data Bank, Health Integrity Protection Data Base (HIPDB)
    """

    underscore_act_payment_code = CodeSystemConcept(
        {
            "code": "_ActPaymentCode",
            "concept": [
                {
                    "code": "ACH",
                    "definition": "Automated Clearing House (ACH).",
                    "display": "Automated Clearing House",
                },
                {
                    "code": "CHK",
                    "definition": "A written order to a bank to pay the amount specified from funds on deposit.",
                    "display": "Cheque",
                },
                {
                    "code": "DDP",
                    "definition": "Electronic Funds Transfer (EFT) deposit into the payee's bank account",
                    "display": "Direct Deposit",
                },
                {
                    "code": "NON",
                    "definition": "Non-Payment Data.",
                    "display": "Non-Payment Data",
                },
            ],
            "definition": "Code identifying the method or the movement of payment instructions.\r\n\n                        Codes are drawn from X12 data element 591 (PaymentMethodCode)",
            "display": "ActPaymentCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActPaymentCode

    Code identifying the method or the movement of payment instructions.

                        Codes are drawn from X12 data element 591 (PaymentMethodCode)
    """

    underscore_act_pharmacy_supply_type = CodeSystemConcept(
        {
            "code": "_ActPharmacySupplyType",
            "concept": [
                {
                    "code": "DF",
                    "definition": "A fill providing sufficient supply for one day",
                    "display": "Daily Fill",
                },
                {
                    "code": "EM",
                    "concept": [
                        {
                            "code": "SO",
                            "definition": "An emergency supply where the expectation is that a formal order authorizing the supply will be provided at a later date.",
                            "display": "Script Owing",
                        }
                    ],
                    "definition": "A supply action where there is no 'valid' order for the supplied medication.  E.g. Emergency vacation supply, weekend supply (when prescriber is unavailable to provide a renewal prescription)",
                    "display": "Emergency Supply",
                },
                {
                    "code": "FF",
                    "concept": [
                        {
                            "code": "FFC",
                            "definition": "A first fill where the quantity supplied is equal to one full repetition of the ordered amount. (e.g. If the order was 90 tablets, 3 refills, a complete fill would be for the full 90 tablets).",
                            "display": "First Fill - Complete",
                            "property": [{"code": "child", "valueCode": "FFCS"}],
                        },
                        {
                            "code": "FFP",
                            "definition": "A first fill where the quantity supplied is less than one full repetition of the ordered amount. (e.g. If the order was 90 tablets, 3 refills, a partial fill might be for only 30 tablets.)",
                            "display": "First Fill - Part Fill",
                        },
                        {
                            "code": "FFSS",
                            "definition": "A first fill where the strength supplied is less than the ordered strength. (e.g. 10mg for an order of 50mg where a subsequent fill will dispense 40mg tablets).",
                            "display": "first fill, partial strength",
                            "property": [
                                {"code": "child", "valueCode": "FFPS"},
                                {"code": "child", "valueCode": "FFCS"},
                                {"code": "child", "valueCode": "TFS"},
                            ],
                        },
                        {
                            "code": "TF",
                            "definition": "A fill where a small portion is provided to allow for determination of the therapy effectiveness and patient tolerance.",
                            "display": "Trial Fill",
                            "property": [{"code": "child", "valueCode": "TFS"}],
                        },
                    ],
                    "definition": "The initial fill against an order.  (This includes initial fills against refill orders.)",
                    "display": "First Fill",
                    "property": [
                        {"code": "child", "valueCode": "FFS"},
                        {"code": "child", "valueCode": "FFPS"},
                    ],
                },
                {
                    "code": "FS",
                    "definition": "A supply action to restock a smaller more local dispensary.",
                    "display": "Floor stock",
                },
                {
                    "code": "MS",
                    "definition": "A supply of a manufacturer sample",
                    "display": "Manufacturer Sample",
                },
                {
                    "code": "RF",
                    "concept": [
                        {
                            "code": "UD",
                            "definition": "A supply action that provides sufficient material for a single dose.",
                            "display": "Unit Dose",
                        },
                        {
                            "code": "RFC",
                            "concept": [
                                {
                                    "code": "RFCS",
                                    "definition": "A refill where the quantity supplied is equal to one full repetition of the ordered amount. (e.g. If the order was 90 tablets, 3 refills, a complete fill would be for the full 90 tablets.) and where the strength supplied is less than the ordered strength (e.g. 10mg for an order of 50mg where a subsequent fill will dispense 40mg tablets).",
                                    "display": "refill complete partial strength",
                                }
                            ],
                            "definition": "A refill where the quantity supplied is equal to one full repetition of the ordered amount. (e.g. If the order was 90 tablets, 3 refills, a complete fill would be for the full 90 tablets.)",
                            "display": "Refill - Complete",
                        },
                        {
                            "code": "RFF",
                            "concept": [
                                {
                                    "code": "RFFS",
                                    "definition": "The first fill against an order that has already been filled at least once at another facility and where the strength supplied is less than the ordered strength (e.g. 10mg for an order of 50mg where a subsequent fill will dispense 40mg tablets).",
                                    "display": "refill partial strength (first fill this facility)",
                                }
                            ],
                            "definition": "The first fill against an order that has already been filled at least once at another facility.",
                            "display": "Refill (First fill this facility)",
                        },
                        {
                            "code": "RFP",
                            "concept": [
                                {
                                    "code": "RFPS",
                                    "definition": "A refill where the quantity supplied is less than one full repetition of the ordered amount. (e.g. If the order was 90 tablets, 3 refills, a partial fill might be for only 30 tablets.) and where the strength supplied is less than the ordered strength (e.g. 10mg for an order of 50mg where a subsequent fill will dispense 40mg tablets).",
                                    "display": "refill part fill partial strength",
                                }
                            ],
                            "definition": "A refill where the quantity supplied is less than one full repetition of the ordered amount. (e.g. If the order was 90 tablets, 3 refills, a partial fill might be for only 30 tablets.)",
                            "display": "Refill - Part Fill",
                        },
                        {
                            "code": "RFS",
                            "definition": "A fill against an order that has already been filled (or partially filled) at least once and where the strength supplied is less than the ordered strength (e.g. 10mg for an order of 50mg where a subsequent fill will dispense 40mg tablets).",
                            "display": "refill partial strength",
                        },
                        {
                            "code": "TB",
                            "concept": [
                                {
                                    "code": "TBS",
                                    "definition": "A fill where the remainder of a 'complete' fill is provided after a trial fill has been provided and where the strength supplied is less than the ordered strength (e.g. 10mg for an order of 50mg where a subsequent fill will dispense 40mg tablets).",
                                    "display": "trial balance partial strength",
                                }
                            ],
                            "definition": "A fill where the remainder of a 'complete' fill is provided after a trial fill has been provided.",
                            "display": "Trial Balance",
                        },
                    ],
                    "definition": "A fill against an order that has already been filled (or partially filled) at least once.",
                    "display": "Refill",
                    "property": [{"code": "child", "valueCode": "DF"}],
                },
                {
                    "code": "UDE",
                    "definition": "A supply action that provides sufficient material for a single dose via multiple products.  E.g. 2 50mg tablets for a 100mg unit dose.",
                    "display": "unit dose equivalent",
                },
            ],
            "definition": "Identifies types of dispensing events",
            "display": "ActPharmacySupplyType",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "child", "valueCode": "UD"},
            ],
        }
    )
    """
    ActPharmacySupplyType

    Identifies types of dispensing events
    """

    underscore_act_policy_type = CodeSystemConcept(
        {
            "code": "_ActPolicyType",
            "concept": [
                {
                    "code": "_ActPrivacyPolicy",
                    "concept": [
                        {
                            "code": "_ActConsentDirective",
                            "concept": [
                                {
                                    "code": "EMRGONLY",
                                    "definition": "This general consent directive specifically limits disclosure of health information for purpose of emergency treatment. Additional parameters may further limit the disclosure to specific users, roles, duration, types of information, and impose uses obligations.\r\n\n                        \n                           Definition: Opt-in to disclosure of health information for emergency only consent directive.",
                                    "display": "emergency only",
                                },
                                {
                                    "code": "GRANTORCHOICE",
                                    "definition": 'A grantor\'s terms of agreement to which a grantee may assent or dissent, and which may include an opportunity for a grantee to request restrictions or extensions.\r\n\n                        \n                           Comment: A grantor typically is able to stipulate preferred terms of agreement when the grantor has control over the topic of the agreement, which a grantee must accept in full or may be offered an opportunity to extend or restrict certain terms.\r\n\n                        \n                           Usage Note: If the grantor\'s term of agreement must be accepted in full, then this is considered "basic consent".  If a grantee is offered an opportunity to extend or restrict certain terms, then the agreement is considered "granular consent".\r\n\n                        \n                           Examples: \n                        \r\n\n                        \n                           Healthcare: A PHR account holder [grantor] may require any PHR user [grantee]  to accept the terms of agreement in full, or may permit a PHR user to extend or restrict terms selected by the account holder or requested by the PHR user.\n                           Non-healthcare: The owner of a resource server [grantor] may require any authorization server [grantee] to meet authorization requirements stipulated in the grantor\'s terms of agreement.',
                                    "display": "grantor choice",
                                },
                                {
                                    "code": "IMPLIED",
                                    "definition": "A grantor's presumed assent to the grantee's terms of agreement is based on the grantor's behavior, which may result from not expressly assenting to the consent directive offered, or from having no right to assent or dissent offered by the grantee.\r\n\n                        \n                           Comment: Implied or \"implicit\" consent occurs when the behavior of the grantor is understood by a reasonable person to signal agreement to the grantee's terms.\r\n\n                        \n                           Usage Note: Implied consent with no opportunity to assent or dissent to certain terms is considered \"basic consent\".\r\n\n                        \n                           Examples: \n                        \r\n\n                        \n                           Healthcare: A patient schedules an appointment with a provider, and either does not take the opportunity to expressly assent or dissent to the provider's consent directive, does not have an opportunity to do so, as in the case where emergency care is required, or simply behaves as though the patient [grantor] agrees to the rights granted to the provider [grantee] in an implicit consent directive.\n                           An injured and unconscious patient is deemed to have assented to emergency treatment by those permitted to do so under jurisdictional laws, e.g., Good Samaritan laws.\n                           Non-healthcare: Upon receiving a driver's license, the driver is deemed to have assented without explicitly consenting to undergoing field sobriety tests.\n                           A corporation that does business in a foreign nation is deemed to have deemed to have assented without explicitly consenting to abide by that nation's laws.",
                                    "display": "implied consent",
                                },
                                {
                                    "code": "IMPLIEDD",
                                    "definition": "A grantor's presumed assent to the grantee's terms of agreement, which is based on the grantor's behavior, and includes a right to dissent to certain terms. \r\n\n                        \n                           Comment: A grantor assenting to the grantee's terms of agreement may or may not exercise a right to dissent to grantor selected terms or to grantee's selected terms to which a grantor may dissent.\r\n\n                        \n                           Usage Note: Implied or \"implicit\" consent with an \"opportunity to dissent\" occurs when the grantor's behavior is understood by a reasonable person to signal assent to the grantee's terms of agreement whether the grantor requests or the grantee approves further restrictions, is considered \"granular consent\".\r\n\n                        \n                           Examples: \n                        \r\n\n                        \n                           Healthcare Examples: A healthcare provider deems a patient's assent to disclosure of health information to family members and friends, but offers an opportunity or permits the patient to dissent to such disclosures.\n                           A health information exchanges deems a patient to have assented to disclosure of health information for treatment purposes, but offers the patient an opportunity to dissents to disclosure to particular provider organizations.\n                           Non-healthcare Examples: A bank deems a banking customer's assent to specified collection, access, use, or disclosure of financial information as a requirement of holding a bank account, but provides the user an opportunity to limit third-party collection, access, use or disclosure of that information for marketing purposes.",
                                    "display": "implied consent with opportunity to dissent",
                                },
                                {
                                    "code": "NOCONSENT",
                                    "definition": "No notification or opportunity is provided for a grantor to assent or dissent to a grantee's terms of agreement.\r\n\n                        \n                           Comment: A \"No Consent\" policy scheme provides no opportunity for accommodation of an individual's preferences, and may not comply with Fair Information Practice Principles [FIPP] by enabling the data subject to object, access collected information, correct errors, or have accounting of disclosures.\r\n\n                        \n                           Usage Note: The grantee's terms of agreement, may be available to the grantor by reviewing the grantee's privacy policies, but there is no notice by which a grantor is apprised of the policy directly or able to acknowledge.\r\n\n                        \n                           Examples: \n                        \r\n\n                        \n                           Healthcare: Without notification or an opportunity to assent or dissent, a patient's health information is automatically included in and available (often according to certain rules) through a health information exchange.  Note that this differs from implied consent, where the patient is assumed to have consented.\n                           Without notification or an opportunity to assent or dissent, a patient's health information is collected, accessed, used, or disclosed for research, public health, security, fraud prevention, court order, or law enforcement.\n                           Non-healthcare: Without notification or an opportunity to assent or dissent, a consumer's healthcare or non-healthcare internet searches are aggregated for secondary uses such as behavioral tracking and profiling.\n                           Without notification or an opportunity to assent or dissent, a consumer's location and activities in a shopping mall are tracked by RFID tags on purchased items.",
                                    "display": "no consent",
                                },
                                {
                                    "code": "NOPP",
                                    "definition": "Acknowledgement of custodian notice of privacy practices.\r\n\n                        \n                           Usage Notes: This type of consent directive acknowledges a custodian's notice of privacy practices including its permitted collection, access, use and disclosure of health information to users and for purposes of use specified.",
                                    "display": "notice of privacy practices",
                                },
                                {
                                    "code": "OPTIN",
                                    "definition": "A grantor's assent to the terms of an agreement offered by a grantee without an opportunity for to dissent to any terms.\r\n\n                        \n                           Comment: Acceptance of a grantee's terms pertaining, for example, to permissible activities, purposes of use, handling caveats, expiry date, and revocation policies.\r\n\n                        \n                           Usage Note: Opt-in with no opportunity for a grantor to restrict certain permissions sought by the grantee is considered \"basic consent\".\r\n\n                        \n                           Examples: \n                        \r\n\n                        \n                           Healthcare: A patient [grantor] signs a provider's [grantee's] consent directive form, which lists permissible collection, access, use, or disclosure activities, purposes of use, handling caveats, and revocation policies.\n                           Non-healthcare: An employee [grantor] signs an employer's [grantee's] non-disclosure and non-compete agreement.",
                                    "display": "opt-in",
                                },
                                {
                                    "code": "OPTINR",
                                    "definition": "A grantor's assent to the grantee's terms of an agreement with an opportunity for to dissent to certain grantor or grantee selected terms.\r\n\n                        \n                           Comment: A grantor dissenting to the grantee's terms of agreement may or may not exercise a right to assent to grantor's pre-approved restrictions or to grantee's selected terms to which a grantor may dissent.\r\n\n                        \n                           Usage Note: Opt-in with restrictions is considered \"granular consent\" because the grantor has an opportunity to narrow the permissions sought by the grantee.\r\n\n                        \n                           Examples: \n                        \r\n\n                        \n                           Healthcare:  A patient assent to grantee's consent directive terms for collection, access, use, or disclosure of health information, and dissents to disclosure to certain recipients as allowed by the provider's pre-approved restriction list.\n                           Non-Healthcare: A cell phone user assents to the cell phone's privacy practices and terms of use, but dissents from location tracking by turning off the cell phone's tracking capability.",
                                    "display": "opt-in with restrictions",
                                },
                                {
                                    "code": "OPTOUT",
                                    "definition": "A grantor's dissent to the terms of agreement offered by a grantee without an opportunity for to assent to any terms.\r\n\n                        \n                           Comment: Rejection of a grantee's terms of agreement pertaining, for example, to permissible activities, purposes of use, handling caveats, expiry date, and revocation policies.\r\n\n                        \n                           Usage Note: Opt-out with no opportunity for a grantor to permit certain permissions sought by the grantee is considered \"basic consent\".\r\n\n                        \n                           Examples: \n                        \r\n\n                        \n                           Healthcare: A patient [grantor] declines to sign a provider's [grantee's] consent directive form, which lists permissible collection, access, use, or disclosure activities, purposes of use, handling caveats, revocation policies, and consequences of not assenting.\n                           Non-healthcare: An employee [grantor] refuses to sign an employer's [grantee's] agreement not to join unions or participate in a strike where state law protects employee's collective bargaining rights.\n                           A citizen [grantor] refuses to enroll in mandatory government [grantee] health insurance based on religious beliefs, which is an exemption.",
                                    "display": "op-out",
                                },
                                {
                                    "code": "OPTOUTE",
                                    "definition": 'A grantor\'s dissent to the grantee\'s terms of agreement except for certain grantor or grantee selected terms.\r\n\n                        \n                           Comment: A rejection of a grantee\'s terms of agreement while assenting to certain permissions sought by the grantee or requesting approval of additional grantor terms.\r\n\n                        \n                           Usage Note: Opt-out with exceptions is considered a "granular consent" because the grantor has an opportunity to accept certain permissions sought by the grantee or request additional grantor terms, while rejecting other grantee terms.\r\n\n                        \n                           Examples: \n                        \r\n\n                        \n                           Healthcare: A patient [grantor] dissents to a health information exchange consent directive with the exception of disclosure based on a limited "time to live" shared secret [e.g., a token or password], which the patient can give to a provider when seeking care.\n                           Non-healthcare: A social media user [grantor] dissents from public access to their account, but assents to access to a circle of friends.',
                                    "display": "opt-out with exceptions",
                                },
                            ],
                            "definition": 'Specifies the type of agreement between one or more grantor and grantee in which rights and obligations related to one or more shared items of interest are allocated.\r\n\n                        \n                           Usage Note: Such agreements may be considered "consent directives" or "contracts" depending on the context, and are considered closely related or synonymous from a legal perspective.\r\n\n                        \n                           Examples: \n                        \r\n\n                        \n                           Healthcare Privacy Consent Directive permitting or restricting in whole or part the collection, access, use, and disclosure of health information, and any associated handling caveats.\n                           Healthcare Medical Consent Directive to receive medical procedures after being informed of risks and benefits, thereby reducing the grantee\'s liability.\n                           Research Informed Consent for participation in clinical trials and disclosure of health information after being informed of risks and benefits, thereby reducing the grantee\'s liability.\n                           Substitute decision maker delegation in which the grantee assumes responsibility to act on behalf of the grantor.\n                           Contracts in which the agreement requires assent/dissent by the grantor of terms offered by a grantee, a consumer opts out of an "award" system for use of a retailer\'s marketing or credit card vendor\'s point collection cards in exchange for allowing purchase tracking and profiling.\n                           A mobile device or App privacy policy and terms of service to which a user must agree in whole or in part in order to utilize the service.\n                           Agreements between a client and an authorization server or between an authorization server and a resource operator and/or resource owner permitting or restricting e.g., collection, access, use, and disclosure of information, and any associated handling caveats.',
                            "display": "ActConsentDirective",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_ActPrivacyLaw",
                            "concept": [
                                {
                                    "code": "_ActUSPrivacyLaw",
                                    "concept": [
                                        {
                                            "code": "42CFRPart2",
                                            "definition": "42 CFR Part 2 stipulates the right of an individual who has applied for or been given diagnosis or treatment for alcohol or drug abuse at a federally assisted program.\r\n\n                        \n                           Definition: Non-disclosure of health information relating to health care paid for by a federally assisted substance abuse program without patient consent.\r\n\n                        \n                           Usage Note: May be associated with an Act or a Role to indicate the legal provision to which the assignment of an Act.confidentialityCode or Role.confidentialityCode complies.",
                                            "display": "42 CFR Part2",
                                        },
                                        {
                                            "code": "CommonRule",
                                            "definition": "U.S. Federal regulations governing the protection of human subjects in research (codified at Subpart A of 45 CFR part 46) that has been adopted by 15 U.S. Federal departments and agencies in an effort to promote uniformity, understanding, and compliance with human subject protections. Existing regulations governing the protection of human subjects in Food and Drug Administration (FDA)-regulated research (21 CFR parts 50, 56, 312, and 812) are separate from the Common Rule but include similar requirements.\r\n\n                        \n                           Definition: U.S. federal laws governing research-related privacy policies.\r\n\n                        \n                           Usage Note: May be associated with an Act or a Role to indicate the legal provision to which the assignment of an Act.confidentialityCode or Role.confidentialtyCode complies.",
                                            "display": "Common Rule",
                                        },
                                        {
                                            "code": "HIPAANOPP",
                                            "definition": "The U.S. Public Law 104-191 Health Insurance Portability and Accountability Act (HIPAA) Privacy Rule (45 CFR Part 164 Subpart E) permits access, use and disclosure of certain personal health information (PHI as defined under the law) for purposes of Treatment, Payment, and Operations, and requires that the provider ask that patients acknowledge the Provider's Notice of Privacy Practices as permitted conduct under the law.\r\n\n                        \n                           Definition: Notification of HIPAA Privacy Practices.\r\n\n                        \n                           Usage Note: May be associated with an Act or a Role to indicate the legal provision to which the assignment of an Act.confidentialityCode or Role.confidentialtyCode complies.",
                                            "display": "HIPAA notice of privacy practices",
                                        },
                                        {
                                            "code": "HIPAAPsyNotes",
                                            "definition": "The U.S. Public Law 104-191 Health Insurance Portability and Accountability Act (HIPAA) Privacy Rule (45 CFR Part 164 Section 164.508) requires authorization for certain uses and disclosure of psychotherapy notes.\r\n\n                        \n                           Definition: Authorization that must be obtained for disclosure of psychotherapy notes.\r\n\n                        \n                           Usage Note: May be associated with an Act or a Role to indicate the legal provision to which the assignment of an Act.confidentialityCode or Role.confidentialityCode complies.",
                                            "display": "HIPAA psychotherapy notes",
                                        },
                                        {
                                            "code": "HIPAASelfPay",
                                            "definition": "Section 13405(a) of the Health Information Technology for Economic and Clinical Health Act (HITECH) stipulates the right of an individual to have disclosures regarding certain health care items or services for which the individual pays out of pocket in full restricted from a health plan.\r\n\n                        \n                           Definition: Non-disclosure of health information to a health plan relating to health care items or services for which an individual pays out of pocket in full.\r\n\n                        \n                           Usage Note: May be associated with an Act or a Role to indicate the legal provision to which the assignment of an Act.confidentialityCode or Role.confidentialityCode complies.",
                                            "display": "HIPAA self-pay",
                                        },
                                        {
                                            "code": "Title38Section7332",
                                            "definition": "Title 38 Part 1-protected information may only be disclosed to a third party with the special written consent of the patient except where expressly authorized by 38 USC 7332. VA may disclose this information for specific purposes to: VA employees on a need to know basis - more restrictive than Privacy Act need to know; contractors who need the information in order to perform or fulfil the duties of the contract; and researchers who provide assurances that the information will not be identified in any report. This information may also be disclosed without consent where patient lacks decision-making capacity; in a medical emergency for the purpose of treating a condition which poses an immediate threat to the health of any individual and which requires immediate medical intervention; for eye, tissue, or organ donation purposes; and disclosure of HIV information for public health purposes.\r\n\n                        \n                           Definition: Title 38 Part 1 - Section 1.462 Confidentiality restrictions.\r\n\n                        (a) General. The patient records to which Sections 1.460 through 1.499 of this part apply may be disclosed or used only as permitted by these regulations and may not otherwise be disclosed or used in any civil, criminal, administrative, or legislative proceedings conducted by any Federal, State, or local authority. Any disclosure made under these regulations must be limited to that information which is necessary to carry out the purpose of the disclosure. SUBCHAPTER III--PROTECTION OF PATIENT RIGHTS Sec. 7332. Confidentiality of certain medical records (a)(1) Records of the identity, diagnosis, prognosis, or treatment of any patient or subject which are maintained in connection with the performance of any program or activity (including education, training, treatment, rehabilitation, or research) relating to drug abuse, alcoholism or alcohol abuse, infection with the human immunodeficiency virus, or sickle cell anemia which is carried out by or for the Department under this title shall, except as provided in subsections (e) and (f), be confidential, and (section 5701 of this title to the contrary notwithstanding) such records may be disclosed only for the purposes and under the circumstances expressly authorized under subsection (b).\r\n\n                        \n                           Usage Note: May be associated with an Act or a Role to indicate the legal provision to which the assignment of an Act.confidentialityCode or Role.confidentialityCode complies.",
                                            "display": "Title 38 Section 7332",
                                        },
                                    ],
                                    "definition": "Definition: A jurisdictional mandate in the U.S. relating to privacy.\r\n\n                        \n                           Usage Note: ActPrivacyLaw codes may be associated with an Act or a Role to indicate the legal provision to which the assignment of an Act.confidentialityCode or Role.confidentialtyCode complies.  May be used to further specify rationale for assignment of other ActPrivacyPolicy codes in the US realm, e.g., ETH and 42CFRPart2 can be differentiated from ETH and Title38Part1.",
                                    "display": "_ActUSPrivacyLaw",
                                }
                            ],
                            "definition": "A jurisdictional mandate, regulation, obligation, requirement, rule, or expectation deeming certain information to be private to an individual or organization, which is imposed on:\r\n\n                        \n                           The activity of a governed party\n                           The behavior of a governed party\n                           The manner in which an act is executed by a governed party",
                            "display": "ActPrivacyLaw",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_InformationSensitivityPolicy",
                            "concept": [
                                {
                                    "code": "_ActInformationSensitivityPolicy",
                                    "concept": [
                                        {
                                            "code": "ETH",
                                            "definition": "Policy for handling alcohol or drug-abuse information, which will be afforded heightened confidentiality.  Information handling protocols based on organizational policies related to alcohol or drug-abuse information that is deemed sensitive.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                            "display": "substance abuse information sensitivity",
                                        },
                                        {
                                            "code": "GDIS",
                                            "definition": "Policy for handling genetic disease information, which will be afforded heightened confidentiality. Information handling protocols based on organizational policies related to genetic disease information that is deemed sensitive.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                            "display": "genetic disease information sensitivity",
                                        },
                                        {
                                            "code": "HIV",
                                            "definition": "Policy for handling HIV or AIDS information, which will be afforded heightened confidentiality. Information handling protocols based on organizational policies related to HIV or AIDS information that is deemed sensitive.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                            "display": "HIV/AIDS information sensitivity",
                                        },
                                        {
                                            "code": "MST",
                                            "definition": "Policy for handling information related to sexual assault or repeated, threatening sexual harassment that occurred while the patient was in the military, which is afforded heightened confidentiality. \r\n\n                        Access control concerns for military sexual trauma is based on the patient being subject to control by a higher ranking military perpetrator and/or censure by others within the military unit.  Due to the relatively unfettered access to healthcare information by higher ranking military personnel and those who have command over the patient, there is a need to sequester this information outside of the typical controls on access to military health records.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law in addition to this more generic code.",
                                            "display": "military sexual trauma information sensitivity",
                                        },
                                        {
                                            "code": "SCA",
                                            "definition": "Policy for handling sickle cell disease information, which is afforded heightened confidentiality.  Information handling protocols are based on organizational policies related to sickle cell disease information, which is deemed sensitive.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then the Act valued with this ActCode should be associated with an Act valued with any applicable laws from the ActPrivacyLaw code system.",
                                            "display": "sickle cell anemia information sensitivity",
                                        },
                                        {
                                            "code": "SDV",
                                            "definition": "Policy for handling sexual assault, abuse, or domestic violence information, which will be afforded heightened confidentiality. Information handling protocols based on organizational policies related to sexual assault, abuse, or domestic violence information that is deemed sensitive.\r\n\n                        SDV code covers violence perpetrated by related and non-related persons. This code should be specific to physical and mental trauma caused by a related person only.  The access control concerns are keeping the patient safe from the perpetrator who may have an abusive psychological control over the patient, may be stalking the patient, or may try to manipulate care givers into allowing the perpetrator to make contact with the patient.  The definition needs to be clarified.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                            "display": "sexual assault, abuse, or domestic violence information sensitivity",
                                        },
                                        {
                                            "code": "SEX",
                                            "definition": "Policy for handling sexuality and reproductive health information, which will be afforded heightened confidentiality.  Information handling protocols based on organizational policies related to sexuality and reproductive health information that is deemed sensitive.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                            "display": "sexuality and reproductive health information sensitivity",
                                        },
                                        {
                                            "code": "SPI",
                                            "concept": [
                                                {
                                                    "code": "BH",
                                                    "concept": [
                                                        {
                                                            "code": "COGN",
                                                            "definition": "Policy for handling information related to cognitive disability disorders and conditions caused by these disorders, which are afforded heightened confidentiality.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law in addition to this more generic code.\r\n\n                        Examples may include dementia, traumatic brain injury, attention deficit, hearing and visual disability such as dyslexia and other disorders and related conditions which impair learning and self-sufficiency.  However, the cognitive disabilities to which this term may apply  versus other behavioral health categories varies by jurisdiction and organizational policy in part due to overlap with other behavioral health conditions. Implementers should constrain to those diagnoses applicable in the domain in which this code is used.",
                                                            "display": "cognitive disability information sensitivity",
                                                        },
                                                        {
                                                            "code": "DVD",
                                                            "definition": "Policy for handling information related to developmental disability disorders and conditions caused by these disorders, which is afforded heightened confidentiality.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law in addition to this more generic code.\r\n\n                        A diverse group of chronic conditions that are due to mental or physical impairments impacting activities of daily living, self-care, language acuity, learning, mobility, independent living and economic self-sufficiency. Examples may include Down syndrome and  Autism spectrum. However, the developmental disabilities to which this term applies versus other behavioral health categories varies by jurisdiction and organizational policy in part due to overlap with other behavioral health conditions.  Implementers should constrain to those diagnoses applicable in the domain in which this code is used.",
                                                            "display": "developmental disability information sensitivity",
                                                        },
                                                        {
                                                            "code": "EMOTDIS",
                                                            "definition": "Policy for handling information related to emotional disturbance disorders and conditions caused by these disorders, which is afforded heightened confidentiality.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law in addition to this more generic code.\r\n\n                        Typical used to characterize behavioral and mental health issues of adolescents where the disorder may be temporarily diagnosed in order to avoid the potential and unnecessary stigmatizing diagnoses of disorder long term.",
                                                            "display": "emotional disturbance information sensitivity",
                                                        },
                                                    ],
                                                    "definition": "Policy for handling information related to behavioral and emotional disturbances affecting social adjustment and physical health, which is afforded heightened confidentiality.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law in addition to this more generic code.",
                                                    "display": "behavioral health information sensitivity",
                                                },
                                                {
                                                    "code": "MH",
                                                    "definition": "Policy for handling information related to psychological disorders, which is afforded heightened confidentiality. Mental health information may be deemed specifically sensitive and distinct from physical health, substance use disorders, and behavioral disabilities and disorders in some jurisdictions.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law in addition to this more generic code.",
                                                    "display": "mental health information sensitivity",
                                                },
                                                {
                                                    "code": "PSY",
                                                    "definition": "Policy for handling psychiatry psychiatric disorder information, which is afforded heightened confidentiality. \r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                                    "display": "psychiatry disorder information sensitivity",
                                                },
                                                {
                                                    "code": "PSYTHPN",
                                                    "definition": "Policy for handling psychotherapy note information, which is afforded heightened confidentiality. \r\n\n                        \n                           Usage Note: In some jurisdiction, disclosure of psychotherapy notes requires patient consent.\r\n\n                        If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                                    "display": "psychotherapy note information sensitivity",
                                                },
                                                {
                                                    "code": "SUD",
                                                    "concept": [
                                                        {
                                                            "code": "ETHUD",
                                                            "definition": "Policy for handling information related to alcohol use disorders and conditions caused by these disorders, which is afforded heightened confidentiality. \r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law in addition to this more generic code.",
                                                            "display": "alcohol use disorder information sensitivity",
                                                        },
                                                        {
                                                            "code": "OPIOIDUD",
                                                            "definition": "Policy for handling information related to opioid use disorders and conditions caused by these disorders, which is afforded heightened confidentiality. \r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law in addition to this more generic code.",
                                                            "display": "opioid use disorder information sensitivity",
                                                        },
                                                    ],
                                                    "definition": "Policy for handling information related to alcohol or drug use disorders and conditions caused by these disorders, which is afforded heightened confidentiality. \r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law in addition to this more generic code.",
                                                    "display": "substance use disorder information sensitivity",
                                                },
                                            ],
                                            "definition": "Policy for handling information deemed specially protected by law or policy including substance abuse, substance use, psychiatric, mental health, behavioral health, and cognitive disorders, which is afforded heightened confidentiality.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law in addition to this more generic code.",
                                            "display": "specially protected information sensitivity",
                                        },
                                        {
                                            "code": "STD",
                                            "definition": "Policy for handling sexually transmitted disease information, which will be afforded heightened confidentiality.\n Information handling protocols based on organizational policies related to sexually transmitted disease information that is deemed sensitive.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                            "display": "sexually transmitted disease information sensitivity",
                                        },
                                        {
                                            "code": "TBOO",
                                            "definition": "Policy for handling information not to be initially disclosed or discussed with patient except by a physician assigned to patient in this case. Information handling protocols based on organizational policies related to sensitive patient information that must be initially discussed with the patient by an attending physician before being disclosed to the patient.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.\r\n\n                        \n                           Open Issue: This definition conflates a rule and a characteristic, and there may be a similar issue with ts sibling codes.",
                                            "display": "taboo",
                                        },
                                        {
                                            "code": "VIO",
                                            "definition": "Policy for handling information related to harm by violence, which is afforded heightened confidentiality. Harm by violence is perpetrated by an unrelated person.\r\n\n                        Access control concerns for information about mental or physical harm resulting from violence caused by an unrelated person may include manipulation of care givers or access to records that enable the perpetrator contact or locate the patient, but the perpetrator will likely not have established abusive psychological control over the patient. \r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law in addition to this more generic code.",
                                            "display": "violence information sensitivity",
                                        },
                                        {
                                            "code": "SICKLE",
                                            "definition": 'Types of sensitivity policies that apply to Acts.  Act.confidentialityCode is defined in the RIM as "constraints around appropriate disclosure of information about this Act, regardless of mood."\r\n\n                        \n                           Usage Note: ActSensitivity codes are used to bind information to an Act.confidentialityCode according to local sensitivity policy so that those confidentiality codes can then govern its handling across enterprises.  Internally to a policy domain, however, local policies guide the access control system on how end users in that policy domain are able to use information tagged with these sensitivity values.',
                                            "display": "sickle cell",
                                            "property": [
                                                {
                                                    "code": "status",
                                                    "valueCode": "retired",
                                                }
                                            ],
                                        },
                                    ],
                                    "definition": 'Types of sensitivity policies that apply to Acts.  Act.confidentialityCode is defined in the RIM as "constraints around appropriate disclosure of information about this Act, regardless of mood."\r\n\n                        \n                           Usage Note: ActSensitivity codes are used to bind information to an Act.confidentialityCode according to local sensitivity policy so that those confidentiality codes can then govern its handling across enterprises.  Internally to a policy domain, however, local policies guide the access control system on how end users in that policy domain are  able to use information tagged with these sensitivity values.',
                                    "display": "ActInformationSensitivityPolicy",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "_EntitySensitivityPolicyType",
                                    "concept": [
                                        {
                                            "code": "DEMO",
                                            "definition": "Policy for handling all demographic information about an information subject, which will be afforded heightened confidentiality. Policies may govern sensitivity of information related to all demographic about an information subject, the disclosure of which could impact the privacy, well-being, or safety of that subject.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                            "display": "all demographic information sensitivity",
                                        },
                                        {
                                            "code": "DOB",
                                            "definition": "Policy for handling information related to an information subject's date of birth, which will be afforded heightened confidentiality.Policies may govern sensitivity of information related to an information subject's date of birth, the disclosure of which could impact the privacy, well-being, or safety of that subject.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                            "display": "date of birth information sensitivity",
                                        },
                                        {
                                            "code": "GENDER",
                                            "definition": "Policy for handling information related to an information subject's gender and sexual orientation, which will be afforded heightened confidentiality.  Policies may govern sensitivity of information related to an information subject's gender and sexual orientation, the disclosure of which could impact the privacy, well-being, or safety of that subject.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                            "display": "gender and sexual orientation information sensitivity",
                                        },
                                        {
                                            "code": "LIVARG",
                                            "definition": "Policy for handling information related to an information subject's living arrangement, which will be afforded heightened confidentiality.  Policies may govern sensitivity of information related to an information subject's living arrangement, the disclosure of which could impact the privacy, well-being, or safety of that subject.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                            "display": "living arrangement information sensitivity",
                                        },
                                        {
                                            "code": "MARST",
                                            "definition": "Policy for handling information related to an information subject's marital status, which will be afforded heightened confidentiality. Policies may govern sensitivity of information related to an information subject's marital status, the disclosure of which could impact the privacy, well-being, or safety of that subject.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                            "display": "marital status information sensitivity",
                                        },
                                        {
                                            "code": "RACE",
                                            "definition": "Policy for handling information related to an information subject's race, which will be afforded heightened confidentiality.  Policies may govern sensitivity of information related to an information subject's race, the disclosure of which could impact the privacy, well-being, or safety of that subject.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                            "display": "race information sensitivity",
                                        },
                                        {
                                            "code": "REL",
                                            "definition": "Policy for handling information related to an information subject's religious affiliation, which will be afforded heightened confidentiality.  Policies may govern sensitivity of information related to an information subject's religion, the disclosure of which could impact the privacy, well-being, or safety of that subject.\r\n\n                        \n                           Usage Notes: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                            "display": "religion information sensitivity",
                                        },
                                    ],
                                    "definition": 'Types of sensitivity policies that may apply to a sensitive attribute on an Entity.\r\n\n                        \n                           Usage Note: EntitySensitivity codes are used to convey a policy that is applicable to sensitive information conveyed by an entity attribute.  May be used to bind a Role.confidentialityCode associated with an Entity per organizational policy.  Role.confidentialityCode is defined in the RIM as "an indication of the appropriate disclosure of information about this Role with respect to the playing Entity."',
                                    "display": "EntityInformationSensitivityPolicy",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "_RoleInformationSensitivityPolicy",
                                    "concept": [
                                        {
                                            "code": "B",
                                            "definition": "Policy for handling trade secrets such as financial information or intellectual property, which will be afforded heightened confidentiality.  Description:  Since the service class can represent knowledge factory that may be considered a trade or business secret, there is sometimes (though rarely) the need to flag those items as of business level confidentiality.\r\n\n                        \n                           Usage Notes: No patient related information may ever be of this confidentiality level.   If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                            "display": "business information sensitivity",
                                        },
                                        {
                                            "code": "EMPL",
                                            "definition": "Policy for handling information related to an employer which is deemed classified to protect an employee who is the information subject, and which will be afforded heightened confidentiality.  Description:  Policies may govern sensitivity of information related to an employer, such as law enforcement or national security, the identity of which could impact the privacy, well-being, or safety of an information subject who is an employee.\r\n\n                        \n                           Usage Notes: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                            "display": "employer information sensitivity",
                                        },
                                        {
                                            "code": "LOCIS",
                                            "definition": "Policy for handling information related to the location of the information subject, which will be afforded heightened confidentiality.  Description:  Policies may govern sensitivity of information related to the location of the information subject, the disclosure of which could impact the privacy, well-being, or safety of that subject.\r\n\n                        \n                           Usage Notes: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                            "display": "location information sensitivity",
                                        },
                                        {
                                            "code": "SSP",
                                            "definition": "Policy for handling information related to a provider of sensitive services, which will be afforded heightened confidentiality.  Description:  Policies may govern sensitivity of information related to providers who deliver sensitive healthcare services in order to protect the privacy, well-being, and safety of the provider and of patients receiving sensitive services.\r\n\n                        \n                           Usage Notes: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                            "display": "sensitive service provider information sensitivity",
                                        },
                                    ],
                                    "definition": 'Types of sensitivity policies that apply to Roles.\r\n\n                        \n                           Usage Notes: RoleSensitivity codes are used to bind information to a Role.confidentialityCode per organizational policy.  Role.confidentialityCode is defined in the RIM as "an indication of the appropriate disclosure of information about this Role with respect to the playing Entity."',
                                    "display": "RoleInformationSensitivityPolicy",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "ADOL",
                                    "definition": "Policy for handling information related to an adolescent, which will be afforded heightened confidentiality per applicable organizational or jurisdictional policy.  An enterprise may have a policy that requires that adolescent patient information be provided heightened confidentiality.  Information deemed sensitive typically includes health information and patient role information including patient status, demographics, next of kin, and location.\r\n\n                        \n                           Usage Note: For use within an enterprise in which an adolescent is the information subject.  If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                    "display": "adolescent information sensitivity",
                                },
                                {
                                    "code": "CEL",
                                    "definition": "Policy for handling information related to a celebrity (people of public interest (VIP), which will be afforded heightened confidentiality.  Celebrities are people of public interest (VIP) about whose information an enterprise may have a policy that requires heightened confidentiality.  Information deemed sensitive may include health information and patient role information including patient status, demographics, next of kin, and location.\r\n\n                        \n                           Usage Note:  For use within an enterprise in which the information subject is deemed a celebrity or very important person.  If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                    "display": "celebrity information sensitivity",
                                },
                                {
                                    "code": "DIA",
                                    "definition": "Policy for handling information related to a diagnosis, health condition or health problem, which will be afforded heightened confidentiality.  Diagnostic, health condition or health problem related information may be deemed sensitive by organizational policy, and require heightened confidentiality.\r\n\n                        \n                           Usage Note: For use within an enterprise that provides heightened confidentiality to  diagnostic, health condition or health problem related information deemed sensitive.   If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                    "display": "diagnosis information sensitivity",
                                },
                                {
                                    "code": "DRGIS",
                                    "definition": "Policy for handling information related to a drug, which will be afforded heightened confidentiality. Drug information may be deemed sensitive by organizational policy, and require heightened confidentiality.\r\n\n                        \n                           Usage Note: For use within an enterprise that provides heightened confidentiality to drug information deemed sensitive.   If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                    "display": "drug information sensitivity",
                                },
                                {
                                    "code": "EMP",
                                    "definition": "Policy for handling information related to an employee, which will be afforded heightened confidentiality. When a patient is an employee, an enterprise may have a policy that requires heightened confidentiality.  Information deemed sensitive typically includes health information and patient role information including patient status, demographics, next of kin, and location.\r\n\n                        \n                           Usage Note: Policy for handling information related to an employee, which will be afforded heightened confidentiality.  Description:  When a patient is an employee, an enterprise may have a policy that requires heightened confidentiality.  Information deemed sensitive typically includes health information and patient role information including patient status, demographics, next of kin, and location.",
                                    "display": "employee information sensitivity",
                                },
                                {
                                    "code": "PDS",
                                    "definition": "Policy for specially protecting information reported by or about a patient, which is deemed sensitive within the enterprise (i.e., by default regardless of whether the patient requested that the information be deemed sensitive for another reason.) For example information reported by the patient about another person, e.g., a family member, may be deemed sensitive by default. Organizational policy may allow the sensitivity tag to be cleared on patient's request. \r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law in addition to this more generic code.\r\n\n                        For example, VA deems employee information sensitive by default.  Information about a patient who is being stalked or a victim of abuse or violence may be deemed sensitive by default per a provider organization's policies.",
                                    "display": "patient default information sensitivity",
                                },
                                {
                                    "code": "PHY",
                                    "definition": "Policy for handling information about a patient, which a physician or other licensed healthcare provider deems sensitive.  Once tagged by the provider, this may trigger alerts for follow up actions according to organizational policy or jurisdictional law.\r\n\n                        \n                           Usage Note: For use within an enterprise that provides heightened confidentiality to certain types of information designated by a physician as sensitive. If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.\r\n\n                        Use cases in which this code could be used are, e.g.,  in systems that lack the ability to automatically detect sensitive information and must rely on manual tagging; a system that lacks an applicable sensitivity tag, or for ad hoc situations where criticality of the situation requires that the tagging be done immediately by the provider before coding or transcription of consult notes can be completed, e.g., upon detection of a patient with suicidal tendencies or potential for violence.",
                                    "display": "physician requested information sensitivity",
                                },
                                {
                                    "code": "PRS",
                                    "definition": "Policy for specially protecting information reported by or about a patient, which the patient deems sensitive, and the patient requests that collection, access, use, or disclosure of that information be restricted.  For example, a minor patient may request that information about reproductive health not be disclosed to the patient's family or to particular providers and payers.\r\n\n                        \n                           Usage Note: If there is a jurisdictional mandate, then use the applicable ActPrivacyLaw code system, and specify the law rather than or in addition to this more generic code.",
                                    "display": "patient requested information sensitivity",
                                },
                            ],
                            "definition": "A mandate, obligation, requirement, rule, or expectation characterizing the value or importance of a resource and may include its vulnerability. (Based on ISO7498-2:1989. Note: The vulnerability of personally identifiable sensitive information may be based on concerns that the unauthorized disclosure may result in social stigmatization or discrimination.) Description:  Types of Sensitivity policy that apply to Acts or Roles.  A sensitivity policy is adopted by an enterprise or group of enterprises (a 'policy domain') through a formal data use agreement that stipulates the value, importance, and vulnerability of information. A sensitivity code representing a sensitivity policy may be associated with criteria such as categories of information or sets of information identifiers (e.g., a value set of clinical codes or branch in a code system hierarchy).   These criteria may in turn be used for the Policy Decision Point in a Security Engine.  A sensitivity code may be used to set the confidentiality code used on information about Acts and Roles to trigger the security mechanisms required to control how security principals (i.e., a person, a machine, a software application) may act on the information (e.g., collection, access, use, or disclosure). Sensitivity codes are never assigned to the transport or business envelope containing patient specific information being exchanged outside of a policy domain as this would disclose the information intended to be protected by the policy.  When sensitive information is exchanged with others outside of a policy domain, the confidentiality code on the transport or business envelope conveys the receiver's responsibilities and indicates the how the information is to be safeguarded without unauthorized disclosure of the sensitive information.  This ensures that sensitive information is treated by receivers as the sender intends, accomplishing interoperability without point to point negotiations.\r\n\n                        \n                           Usage Note: Sensitivity codes are not useful for interoperability outside of a policy domain because sensitivity policies are typically localized and vary drastically across policy domains even for the same information category because of differing organizational business rules, security policies, and jurisdictional requirements.  For example, an employee's sensitivity code would make little sense for use outside of a policy domain.   'Taboo' would rarely be useful outside of a policy domain unless there are jurisdictional requirements requiring that a provider disclose sensitive information to a patient directly.  Sensitivity codes may be more appropriate in a legacy system's Master Files in order to notify those who access a patient's orders and observations about the sensitivity policies that apply.  Newer systems may have a security engine that uses a sensitivity policy's criteria directly.  The specializable InformationSensitivityPolicy Act.code may be useful in some scenarios if used in combination with a sensitivity identifier and/or Act.title.",
                            "display": "InformationSensitivityPolicy",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "COMPT",
                            "concept": [
                                {
                                    "code": "ACOCOMPT",
                                    "definition": "A group of health care entities, which may include health care providers, care givers, hospitals, facilities, health plans, and other health care constituents who coordinate care for reimbursement based on quality metrics for improving outcomes and lowering costs, and may be authorized to access the consumer's health information because of membership in that group.\r\n\n                        Security Compartment Labels assigned to a consumer's information use in accountable care workflows should be met or exceeded by the Security Compartment attribute claimed by a participant in a an accountable care workflow who is requesting access to that information",
                                    "display": "accountable care organization compartment",
                                },
                                {
                                    "code": "CTCOMPT",
                                    "definition": "Care coordination across participants in a care plan requires sharing of a healthcare consumer's information specific to that workflow.  A care team member should only have access to that information while participating in that workflow or for other authorized uses.\r\n\n                        Security Compartment Labels assigned to a consumer's information use in care coordination workflows should be met or exceeded by the Security Compartment attribute claimed by a participant in a care team member workflow who is requesting access to that information",
                                    "display": "care team compartment",
                                },
                                {
                                    "code": "FMCOMPT",
                                    "definition": "Financial management department members who have access to healthcare consumer information as part of a patient account, billing and claims workflows.\r\n\n                        Security Compartment Labels assigned to consumer information used in these workflows should be met or exceeded by the Security Compartment attribute claimed by a participant in a financial management workflow who is requesting access to that information.",
                                    "display": "financial management compartment",
                                },
                                {
                                    "code": "HRCOMPT",
                                    "definition": "A security category label field value, which indicates that access and use of an IT resource is restricted to members of human resources department or workflow.",
                                    "display": "human resource compartment",
                                },
                                {
                                    "code": "LRCOMPT",
                                    "definition": "Providers and care givers who have an established relationship per criteria determined by policy are considered to have an established care provision relations with a healthcare consumer, and may be authorized to access the consumer's health information because of that relationship.  Providers and care givers should only have access to that information while participating in legitimate relationship workflows or for other authorized uses.\r\n\n                        Security Compartment Labels assigned to a consumer's information use in legitimate relationship workflows should be met or exceeded by the Security Compartment attribute claimed by a participant in a legitimate relationship workflow who is requesting access to that information.",
                                    "display": "legitimate relationship compartment",
                                },
                                {
                                    "code": "PACOMPT",
                                    "definition": "Patient administration members who have access to healthcare consumer information as part of a patient administration workflows.\r\n\n                        Security Compartment Labels assigned to consumer information used in these workflows should be met or exceeded by the Security Compartment attribute claimed by a participant in a patient administration workflow who is requesting access to that information.",
                                    "display": "patient administration compartment",
                                },
                                {
                                    "code": "RESCOMPT",
                                    "definition": "A security category label field value, which indicates that access and use of an IT resource is restricted to members of a research project.",
                                    "display": "research project compartment",
                                },
                                {
                                    "code": "RMGTCOMPT",
                                    "definition": "A security category label field value, which indicates that access and use of an IT resource is restricted to members of records management department or workflow.",
                                    "display": "records management compartment",
                                },
                            ],
                            "definition": "This is the healthcare analog to the US Intelligence Community's concept of a Special Access Program.  Compartment codes may be used in as a field value in an initiator's clearance to indicate permission to access and use an IT Resource with a security label having the same compartment value in security category label field.\r\n\n                        Map: Aligns with ISO 2382-8 definition of Compartment - \"A division of data into isolated blocks with separate security controls for the purpose of reducing risk.\"",
                            "display": "compartment",
                        },
                    ],
                    "definition": "A policy deeming certain information to be private to an individual or organization.\r\n\n                        \n                           Definition: A mandate, obligation, requirement, rule, or expectation relating to privacy.\r\n\n                        \n                           Discussion: ActPrivacyPolicyType codes support the designation of the 1..* policies that are applicable to an Act such as a Consent Directive, a Role such as a VIP Patient, or an Entity such as a patient who is a minor.  1..* ActPrivacyPolicyType values may be associated with an Act or Role to indicate the policies that govern the assignment of an Act or Role confidentialityCode.  Use of multiple ActPrivacyPolicyType values enables fine grain specification of applicable policies, but must be carefully assigned to ensure cogency and avoid creation of conflicting policy mandates.\r\n\n                        \n                           Usage Note: Statutory title may be named in the ActClassPolicy Act Act.title to specify which privacy policy is being referenced.",
                    "display": "ActPrivacyPolicy",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "ActTrustPolicyType",
                    "concept": [
                        {
                            "code": "TRSTACCRD",
                            "definition": "Type of security metadata about the formal declaration by an authority or neutral third party that validates the technical, security, trust, and business practice conformance of Trust Agents to facilitate security, interoperability, and trust among participants within a security domain or trust framework.",
                            "display": "trust accreditation",
                        },
                        {
                            "code": "TRSTAGRE",
                            "definition": "Type of security metadata about privacy and security requirements with which a security domain must comply. [ISO IEC 10181-1]",
                            "display": "trust agreement",
                        },
                        {
                            "code": "TRSTASSUR",
                            "definition": "Type of security metadata about the digital quality or reliability of a trust assertion, activity, capability, information exchange, mechanism, process, or protocol.",
                            "display": "trust assurance",
                        },
                        {
                            "code": "TRSTCERT",
                            "definition": "Type of security metadata about a set of security-relevant data issued by a security authority or trusted third party, together with security information which is used to provide the integrity and data origin authentication services for an IT resource (data, information object, service, or system capability). [Based on ISO IEC 10181-1]",
                            "display": "trust certificate",
                        },
                        {
                            "code": "TRSTFWK",
                            "definition": "Type of security metadata about a complete set of contracts, regulations, or commitments that enable participating actors to rely on certain assertions by other actors to fulfill their information security requirements. [Kantara Initiative]",
                            "display": "trust framework",
                        },
                        {
                            "code": "TRSTMEC",
                            "definition": "Type of security metadata about a security architecture system component that supports enforcement of security policies.",
                            "display": "trust mechanism",
                        },
                    ],
                    "definition": "A mandate, obligation, requirement, rule, or expectation conveyed as security metadata between senders and receivers required to establish the reliability, authenticity, and trustworthiness of their transactions.\r\n\n                        Trust security metadata are observation made about aspects of trust applicable to an IT resource (data, information object, service, or system capability).\r\n\n                        Trust applicable to IT resources is established and maintained in and among security domains, and may be comprised of observations about the domain's trust authority, trust framework, trust policy, trust interaction rules, means for assessing and monitoring adherence to trust policies, mechanisms that enforce trust, and quality and reliability measures of assurance in those mechanisms. [Based on ISO IEC 10181-1 and NIST SP 800-63-2]\r\n\n                        For example, identity proofing , level of assurance, and Trust Framework.",
                    "display": "trust policy",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "COVPOL",
                    "definition": "Description:A mandate, obligation, requirement, rule, or expectation unilaterally imposed on benefit coverage under a policy or program by a sponsor, underwriter or payor on:\r\n\n                        \n                           \n                              The activity of another party\r\n\n                           \n                           \n                              The behavior of another party\r\n\n                           \n                           \n                              The manner in which an act is executed\r\n\n                           \n                        \n                        \n                           Examples:A clinical protocol imposed by a payer to which a provider must adhere in order to be paid for providing the service.  A formulary from which a provider must select prescribed drugs in order for the patient to incur a lower copay.",
                    "display": "benefit policy",
                },
                {
                    "code": "SecurityPolicy",
                    "concept": [
                        {
                            "code": "AUTHPOL",
                            "concept": [
                                {
                                    "code": "ACCESSCONSCHEME",
                                    "definition": 'An access control policy specific to the type of access control scheme, which is used to enforce one or more authorization policies.  \r\n\n                        \n                           Usage Note: Access control schemes are the type of access control policy, which is comprised of access control policy rules concerning the provision of the access control service.\r\n\n                        There are two categories of access control policies, rule-based and identity-based, which are identified in CCITT Rec. X.800 aka ISO 7498-2. Rule-based access control policies are intended to apply to all access requests by any initiator on any target in a security domain. Identity-based access control policies are based on rules specific to an individual initiator, a group of initiators, entities acting on behalf of initiators, or originators acting in a specific role. Context can modify rule-based or identity-based access control policies. Context rules may define the entire policy in effect. Real systems will usually employ a combination of these policy types; if a rule-based policy is used, then an identity-based policy is usually in effect also.\r\n\n                        An access control scheme may be based on access control lists, capabilities, labels, and context or a combination of these.  An access control scheme is a component of an access control mechanism or "service") along with the supporting mechanisms required by that scheme to provide access control decision information (ADI) supplied by the scheme to the access decision facility (ADF also known as a PDP). (Based on ISO/IEC 10181-3:1996)\r\n\n                        \n                           Examples: \n                        \r\n\n                        \n                           Attribute Based Access Control (ABAC)\n                           Discretionary Access Control (DAC)\n                           History Based Access Control (HBAC)\n                           Identity Based Access Control (IBAC)\n                           Mandatory Access Control (MAC)\n                           Organization Based Access Control (OrBAC)\n                           Relationship Based Access Control (RelBac)\n                           Responsibility Based Access Control (RespBAC)\n                           Risk Adaptable Access Control (RAdAC)\n                        >',
                                    "display": "access control scheme",
                                }
                            ],
                            "definition": "Authorisation policies are essentially security policies related to access-control and specify what activities a subject is permitted or forbidden to do, to a set of target objects. They are designed to protect target objects so are interpreted by access control agents or the run-time systems at the target system.\r\n\n                        A positive authorisation policy defines the actions that a subject is permitted to perform on a target. A negative authorisation policy specifies the actions that a subject is forbidden to perform on a target. Positive authorisation policies may also include filters to transform the parameters associated with their actions.  (Based on PONDERS)",
                            "display": "authorization policy",
                        },
                        {
                            "code": "DELEPOL",
                            "definition": "Delegation policies specify which actions subjects are allowed to delegate to others. A delegation policy thus specifies an authorisation to delegate. Subjects must already possess the access rights to be delegated.\r\n\n                        Delegation policies are aimed at subjects delegating rights to servers or third parties to perform actions on their behalf and are not meant to be the means by which security administrators would assign rights to subjects. A negative delegation policy identifies what delegations are forbidden.\r\n\n                        A Delegation policy specifies the authorisation policy from which delegated rights are derived, the grantors, which are the entities which can delegate these access rights, and the grantees, which are the entities to which the access rights can be delegated. There are two types of delegation policy, positive and negative. (Based on PONDERS)",
                            "display": "delegation policy",
                        },
                        {
                            "code": "ObligationPolicy",
                            "concept": [
                                {
                                    "code": "ANONY",
                                    "definition": "Custodian system must remove any information that could result in identifying the information subject.",
                                    "display": "anonymize",
                                },
                                {
                                    "code": "AOD",
                                    "definition": "Custodian system must make available to an information subject upon request an accounting of certain disclosures of the individual????????s protected health information over a period of time.  Policy may dictate that the accounting include information about the information disclosed,  the date of disclosure, the identification of the receiver, the purpose of the disclosure, the time in which the disclosing entity must provide a response and the time period for which accountings of disclosure can be requested.",
                                    "display": "accounting of disclosure",
                                },
                                {
                                    "code": "AUDIT",
                                    "definition": "Custodian system must monitor systems to ensure that all users are authorized to operate on information objects.",
                                    "display": "audit",
                                },
                                {
                                    "code": "AUDTR",
                                    "definition": "Custodian system must monitor and maintain retrievable log for each user and operation on information.",
                                    "display": "audit trail",
                                },
                                {
                                    "code": "CPLYCC",
                                    "definition": "Custodian security system must retrieve, evaluate, and comply with the information handling directions of the Confidentiality Code associated with an information target.",
                                    "display": "comply with confidentiality code",
                                },
                                {
                                    "code": "CPLYCD",
                                    "definition": "Custodian security system must retrieve, evaluate, and comply with applicable information subject consent directives.",
                                    "display": "comply with consent directive",
                                },
                                {
                                    "code": "CPLYJPP",
                                    "definition": "Custodian security system must retrieve, evaluate, and comply with applicable jurisdictional privacy policies associated with the target information.",
                                    "display": "comply with jurisdictional privacy policy",
                                },
                                {
                                    "code": "CPLYOPP",
                                    "definition": "Custodian security system must retrieve, evaluate, and comply with applicable organizational privacy policies associated with the target information.",
                                    "display": "comply with organizational privacy policy",
                                },
                                {
                                    "code": "CPLYOSP",
                                    "definition": "Custodian security system must retrieve, evaluate, and comply with the organizational security policies associated with the target information.",
                                    "display": "comply with organizational security policy",
                                },
                                {
                                    "code": "CPLYPOL",
                                    "definition": "Custodian security system must retrieve, evaluate, and comply with applicable policies associated with the target information.",
                                    "display": "comply with policy",
                                },
                                {
                                    "code": "DECLASSIFYLABEL",
                                    "definition": "Custodian security system must declassify information assigned security labels by instantiating a new version of the classified information so as to break the binding of the classifying security label when assigning a new security label that marks the information as unclassified in accordance with applicable jurisdictional privacy policies associated with the target information. The system must retain an immutable record of the previous assignment and binding.",
                                    "display": "declassify security label",
                                },
                                {
                                    "code": "DEID",
                                    "definition": "Custodian system must strip information of data that would allow the identification of the source of the information or the information subject.",
                                    "display": "deidentify",
                                },
                                {
                                    "code": "DELAU",
                                    "definition": "Custodian system must remove target information from access after use.",
                                    "display": "delete after use",
                                },
                                {
                                    "code": "DOWNGRDLABEL",
                                    "definition": "Custodian security system must downgrade information assigned security labels by instantiating a new version of the classified information so as to break the binding of the classifying security label when assigning a new security label that marks the information as classified at a less protected level in accordance with applicable jurisdictional privacy policies associated with the target information. The system must retain an immutable record of the previous assignment and binding.",
                                    "display": "downgrade security label",
                                },
                                {
                                    "code": "DRIVLABEL",
                                    "definition": "Custodian security system must assign and bind security labels derived from compilations of information by aggregation or disaggregation in order to classify information compiled in the information systems under its control for collection, access, use and disclosure in accordance with applicable jurisdictional privacy policies associated with the target information. The system must retain an immutable record of the previous assignment and binding.",
                                    "display": "derive security label",
                                },
                                {
                                    "code": "ENCRYPT",
                                    "concept": [
                                        {
                                            "code": "ENCRYPTR",
                                            "definition": 'Custodian system must render information unreadable and unusable by algorithmically transforming plaintext into ciphertext when "at rest" or in storage.',
                                            "display": "encrypt at rest",
                                        },
                                        {
                                            "code": "ENCRYPTT",
                                            "definition": 'Custodian system must render information unreadable and unusable by algorithmically transforming plaintext into ciphertext while "in transit" or being transported by any means.',
                                            "display": "encrypt in transit",
                                        },
                                        {
                                            "code": "ENCRYPTU",
                                            "definition": "Custodian system must render information unreadable and unusable by algorithmically transforming plaintext into ciphertext while in use such that operations permitted on the target information are limited by the license granted to the end user.",
                                            "display": "encrypt in use",
                                        },
                                    ],
                                    "definition": "Custodian system must render information unreadable by algorithmically transforming plaintext into ciphertext.  \r\n\n                        \r\n\n                        \n                           Usage Notes: A mathematical transposition of a file or data stream so that it cannot be deciphered at the receiving end without the proper key. Encryption is a security feature that assures that only the parties who are supposed to be participating in a videoconference or data transfer are able to do so. It can include a password, public and private keys, or a complex combination of all.  (Per Infoway.)",
                                    "display": "encrypt",
                                },
                                {
                                    "code": "HUAPRV",
                                    "definition": "Custodian system must require human review and approval for permission requested.",
                                    "display": "human approval",
                                },
                                {
                                    "code": "LABEL",
                                    "definition": "Custodian security system must assign and bind security labels in order to classify information created in the information systems under its control for collection, access, use and disclosure in accordance with applicable jurisdictional privacy policies associated with the target information. The system must retain an immutable record of the assignment and binding.\r\n\n                        \n                           Usage Note: In security systems, security policy label assignments do not change, they may supersede prior assignments, and such reassignments are always tracked for auditing and other purposes.",
                                    "display": "assign security label",
                                },
                                {
                                    "code": "MASK",
                                    "definition": 'Custodian system must render information unreadable and unusable by algorithmically transforming plaintext into ciphertext.  User may be provided a key to decrypt per license or "shared secret".',
                                    "display": "mask",
                                },
                                {
                                    "code": "MINEC",
                                    "definition": 'Custodian must limit access and disclosure to the minimum information required to support an authorized user\'s purpose of use.  \r\n\n                        \n                           Usage Note: Limiting the information available for access and disclosure to that an authorized user or receiver "needs to know" in order to perform permitted workflow or purpose of use.',
                                    "display": "minimum necessary",
                                },
                                {
                                    "code": "PERSISTLABEL",
                                    "definition": "Custodian security system must persist the binding of security labels to classify information received or imported by information systems under its control for collection, access, use and disclosure in accordance with applicable jurisdictional privacy policies associated with the target information.  The system must retain an immutable record of the assignment and binding.",
                                    "display": "persist security label",
                                },
                                {
                                    "code": "PRIVMARK",
                                    "definition": 'Custodian must create and/or maintain human readable security label tags as required by policy.\r\n\n                        Map:  Aligns with ISO 22600-3 Section A.3.4.3 description of privacy mark:  "If present, the privacy-mark is not used for access control. The content of the privacy-mark may be defined by the security policy in force (identified by the security-policy-identifier) which may define a list of values to be used. Alternately, the value may be determined by the originator of the security-label."',
                                    "display": "privacy mark",
                                },
                                {
                                    "code": "PSEUD",
                                    "definition": "Custodian system must strip information of data that would allow the identification of the source of the information or the information subject.  Custodian may retain a key to relink data necessary to reidentify the information subject.",
                                    "display": "pseudonymize",
                                },
                                {
                                    "code": "REDACT",
                                    "definition": "Custodian system must remove information, which is not authorized to be access, used, or disclosed from records made available to otherwise authorized users.",
                                    "display": "redact",
                                },
                                {
                                    "code": "UPGRDLABEL",
                                    "definition": "Custodian security system must declassify information assigned security labels by instantiating a new version of the classified information so as to break the binding of the classifying security label when assigning a new security label that marks the information as classified at a more protected level  in accordance with applicable jurisdictional privacy policies associated with the target information. The system must retain an immutable record of the previous assignment and binding.",
                                    "display": "upgrade security label",
                                },
                            ],
                            "definition": "Conveys the mandated workflow action that an information custodian, receiver, or user must perform.  \r\n\n                        \n                           Usage Notes: Per ISO 22600-2, ObligationPolicy instances 'are event-triggered and define actions to be performed by manager agent'. Per HL7 Composite Security and Privacy Domain Analysis Model:  This value set refers to the action required to receive the permission specified in the privacy rule. Per OASIS XACML, an obligation is an operation specified in a policy or policy that is performed in conjunction with the enforcement of an access control decision.",
                            "display": "obligation policy",
                        },
                        {
                            "code": "RefrainPolicy",
                            "concept": [
                                {
                                    "code": "NOAUTH",
                                    "definition": "Prohibition on disclosure without information subject's authorization.",
                                    "display": "no disclosure without subject authorization",
                                },
                                {
                                    "code": "NOCOLLECT",
                                    "definition": "Prohibition on collection or storage of the information.",
                                    "display": "no collection",
                                },
                                {
                                    "code": "NODSCLCD",
                                    "definition": "Prohibition on disclosure without organizational approved patient restriction.",
                                    "display": "no disclosure without consent directive",
                                },
                                {
                                    "code": "NODSCLCDS",
                                    "definition": "Prohibition on disclosure without a consent directive from the information subject.",
                                    "display": "no disclosure without information subject's consent directive",
                                },
                                {
                                    "code": "NOINTEGRATE",
                                    "definition": "Prohibition on Integration into other records.",
                                    "display": "no integration",
                                },
                                {
                                    "code": "NOLIST",
                                    "definition": "Prohibition on disclosure except to entities on specific access list.",
                                    "display": "no unlisted entity disclosure",
                                },
                                {
                                    "code": "NOMOU",
                                    "definition": "Prohibition on disclosure without an interagency service agreement or memorandum of understanding (MOU).",
                                    "display": "no disclosure without MOU",
                                },
                                {
                                    "code": "NOORGPOL",
                                    "definition": "Prohibition on disclosure without organizational authorization.",
                                    "display": "no disclosure without organizational authorization",
                                },
                                {
                                    "code": "NOPAT",
                                    "definition": 'Prohibition on disclosing information to patient, family or caregivers without attending provider\'s authorization.\r\n\n                        \n                           Usage Note: The information may be labeled with the ActInformationSensitivity TBOO code, triggering application of this RefrainPolicy code as a handling caveat controlling access.\r\n\n                        Maps to FHIR NOPAT: Typically, this is used on an Alert resource, when the alert records information on patient abuse or non-compliance.\r\n\n                        FHIR print name is "keep information from patient". Maps to the French realm - code: INVISIBLE_PATIENT.\r\n\n                        \n                           displayName: Document non visible par le patient\n                           codingScheme: 1.2.250.1.213.1.1.4.13\n                        \n                        French use case:  A label for documents that the author  chose to hide from the patient until the content can be disclose to the patient in a face to face meeting between a healthcare professional and the patient (in French law some results like cancer diagnosis or AIDS diagnosis must be announced to the patient by a healthcare professional and should not be find out by the patient alone).',
                                    "display": "no disclosure to patient, family or caregivers without attending provider's authorization",
                                },
                                {
                                    "code": "NOPERSISTP",
                                    "definition": "Prohibition on collection of the information beyond time necessary to accomplish authorized purpose of use is prohibited.",
                                    "display": "no collection beyond purpose of use",
                                },
                                {
                                    "code": "NORDSCLCD",
                                    "definition": "Prohibition on redisclosure without patient consent directive.",
                                    "display": "no redisclosure without consent directive",
                                },
                                {
                                    "code": "NORDSCLCDS",
                                    "definition": "Prohibition on redisclosure without a consent directive from the information subject.",
                                    "display": "no redisclosure without information subject's consent directive",
                                },
                                {
                                    "code": "NORDSCLW",
                                    "definition": "Prohibition on disclosure without authorization under jurisdictional law.",
                                    "display": "no disclosure without jurisdictional authorization",
                                },
                                {
                                    "code": "NORELINK",
                                    "definition": "Prohibition on associating de-identified or pseudonymized information with other information in a manner that could or does result in disclosing information intended to be masked.",
                                    "display": "no relinking",
                                },
                                {
                                    "code": "NOREUSE",
                                    "definition": "Prohibition on use of the information beyond the purpose of use initially authorized.",
                                    "display": "no reuse beyond purpose of use",
                                },
                                {
                                    "code": "NOVIP",
                                    "definition": "Prohibition on disclosure except to principals with access permission to specific VIP information.",
                                    "display": "no unauthorized VIP disclosure",
                                },
                                {
                                    "code": "ORCON",
                                    "definition": "Prohibition on disclosure except as permitted by the information originator.",
                                    "display": "no disclosure without originator authorization",
                                },
                            ],
                            "definition": 'Conveys prohibited actions which an information custodian, receiver, or user is not permitted to perform unless otherwise authorized or permitted under specified circumstances.\r\n\n                        \r\n\n                        \n                           Usage Notes: ISO 22600-2 species that a Refrain Policy "defines actions the subjects must refrain from performing".  Per HL7 Composite Security and Privacy Domain Analysis Model:  May be used to indicate that a specific action is prohibited based on specific access control attributes e.g., purpose of use, information type, user role, etc.',
                            "display": "refrain policy",
                        },
                    ],
                    "definition": "Types of security policies that further specify the ActClassPolicy value set.\r\n\n                        \n                           Examples:\n                        \r\n\n                        \n                           obligation to encrypt\n                           refrain from redisclosure without consent",
                    "display": "security policy",
                },
            ],
            "definition": "Description:Types of policies that further specify the ActClassPolicy value set.",
            "display": "ActPolicyType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActPolicyType

    Description:Types of policies that further specify the ActClassPolicy value set.
    """

    underscore_act_product_acquisition_code = CodeSystemConcept(
        {
            "code": "_ActProductAcquisitionCode",
            "concept": [
                {
                    "code": "LOAN",
                    "concept": [
                        {
                            "code": "RENT",
                            "definition": "Temporary supply of a product with financial compensation, without transfer of ownership for the product.",
                            "display": "Rent",
                        }
                    ],
                    "definition": "Temporary supply of a product without transfer of ownership for the product.",
                    "display": "Loan",
                },
                {
                    "code": "TRANSFER",
                    "concept": [
                        {
                            "code": "SALE",
                            "definition": "Transfer of ownership for a product for financial compensation.",
                            "display": "Sale",
                        }
                    ],
                    "definition": "Transfer of ownership for a product.",
                    "display": "Transfer",
                },
            ],
            "definition": "The method that a product is obtained for use by the subject of the supply act (e.g. patient).  Product examples are consumable or durable goods.",
            "display": "ActProductAcquisitionCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActProductAcquisitionCode

    The method that a product is obtained for use by the subject of the supply act (e.g. patient).  Product examples are consumable or durable goods.
    """

    underscore_act_specimen_transport_code = CodeSystemConcept(
        {
            "code": "_ActSpecimenTransportCode",
            "concept": [
                {
                    "code": "SREC",
                    "definition": "Description:Specimen has been received by the participating organization/department.",
                    "display": "specimen received",
                },
                {
                    "code": "SSTOR",
                    "definition": "Description:Specimen has been placed into storage at a participating location.",
                    "display": "specimen in storage",
                },
                {
                    "code": "STRAN",
                    "definition": "Description:Specimen has been put in transit to a participating receiver.",
                    "display": "specimen in transit",
                },
            ],
            "definition": "Transportation of a specimen.",
            "display": "ActSpecimenTransportCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActSpecimenTransportCode

    Transportation of a specimen.
    """

    underscore_act_specimen_treatment_code = CodeSystemConcept(
        {
            "code": "_ActSpecimenTreatmentCode",
            "concept": [
                {
                    "code": "ACID",
                    "definition": "The lowering of specimen pH through the addition of an acid",
                    "display": "Acidification",
                },
                {
                    "code": "ALK",
                    "definition": "The act rendering alkaline by impregnating with an alkali; a conferring of alkaline qualities.",
                    "display": "Alkalization",
                },
                {
                    "code": "DEFB",
                    "definition": "The removal of fibrin from whole blood or plasma through physical or chemical means",
                    "display": "Defibrination",
                },
                {
                    "code": "FILT",
                    "definition": "The passage of a liquid through a filter, accomplished by gravity, pressure or vacuum (suction).",
                    "display": "Filtration",
                },
                {
                    "code": "LDLP",
                    "definition": "LDL Precipitation",
                    "display": "LDL Precipitation",
                },
                {
                    "code": "NEUT",
                    "definition": "The act or process by which an acid and a base are combined in such proportions that the resulting compound is neutral.",
                    "display": "Neutralization",
                },
                {
                    "code": "RECA",
                    "definition": "The addition of calcium back to a specimen after it was removed by chelating agents",
                    "display": "Recalcification",
                },
                {
                    "code": "UFIL",
                    "definition": "The filtration of a colloidal substance through a semipermeable medium that allows only the passage of small molecules.",
                    "display": "Ultrafiltration",
                },
            ],
            "definition": "Set of codes related to specimen treatments",
            "display": "ActSpecimenTreatmentCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActSpecimenTreatmentCode

    Set of codes related to specimen treatments
    """

    underscore_act_substance_administration_code = CodeSystemConcept(
        {
            "code": "_ActSubstanceAdministrationCode",
            "concept": [
                {
                    "code": "DRUG",
                    "definition": "The introduction of a drug into a subject with the intention of altering its biologic state with the intent of improving its health status.",
                    "display": "Drug therapy",
                },
                {
                    "code": "FD",
                    "definition": "Description: The introduction of material into a subject with the intent of providing nutrition or other dietary supplements (e.g. minerals or vitamins).",
                    "display": "food",
                },
                {
                    "code": "IMMUNIZ",
                    "concept": [
                        {
                            "code": "BOOSTER",
                            "definition": "An additional immunization administration within a series intended to bolster or enhance immunity.",
                            "display": "Booster Immunization",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                        {
                            "code": "INITIMMUNIZ",
                            "definition": "The first immunization administration in a series intended to produce immunity",
                            "display": "Initial Immunization",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                    ],
                    "definition": "The introduction of an immunogen with the intent of stimulating an immune response, aimed at preventing subsequent infections by more viable agents.",
                    "display": "Immunization",
                },
            ],
            "definition": "Description: Describes the type of substance administration being performed.  This should not be used to carry codes for identification of products.  Use an associated role or entity to carry such information.",
            "display": "ActSubstanceAdministrationCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActSubstanceAdministrationCode

    Description: Describes the type of substance administration being performed.  This should not be used to carry codes for identification of products.  Use an associated role or entity to carry such information.
    """

    underscore_act_task_code = CodeSystemConcept(
        {
            "code": "_ActTaskCode",
            "concept": [
                {
                    "code": "OE",
                    "concept": [
                        {
                            "code": "LABOE",
                            "definition": "A clinician creates a request for a laboratory test to be done for a given patient.",
                            "display": "laboratory test order entry task",
                        },
                        {
                            "code": "MEDOE",
                            "definition": "A clinician creates a request for the administration of one or more medications to a given patient.",
                            "display": "medication order entry task",
                        },
                    ],
                    "definition": "A clinician creates a request for a service to be performed for a given patient.",
                    "display": "order entry task",
                },
                {
                    "code": "PATDOC",
                    "concept": [
                        {
                            "code": "ALLERLREV",
                            "definition": "Description: A person reviews a list of known allergies of a given patient.",
                            "display": "allergy list review",
                        },
                        {
                            "code": "CLINNOTEE",
                            "concept": [
                                {
                                    "code": "DIAGLISTE",
                                    "definition": "A clinician enters a diagnosis for a given patient.",
                                    "display": "diagnosis list entry task",
                                },
                                {
                                    "code": "DISCHINSTE",
                                    "definition": "A person provides a discharge instruction to a patient.",
                                    "display": "discharge instruction entry",
                                },
                                {
                                    "code": "DISCHSUME",
                                    "definition": "A clinician enters a discharge summary for a given patient.",
                                    "display": "discharge summary entry task",
                                },
                                {
                                    "code": "PATEDUE",
                                    "definition": "A person provides a patient-specific education handout to a patient.",
                                    "display": "patient education entry",
                                },
                                {
                                    "code": "PATREPE",
                                    "definition": "A pathologist enters a report for a given patient.",
                                    "display": "pathology report entry task",
                                },
                                {
                                    "code": "PROBLISTE",
                                    "definition": "A clinician enters a problem for a given patient.",
                                    "display": "problem list entry task",
                                },
                                {
                                    "code": "RADREPE",
                                    "definition": "A radiologist enters a report for a given patient.",
                                    "display": "radiology report entry task",
                                },
                            ],
                            "definition": "A clinician enters a clinical note about a given patient",
                            "display": "clinical note entry task",
                        },
                        {
                            "code": "IMMLREV",
                            "definition": "Description: A person reviews a list of immunizations due or received for a given patient.",
                            "display": "immunization list review",
                        },
                        {
                            "code": "REMLREV",
                            "concept": [
                                {
                                    "code": "WELLREMLREV",
                                    "definition": "Description: A person reviews a list of wellness or preventive care reminders for a given patient.",
                                    "display": "wellness reminder list review",
                                }
                            ],
                            "definition": "Description: A person reviews a list of health care reminders for a given patient.",
                            "display": "reminder list review",
                        },
                    ],
                    "definition": "A person enters documentation about a given patient.",
                    "display": "patient documentation task",
                },
                {
                    "code": "PATINFO",
                    "concept": [
                        {
                            "code": "ALLERLE",
                            "definition": "Description: A person enters a known allergy for a given patient.",
                            "display": "allergy list entry",
                        },
                        {
                            "code": "CDSREV",
                            "definition": "A person reviews a recommendation/assessment provided automatically by a clinical decision support application for a given patient.",
                            "display": "clinical decision support intervention review",
                        },
                        {
                            "code": "CLINNOTEREV",
                            "concept": [
                                {
                                    "code": "DISCHSUMREV",
                                    "definition": "A person reviews a discharge summary of a given patient.",
                                    "display": "discharge summary review task",
                                }
                            ],
                            "definition": "A person reviews a clinical note of a given patient.",
                            "display": "clinical note review task",
                        },
                        {
                            "code": "DIAGLISTREV",
                            "definition": "A person reviews a list of diagnoses of a given patient.",
                            "display": "diagnosis list review task",
                        },
                        {
                            "code": "IMMLE",
                            "definition": "Description: A person enters an immunization due or received for a given patient.",
                            "display": "immunization list entry",
                        },
                        {
                            "code": "LABRREV",
                            "definition": "A person reviews a list of laboratory results of a given patient.",
                            "display": "laboratory results review task",
                        },
                        {
                            "code": "MICRORREV",
                            "concept": [
                                {
                                    "code": "MICROORGRREV",
                                    "definition": "A person reviews organisms of microbiology results of a given patient.",
                                    "display": "microbiology organisms results review task",
                                },
                                {
                                    "code": "MICROSENSRREV",
                                    "definition": "A person reviews the sensitivity test of microbiology results of a given patient.",
                                    "display": "microbiology sensitivity test results review task",
                                },
                            ],
                            "definition": "A person reviews a list of microbiology results of a given patient.",
                            "display": "microbiology results review task",
                        },
                        {
                            "code": "MLREV",
                            "concept": [
                                {
                                    "code": "MARWLREV",
                                    "definition": "A clinician reviews a work list of medications to be administered to a given patient.",
                                    "display": "medication administration record work list review task",
                                }
                            ],
                            "definition": "A person reviews a list of medication orders submitted to a given patient",
                            "display": "medication list review task",
                        },
                        {
                            "code": "OREV",
                            "definition": "A person reviews a list of orders submitted to a given patient.",
                            "display": "orders review task",
                        },
                        {
                            "code": "PATREPREV",
                            "definition": "A person reviews a pathology report of a given patient.",
                            "display": "pathology report review task",
                        },
                        {
                            "code": "PROBLISTREV",
                            "definition": "A person reviews a list of problems of a given patient.",
                            "display": "problem list review task",
                        },
                        {
                            "code": "RADREPREV",
                            "definition": "A person reviews a radiology report of a given patient.",
                            "display": "radiology report review task",
                        },
                        {
                            "code": "REMLE",
                            "concept": [
                                {
                                    "code": "WELLREMLE",
                                    "definition": "Description: A person enters a wellness or preventive care reminder for a given patient.",
                                    "display": "wellness reminder list entry",
                                }
                            ],
                            "definition": "Description: A person enters a health care reminder for a given patient.",
                            "display": "reminder list entry",
                        },
                        {
                            "code": "RISKASSESS",
                            "concept": [
                                {
                                    "code": "FALLRISK",
                                    "definition": "A person reviews a Falls Risk Assessment Instrument report of a given patient.",
                                    "display": "falls risk assessment instrument task",
                                }
                            ],
                            "definition": "A person reviews a Risk Assessment Instrument report of a given patient.",
                            "display": "risk assessment instrument task",
                        },
                    ],
                    "definition": "A person (e.g., clinician, the patient herself) reviews patient information in the electronic medical record.",
                    "display": "patient information review task",
                },
            ],
            "definition": "Description: A task or action that a user may perform in a clinical information system (e.g., medication order entry, laboratory test results review, problem list entry).",
            "display": "ActTaskCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActTaskCode

    Description: A task or action that a user may perform in a clinical information system (e.g., medication order entry, laboratory test results review, problem list entry).
    """

    underscore_act_transportation_mode_code = CodeSystemConcept(
        {
            "code": "_ActTransportationModeCode",
            "concept": [
                {
                    "code": "_ActPatientTransportationModeCode",
                    "concept": [
                        {
                            "code": "AFOOT",
                            "definition": "pedestrian transport",
                            "display": "pedestrian transport",
                        },
                        {
                            "code": "AMBT",
                            "concept": [
                                {
                                    "code": "AMBAIR",
                                    "definition": "fixed-wing ambulance transport",
                                    "display": "fixed-wing ambulance transport",
                                },
                                {
                                    "code": "AMBGRND",
                                    "definition": "ground ambulance transport",
                                    "display": "ground ambulance transport",
                                },
                                {
                                    "code": "AMBHELO",
                                    "definition": "helicopter ambulance transport",
                                    "display": "helicopter ambulance transport",
                                },
                            ],
                            "definition": "ambulance transport",
                            "display": "ambulance transport",
                        },
                        {
                            "code": "LAWENF",
                            "definition": "law enforcement transport",
                            "display": "law enforcement transport",
                        },
                        {
                            "code": "PRVTRN",
                            "definition": "private transport",
                            "display": "private transport",
                        },
                        {
                            "code": "PUBTRN",
                            "definition": "public transport",
                            "display": "public transport",
                        },
                    ],
                    "definition": "Definition: Characterizes how a patient was or will be transported to the site of a patient encounter.\r\n\n                        \n                           Examples: Via ambulance, via public transit, on foot.",
                    "display": "ActPatientTransportationModeCode",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                }
            ],
            "definition": "Characterizes how a transportation act was or will be carried out.\r\n\n                        \n                           Examples: Via private transport, via public transit, via courier.",
            "display": "ActTransportationModeCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActTransportationModeCode

    Characterizes how a transportation act was or will be carried out.


                           Examples: Via private transport, via public transit, via courier.
    """

    underscore_observation_type = CodeSystemConcept(
        {
            "code": "_ObservationType",
            "concept": [
                {
                    "code": "_ActSpecObsCode",
                    "concept": [
                        {
                            "code": "ARTBLD",
                            "definition": "Describes the artificial blood identifier that is associated with the specimen.",
                            "display": "ActSpecObsArtBldCode",
                        },
                        {
                            "code": "DILUTION",
                            "concept": [
                                {
                                    "code": "AUTO-HIGH",
                                    "definition": "The dilution of a sample performed by automated equipment.  The value is specified by the equipment",
                                    "display": "Auto-High Dilution",
                                },
                                {
                                    "code": "AUTO-LOW",
                                    "definition": "The dilution of a sample performed by automated equipment.  The value is specified by the equipment",
                                    "display": "Auto-Low Dilution",
                                },
                                {
                                    "code": "PRE",
                                    "definition": "The dilution of the specimen made prior to being loaded onto analytical equipment",
                                    "display": "Pre-Dilution",
                                },
                                {
                                    "code": "RERUN",
                                    "definition": "The value of the dilution of a sample after it had been analyzed at a prior dilution value",
                                    "display": "Rerun Dilution",
                                },
                            ],
                            "definition": "An observation that reports the dilution of a sample.",
                            "display": "ActSpecObsDilutionCode",
                        },
                        {
                            "code": "EVNFCTS",
                            "definition": "Domain provides codes that qualify the ActLabObsEnvfctsCode domain. (Environmental Factors)",
                            "display": "ActSpecObsEvntfctsCode",
                        },
                        {
                            "code": "INTFR",
                            "concept": [
                                {
                                    "code": "FIBRIN",
                                    "definition": "The Fibrin Index of the specimen. In the case of only differentiating between Absent and Present, recommend using 0 and 1",
                                    "display": "Fibrin",
                                },
                                {
                                    "code": "HEMOLYSIS",
                                    "definition": "An observation of the hemolysis index of the specimen in g/L",
                                    "display": "Hemolysis",
                                },
                                {
                                    "code": "ICTERUS",
                                    "definition": "An observation that describes the icterus index of the specimen.  It is recommended to use mMol/L of bilirubin",
                                    "display": "Icterus",
                                },
                                {
                                    "code": "LIPEMIA",
                                    "definition": "An observation used to describe the Lipemia Index of the specimen. It is recommended to use the optical turbidity at 600 nm (in absorbance units).",
                                    "display": "Lipemia",
                                },
                            ],
                            "definition": "An observation that relates to factors that may potentially cause interference with the observation",
                            "display": "ActSpecObsInterferenceCode",
                        },
                        {
                            "code": "VOLUME",
                            "concept": [
                                {
                                    "code": "AVAILABLE",
                                    "definition": "The available quantity of specimen.   This is the current quantity minus any planned consumption (e.g., tests that are planned)",
                                    "display": "Available Volume",
                                },
                                {
                                    "code": "CONSUMPTION",
                                    "definition": "The quantity of specimen that is used each time the equipment uses this substance",
                                    "display": "Consumption Volume",
                                },
                                {
                                    "code": "CURRENT",
                                    "definition": "The current quantity of the specimen, i.e., initial quantity minus what has been actually used.",
                                    "display": "Current Volume",
                                },
                                {
                                    "code": "INITIAL",
                                    "definition": "The initial quantity of the specimen in inventory",
                                    "display": "Initial Volume",
                                },
                            ],
                            "definition": "An observation that reports the volume of a sample.",
                            "display": "ActSpecObsVolumeCode",
                        },
                    ],
                    "definition": "Identifies the type of observation that is made about a specimen that may affect its processing, analysis or further result interpretation",
                    "display": "ActSpecObsCode",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_AnnotationType",
                    "concept": [
                        {
                            "code": "_ActPatientAnnotationType",
                            "concept": [
                                {
                                    "code": "ANNDI",
                                    "definition": "Description:A note that is specific to a patient's diagnostic images, either historical, current or planned.",
                                    "display": "diagnostic image note",
                                },
                                {
                                    "code": "ANNGEN",
                                    "definition": "Description:A general or uncategorized note.",
                                    "display": "general note",
                                },
                                {
                                    "code": "ANNIMM",
                                    "definition": "A note that is specific to a patient's immunizations, either historical, current or planned.",
                                    "display": "immunization note",
                                },
                                {
                                    "code": "ANNLAB",
                                    "definition": "Description:A note that is specific to a patient's laboratory results, either historical, current or planned.",
                                    "display": "laboratory note",
                                },
                                {
                                    "code": "ANNMED",
                                    "definition": "Description:A note that is specific to a patient's medications, either historical, current or planned.",
                                    "display": "medication note",
                                },
                            ],
                            "definition": "Description:Provides a categorization for annotations recorded directly against the patient .",
                            "display": "ActPatientAnnotationType",
                        }
                    ],
                    "definition": "AnnotationType",
                    "display": "AnnotationType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_GeneticObservationType",
                    "concept": [
                        {
                            "code": "GENE",
                            "definition": "Description: A DNA segment that contributes to phenotype/function. In the absence of demonstrated function a gene may be characterized by sequence, transcription or homology",
                            "display": "gene",
                        }
                    ],
                    "definition": "Description: None provided",
                    "display": "GeneticObservationType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_ImmunizationObservationType",
                    "concept": [
                        {
                            "code": "OBSANTC",
                            "definition": "Description: Indicates the valid antigen count.",
                            "display": "antigen count",
                        },
                        {
                            "code": "OBSANTV",
                            "definition": "Description: Indicates whether an antigen is valid or invalid.",
                            "display": "antigen validity",
                        },
                    ],
                    "definition": "Description: Observation codes which describe characteristics of the immunization material.",
                    "display": "ImmunizationObservationType",
                },
                {
                    "code": "_IndividualCaseSafetyReportType",
                    "concept": [
                        {
                            "code": "PAT_ADV_EVNT",
                            "definition": "Indicates that the ICSR is describing problems that a patient experienced after receiving a vaccine product.",
                            "display": "patient adverse event",
                        },
                        {
                            "code": "VAC_PROBLEM",
                            "definition": "Indicates that the ICSR is describing a problem with the actual vaccine product such as physical defects (cloudy, particulate matter) or inability to confer immunity.",
                            "display": "vaccine product problem",
                        },
                    ],
                    "definition": "A code that is used to indicate the type of case safety report received from sender. The current code example reference is from the International Conference on Harmonisation (ICH) Expert Workgroup guideline on Clinical Safety Data Management: Data Elements for Transmission of Individual Case Safety Reports. The unknown/unavailable option allows the transmission of information from a secondary sender where the initial sender did not specify the type of report.\r\n\n                        Example concepts include: Spontaneous, Report from study, Other.",
                    "display": "Individual Case Safety Report Type",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_LOINCObservationActContextAgeType",
                    "concept": [
                        {
                            "code": "21611-9",
                            "definition": "Definition:Estimated age.",
                            "display": "age patient qn est",
                        },
                        {
                            "code": "21612-7",
                            "definition": "Definition:Reported age.",
                            "display": "age patient qn reported",
                        },
                        {
                            "code": "29553-5",
                            "definition": "Definition:Calculated age.",
                            "display": "age patient qn calc",
                        },
                        {
                            "code": "30525-0",
                            "definition": "Definition:General specification of age with no implied method of determination.",
                            "display": "age patient qn definition",
                        },
                        {
                            "code": "30972-4",
                            "definition": "Definition:Age at onset of associated adverse event; no implied method of determination.",
                            "display": "age at onset of adverse event",
                        },
                    ],
                    "definition": "Definition:The set of LOINC codes for the act of determining the period of time that has elapsed since an entity was born or created.",
                    "display": "LOINCObservationActContextAgeType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_MedicationObservationType",
                    "concept": [
                        {
                            "code": "REP_HALF_LIFE",
                            "definition": "Description:This observation represents an 'average' or 'expected' half-life typical of the product.",
                            "display": "representative half-life",
                        },
                        {
                            "code": "SPLCOATING",
                            "definition": "Definition: A characteristic of an oral solid dosage form of a medicinal product, indicating whether it has one or more coatings such as sugar coating, film coating, or enteric coating.  Only coatings to the external surface or the dosage form should be considered (for example, coatings to individual pellets or granules inside a capsule or tablet are excluded from consideration).\r\n\n                        \n                           Constraints: The Observation.value must be a Boolean (BL) with true for the presence or false for the absence of one or more coatings on a solid dosage form.",
                            "display": "coating",
                        },
                        {
                            "code": "SPLCOLOR",
                            "definition": "Definition:  A characteristic of an oral solid dosage form of a medicinal product, specifying the color or colors that most predominantly define the appearance of the dose form. SPLCOLOR is not an FDA specification for the actual color of solid dosage forms or the names of colors that can appear in labeling.\r\n\n                        \n                           Constraints: The Observation.value must be a single coded value or a list of multiple coded values, specifying one or more distinct colors that approximate of the color(s) of distinct areas of the solid dosage form, such as the different sides of a tablet or one-part capsule, or the different halves of a two-part capsule.  Bands on banded capsules, regardless of the color, are not considered when assigning an SPLCOLOR. Imprints on the dosage form, regardless of their color are not considered when assigning an SPLCOLOR. If more than one color exists on a particular side or half, then the most predominant color on that side or half is recorded.  If the gelatin capsule shell is colorless and transparent, use the predominant color of the contents that appears through the colorless and transparent capsule shell. Colors can include: Black;Gray;White;Red;Pink;Purple;Green;Yellow;Orange;Brown;Blue;Turquoise.",
                            "display": "color",
                        },
                        {
                            "code": "SPLIMAGE",
                            "definition": "Description: A characteristic representing a single file reference that contains two or more views of the same dosage form of the product; in most cases this should represent front and back views of the dosage form, but occasionally additional views might be needed in order to capture all of the important physical characteristics of the dosage form.  Any imprint and/or symbol should be clearly identifiable, and the viewer should not normally need to rotate the image in order to read it.  Images that are submitted with SPL should be included in the same directory as the SPL file.",
                            "display": "image",
                        },
                        {
                            "code": "SPLIMPRINT",
                            "definition": "Definition:  A characteristic of an oral solid dosage form of a medicinal product, specifying the alphanumeric text that appears on the solid dosage form, including text that is embossed, debossed, engraved or printed with ink. The presence of other non-textual distinguishing marks or symbols is recorded by SPLSYMBOL.\r\n\n                        \n                           Examples: Included in SPLIMPRINT are alphanumeric text that appears on the bands of banded capsules and logos and other symbols that can be interpreted as letters or numbers.\r\n\n                        \n                           Constraints: The Observation.value must be of type Character String (ST). Excluded from SPLIMPRINT are internal and external cut-outs in the form of alphanumeric text and the letter 'R' with a circle around it (when referring to a registered trademark) and the letters 'TM' (when referring to a 'trade mark').  To record text, begin on either side or part of the dosage form. Start at the top left and progress as one would normally read a book.  Enter a semicolon to show separation between words or line divisions.",
                            "display": "imprint",
                        },
                        {
                            "code": "SPLSCORING",
                            "definition": "Definition: A characteristic of an oral solid dosage form of a medicinal product, specifying the number of equal pieces that the solid dosage form can be divided into using score line(s). \r\n\n                        \n                           Example: One score line creating two equal pieces is given a value of 2, two parallel score lines creating three equal pieces is given a value of 3.\r\n\n                        \n                           Constraints: Whether three parallel score lines create four equal pieces or two intersecting score lines create two equal pieces using one score line and four equal pieces using both score lines, both have the scoring value of 4. Solid dosage forms that are not scored are given a value of 1. Solid dosage forms that can only be divided into unequal pieces are given a null-value with nullFlavor other (OTH).",
                            "display": "scoring",
                        },
                        {
                            "code": "SPLSHAPE",
                            "definition": "Description: A characteristic of an oral solid dosage form of a medicinal product, specifying the two dimensional representation of the solid dose form, in terms of the outside perimeter of a solid dosage form when the dosage form, resting on a flat surface, is viewed from directly above, including slight rounding of corners. SPLSHAPE does not include embossing, scoring, debossing, or internal cut-outs.  SPLSHAPE is independent of the orientation of the imprint and logo. Shapes can include: Triangle (3 sided); Square; Round; Semicircle; Pentagon (5 sided); Diamond; Double circle; Bullet; Hexagon (6 sided); Rectangle; Gear; Capsule; Heptagon (7 sided); Trapezoid; Oval; Clover; Octagon (8 sided); Tear; Freeform.",
                            "display": "shape",
                        },
                        {
                            "code": "SPLSIZE",
                            "definition": "Definition: A characteristic of an oral solid dosage form of a medicinal product, specifying the longest single dimension of the solid dosage form as a physical quantity in the dimension of length (e.g., 3 mm). The length is should be specified in millimeters and should be rounded to the nearest whole millimeter.\r\n\n                        \n                           Example: SPLSIZE for a rectangular shaped tablet is the length and SPLSIZE for a round shaped tablet is the diameter.",
                            "display": "size",
                        },
                        {
                            "code": "SPLSYMBOL",
                            "definition": "Definition: A characteristic of an oral solid dosage form of a medicinal product, to describe whether or not the medicinal product has a mark or symbol appearing on it for easy and definite recognition.  Score lines, letters, numbers, and internal and external cut-outs are not considered marks or symbols. See SPLSCORING and SPLIMPRINT for these characteristics.\r\n\n                        \n                           Constraints: The Observation.value must be a Boolean (BL) with <u>true</u> indicating the presence and <u>false</u> for the absence of marks or symbols.\r\n\n                        \n                           Example:",
                            "display": "symbol",
                        },
                    ],
                    "definition": "MedicationObservationType",
                    "display": "MedicationObservationType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_ObservationIssueTriggerCodedObservationType",
                    "concept": [
                        {
                            "code": "_CaseTransmissionMode",
                            "concept": [
                                {
                                    "code": "AIRTRNS",
                                    "definition": "Communication of an agent from a living subject or environmental source to a living subject through indirect contact via oral or nasal inhalation.",
                                    "display": "airborne transmission",
                                },
                                {
                                    "code": "ANANTRNS",
                                    "definition": "Communication of an agent from one animal to another proximate animal.",
                                    "display": "animal to animal transmission",
                                },
                                {
                                    "code": "ANHUMTRNS",
                                    "definition": "Communication of an agent from an animal to a proximate person.",
                                    "display": "animal to human transmission",
                                },
                                {
                                    "code": "BDYFLDTRNS",
                                    "definition": "Communication of an agent from one living subject to another living subject through direct contact with any body fluid.",
                                    "display": "body fluid contact transmission",
                                },
                                {
                                    "code": "BLDTRNS",
                                    "definition": "Communication of an agent to a living subject through direct contact with blood or blood products whether the contact with blood is part of  a therapeutic procedure or not.",
                                    "display": "blood borne transmission",
                                },
                                {
                                    "code": "DERMTRNS",
                                    "definition": "Communication of an agent from a living subject or environmental source to a living subject via agent migration through intact skin.",
                                    "display": "transdermal transmission",
                                },
                                {
                                    "code": "ENVTRNS",
                                    "definition": "Communication of an agent from an environmental surface or source to a living subject by direct contact.",
                                    "display": "environmental exposure transmission",
                                },
                                {
                                    "code": "FECTRNS",
                                    "definition": "Communication of an agent from a living subject or environmental source to a living subject through oral contact with material contaminated by person or animal fecal material.",
                                    "display": "fecal-oral transmission",
                                },
                                {
                                    "code": "FOMTRNS",
                                    "definition": "Communication of an agent from an non-living material to a living subject through direct contact.",
                                    "display": "fomite transmission",
                                },
                                {
                                    "code": "FOODTRNS",
                                    "definition": "Communication of an agent from a food source to a living subject via oral consumption.",
                                    "display": "food-borne transmission",
                                },
                                {
                                    "code": "HUMHUMTRNS",
                                    "definition": "Communication of an agent from a person to a proximate person.",
                                    "display": "human to human transmission",
                                },
                                {
                                    "code": "INDTRNS",
                                    "definition": "Communication of an agent to a living subject via an undetermined route.",
                                    "display": "indeterminate disease transmission mode",
                                },
                                {
                                    "code": "LACTTRNS",
                                    "definition": "Communication of an agent from one living subject to another living subject through direct contact with mammalian milk or colostrum.",
                                    "display": "lactation transmission",
                                },
                                {
                                    "code": "NOSTRNS",
                                    "definition": "Communication of an agent from any entity to a living subject while the living subject is in the patient role in a healthcare facility.",
                                    "display": "nosocomial transmission",
                                },
                                {
                                    "code": "PARTRNS",
                                    "definition": "Communication of an agent from a living subject or environmental source to a living subject where the acquisition of the agent is not via the alimentary canal.",
                                    "display": "parenteral transmission",
                                },
                                {
                                    "code": "PLACTRNS",
                                    "definition": "Communication of an agent from a living subject to the progeny of that living subject via agent migration across the maternal-fetal placental membranes while in utero.",
                                    "display": "transplacental transmission",
                                },
                                {
                                    "code": "SEXTRNS",
                                    "definition": "Communication of an agent from one living subject to another living subject through direct contact with genital or oral tissues as part of a sexual act.",
                                    "display": "sexual transmission",
                                },
                                {
                                    "code": "TRNSFTRNS",
                                    "definition": "Communication of an agent from one living subject to another living subject through direct contact with blood or blood products where the contact with blood is part of  a therapeutic procedure.",
                                    "display": "transfusion transmission",
                                },
                                {
                                    "code": "VECTRNS",
                                    "definition": "Communication of an agent from a living subject acting as a required intermediary in the agent transmission process to a recipient living subject via direct contact.",
                                    "display": "vector-borne transmission",
                                },
                                {
                                    "code": "WATTRNS",
                                    "definition": "Communication of an agent from a contaminated water source to a living subject whether the water is ingested as a food or not. The route of entry of the water may be through any bodily orifice.",
                                    "display": "water-borne transmission",
                                },
                            ],
                            "definition": "Code for the mechanism by which disease was acquired by the living subject involved in the public health case. Includes sexually transmitted, airborne, bloodborne, vectorborne, foodborne, zoonotic, nosocomial, mechanical, dermal, congenital, environmental exposure, indeterminate.",
                            "display": "case transmission mode",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        }
                    ],
                    "definition": "Distinguishes the kinds of coded observations that could be the trigger for clinical issue detection. These are observations that are not measurable, but instead can be defined with codes. Coded observation types include: Allergy, Intolerance, Medical Condition, Pregnancy status, etc.",
                    "display": "ObservationIssueTriggerCodedObservationType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_ObservationQualityMeasureAttribute",
                    "concept": [
                        {
                            "code": "AGGREGATE",
                            "definition": "Indicates that the observation is carrying out an aggregation calculation, contained in the value element.",
                            "display": "aggregate measure observation",
                        },
                        {
                            "code": "CMPMSRMTH",
                            "definition": "Indicates what method is used in a quality measure to combine the component measure results included in an composite measure.",
                            "display": "composite measure method",
                        },
                        {
                            "code": "CMPMSRSCRWGHT",
                            "definition": "An attribute of a quality measure describing the weight this component measure score is to carry in determining the overall composite measure final score. The value is real value greater than 0 and less than 1.0. Each component measure score will be multiplied by its CMPMSRSCRWGHT and then summed with the other component measures to determine the final overall composite measure score. The sum across all CMPMSRSCRWGHT values within a single composite measure SHALL be 1.0. The value assigned is scoped to the composite measure referencing this component measure only.",
                            "display": "component measure scoring weight",
                        },
                        {
                            "code": "COPY",
                            "definition": "Identifies the organization(s) who own the intellectual property represented by the eMeasure.",
                            "display": "copyright",
                        },
                        {
                            "code": "CRS",
                            "definition": "Summary of relevant clinical guidelines or other clinical recommendations supporting this eMeasure.",
                            "display": "clinical recommendation statement",
                        },
                        {
                            "code": "DEF",
                            "definition": "Description of individual terms, provided as needed.",
                            "display": "definition",
                        },
                        {
                            "code": "DISC",
                            "definition": "Disclaimer information for the eMeasure.",
                            "display": "disclaimer",
                        },
                        {
                            "code": "FINALDT",
                            "definition": "The timestamp when the eMeasure was last packaged in the Measure Authoring Tool.",
                            "display": "finalized date/time",
                        },
                        {
                            "code": "GUIDE",
                            "definition": "Used to allow measure developers to provide additional guidance for implementers to understand greater specificity than could be provided in the logic for data criteria.",
                            "display": "guidance",
                        },
                        {
                            "code": "IDUR",
                            "definition": "Information on whether an increase or decrease in score is the preferred result \n(e.g., a higher score indicates better quality OR a lower score indicates better quality OR quality is within a range).",
                            "display": "improvement notation",
                        },
                        {
                            "code": "ITMCNT",
                            "definition": "Describes the items counted by the measure (e.g., patients, encounters, procedures, etc.)",
                            "display": "items counted",
                        },
                        {
                            "code": "KEY",
                            "definition": "A significant word that aids in discoverability.",
                            "display": "keyword",
                        },
                        {
                            "code": "MEDT",
                            "definition": "The end date of the measurement period.",
                            "display": "measurement end date",
                        },
                        {
                            "code": "MSD",
                            "definition": "The start date of the measurement period.",
                            "display": "measurement start date",
                        },
                        {
                            "code": "MSRADJ",
                            "definition": "The method of adjusting for clinical severity and conditions present at the start of care that can influence patient outcomes for making valid comparisons of outcome measures across providers. Indicates whether an eMeasure is subject to the statistical process for reducing, removing, or clarifying the influences of confounding factors to allow more useful comparisons.",
                            "display": "risk adjustment",
                        },
                        {
                            "code": "MSRAGG",
                            "definition": "Describes how to combine information calculated based on logic in each of several populations into one summarized result. It can also be used to describe how to risk adjust the data based on supplemental data elements described in the eMeasure. (e.g., pneumonia hospital measures antibiotic selection in the ICU versus non-ICU and then the roll-up of the two). \r\n\n                        \n                           Open Issue: The description does NOT align well with the definition used in the HQMF specfication; correct the MSGAGG definition, and the possible distinction of MSRAGG as a child of AGGREGATE.",
                            "display": "rate aggregation",
                        },
                        {
                            "code": "MSRIMPROV",
                            "definition": "Information on whether an increase or decrease in score is the preferred result. This should reflect information on which way is better, an increase or decrease in score.",
                            "display": "health quality measure improvement notation",
                        },
                        {
                            "code": "MSRJUR",
                            "definition": "The list of jurisdiction(s) for which the measure applies.",
                            "display": "jurisdiction",
                        },
                        {
                            "code": "MSRRPTR",
                            "definition": "Type of person or organization that is expected to report the issue.",
                            "display": "reporter type",
                        },
                        {
                            "code": "MSRRPTTIME",
                            "definition": "The maximum time that may elapse following completion of the measure until the measure report must be sent to the receiver.",
                            "display": "timeframe for reporting",
                        },
                        {
                            "code": "MSRSCORE",
                            "definition": "Indicates how the calculation is performed for the eMeasure \n(e.g., proportion, continuous variable, ratio)",
                            "display": "measure scoring",
                        },
                        {
                            "code": "MSRSET",
                            "definition": "Location(s) in which care being measured is rendered\r\n\n                        Usage Note: MSRSET is used rather than RoleCode because the setting applies to what is being measured, as opposed to participating directly in the health quality measure documantion itself).",
                            "display": "health quality measure care setting",
                        },
                        {
                            "code": "MSRTOPIC",
                            "definition": "health quality measure topic type",
                            "display": "health quality measure topic type",
                        },
                        {
                            "code": "MSRTP",
                            "definition": "The time period for which the eMeasure applies.",
                            "display": "measurement period",
                        },
                        {
                            "code": "MSRTYPE",
                            "definition": "Indicates whether the eMeasure is used to examine a process or an outcome over time \n(e.g., Structure, Process, Outcome).",
                            "display": "measure type",
                        },
                        {
                            "code": "RAT",
                            "definition": "Succinct statement of the need for the measure. Usually includes statements pertaining to Importance criterion: impact, gap in care and evidence.",
                            "display": "rationale",
                        },
                        {
                            "code": "REF",
                            "definition": "Identifies bibliographic citations or references to clinical practice guidelines, sources of evidence, or other relevant materials supporting the intent and rationale of the eMeasure.",
                            "display": "reference",
                        },
                        {
                            "code": "SDE",
                            "definition": "Comparison of results across strata can be used to show where disparities exist or where there is a need to expose differences in results. For example, Centers for Medicare & Medicaid Services (CMS) in the U.S. defines four required Supplemental Data Elements (payer, ethnicity, race, and gender), which are variables used to aggregate data into various subgroups. Additional supplemental data elements required for risk adjustment or other purposes of data aggregation can be included in the Supplemental Data Element section.",
                            "display": "supplemental data elements",
                        },
                        {
                            "code": "STRAT",
                            "definition": "Describes the strata for which the measure is to be evaluated. There are three examples of reasons for stratification based on existing work. These include: (1) evaluate the measure based on different age groupings within the population described in the measure (e.g., evaluate the whole [age 14-25] and each sub-stratum [14-19] and [20-25]); (2) evaluate the eMeasure based on either a specific condition, a specific discharge location, or both; (3) evaluate the eMeasure based on different locations within a facility (e.g., evaluate the overall rate for all intensive care units and also some strata include additional findings [specific birth weights for neonatal intensive care units]).",
                            "display": "stratification",
                        },
                        {
                            "code": "TRANF",
                            "definition": "Can be a URL or hyperlinks that link to the transmission formats that are specified for a particular reporting program.",
                            "display": "transmission format",
                        },
                        {
                            "code": "USE",
                            "definition": "Usage notes.",
                            "display": "notice of use",
                        },
                    ],
                    "definition": "Codes used to define various metadata aspects of a health quality measure.",
                    "display": "ObservationQualityMeasureAttribute",
                },
                {
                    "code": "_ObservationSequenceType",
                    "concept": [
                        {
                            "code": "TIME_ABSOLUTE",
                            "definition": 'A sequence of values in the "absolute" time domain.  This is the same time domain that all HL7 timestamps use.  It is time as measured by the Gregorian calendar',
                            "display": "absolute time sequence",
                        },
                        {
                            "code": "TIME_RELATIVE",
                            "definition": 'A sequence of values in a "relative" time domain.  The time is measured relative to the earliest effective time in the Observation Series containing this sequence.',
                            "display": "relative time sequence",
                        },
                    ],
                    "definition": "ObservationSequenceType",
                    "display": "ObservationSequenceType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_ObservationSeriesType",
                    "concept": [
                        {
                            "code": "_ECGObservationSeriesType",
                            "concept": [
                                {
                                    "code": "REPRESENTATIVE_BEAT",
                                    "definition": 'This Observation Series type contains waveforms of a "representative beat" (a.k.a. "median beat" or "average beat").  The waveform samples are measured in relative time, relative to the beginning of the beat as defined by the Observation Series effective time.  The waveforms are not directly acquired from the subject, but rather algorithmically derived from the "rhythm" waveforms.',
                                    "display": "ECG representative beat waveforms",
                                },
                                {
                                    "code": "RHYTHM",
                                    "definition": 'This Observation type contains ECG "rhythm" waveforms.  The waveform samples are measured in absolute time (a.k.a. "subject time" or "effective time").  These waveforms are usually "raw" with some minimal amount of noise reduction and baseline filtering applied.',
                                    "display": "ECG rhythm waveforms",
                                },
                            ],
                            "definition": "ECGObservationSeriesType",
                            "display": "ECGObservationSeriesType",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        }
                    ],
                    "definition": "ObservationSeriesType",
                    "display": "ObservationSeriesType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_PatientImmunizationRelatedObservationType",
                    "concept": [
                        {
                            "code": "CLSSRM",
                            "definition": "Description: The class room associated with the patient during the immunization event.",
                            "display": "classroom",
                        },
                        {
                            "code": "GRADE",
                            "definition": "Description: The school grade or level the patient was in when immunized.",
                            "display": "grade",
                        },
                        {
                            "code": "SCHL",
                            "definition": "Description: The school the patient attended when immunized.",
                            "display": "school",
                        },
                        {
                            "code": "SCHLDIV",
                            "definition": "Description: The school division or district associated with the patient during the immunization event.",
                            "display": "school division",
                        },
                        {
                            "code": "TEACHER",
                            "definition": "Description: The patient's teacher when immunized.",
                            "display": "teacher",
                        },
                    ],
                    "definition": "Description: Reporting codes that are related to an immunization event.",
                    "display": "PatientImmunizationRelatedObservationType",
                },
                {
                    "code": "_PopulationInclusionObservationType",
                    "concept": [
                        {
                            "code": "DENEX",
                            "definition": "Criteria which specify subjects who should be removed from the eMeasure population and denominator before determining if numerator criteria are met. Denominator exclusions are used in proportion and ratio measures to help narrow the denominator.",
                            "display": "denominator exclusions",
                        },
                        {
                            "code": "DENEXCEP",
                            "definition": "Criteria which specify the removal of a subject, procedure or unit of measurement from the denominator, only if the numerator criteria are not met. Denominator exceptions allow for adjustment of the calculated score for those providers with higher risk populations. Denominator exceptions are used only in proportion eMeasures. They are not appropriate for ratio or continuous variable eMeasures. Denominator exceptions allow for the exercise of clinical judgment and should be specifically defined where capturing the information in a structured manner fits the clinical workflow. Generic denominator exception reasons used in proportion eMeasures fall into three general categories:\r\n\n                        \n                           Medical reasons\n                           Patient (or subject) reasons\n                           System reasons",
                            "display": "denominator exceptions",
                        },
                        {
                            "code": "DENOM",
                            "definition": "Criteria for specifying the entities to be evaluated by a specific quality measure, based on a shared common set of characteristics (within a specific measurement set to which a given measure belongs).  The denominator can be the same as the initial population, or it may be a subset of the initial population to further constrain it for the purpose of the eMeasure. Different measures within an eMeasure set may have different denominators. Continuous Variable eMeasures do not have a denominator, but instead define a measure population.",
                            "display": "denominator",
                        },
                        {
                            "code": "IPOP",
                            "concept": [
                                {
                                    "code": "IPPOP",
                                    "definition": "Criteria for specifying the patients to be evaluated by a specific quality measure, based on a shared common set of characteristics (within a specific measurement set to which a given measure belongs). Details often include information based upon specific age groups, diagnoses, diagnostic and procedure codes, and enrollment periods.",
                                    "display": "initial patient population",
                                }
                            ],
                            "definition": "Criteria for specifying the entities to be evaluated by a specific quality measure, based on a shared common set of characteristics (within a specific measurement set to which a given measure belongs).",
                            "display": "initial population",
                        },
                        {
                            "code": "MSROBS",
                            "definition": "Defines the observation to be performed for each patient or event in the measure population. Measure observations for each case in the population are aggregated to determine the overall measure score for the population.\r\n\n                        \n                           Examples: \n                        \r\n\n                        \n                           the median time from arrival in the Emergency Room to departure\n                           the median time from decision to admit to a hospital to the actual admission for Emergency Room patients",
                            "display": "measure observation",
                        },
                        {
                            "code": "MSRPOPL",
                            "definition": "Criteria for specifying\nthe measure population as a narrative description (e.g., all patients seen in the Emergency Department during the measurement period).  This is used only in continuous variable eMeasures.",
                            "display": "measure population",
                        },
                        {
                            "code": "MSRPOPLEX",
                            "definition": "Criteria for specifying subjects who should be removed from the eMeasure's Initial Population and Measure Population. Measure Population Exclusions are used in Continuous Variable measures to help narrow the Measure Population before determining the value(s) of the continuous variable(s).",
                            "display": "measure population exclusions",
                        },
                        {
                            "code": "NUMER",
                            "definition": "Criteria for specifying the processes or outcomes expected for each patient, procedure, or other unit of measurement defined in the denominator for proportion measures, or related to (but not directly derived from) the denominator for ratio measures (e.g., a numerator listing the number of central line blood stream infections and a denominator indicating the days per thousand of central line usage in a specific time period).",
                            "display": "numerator",
                        },
                        {
                            "code": "NUMEX",
                            "definition": "Criteria for specifying instances that should not be included in the numerator data. (e.g., if the number of central line blood stream infections per 1000 catheter days were to exclude infections with a specific bacterium, that bacterium would be listed as a numerator exclusion).  Numerator Exclusions are used only in ratio eMeasures.",
                            "display": "numerator exclusions",
                        },
                    ],
                    "definition": "Observation types for specifying criteria used to assert that a subject is included in a particular population.",
                    "display": "PopulationInclusionObservationType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_PreferenceObservationType",
                    "concept": [
                        {
                            "code": "PREFSTRENGTH",
                            "definition": "An observation about how important a preference is to the target of the preference.",
                            "display": "preference strength",
                        }
                    ],
                    "definition": "Types of observations that can be made about Preferences.",
                    "display": "_PreferenceObservationType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "ADVERSE_REACTION",
                    "definition": "Indicates that the observation is of an unexpected negative occurrence in the subject suspected to result from the subject's exposure to one or more agents.  Observation values would be the symptom resulting from the reaction.",
                    "display": "Adverse Reaction",
                },
                {
                    "code": "ASSERTION",
                    "definition": 'Description:Refines classCode OBS to indicate an observation in which observation.value contains a finding or other nominalized statement, where the encoded information in Observation.value is not altered by Observation.code.  For instance, observation.code="ASSERTION" and observation.value="fracture of femur present" is an assertion of a clinical finding of femur fracture.',
                    "display": "Assertion",
                },
                {
                    "code": "CASESER",
                    "definition": "Definition:An observation that provides a characterization of the level of harm to an investigation subject as a result of a reaction or event.",
                    "display": "case seriousness criteria",
                },
                {
                    "code": "CDIO",
                    "definition": "An observation that states whether the disease was likely acquired outside the jurisdiction of observation, and if so, the nature of the inter-jurisdictional relationship.\r\n\n                        \n                           OpenIssue: This code could be moved to LOINC if it can be done before there are significant implemenations using it.",
                    "display": "case disease imported observation",
                },
                {
                    "code": "CRIT",
                    "definition": "A clinical judgment as to the worst case result of a future exposure (including substance administration). When the worst case result is assessed to have a life-threatening or organ system threatening potential, it is considered to be of high criticality.",
                    "display": "criticality",
                },
                {
                    "code": "CTMO",
                    "definition": "An observation that states the mechanism by which disease was acquired by the living subject involved in the public health case.\r\n\n                        \n                           OpenIssue: This code could be moved to LOINC if it can be done before there are significant implemenations using it.",
                    "display": "case transmission mode observation",
                },
                {
                    "code": "DX",
                    "concept": [
                        {
                            "code": "ADMDX",
                            "definition": "Admitting diagnosis are the diagnoses documented  for administrative purposes as the basis for a hospital admission.",
                            "display": "admitting diagnosis",
                        },
                        {
                            "code": "DISDX",
                            "definition": "Discharge diagnosis are the diagnoses documented for administrative purposes as the time of hospital discharge.",
                            "display": "discharge diagnosis",
                        },
                        {
                            "code": "INTDX",
                            "definition": "Intermediate diagnoses are those diagnoses documented for administrative purposes during the course of a hospital stay.",
                            "display": "intermediate diagnosis",
                        },
                        {
                            "code": "NOI",
                            "definition": "The type of injury that the injury coding specifies.",
                            "display": "nature of injury",
                        },
                    ],
                    "definition": "Includes all codes defining types of indications such as diagnosis, symptom and other indications such as contrast agents for lab tests.",
                    "display": "ObservationDiagnosisTypes",
                },
                {
                    "code": "GISTIER",
                    "definition": "Description: Accuracy determined as per the GIS tier code system.",
                    "display": "GIS tier",
                },
                {
                    "code": "HHOBS",
                    "definition": "Indicates that the observation is of a person???s living situation in a household including the household composition and circumstances.",
                    "display": "household situation observation",
                },
                {
                    "code": "ISSUE",
                    "concept": [
                        {
                            "code": "_ActAdministrativeDetectedIssueCode",
                            "concept": [
                                {
                                    "code": "_ActAdministrativeAuthorizationDetectedIssueCode",
                                    "concept": [
                                        {
                                            "code": "NAT",
                                            "definition": "The requesting party has insufficient authorization to invoke the interaction.",
                                            "display": "Insufficient authorization",
                                        },
                                        {
                                            "code": "SUPPRESSED",
                                            "definition": "Description: One or more records in the query response have been suppressed due to consent or privacy restrictions.",
                                            "display": "record suppressed",
                                        },
                                        {
                                            "code": "VALIDAT",
                                            "concept": [
                                                {
                                                    "code": "KEY204",
                                                    "definition": "The ID of the patient, order, etc., was not found. Used for transactions other than additions, e.g. transfer of a non-existent patient.",
                                                    "display": "Unknown key identifier",
                                                },
                                                {
                                                    "code": "KEY205",
                                                    "definition": "The ID of the patient, order, etc., already exists. Used in response to addition transactions (Admit, New Order, etc.).",
                                                    "display": "Duplicate key identifier",
                                                },
                                                {
                                                    "code": "COMPLY",
                                                    "concept": [
                                                        {
                                                            "code": "DUPTHPY",
                                                            "concept": [
                                                                {
                                                                    "code": "DUPTHPCLS",
                                                                    "definition": "Description:The proposed therapy appears to have the same intended therapeutic benefit as an existing therapy, though the specific mechanisms of action vary.",
                                                                    "display": "duplicate therapeutic alass alert",
                                                                },
                                                                {
                                                                    "code": "DUPTHPGEN",
                                                                    "definition": "Description:The proposed therapy appears to have the same intended therapeutic benefit as an existing therapy and uses the same mechanisms of action as the existing therapy.",
                                                                    "display": "duplicate generic alert",
                                                                },
                                                            ],
                                                            "definition": "The proposed therapy appears to duplicate an existing therapy",
                                                            "display": "Duplicate Therapy Alert",
                                                        },
                                                        {
                                                            "code": "ABUSE",
                                                            "definition": "Description:The proposed therapy is frequently misused or abused and therefore should be used with caution and/or monitoring.",
                                                            "display": "commonly abused/misused alert",
                                                        },
                                                        {
                                                            "code": "FRAUD",
                                                            "definition": "Description:The request is suspected to have a fraudulent basis.",
                                                            "display": "potential fraud",
                                                        },
                                                        {
                                                            "code": "PLYDOC",
                                                            "definition": "A similar or identical therapy was recently ordered by a different practitioner.",
                                                            "display": "Poly-orderer Alert",
                                                        },
                                                        {
                                                            "code": "PLYPHRM",
                                                            "definition": "This patient was recently supplied a similar or identical therapy from a different pharmacy or supplier.",
                                                            "display": "Poly-supplier Alert",
                                                        },
                                                    ],
                                                    "definition": "There may be an issue with the patient complying with the intentions of the proposed therapy",
                                                    "display": "Compliance Alert",
                                                },
                                                {
                                                    "code": "DOSE",
                                                    "concept": [
                                                        {
                                                            "code": "DOSECOND",
                                                            "definition": "Description:Proposed dosage is inappropriate due to patient's medical condition.",
                                                            "display": "dosage-condition alert",
                                                        },
                                                        {
                                                            "code": "DOSEDUR",
                                                            "concept": [
                                                                {
                                                                    "code": "DOSEDURH",
                                                                    "concept": [
                                                                        {
                                                                            "code": "DOSEDURHIND",
                                                                            "definition": "Proposed length of therapy is longer than standard practice for the identified indication or diagnosis",
                                                                            "display": "Dose-Duration High for Indication Alert",
                                                                        }
                                                                    ],
                                                                    "definition": "Proposed length of therapy is longer than standard practice",
                                                                    "display": "Dose-Duration High Alert",
                                                                },
                                                                {
                                                                    "code": "DOSEDURL",
                                                                    "concept": [
                                                                        {
                                                                            "code": "DOSEDURLIND",
                                                                            "definition": "Proposed length of therapy is shorter than standard practice for the identified indication or diagnosis",
                                                                            "display": "Dose-Duration Low for Indication Alert",
                                                                        }
                                                                    ],
                                                                    "definition": "Proposed length of therapy is shorter than that necessary for therapeutic effect",
                                                                    "display": "Dose-Duration Low Alert",
                                                                },
                                                            ],
                                                            "definition": "Proposed length of therapy differs from standard practice.",
                                                            "display": "Dose-Duration Alert",
                                                        },
                                                        {
                                                            "code": "DOSEH",
                                                            "concept": [
                                                                {
                                                                    "code": "DOSEHINDA",
                                                                    "definition": "Proposed dosage exceeds standard practice for the patient's age",
                                                                    "display": "High Dose for Age Alert",
                                                                },
                                                                {
                                                                    "code": "DOSEHIND",
                                                                    "definition": "High Dose for Indication Alert",
                                                                    "display": "High Dose for Indication Alert",
                                                                },
                                                                {
                                                                    "code": "DOSEHINDSA",
                                                                    "definition": "Proposed dosage exceeds standard practice for the patient's height or body surface area",
                                                                    "display": "High Dose for Height/Surface Area Alert",
                                                                },
                                                                {
                                                                    "code": "DOSEHINDW",
                                                                    "definition": "Proposed dosage exceeds standard practice for the patient's weight",
                                                                    "display": "High Dose for Weight Alert",
                                                                },
                                                            ],
                                                            "definition": "Proposed dosage exceeds standard practice",
                                                            "display": "High Dose Alert",
                                                        },
                                                        {
                                                            "code": "DOSEIVL",
                                                            "concept": [
                                                                {
                                                                    "code": "DOSEIVLIND",
                                                                    "definition": "Proposed dosage interval/timing differs from standard practice for the identified indication or diagnosis",
                                                                    "display": "Dose-Interval for Indication Alert",
                                                                }
                                                            ],
                                                            "definition": "Proposed dosage interval/timing differs from standard practice",
                                                            "display": "Dose-Interval Alert",
                                                        },
                                                        {
                                                            "code": "DOSEL",
                                                            "concept": [
                                                                {
                                                                    "code": "DOSELINDA",
                                                                    "definition": "Proposed dosage is below suggested therapeutic levels for the patient's age",
                                                                    "display": "Low Dose for Age Alert",
                                                                },
                                                                {
                                                                    "code": "DOSELIND",
                                                                    "definition": "Low Dose for Indication Alert",
                                                                    "display": "Low Dose for Indication Alert",
                                                                },
                                                                {
                                                                    "code": "DOSELINDSA",
                                                                    "definition": "Proposed dosage is below suggested therapeutic levels for the patient's height or body surface area",
                                                                    "display": "Low Dose for Height/Surface Area Alert",
                                                                },
                                                                {
                                                                    "code": "DOSELINDW",
                                                                    "definition": "Proposed dosage is below suggested therapeutic levels for the patient's weight",
                                                                    "display": "Low Dose for Weight Alert",
                                                                },
                                                            ],
                                                            "definition": "Proposed dosage is below suggested therapeutic levels",
                                                            "display": "Low Dose Alert",
                                                        },
                                                        {
                                                            "code": "MDOSE",
                                                            "definition": "Description:The maximum quantity of this drug allowed to be administered within a particular time-range (month, year, lifetime) has been reached or exceeded.",
                                                            "display": "maximum dosage reached",
                                                        },
                                                    ],
                                                    "definition": "Proposed dosage instructions for therapy differ from standard practice.",
                                                    "display": "Dosage problem",
                                                },
                                                {
                                                    "code": "OBSA",
                                                    "concept": [
                                                        {
                                                            "code": "AGE",
                                                            "concept": [
                                                                {
                                                                    "code": "ADALRT",
                                                                    "definition": "Proposed therapy is outside of the standard practice for an adult patient.",
                                                                    "display": "adult alert",
                                                                },
                                                                {
                                                                    "code": "GEALRT",
                                                                    "definition": "Proposed therapy is outside of standard practice for a geriatric patient.",
                                                                    "display": "geriatric alert",
                                                                },
                                                                {
                                                                    "code": "PEALRT",
                                                                    "definition": "Proposed therapy is outside of the standard practice for a pediatric patient.",
                                                                    "display": "pediatric alert",
                                                                },
                                                            ],
                                                            "definition": "Proposed therapy may be inappropriate or contraindicated due to patient age",
                                                            "display": "Age Alert",
                                                            "property": [
                                                                {
                                                                    "code": "child",
                                                                    "valueCode": "DOSEHINDA",
                                                                },
                                                                {
                                                                    "code": "child",
                                                                    "valueCode": "DOSELINDA",
                                                                },
                                                            ],
                                                        },
                                                        {
                                                            "code": "COND",
                                                            "concept": [
                                                                {"code": "HGHT"},
                                                                {
                                                                    "code": "LACT",
                                                                    "definition": "Proposed therapy may be inappropriate or contraindicated when breast-feeding",
                                                                    "display": "Lactation Alert",
                                                                },
                                                                {
                                                                    "code": "PREG",
                                                                    "definition": "Proposed therapy may be inappropriate or contraindicated during pregnancy",
                                                                    "display": "Pregnancy Alert",
                                                                },
                                                                {"code": "WGHT"},
                                                            ],
                                                            "definition": "Proposed therapy may be inappropriate or contraindicated due to an existing/recent patient condition or diagnosis",
                                                            "display": "Condition Alert",
                                                        },
                                                        {
                                                            "code": "CREACT",
                                                            "definition": "Description:Proposed therapy may be inappropriate or contraindicated because of a common but non-patient specific reaction to the product.\r\n\n                        \n                           Example:There is no record of a specific sensitivity for the patient, but the presence of the sensitivity is common and therefore caution is warranted.",
                                                            "display": "common reaction alert",
                                                        },
                                                        {
                                                            "code": "GEN",
                                                            "definition": "Proposed therapy may be inappropriate or contraindicated due to patient genetic indicators.",
                                                            "display": "Genetic Alert",
                                                        },
                                                        {
                                                            "code": "GEND",
                                                            "definition": "Proposed therapy may be inappropriate or contraindicated due to patient gender.",
                                                            "display": "Gender Alert",
                                                        },
                                                        {
                                                            "code": "LAB",
                                                            "definition": "Proposed therapy may be inappropriate or contraindicated due to recent lab test results",
                                                            "display": "Lab Alert",
                                                        },
                                                        {
                                                            "code": "REACT",
                                                            "concept": [
                                                                {
                                                                    "code": "ALGY",
                                                                    "definition": "Proposed therapy may be inappropriate or contraindicated because of a recorded patient allergy to the proposed product.  (Allergies are immune based reactions.)",
                                                                    "display": "Allergy Alert",
                                                                },
                                                                {
                                                                    "code": "INT",
                                                                    "definition": "Proposed therapy may be inappropriate or contraindicated because of a recorded patient intolerance to the proposed product.  (Intolerances are non-immune based sensitivities.)",
                                                                    "display": "Intolerance Alert",
                                                                },
                                                            ],
                                                            "definition": "Proposed therapy may be inappropriate or contraindicated based on the potential for a patient reaction to the proposed product",
                                                            "display": "Reaction Alert",
                                                        },
                                                        {
                                                            "code": "RREACT",
                                                            "concept": [
                                                                {
                                                                    "code": "RALG",
                                                                    "definition": "Proposed therapy may be inappropriate or contraindicated because of a recorded patient allergy to a cross-sensitivity related product.  (Allergies are immune based reactions.)",
                                                                    "display": "Related Allergy Alert",
                                                                },
                                                                {
                                                                    "code": "RAR",
                                                                    "definition": "Proposed therapy may be inappropriate or contraindicated because of a recorded prior adverse reaction to a cross-sensitivity related product.",
                                                                    "display": "Related Prior Reaction Alert",
                                                                },
                                                                {
                                                                    "code": "RINT",
                                                                    "definition": "Proposed therapy may be inappropriate or contraindicated because of a recorded patient intolerance to a cross-sensitivity related product.  (Intolerances are non-immune based sensitivities.)",
                                                                    "display": "Related Intolerance Alert",
                                                                },
                                                            ],
                                                            "definition": "Proposed therapy may be inappropriate or contraindicated because of a potential patient reaction to a cross-sensitivity related product.",
                                                            "display": "Related Reaction Alert",
                                                        },
                                                    ],
                                                    "definition": "Proposed therapy may be inappropriate or contraindicated due to conditions or characteristics of the patient",
                                                    "display": "Observation Alert",
                                                },
                                                {
                                                    "code": "BUS",
                                                    "definition": "Description:A local business rule relating multiple elements has been violated.",
                                                    "display": "business constraint violation",
                                                },
                                                {
                                                    "code": "CODE_INVAL",
                                                    "concept": [
                                                        {
                                                            "code": "CODE_DEPREC",
                                                            "definition": "Description:The specified code has been deprecated and should no longer be used.  Select another code from the code system.",
                                                            "display": "code has been deprecated",
                                                        }
                                                    ],
                                                    "definition": "Description:The specified code is not valid against the list of codes allowed for the element.",
                                                    "display": "code is not valid",
                                                },
                                                {
                                                    "code": "FORMAT",
                                                    "definition": "Description:The element does not follow the formatting or type rules defined for the field.",
                                                    "display": "invalid format",
                                                },
                                                {
                                                    "code": "ILLEGAL",
                                                    "definition": "Description:The request is missing elements or contains elements which cause it to not meet the legal standards for actioning.",
                                                    "display": "illegal",
                                                },
                                                {
                                                    "code": "LEN_RANGE",
                                                    "concept": [
                                                        {
                                                            "code": "LEN_LONG",
                                                            "definition": "Description:The length of the data specified is greater than the maximum length defined for the element.",
                                                            "display": "length is too long",
                                                        },
                                                        {
                                                            "code": "LEN_SHORT",
                                                            "definition": "Description:The length of the data specified is less than the minimum length defined for the element.",
                                                            "display": "length is too short",
                                                        },
                                                    ],
                                                    "definition": "Description:The length of the data specified falls out of the range defined for the element.",
                                                    "display": "length out of range",
                                                },
                                                {
                                                    "code": "MISSCOND",
                                                    "definition": "Description:The specified element must be specified with a non-null value under certain conditions.  In this case, the conditions are true but the element is still missing or null.",
                                                    "display": "conditional element missing",
                                                },
                                                {
                                                    "code": "MISSMAND",
                                                    "definition": "Description:The specified element is mandatory and was not included in the instance.",
                                                    "display": "mandatory element missing",
                                                },
                                                {
                                                    "code": "NODUPS",
                                                    "definition": "Description:More than one element with the same value exists in the set.  Duplicates not permission in this set in a set.",
                                                    "display": "duplicate values are not permitted",
                                                },
                                                {
                                                    "code": "NOPERSIST",
                                                    "definition": "Description: Element in submitted message will not persist in data storage based on detected issue.",
                                                    "display": "element will not be persisted",
                                                },
                                                {
                                                    "code": "REP_RANGE",
                                                    "concept": [
                                                        {
                                                            "code": "MAXOCCURS",
                                                            "definition": "Description:The number of repeating elements is above the maximum number of repetitions allowed.",
                                                            "display": "repetitions above maximum",
                                                        },
                                                        {
                                                            "code": "MINOCCURS",
                                                            "definition": "Description:The number of repeating elements is below the minimum number of repetitions allowed.",
                                                            "display": "repetitions below minimum",
                                                        },
                                                    ],
                                                    "definition": "Description:The number of repeating elements falls outside the range of the allowed number of repetitions.",
                                                    "display": "repetitions out of range",
                                                },
                                            ],
                                            "definition": "Description:The specified element did not pass business-rule validation.",
                                            "display": "validation issue",
                                        },
                                    ],
                                    "definition": "ActAdministrativeAuthorizationDetectedIssueCode",
                                    "display": "ActAdministrativeAuthorizationDetectedIssueCode",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "_ActAdministrativeRuleDetectedIssueCode",
                                    "concept": [
                                        {
                                            "code": "KEY206",
                                            "definition": "Description: Metadata associated with the identification (e.g. name or gender) does not match the identification being verified.",
                                            "display": "non-matching identification",
                                        },
                                        {
                                            "code": "OBSOLETE",
                                            "definition": "Description: One or more records in the query response have a status of 'obsolete'.",
                                            "display": "obsolete record returned",
                                        },
                                    ],
                                    "definition": "ActAdministrativeRuleDetectedIssueCode",
                                    "display": "ActAdministrativeRuleDetectedIssueCode",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True},
                                        {"code": "child", "valueCode": "KEY204"},
                                        {"code": "child", "valueCode": "KEY205"},
                                    ],
                                },
                            ],
                            "definition": 'Identifies types of detectyed issues for Act class "ALRT" for the administrative and patient administrative acts domains.',
                            "display": "ActAdministrativeDetectedIssueCode",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_ActSuppliedItemDetectedIssueCode",
                            "concept": [
                                {
                                    "code": "_AdministrationDetectedIssueCode",
                                    "concept": [
                                        {
                                            "code": "_AppropriatenessDetectedIssueCode",
                                            "concept": [
                                                {
                                                    "code": "_InteractionDetectedIssueCode",
                                                    "concept": [
                                                        {
                                                            "code": "FOOD",
                                                            "definition": "Proposed therapy may interact with certain foods",
                                                            "display": "Food Interaction Alert",
                                                        },
                                                        {
                                                            "code": "TPROD",
                                                            "concept": [
                                                                {
                                                                    "code": "DRG",
                                                                    "definition": "Proposed therapy may interact with an existing or recent drug therapy",
                                                                    "display": "Drug Interaction Alert",
                                                                },
                                                                {
                                                                    "code": "NHP",
                                                                    "definition": "Proposed therapy may interact with existing or recent natural health product therapy",
                                                                    "display": "Natural Health Product Alert",
                                                                },
                                                                {
                                                                    "code": "NONRX",
                                                                    "definition": "Proposed therapy may interact with a non-prescription drug (e.g. alcohol, tobacco, Aspirin)",
                                                                    "display": "Non-Prescription Interaction Alert",
                                                                },
                                                            ],
                                                            "definition": "Proposed therapy may interact with an existing or recent therapeutic product",
                                                            "display": "Therapeutic Product Alert",
                                                        },
                                                    ],
                                                    "definition": "InteractionDetectedIssueCode",
                                                    "display": "InteractionDetectedIssueCode",
                                                    "property": [
                                                        {
                                                            "code": "notSelectable",
                                                            "valueBoolean": True,
                                                        }
                                                    ],
                                                },
                                                {
                                                    "code": "PREVINEF",
                                                    "definition": "Definition:The same or similar treatment has previously been attempted with the patient without achieving a positive effect.",
                                                    "display": "previously ineffective",
                                                },
                                            ],
                                            "definition": "AppropriatenessDetectedIssueCode",
                                            "display": "AppropriatenessDetectedIssueCode",
                                            "property": [
                                                {
                                                    "code": "notSelectable",
                                                    "valueBoolean": True,
                                                },
                                                {"code": "child", "valueCode": "OBSA"},
                                            ],
                                        },
                                        {
                                            "code": "DACT",
                                            "definition": "Description:Proposed therapy may be contraindicated or ineffective based on an existing or recent drug therapy.",
                                            "display": "drug action detected issue",
                                        },
                                        {
                                            "code": "TIME",
                                            "concept": [
                                                {
                                                    "code": "ALRTENDLATE",
                                                    "definition": "Definition:Proposed therapy may be inappropriate or ineffective because the end of administration is too close to another planned therapy.",
                                                    "display": "end too late alert",
                                                },
                                                {
                                                    "code": "ALRTSTRTLATE",
                                                    "definition": "Definition:Proposed therapy may be inappropriate or ineffective because the start of administration is too late after the onset of the condition.",
                                                    "display": "start too late alert",
                                                },
                                            ],
                                            "definition": "Description:Proposed therapy may be inappropriate or ineffective based on the proposed start or end time.",
                                            "display": "timing detected issue",
                                        },
                                        {
                                            "code": "_TimingDetectedIssueCode",
                                            "concept": [
                                                {
                                                    "code": "ENDLATE",
                                                    "definition": "Proposed therapy may be inappropriate or ineffective because the end of administration is too close to another planned therapy",
                                                    "display": "End Too Late Alert",
                                                },
                                                {
                                                    "code": "STRTLATE",
                                                    "definition": "Proposed therapy may be inappropriate or ineffective because the start of administration is too late after the onset of the condition",
                                                    "display": "Start Too Late Alert",
                                                },
                                            ],
                                            "definition": "Proposed therapy may be inappropriate or ineffective based on the proposed start or end time.",
                                            "display": "TimingDetectedIssueCode",
                                            "property": [
                                                {
                                                    "code": "notSelectable",
                                                    "valueBoolean": True,
                                                },
                                                {
                                                    "code": "status",
                                                    "valueCode": "retired",
                                                },
                                            ],
                                        },
                                    ],
                                    "definition": "Administration of the proposed therapy may be inappropriate or contraindicated as proposed",
                                    "display": "AdministrationDetectedIssueCode",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True},
                                        {"code": "child", "valueCode": "COMPLY"},
                                        {"code": "child", "valueCode": "DOSE"},
                                        {"code": "child", "valueCode": "DUPTHPY"},
                                    ],
                                },
                                {
                                    "code": "_SupplyDetectedIssueCode",
                                    "concept": [
                                        {
                                            "code": "ALLDONE",
                                            "definition": "Definition:The requested action has already been performed and so this request has no effect",
                                            "display": "already performed",
                                        },
                                        {
                                            "code": "FULFIL",
                                            "concept": [
                                                {
                                                    "code": "NOTACTN",
                                                    "definition": "Definition:The status of the request being fulfilled has changed such that it is no longer actionable.  This may be because the request has expired, has already been completely fulfilled or has been otherwise stopped or disabled.  (Not used for 'suspended' orders.)",
                                                    "display": "no longer actionable",
                                                },
                                                {
                                                    "code": "NOTEQUIV",
                                                    "concept": [
                                                        {
                                                            "code": "NOTEQUIVGEN",
                                                            "definition": "Definition:The therapy being performed is not generically equivalent (having the identical biological action) to the therapy which was requested.",
                                                            "display": "not generically equivalent alert",
                                                        },
                                                        {
                                                            "code": "NOTEQUIVTHER",
                                                            "definition": "Definition:The therapy being performed is not therapeutically equivalent (having the same overall patient effect) to the therapy which was requested.",
                                                            "display": "not therapeutically equivalent alert",
                                                        },
                                                    ],
                                                    "definition": "Definition:The therapy being performed is not sufficiently equivalent to the therapy which was requested.",
                                                    "display": "not equivalent alert",
                                                },
                                                {
                                                    "code": "TIMING",
                                                    "concept": [
                                                        {
                                                            "code": "INTERVAL",
                                                            "definition": "Definition:The therapy action is being performed outside the bounds of the time period requested",
                                                            "display": "outside requested time",
                                                        },
                                                        {
                                                            "code": "MINFREQ",
                                                            "definition": "Definition:The therapy action is being performed too soon after the previous occurrence based on the requested frequency",
                                                            "display": "too soon within frequency based on the usage",
                                                        },
                                                    ],
                                                    "definition": "Definition:The therapy is being performed at a time which diverges from the time the therapy was requested",
                                                    "display": "event timing incorrect alert",
                                                },
                                            ],
                                            "definition": "Definition:The therapy being performed is in some way out of alignment with the requested therapy.",
                                            "display": "fulfillment alert",
                                        },
                                        {
                                            "code": "HELD",
                                            "definition": "Definition:There should be no actions taken in fulfillment of a request that has been held or suspended.",
                                            "display": "held/suspended alert",
                                        },
                                        {
                                            "code": "TOOLATE",
                                            "definition": "The patient is receiving a subsequent fill significantly later than would be expected based on the amount previously supplied and the therapy dosage instructions",
                                            "display": "Refill Too Late Alert",
                                        },
                                        {
                                            "code": "TOOSOON",
                                            "definition": "The patient is receiving a subsequent fill significantly earlier than would be expected based on the amount previously supplied and the therapy dosage instructions",
                                            "display": "Refill Too Soon Alert",
                                        },
                                    ],
                                    "definition": "Supplying the product at this time may be inappropriate or indicate compliance issues with the associated therapy",
                                    "display": "SupplyDetectedIssueCode",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "HISTORIC",
                                    "definition": "Description: While the record was accepted in the repository, there is a more recent version of a record of this type.",
                                    "display": "record recorded as historical",
                                },
                                {
                                    "code": "PATPREF",
                                    "concept": [
                                        {
                                            "code": "PATPREFALT",
                                            "definition": "Definition:The proposed therapy goes against preferences or consent constraints recorded in the patient's record.  An alternate therapy meeting those constraints is available.",
                                            "display": "violates stated preferences, alternate available",
                                        }
                                    ],
                                    "definition": "Definition:The proposed therapy goes against preferences or consent constraints recorded in the patient's record.",
                                    "display": "violates stated preferences",
                                },
                            ],
                            "definition": "Identifies types of detected issues regarding the administration or supply of an item to a patient.",
                            "display": "ActSuppliedItemDetectedIssueCode",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                    ],
                    "definition": "There is a clinical issue for the therapy that makes continuation of the therapy inappropriate.\r\n\n                        \n                           Open Issue: The definition of this code does not correctly represent the concept space of its specializations (children)",
                    "display": "detected issue",
                },
                {
                    "code": "KSUBJ",
                    "definition": "Categorization of types of observation that capture the main clinical knowledge subject which may be a medication, a laboratory test, a disease.",
                    "display": "knowledge subject",
                },
                {
                    "code": "KSUBT",
                    "definition": "Categorization of types of observation that capture a knowledge subtopic which might be treatment, etiology, or prognosis.",
                    "display": "knowledge subtopic",
                },
                {
                    "code": "OINT",
                    "concept": [
                        {
                            "code": "ALG",
                            "concept": [
                                {
                                    "code": "DALG",
                                    "definition": "An allergy to a pharmaceutical product.",
                                    "display": "Drug Allergy",
                                },
                                {
                                    "code": "EALG",
                                    "definition": "An allergy to a substance other than a drug or a food.  E.g. Latex, pollen, etc.",
                                    "display": "Environmental Allergy",
                                },
                                {
                                    "code": "FALG",
                                    "definition": "An allergy to a substance generally consumed for nutritional purposes.",
                                    "display": "Food Allergy",
                                },
                            ],
                            "definition": "Hypersensitivity to an agent caused by an immunologic response to an initial exposure",
                            "display": "Allergy",
                        },
                        {
                            "code": "DINT",
                            "concept": [
                                {
                                    "code": "DNAINT",
                                    "definition": "Hypersensitivity to an agent caused by a mechanism other than an immunologic response to an initial exposure",
                                    "display": "Drug Non-Allergy Intolerance",
                                }
                            ],
                            "definition": "Hypersensitivity resulting in an adverse reaction upon exposure to a drug.",
                            "display": "Drug Intolerance",
                            "property": [{"code": "child", "valueCode": "DALG"}],
                        },
                        {
                            "code": "EINT",
                            "concept": [
                                {
                                    "code": "ENAINT",
                                    "definition": "Hypersensitivity to an agent caused by a mechanism other than an immunologic response to an initial exposure",
                                    "display": "Environmental Non-Allergy Intolerance",
                                }
                            ],
                            "definition": "Hypersensitivity resulting in an adverse reaction upon exposure to environmental conditions.",
                            "display": "Environmental Intolerance",
                            "property": [{"code": "child", "valueCode": "EALG"}],
                        },
                        {
                            "code": "FINT",
                            "concept": [
                                {
                                    "code": "FNAINT",
                                    "definition": "Hypersensitivity to an agent caused by a mechanism other than an immunologic response to an initial exposure",
                                    "display": "Food Non-Allergy Intolerance",
                                }
                            ],
                            "definition": "Hypersensitivity resulting in an adverse reaction upon exposure to food.",
                            "display": "Food Intolerance",
                            "property": [{"code": "child", "valueCode": "FALG"}],
                        },
                        {
                            "code": "NAINT",
                            "definition": "Hypersensitivity to an agent caused by a mechanism other than an immunologic response to an initial exposure",
                            "display": "Non-Allergy Intolerance",
                            "property": [
                                {"code": "child", "valueCode": "DNAINT"},
                                {"code": "child", "valueCode": "ENAINT"},
                                {"code": "child", "valueCode": "FNAINT"},
                            ],
                        },
                    ],
                    "definition": "Hypersensitivity resulting in an adverse reaction upon exposure to an agent.",
                    "display": "intolerance",
                },
                {
                    "code": "SEV",
                    "definition": "A subjective evaluation of the seriousness or intensity associated with another observation.",
                    "display": "Severity Observation",
                },
                {
                    "code": "_FDALabelData",
                    "concept": [
                        {
                            "code": "FDACOATING",
                            "definition": "FDA label coating",
                            "display": "coating",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                        {
                            "code": "FDACOLOR",
                            "definition": "FDA label color",
                            "display": "color",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                        {
                            "code": "FDAIMPRINTCD",
                            "definition": "FDA label imprint code",
                            "display": "imprint code",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                        {
                            "code": "FDALOGO",
                            "definition": "FDA label logo",
                            "display": "logo",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                        {
                            "code": "FDASCORING",
                            "definition": "FDA label scoring",
                            "display": "scoring",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                        {
                            "code": "FDASHAPE",
                            "definition": "FDA label shape",
                            "display": "shape",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                        {
                            "code": "FDASIZE",
                            "definition": "FDA label size",
                            "display": "size",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                    ],
                    "definition": "FDA label data",
                    "display": "FDALabelData",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "status", "valueCode": "retired"},
                    ],
                },
            ],
            "definition": "Identifies the kinds of observations that can be performed",
            "display": "ObservationType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ObservationType

    Identifies the kinds of observations that can be performed
    """

    underscore_roioverlay_shape = CodeSystemConcept(
        {
            "code": "_ROIOverlayShape",
            "concept": [
                {
                    "code": "CIRCLE",
                    "definition": "A circle defined by two (column,row) pairs. The first point is the center of the circle and the second point is a point on the perimeter of the circle.",
                    "display": "circle",
                },
                {
                    "code": "ELLIPSE",
                    "definition": "An ellipse defined by four (column,row) pairs, the first two points specifying the endpoints of the major axis and the second two points specifying the endpoints of the minor axis.",
                    "display": "ellipse",
                },
                {
                    "code": "POINT",
                    "definition": "A single point denoted by a single (column,row) pair, or multiple points each denoted by a (column,row) pair.",
                    "display": "point",
                },
                {
                    "code": "POLY",
                    "definition": "A series of connected line segments with ordered vertices denoted by (column,row) pairs; if the first and last vertices are the same, it is a closed polygon.",
                    "display": "polyline",
                },
            ],
            "definition": "Shape of the region on the object being referenced",
            "display": "ROIOverlayShape",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ROIOverlayShape

    Shape of the region on the object being referenced
    """

    c = CodeSystemConcept(
        {
            "code": "C",
            "definition": "Description:Indicates that result data has been corrected.",
            "display": "corrected",
        }
    )
    """
    corrected

    Description:Indicates that result data has been corrected.
    """

    diet = CodeSystemConcept(
        {
            "code": "DIET",
            "concept": [
                {
                    "code": "BR",
                    "definition": "A diet exclusively composed of oatmeal, semolina, or rice, to be extremely easy to eat and digest.",
                    "display": "breikost (GE)",
                },
                {
                    "code": "DM",
                    "definition": "A diet that uses carbohydrates sparingly.  Typically with a restriction in daily energy content (e.g. 1600-2000 kcal).",
                    "display": "diabetes mellitus diet",
                },
                {
                    "code": "FAST",
                    "definition": "No enteral intake of foot or liquids  whatsoever, no smoking.  Typically 6 to 8 hours before anesthesia.",
                    "display": "fasting",
                },
                {
                    "code": "FORMULA",
                    "definition": "A diet consisting of a formula feeding, either for an infant or an adult, to provide nutrition either orally or through the gastrointestinal tract via tube, catheter or stoma.",
                    "display": "formula diet",
                },
                {
                    "code": "GF",
                    "definition": "Gluten free diet for celiac disease.",
                    "display": "gluten free",
                },
                {
                    "code": "LF",
                    "definition": "A diet low in fat, particularly to patients with hepatic diseases.",
                    "display": "low fat",
                },
                {
                    "code": "LP",
                    "definition": "A low protein diet for patients with renal failure.",
                    "display": "low protein",
                },
                {
                    "code": "LQ",
                    "definition": "A strictly liquid diet, that can be fully absorbed in the intestine, and therefore may not contain fiber.  Used before enteral surgeries.",
                    "display": "liquid",
                },
                {
                    "code": "LS",
                    "definition": "A diet low in sodium for patients with congestive heart failure and/or renal failure.",
                    "display": "low sodium",
                },
                {
                    "code": "N",
                    "definition": "A normal diet, i.e. no special preparations or restrictions for medical reasons. This is notwithstanding any preferences the patient might have regarding special foods, such as vegetarian, kosher, etc.",
                    "display": "normal diet",
                },
                {
                    "code": "NF",
                    "definition": "A no fat diet for acute hepatic diseases.",
                    "display": "no fat",
                },
                {
                    "code": "PAF",
                    "definition": "Phenylketonuria diet.",
                    "display": "phenylalanine free",
                },
                {
                    "code": "PAR",
                    "definition": "Patient is supplied with parenteral nutrition, typically described in terms of i.v. medications.",
                    "display": "parenteral",
                },
                {
                    "code": "RD",
                    "definition": "A diet that seeks to reduce body fat, typically low energy content (800-1600 kcal).",
                    "display": "reduction diet",
                },
                {
                    "code": "SCH",
                    "definition": "A diet that avoids ingredients that might cause digestion problems, e.g., avoid excessive fat, avoid too much fiber (cabbage, peas, beans).",
                    "display": "schonkost (GE)",
                },
                {
                    "code": "SUPPLEMENT",
                    "definition": "A diet that is not intended to be complete but is added to other diets.",
                    "display": "nutritional supplement",
                },
                {
                    "code": "T",
                    "definition": "This is not really a diet, since it contains little nutritional value, but is essentially just water.  Used before coloscopy examinations.",
                    "display": "tea only",
                },
                {
                    "code": "VLI",
                    "definition": 'Diet with low content of the amino-acids valin, leucin, and isoleucin, for "maple syrup disease."',
                    "display": "low valin, leucin, isoleucin",
                },
            ],
            "definition": "Code set to define specialized/allowed diets",
            "display": "Diet",
        }
    )
    """
    Diet

    Code set to define specialized/allowed diets
    """

    drugprg = CodeSystemConcept(
        {
            "code": "DRUGPRG",
            "definition": "Definition: A public or government health program that administers and funds coverage for prescription drugs to assist program eligible who meet financial and health status criteria.",
            "display": "drug program",
        }
    )
    """
    drug program

    Definition: A public or government health program that administers and funds coverage for prescription drugs to assist program eligible who meet financial and health status criteria.
    """

    f = CodeSystemConcept(
        {
            "code": "F",
            "definition": "Description:Indicates that a result is complete.  No further results are to come.  This maps to the 'complete' state in the observation result status code.",
            "display": "final",
        }
    )
    """
    final

    Description:Indicates that a result is complete.  No further results are to come.  This maps to the 'complete' state in the observation result status code.
    """

    prlmn = CodeSystemConcept(
        {
            "code": "PRLMN",
            "definition": "Description:Indicates that a result is incomplete.  There are further results to come.  This maps to the 'active' state in the observation result status code.",
            "display": "preliminary",
        }
    )
    """
    preliminary

    Description:Indicates that a result is incomplete.  There are further results to come.  This maps to the 'active' state in the observation result status code.
    """

    secobs = CodeSystemConcept(
        {
            "code": "SECOBS",
            "concept": [
                {
                    "code": "SECCATOBS",
                    "definition": 'Type of security metadata observation made about the category of an IT resource (data, information object, service, or system capability), which may be used to make access control decisions. Security category metadata is defined by ISO/IEC 2382-8:1998(E/F)/ T-REC-X.812-1995 as: "A nonhierarchical grouping of sensitive information used to control access to data more finely than with hierarchical security classification alone."\r\n\n                        \n                           Rationale: A security category observation supports requirement to specify the type of IT resource to facilitate application of appropriate levels of information security according to a range of levels of impact or consequences that might result from the unauthorized disclosure, modification, or use of the information or information system.  A resource is assigned to a specific category of information (e.g., privacy, medical, proprietary, financial, investigative, contractor sensitive, security management) defined by an organization or in some instances, by a specific law, Executive Order, directive, policy, or regulation. [FIPS 199]\r\n\n                        \n                           Examples: Types of security categories include:\r\n\n                        \n                           Compartment:  A division of data into isolated blocks with separate security controls for the purpose of reducing risk. (ISO 2382-8).  A security label tag that "segments" an IT resource by indicating that access and use is restricted to members of a defined community or project. (HL7 Healthcare Classification System)  \n                           Sensitivity:  The characteristic of an IT resource which implies its value or importance and may include its vulnerability. (ISO 7492-2)  Privacy metadata for information perceived as undesirable to share.  (HL7 Healthcare Classification System)',
                    "display": "security category observation",
                },
                {
                    "code": "SECCLASSOBS",
                    "definition": 'Type of security metadata observation made about the classification of an IT resource (data, information object, service, or system capability), which may be used to make access control decisions.  Security classification is defined by ISO/IEC 2382-8:1998(E/F)/ T-REC-X.812-1995 as: "The determination of which specific degree of protection against access the data or information requires, together with a designation of that degree of protection."  Security classification metadata is based on an analysis of applicable policies and the risk of financial, reputational, or other harm that could result from unauthorized disclosure.\r\n\n                        \n                           Rationale: A security classification observation may indicate that the confidentiality level indicated by an Act or Role confidentiality attribute has been overridden by the entity responsible for ascribing the SecurityClassificationObservationValue.  This supports the business requirement for increasing or decreasing the level of confidentiality (classification or declassification) based on parameters beyond the original assignment of an Act or Role confidentiality.\r\n\n                        \n                           Examples: Types of security classification include: HL7 Confidentiality Codes such as very restricted, unrestricted, and normal.  Intelligence community examples include top secret, secret, and confidential.\r\n\n                        \n                           Usage Note: Security classification observation type codes designate security label field types, which are valued with an applicable SecurityClassificationObservationValue code as the "security label tag".',
                    "display": "security classification observation",
                },
                {
                    "code": "SECCONOBS",
                    "definition": "Type of security metadata observation made about the control of an IT resource (data, information object, service, or system capability), which may be used to make access control decisions.  Security control metadata convey instructions to users and receivers for secure distribution, transmission, and storage; dictate obligations or mandated actions; specify any action prohibited by refrain policy such as dissemination controls; and stipulate the permissible purpose of use of an IT resource.  \r\n\n                        \n                           Rationale: A security control observation supports requirement to specify applicable management, operational, and technical controls (i.e., safeguards or countermeasures) prescribed for an information system to protect the confidentiality, integrity, and availability of the system and its information. [FIPS 199]\r\n\n                        \n                           Examples: Types of security control metadata include: \r\n\n                        \n                           handling caveats\n                           dissemination controls\n                           obligations\n                           refrain policies\n                           purpose of use constraints",
                    "display": "security control observation",
                },
                {
                    "code": "SECINTOBS",
                    "concept": [
                        {
                            "code": "SECALTINTOBS",
                            "definition": "Type of security metadata observation made about the alteration integrity of an IT resource (data, information object, service, or system capability), which indicates the mechanism used for authorized transformations of the resource.\r\n\n                        \n                           Examples: Types of security alteration integrity observation metadata, which may value the observation with a code used to indicate the mechanism used for authorized transformation of an IT resource, including: \r\n\n                        \n                           translation\n                           syntactic transformation\n                           semantic mapping\n                           redaction\n                           masking\n                           pseudonymization\n                           anonymization",
                            "display": "security alteration integrity observation",
                        },
                        {
                            "code": "SECDATINTOBS",
                            "definition": 'Type of security metadata observation made about the data integrity of an IT resource (data, information object, service, or system capability), which indicates the security mechanism used to preserve resource accuracy and consistency.  Data integrity is defined by ISO 22600-23.3.21 as: "The property that data has not been altered or destroyed in an unauthorized manner", and by ISO/IEC 2382-8:  The property of data whose accuracy and consistency are preserved regardless of changes made."\r\n\n                        \n                           Examples: Types of security data integrity observation metadata, which may value the observation, include cryptographic hash function and digital signature.',
                            "display": "security data integrity observation",
                        },
                        {
                            "code": "SECINTCONOBS",
                            "definition": "Type of security metadata observation made about the integrity confidence of an IT resource (data, information object, service, or system capability), which may be used to make access control decisions.\r\n\n                        \n                           Examples: Types of security integrity confidence observation metadata, which may value the observation, include highly reliable, uncertain reliability, and not reliable.\r\n\n                        \n                           Usage Note: A security integrity confidence observation on an Act may indicate that a valued Act.uncertaintycode attribute has been overridden by the entity responsible for ascribing the SecurityIntegrityConfidenceObservationValue.  This supports the business requirements for increasing or decreasing the assessment of the reliability or trustworthiness of an IT resource based on parameters beyond the original assignment of an Act statement level of uncertainty.",
                            "display": "security integrity confidence observation",
                        },
                        {
                            "code": "SECINTPRVOBS",
                            "concept": [
                                {
                                    "code": "SECINTPRVABOBS",
                                    "definition": "Type of security metadata observation made about the integrity provenance of an IT resource (data, information object, service, or system capability), which indicates the entity that made assertions about the resource.  The asserting entity may not be the original informant about the resource.\r\n\n                        \n                           Examples: Types of security integrity provenance asserted by observation metadata, which may value the observation, including: \r\n\n                        \n                           assertions about an IT resource by a patient\n                           assertions about an IT resource by a clinician\n                           assertions about an IT resource by a device",
                                    "display": "security integrity provenance asserted by observation",
                                },
                                {
                                    "code": "SECINTPRVRBOBS",
                                    "definition": "Type of security metadata observation made about the integrity provenance of an IT resource (data, information object, service, or system capability), which indicates the entity that reported the existence of the resource.  The reporting entity may not be the original author of the resource.\r\n\n                        \n                           Examples: Types of security integrity provenance reported by observation metadata, which may value the observation, include: \r\n\n                        \n                           reports about an IT resource by a patient\n                           reports about an IT resource by a clinician\n                           reports about an IT resource by a device",
                                    "display": "security integrity provenance reported by observation",
                                },
                            ],
                            "definition": "Type of security metadata observation made about the provenance integrity of an IT resource (data, information object, service, or system capability), which indicates the lifecycle completeness of an IT resource in terms of workflow status such as its creation, modification, suspension, and deletion; locations in which the resource has been collected or archived, from which it may be retrieved, and the history of its distribution and disclosure.  Integrity provenance metadata about an IT resource may be used to assess its veracity, reliability, and trustworthiness.\r\n\n                        \n                           Examples: Types of security integrity provenance observation metadata, which may value the observation about an IT resource, include: \r\n\n                        \n                           completeness or workflow status, such as authentication\n                           the entity responsible for original authoring or informing about an IT resource\n                           the entity responsible for a report or assertion about an IT resource relayed ???????second-hand??????\n                           the entity responsible for excerpting, transforming, or compiling an IT resource",
                            "display": "security integrity provenance observation",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "SECINTSTOBS",
                            "definition": "Type of security metadata observation made about the integrity status of an IT resource (data, information object, service, or system capability), which may be used to make access control decisions.  Indicates the completeness of an IT resource in terms of workflow status, which may impact users that are authorized to access and use the resource.\r\n\n                        \n                           Examples: Types of security integrity status observation metadata, which may value the observation, include codes from the HL7 DocumentCompletion code system such as legally authenticated, in progress, and incomplete.",
                            "display": "security integrity status observation",
                        },
                    ],
                    "definition": 'Type of security metadata observation made about the integrity of an IT resource (data, information object, service, or system capability), which may be used to make access control decisions.\r\n\n                        \n                           Rationale: A security integrity observation supports the requirement to guard against improper information modification or destruction, and includes ensuring information non-repudiation and authenticity. (44 U.S.C., SEC. 3542)\r\n\n                        \n                           Examples: Types of security integrity metadata include: \r\n\n                        \n                           Integrity status, which indicates the completeness or workflow status of an IT resource (data, information object, service, or system capability)\n                           Integrity confidence, which indicates the reliability and trustworthiness of an IT resource\n                           Integrity control, which indicates pertinent handling caveats, obligations, refrain policies, and purpose of use for  the resource\n                           Data integrity, which indicate the security mechanisms used to ensure that the accuracy and consistency are preserved regardless of changes made (ISO/IEC DIS 2382-8)\n                           Alteration integrity, which indicate the security mechanisms used for authorized transformations of the resource\n                           Integrity provenance, which indicates the entity responsible for a report or assertion relayed "second-hand" about an IT resource',
                    "display": "security integrity observation",
                },
                {
                    "code": "SECTRSTOBS",
                    "concept": [
                        {
                            "code": "TRSTACCRDOBS",
                            "definition": "Type of security metadata observation made about the formal declaration by an authority or neutral third party that validates the technical, security, trust, and business practice conformance of Trust Agents to facilitate security, interoperability, and trust among participants within a security domain or trust framework.",
                            "display": "trust accreditation observation",
                        },
                        {
                            "code": "TRSTAGREOBS",
                            "definition": "Type of security metadata observation made about privacy and security requirements with which a security domain must comply. [ISO IEC 10181-1]",
                            "display": "trust agreement observation",
                        },
                        {
                            "code": "TRSTCERTOBS",
                            "definition": "Type of security metadata observation made about a set of security-relevant data issued by a security authority or trusted third party, together with security information which is used to provide the integrity and data origin authentication services for an IT resource (data, information object, service, or system capability). [Based on ISO IEC 10181-1]\r\n\n                        \n                           For example,\n                        \r\n\n                        \n                           A Certificate Policy (CP), which is a named set of rules that indicates the applicability of a certificate to a particular community and/or class of application with common security requirements. For example, a particular Certificate Policy might indicate the applicability of a type of certificate to the authentication of electronic data interchange transactions for the trading of goods within a given price range. [Trust Service Principles and Criteria for Certification Authorities Version 2.0 March 2011 Copyright 2011 by Canadian Institute of Chartered Accountants.\n                           A Certificate Practice Statement (CSP), which is a statement of the practices which an Authority employs in issuing and managing certificates. [Trust Service Principles and Criteria for Certification Authorities Version 2.0 March 2011 Copyright 2011 by Canadian Institute of Chartered Accountants.]",
                            "display": "trust certificate observation",
                        },
                        {
                            "code": "TRSTFWKOBS",
                            "definition": "Type of security metadata observation made about a complete set of contracts, regulations or commitments that enable participating actors to rely on certain assertions by other actors to fulfill their information security requirements. [Kantara Initiative]",
                            "display": "trust framework observation",
                        },
                        {
                            "code": "TRSTLOAOBS",
                            "definition": "Type of security metadata observation made about the digital quality or reliability of a trust assertion, activity, capability, information exchange, mechanism, process, or protocol.",
                            "display": "trust assurance observation",
                        },
                        {
                            "code": "TRSTMECOBS",
                            "definition": "Type of security metadata observation made about a security architecture system component that supports enforcement of security policies.",
                            "display": "trust mechanism observation",
                        },
                    ],
                    "definition": "An observation identifying trust metadata about an IT resource (data, information object, service, or system capability), which may be used as a trust attribute to populate a computable trust policy, trust credential, trust assertion, or trust label field in a security label or trust policy, which are principally used for authentication, authorization, and access control decisions.",
                    "display": "SECTRSTOBS",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": "An observation identifying security metadata about an IT resource (data, information object, service, or system capability), which may be used to make access control decisions.  Security metadata are used to name security labels.  \r\n\n                        \n                           Rationale: According to ISO/TS 22600-3:2009(E) A.9.1.7 SECURITY LABEL MATCHING, Security label matching compares the initiator's clearance to the target's security label.  All of the following must be true for authorization to be granted:\r\n\n                        \n                           The security policy identifiers shall be identical\n                           The classification level of the initiator shall be greater than or equal to that of the target (that is, there shall be at least one value in the classification list of the clearance greater than or equal to the classification of the target), and \n                           For each security category in the target label, there shall be a security category of the same type in the initiator's clearance and the initiator's classification level shall dominate that of the target.\n                        \n                        \n                           Examples: SecurityObservationType  security label fields include:\r\n\n                        \n                           Confidentiality classification\n                           Compartment category\n                           Sensitivity category\n                           Security mechanisms used to ensure data integrity or to perform authorized data transformation\n                           Indicators of an IT resource completeness, veracity, reliability, trustworthiness, or provenance.\n                        \n                        \n                           Usage Note: SecurityObservationType codes designate security label field types, which are valued with an applicable SecurityObservationValue code as the \"security label tag\".",
            "display": "SecurityObservationType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    SecurityObservationType

    An observation identifying security metadata about an IT resource (data, information object, service, or system capability), which may be used to make access control decisions.  Security metadata are used to name security labels.


                           Rationale: According to ISO/TS 22600-3:2009(E) A.9.1.7 SECURITY LABEL MATCHING, Security label matching compares the initiator's clearance to the target's security label.  All of the following must be true for authorization to be granted:


                           The security policy identifiers shall be identical
                           The classification level of the initiator shall be greater than or equal to that of the target (that is, there shall be at least one value in the classification list of the clearance greater than or equal to the classification of the target), and
                           For each security category in the target label, there shall be a security category of the same type in the initiator's clearance and the initiator's classification level shall dominate that of the target.


                           Examples: SecurityObservationType  security label fields include:


                           Confidentiality classification
                           Compartment category
                           Sensitivity category
                           Security mechanisms used to ensure data integrity or to perform authorized data transformation
                           Indicators of an IT resource completeness, veracity, reliability, trustworthiness, or provenance.


                           Usage Note: SecurityObservationType codes designate security label field types, which are valued with an applicable SecurityObservationValue code as the "security label tag".
    """

    subsidffs = CodeSystemConcept(
        {
            "code": "SUBSIDFFS",
            "definition": "Definition: A government health program that provides coverage on a fee for service basis for health services to persons meeting eligibility criteria such as income, location of residence, access to other coverages, health condition, and age, the cost of which is to some extent subsidized by public funds.\r\n\n                        \n                           Discussion: The structure and business processes for underwriting and administering a subsidized fee for service program is further specified by the Underwriter and Payer Role.class and Role.code.",
            "display": "subsidized fee for service program",
        }
    )
    """
    subsidized fee for service program

    Definition: A government health program that provides coverage on a fee for service basis for health services to persons meeting eligibility criteria such as income, location of residence, access to other coverages, health condition, and age, the cost of which is to some extent subsidized by public funds.


                           Discussion: The structure and business processes for underwriting and administering a subsidized fee for service program is further specified by the Underwriter and Payer Role.class and Role.code.
    """

    wrkcomp = CodeSystemConcept(
        {
            "code": "WRKCOMP",
            "definition": "Definition: Government mandated program providing coverage, disability income, and vocational rehabilitation for injuries sustained in the work place or in the course of employment.  Employers may either self-fund the program, purchase commercial coverage, or pay a premium to a government entity that administers the program.  Employees may be required to pay premiums toward the cost of coverage as well.",
            "display": "(workers compensation program",
        }
    )
    """
    (workers compensation program

    Definition: Government mandated program providing coverage, disability income, and vocational rehabilitation for injuries sustained in the work place or in the course of employment.  Employers may either self-fund the program, purchase commercial coverage, or pay a premium to a government entity that administers the program.  Employees may be required to pay premiums toward the cost of coverage as well.
    """

    underscore_act_procedure_code = CodeSystemConcept(
        {
            "code": "_ActProcedureCode",
            "concept": [
                {
                    "code": "_ActBillableServiceCode",
                    "definition": "Definition: An identifying code for billable services, as opposed to codes for similar services used to identify them for functional purposes.",
                    "display": "ActBillableServiceCode",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "status", "valueCode": "retired"},
                    ],
                }
            ],
            "definition": "An identifying code for healthcare interventions/procedures.",
            "display": "ActProcedureCode",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "status", "valueCode": "retired"},
            ],
        }
    )
    """
    ActProcedureCode

    An identifying code for healthcare interventions/procedures.
    """

    underscore_hl7_defined_act_codes = CodeSystemConcept(
        {
            "code": "_HL7DefinedActCodes",
            "definition": "Domain provides the root for HL7-defined detailed or rich codes for the Act classes.",
            "display": "HL7DefinedActCodes",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "status", "valueCode": "retired"},
            ],
        }
    )
    """
    HL7DefinedActCodes

    Domain provides the root for HL7-defined detailed or rich codes for the Act classes.
    """

    copay = CodeSystemConcept(
        {"code": "COPAY", "property": [{"code": "status", "valueCode": "retired"}]}
    )
    """
    None


    """

    deduct = CodeSystemConcept(
        {"code": "DEDUCT", "property": [{"code": "status", "valueCode": "retired"}]}
    )
    """
    None


    """

    doseind = CodeSystemConcept(
        {"code": "DOSEIND", "property": [{"code": "status", "valueCode": "retired"}]}
    )
    """
    None


    """

    pra = CodeSystemConcept(
        {"code": "PRA", "property": [{"code": "status", "valueCode": "retired"}]}
    )
    """
    None


    """

    store = CodeSystemConcept(
        {
            "code": "STORE",
            "definition": 'The act of putting something away for safe keeping. The "something" may be physical object such as a specimen, or information, such as observations regarding a specimen.',
            "display": "Storage",
            "property": [
                {"code": "status", "valueCode": "retired"},
                {"code": "deprecationDate", "valueDateTime": "2008-12-20"},
            ],
        }
    )
    """
    Storage

    The act of putting something away for safe keeping. The "something" may be physical object such as a specimen, or information, such as observations regarding a specimen.
    """

    class Meta:
        resource = _resource
