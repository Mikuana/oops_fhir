from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3hl7PublishingDomain"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7PublishingDomain:
    """
    v3 Code System hl7PublishingDomain

      Description:  Codes for HL7 publishing domains (specific content area)

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-hl7PublishingDomain
    """

    ab = CodeSystemConcept(
        {
            "code": "AB",
            "definition": 'Description: Represents the HL7 content "domain" that supports accounting and billing functions - and "provides support for the creation and management of patient billing accounts and the post of financial transactions against patient billing accounts for the purpose of aggregating financial transactions that will be submitted as claims or invoices for reimbursemen"\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "accounting & billing",
        }
    )
    """
    accounting & billing

    Description: Represents the HL7 content "domain" that supports accounting and billing functions - and "provides support for the creation and management of patient billing accounts and the post of financial transactions against patient billing accounts for the purpose of aggregating financial transactions that will be submitted as claims or invoices for reimbursemen"

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    ai = CodeSystemConcept(
        {
            "code": "AI",
            "definition": 'Description: Represents the HL7 content "domain" that supports trigger event control act infrastructure - and "covers the alternate structures of the message Trigger Event Control Acts in the HL7 Composite Message."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "trigger event control act infrastructure",
        }
    )
    """
    trigger event control act infrastructure

    Description: Represents the HL7 content "domain" that supports trigger event control act infrastructure - and "covers the alternate structures of the message Trigger Event Control Acts in the HL7 Composite Message."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    al = CodeSystemConcept(
        {
            "code": "AL",
            "definition": 'Description: Represents the HL7 content "domain" that was defined as an "artificial listing" domain to support publication testing.',
            "display": "artificial listing for test purposes - faux Domain for testing",
        }
    )
    """
    artificial listing for test purposes - faux Domain for testing

    Description: Represents the HL7 content "domain" that was defined as an "artificial listing" domain to support publication testing.
    """

    bb = CodeSystemConcept(
        {
            "code": "BB",
            "definition": 'Description: Represents the HL7 content "domain" that supports blood tissue and organ domain - and "comprises the models, messages, and other artIfacts that are needed to support messaging related to the process of blood, tissue, and organ banking operations such as donations, eligibility, storage, dispense, administration/transfusion, explantation, and implantation. "\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "blood tissue and organ",
        }
    )
    """
    blood tissue and organ

    Description: Represents the HL7 content "domain" that supports blood tissue and organ domain - and "comprises the models, messages, and other artIfacts that are needed to support messaging related to the process of blood, tissue, and organ banking operations such as donations, eligibility, storage, dispense, administration/transfusion, explantation, and implantation. "

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    cd = CodeSystemConcept(
        {
            "code": "CD",
            "definition": 'Description: Represents the HL7 content "domain" that supports the clinical document architecture.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "clinical document architecture",
        }
    )
    """
    clinical document architecture

    Description: Represents the HL7 content "domain" that supports the clinical document architecture.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    cg = CodeSystemConcept(
        {
            "code": "CG",
            "definition": 'Description: Represents the HL7 content "domain" that supports clinical genomics - and includes " standards to enable the exchange of interrelated clinical and personalized genomic data between interested parties."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "clinical genomics",
        }
    )
    """
    clinical genomics

    Description: Represents the HL7 content "domain" that supports clinical genomics - and includes " standards to enable the exchange of interrelated clinical and personalized genomic data between interested parties."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    ci = CodeSystemConcept(
        {
            "code": "CI",
            "definition": 'Description: Represents the HL7 content "domain" that supports transmission infrastructure - and " is primarily concerned with the data content of exchanges between healthcare applications, the sequence or interrelationships in the flow of messages and the communication of significant application level exceptions or error conditions."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "transmission infrastructure",
        }
    )
    """
    transmission infrastructure

    Description: Represents the HL7 content "domain" that supports transmission infrastructure - and " is primarily concerned with the data content of exchanges between healthcare applications, the sequence or interrelationships in the flow of messages and the communication of significant application level exceptions or error conditions."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    co = CodeSystemConcept(
        {
            "code": "CO",
            "definition": 'Description: Represents the HL7 content "domain" that supports Coverage - and provides support for managing health care coverage in the reimbursement system(s).\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "coverage",
        }
    )
    """
    coverage

    Description: Represents the HL7 content "domain" that supports Coverage - and provides support for managing health care coverage in the reimbursement system(s).

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    cp = CodeSystemConcept(
        {
            "code": "CP",
            "definition": 'Description: Represents the HL7 content "domain" that supports the common product model - which "is used to improve the alignment between the different representations of products used within the body of HL7 Version 3 models."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "common product model",
        }
    )
    """
    common product model

    Description: Represents the HL7 content "domain" that supports the common product model - which "is used to improve the alignment between the different representations of products used within the body of HL7 Version 3 models."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    cr = CodeSystemConcept(
        {
            "code": "CR",
            "definition": 'Description: Represents the HL7 content "domain" that supports Claims and Reimbursement - and "provides support for Generic, Pharmacy, Preferred Accommodation, Physician, Oral Health Vision Care and Hospital claims for eligibility, authorization, coverage extension, pre-determination, invoice adjudication, payment advice and Statement of Financial Activity (SOFA) Release 3 of this document adds claims messaging support for Physician, Oral Health Vision Care and Hospital claims."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "claims and reimbursement",
        }
    )
    """
    claims and reimbursement

    Description: Represents the HL7 content "domain" that supports Claims and Reimbursement - and "provides support for Generic, Pharmacy, Preferred Accommodation, Physician, Oral Health Vision Care and Hospital claims for eligibility, authorization, coverage extension, pre-determination, invoice adjudication, payment advice and Statement of Financial Activity (SOFA) Release 3 of this document adds claims messaging support for Physician, Oral Health Vision Care and Hospital claims."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    cs = CodeSystemConcept(
        {
            "code": "CS",
            "definition": 'Description: Represents the HL7 content "domain" that supports a common clinical statement pattern - and "is a \'pattern\' designed to be used within multiple HL7 Version 3 domain models. This pattern is intended to facilitate the consistent design of communications that convey clinical information to meet specific use cases."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "clinical statement",
        }
    )
    """
    clinical statement

    Description: Represents the HL7 content "domain" that supports a common clinical statement pattern - and "is a 'pattern' designed to be used within multiple HL7 Version 3 domain models. This pattern is intended to facilitate the consistent design of communications that convey clinical information to meet specific use cases."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    ct = CodeSystemConcept(
        {
            "code": "CT",
            "definition": 'Description: Represents the HL7 content "domain" that supports common model types - and "are a work product produced by a particular committee for expressing a common, useful and reusable concept."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "common types",
        }
    )
    """
    common types

    Description: Represents the HL7 content "domain" that supports common model types - and "are a work product produced by a particular committee for expressing a common, useful and reusable concept."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    dd = CodeSystemConcept(
        {
            "code": "DD",
            "definition": 'Description: Represents the HL7 content "domain" that was created to support testing and initial set-up functions.',
            "display": "dummy domain",
        }
    )
    """
    dummy domain

    Description: Represents the HL7 content "domain" that was created to support testing and initial set-up functions.
    """

    di = CodeSystemConcept(
        {
            "code": "DI",
            "definition": 'Description: This domain has been retired in favor of "imaging integration" (II).',
            "display": "diagnostic imaging",
        }
    )
    """
    diagnostic imaging

    Description: This domain has been retired in favor of "imaging integration" (II).
    """

    ds = CodeSystemConcept(
        {
            "code": "DS",
            "definition": 'Description: Represents the HL7 content "domain" that provides decision support.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "decision support",
        }
    )
    """
    decision support

    Description: Represents the HL7 content "domain" that provides decision support.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    em = CodeSystemConcept(
        {
            "code": "EM",
            "definition": 'Description: Represents the HL7 content "domain" that supports Emergency Medical Services.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "emergency medical services",
        }
    )
    """
    emergency medical services

    Description: Represents the HL7 content "domain" that supports Emergency Medical Services.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    ii = CodeSystemConcept(
        {
            "code": "II",
            "definition": 'Description: Represents the HL7 content "domain" that supports imaging integration - and is "comprises the models, implementation guides, sample documents and images that are needed to illustrate the transformation of DICOM structured reports to CDA Release 2 as well as the creation of CDA diagnostic imaging reports."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "imaging integration",
        }
    )
    """
    imaging integration

    Description: Represents the HL7 content "domain" that supports imaging integration - and is "comprises the models, implementation guides, sample documents and images that are needed to illustrate the transformation of DICOM structured reports to CDA Release 2 as well as the creation of CDA diagnostic imaging reports."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    iz = CodeSystemConcept(
        {
            "code": "IZ",
            "definition": 'Description: Represents the HL7 content "domain" that supports immunization - and "describes communication of information about immunization: the administration of vaccines (and/or antisera) to individuals to prevent infectious disease."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "immunization",
        }
    )
    """
    immunization

    Description: Represents the HL7 content "domain" that supports immunization - and "describes communication of information about immunization: the administration of vaccines (and/or antisera) to individuals to prevent infectious disease."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    lb = CodeSystemConcept(
        {
            "code": "LB",
            "definition": 'Description: Represents the HL7 content "domain" that supports clinical laboratory functions - and is "comprises the models, messages, and other artifacts that are needed to support messaging related to laboratory tests or observations. "\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "laboratory",
        }
    )
    """
    laboratory

    Description: Represents the HL7 content "domain" that supports clinical laboratory functions - and is "comprises the models, messages, and other artifacts that are needed to support messaging related to laboratory tests or observations. "

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    me = CodeSystemConcept(
        {
            "code": "ME",
            "definition": 'Description: Represents the HL7 content "domain" that supports medication - and  "deals with the description of a medicine for the purposes of messaging information about medicines" and the applications of these descriptions.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "medication",
        }
    )
    """
    medication

    Description: Represents the HL7 content "domain" that supports medication - and  "deals with the description of a medicine for the purposes of messaging information about medicines" and the applications of these descriptions.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    mi = CodeSystemConcept(
        {
            "code": "MI",
            "definition": 'Description: Represents the HL7 content "domain" that supports master file infrastructure - and is "comprises the classes and attributes needed to support Master Files and Registries."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "masterfile infrastructure",
        }
    )
    """
    masterfile infrastructure

    Description: Represents the HL7 content "domain" that supports master file infrastructure - and is "comprises the classes and attributes needed to support Master Files and Registries."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    mm = CodeSystemConcept(
        {
            "code": "MM",
            "definition": 'Description: Represents the HL7 content "domain" that supports Materials Management - and is "supports the simple scenario of a Materials Management application sending requests, notifications and queries to an auxiliary application. The intent is to establish a standard for the minimum functionality that is useful and comprehensive enough to explore the important concepts relative to inventory management."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "materials management",
        }
    )
    """
    materials management

    Description: Represents the HL7 content "domain" that supports Materials Management - and is "supports the simple scenario of a Materials Management application sending requests, notifications and queries to an auxiliary application. The intent is to establish a standard for the minimum functionality that is useful and comprehensive enough to explore the important concepts relative to inventory management."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    mr = CodeSystemConcept(
        {
            "code": "MR",
            "definition": 'Description: Represents the HL7 content "domain" that supports medical records - and is "supports clinical document management, and document querying."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "medical records",
        }
    )
    """
    medical records

    Description: Represents the HL7 content "domain" that supports medical records - and is "supports clinical document management, and document querying."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    mt = CodeSystemConcept(
        {
            "code": "MT",
            "definition": 'Description: Represents the HL7 content "domain" that supports shared messages - and "are a work product produced for expressing common, useful and reusable message types."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "shared messages",
        }
    )
    """
    shared messages

    Description: Represents the HL7 content "domain" that supports shared messages - and "are a work product produced for expressing common, useful and reusable message types."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    ob = CodeSystemConcept(
        {
            "code": "OB",
            "definition": 'Description: Represents the HL7 content "domain" that supports observations - and is "comprises the models, messages, and other artifacts that are needed to support messaging related to resulting basic healthcare diagnostic services. "\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "observations",
        }
    )
    """
    observations

    Description: Represents the HL7 content "domain" that supports observations - and is "comprises the models, messages, and other artifacts that are needed to support messaging related to resulting basic healthcare diagnostic services. "

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    oo = CodeSystemConcept(
        {
            "code": "OO",
            "definition": 'Description: Represents the HL7 content "domain" that supports orders and observations - and will provide over-arching support information for the "Orders" (OR) and "Observations" (OB) domains.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "orders & observations",
        }
    )
    """
    orders & observations

    Description: Represents the HL7 content "domain" that supports orders and observations - and will provide over-arching support information for the "Orders" (OR) and "Observations" (OB) domains.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    or_ = CodeSystemConcept(
        {
            "code": "OR",
            "definition": 'Description: Represents the HL7 content "domain" that supports orders - and "comprises the models, messages, and other artifacts that are needed to support messaging related to ordering basic healthcare services."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "orders",
        }
    )
    """
    orders

    Description: Represents the HL7 content "domain" that supports orders - and "comprises the models, messages, and other artifacts that are needed to support messaging related to ordering basic healthcare services."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    pa = CodeSystemConcept(
        {
            "code": "PA",
            "definition": 'Description: Represents the HL7 content "domain" that supports Patient Administration - and "defines person and patient demographics and visit information about patients"\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "patient administration",
        }
    )
    """
    patient administration

    Description: Represents the HL7 content "domain" that supports Patient Administration - and "defines person and patient demographics and visit information about patients"

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    pc = CodeSystemConcept(
        {
            "code": "PC",
            "definition": 'Description: Represents the HL7 content "domain" that supports Care Provision - and "addresses the information that is needed for the ongoing care of individuals, populations, and other targets of care."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "care provision",
        }
    )
    """
    care provision

    Description: Represents the HL7 content "domain" that supports Care Provision - and "addresses the information that is needed for the ongoing care of individuals, populations, and other targets of care."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    ph = CodeSystemConcept(
        {
            "code": "PH",
            "definition": 'Description: Represents the HL7 content "domain" that supports public health - and is "the source of a number of Common Model Element Types (CMET) designed to meet the needs of public health data exchange."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "public health",
        }
    )
    """
    public health

    Description: Represents the HL7 content "domain" that supports public health - and is "the source of a number of Common Model Element Types (CMET) designed to meet the needs of public health data exchange."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    pm = CodeSystemConcept(
        {
            "code": "PM",
            "definition": 'Description: Represents the HL7 content "domain" that supports Personnel Management - and "spans a variety of clinical-administrative information functions associated with the organizations, individuals, animals and devices involved in the delivery and support of healthcare services."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "personnel management",
        }
    )
    """
    personnel management

    Description: Represents the HL7 content "domain" that supports Personnel Management - and "spans a variety of clinical-administrative information functions associated with the organizations, individuals, animals and devices involved in the delivery and support of healthcare services."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    qi = CodeSystemConcept(
        {
            "code": "QI",
            "definition": 'Description: Represents the HL7 content "domain" that supports query infrastructure - and "specifies the formation of information queries and the responses to these queries to meet the needs of healthcare applications using the HL7 version 3 messaging standard."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "query infrastructure",
        }
    )
    """
    query infrastructure

    Description: Represents the HL7 content "domain" that supports query infrastructure - and "specifies the formation of information queries and the responses to these queries to meet the needs of healthcare applications using the HL7 version 3 messaging standard."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    qm = CodeSystemConcept(
        {
            "code": "QM",
            "definition": 'Description: Represents the HL7 content "domain" that supports Quality Measures - and "is a standard for representing a health quality measure as an electronic document."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "quality measures",
        }
    )
    """
    quality measures

    Description: Represents the HL7 content "domain" that supports Quality Measures - and "is a standard for representing a health quality measure as an electronic document."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    rg = CodeSystemConcept(
        {
            "code": "RG",
            "definition": 'Description: Represents the HL7 content "domain" that supports Registries - and "collects HL7 artifacts for administrative  registries."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "registries",
        }
    )
    """
    registries

    Description: Represents the HL7 content "domain" that supports Registries - and "collects HL7 artifacts for administrative  registries."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    ri = CodeSystemConcept(
        {
            "code": "RI",
            "definition": 'Description: Represents the HL7 content "domain" that supports Informative Public Health.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "informative public health",
        }
    )
    """
    informative public health

    Description: Represents the HL7 content "domain" that supports Informative Public Health.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    rp = CodeSystemConcept(
        {
            "code": "RP",
            "definition": 'Description: Represents the HL7 content "domain" that supports Regulated Products - and "includes standards developed as part of the family of messages targeted for the exchange of information about regulated products and the exchange of the data needed to provide approval for such products."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "regulated products",
        }
    )
    """
    regulated products

    Description: Represents the HL7 content "domain" that supports Regulated Products - and "includes standards developed as part of the family of messages targeted for the exchange of information about regulated products and the exchange of the data needed to provide approval for such products."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    rr = CodeSystemConcept(
        {
            "code": "RR",
            "definition": 'Description: Represents the HL7 content "domain" that supports Public Health Reporting - and "includes messages and documents that are specifically designed to support managment, reporting and investigation in the public health context."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "public health reporting",
        }
    )
    """
    public health reporting

    Description: Represents the HL7 content "domain" that supports Public Health Reporting - and "includes messages and documents that are specifically designed to support managment, reporting and investigation in the public health context."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    rt = CodeSystemConcept(
        {
            "code": "RT",
            "definition": 'Description: Represents the HL7 content "domain" that supports Regulated Studies - and is "includes standards developed as part of the family of messages targeted for the exchange of information about the conduct of regulated studies, and the exchange of the data collected during those studies."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "regulated studies",
        }
    )
    """
    regulated studies

    Description: Represents the HL7 content "domain" that supports Regulated Studies - and is "includes standards developed as part of the family of messages targeted for the exchange of information about the conduct of regulated studies, and the exchange of the data collected during those studies."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    rx = CodeSystemConcept(
        {
            "code": "RX",
            "definition": 'Description: Represents the HL7 content "domain" that supports pharmacy - and is a "model used to derive message patterns to describe and communicate processes related to medication."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "pharmacy",
        }
    )
    """
    pharmacy

    Description: Represents the HL7 content "domain" that supports pharmacy - and is a "model used to derive message patterns to describe and communicate processes related to medication."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    sc = CodeSystemConcept(
        {
            "code": "SC",
            "definition": 'Description: Represents the HL7 content "domain" that supports Scheduling - and "offers a generic set of messages and behavior to implement any number of Scheduling scenarios."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "scheduling",
        }
    )
    """
    scheduling

    Description: Represents the HL7 content "domain" that supports Scheduling - and "offers a generic set of messages and behavior to implement any number of Scheduling scenarios."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    sp = CodeSystemConcept(
        {
            "code": "SP",
            "definition": 'Description: Represents the HL7 content "domain" that supports Specimen - and "comprises the models and artifacts that are needed to support the creation of messaging related to specimen."\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "specimen",
        }
    )
    """
    specimen

    Description: Represents the HL7 content "domain" that supports Specimen - and "comprises the models and artifacts that are needed to support the creation of messaging related to specimen."

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    td = CodeSystemConcept(
        {
            "code": "TD",
            "definition": 'Description: Represents the HL7 content "domain" that supports Therapeutic Devices - and is "comprises the models, messages, and other artifacts that are needed to support messaging related to therapy delivery and observations made by a medical device. "\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.',
            "display": "therapeutic devices",
        }
    )
    """
    therapeutic devices

    Description: Represents the HL7 content "domain" that supports Therapeutic Devices - and is "comprises the models, messages, and other artifacts that are needed to support messaging related to therapy delivery and observations made by a medical device. "

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.
    """

    class Meta:
        resource = _resource
