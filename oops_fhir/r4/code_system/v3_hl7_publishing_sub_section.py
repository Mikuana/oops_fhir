from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3hl7PublishingSubSection"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7PublishingSubSection:
    """
    v3 Code System hl7PublishingSubSection

      Description:  Codes for HL7 publishing sub-sections (business sub-
categories)

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-hl7PublishingSubSection
    """

    co = CodeSystemConcept(
        {
            "code": "CO",
            "definition": 'Description: Represents the HL7 V3 publishing sub-section that holds common or shared specifications within the Infrastructure Management (IM) section.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.\r\n\n                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.',
            "display": "common",
        }
    )
    """
    common

    Description: Represents the HL7 V3 publishing sub-section that holds common or shared specifications within the Infrastructure Management (IM) section.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.

                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.
    """

    fi = CodeSystemConcept(
        {
            "code": "FI",
            "definition": 'Description: Represents the HL7 V3 publishing sub-section that holds specifications related to the management of financial information within the Administrative Management (AM) section.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.\r\n\n                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.',
            "display": "financial information",
        }
    )
    """
    financial information

    Description: Represents the HL7 V3 publishing sub-section that holds specifications related to the management of financial information within the Administrative Management (AM) section.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.

                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.
    """

    mc = CodeSystemConcept(
        {
            "code": "MC",
            "definition": 'Description: Represents the HL7 V3 publishing sub-section that holds specifications related to the definition and control of interoperability messages within the Infrastructure Management (IM) section.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.\r\n\n                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.',
            "display": "message control",
        }
    )
    """
    message control

    Description: Represents the HL7 V3 publishing sub-section that holds specifications related to the definition and control of interoperability messages within the Infrastructure Management (IM) section.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.

                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.
    """

    mf = CodeSystemConcept(
        {
            "code": "MF",
            "definition": 'Description: Represents the HL7 V3 publishing sub-section that holds specifications related to master file and registry management activities within the Infrastructure Management (IM) section.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.\r\n\n                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.',
            "display": "master file",
        }
    )
    """
    master file

    Description: Represents the HL7 V3 publishing sub-section that holds specifications related to master file and registry management activities within the Infrastructure Management (IM) section.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.

                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.
    """

    po = CodeSystemConcept(
        {
            "code": "PO",
            "definition": 'Description: Represents the HL7 V3 publishing sub-section that holds specifications related to managing clinical operations within the Health and Clinical Management (HM) section.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.\r\n\n                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.',
            "display": "operations",
        }
    )
    """
    operations

    Description: Represents the HL7 V3 publishing sub-section that holds specifications related to managing clinical operations within the Health and Clinical Management (HM) section.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.

                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.
    """

    pr = CodeSystemConcept(
        {
            "code": "PR",
            "definition": 'Description: Represents the HL7 V3 publishing sub-section that holds specifications related to the management of practice settings within the Administrative Management (AM) section.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.\r\n\n                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.',
            "display": "practice",
        }
    )
    """
    practice

    Description: Represents the HL7 V3 publishing sub-section that holds specifications related to the management of practice settings within the Administrative Management (AM) section.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.

                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.
    """

    qu = CodeSystemConcept(
        {
            "code": "QU",
            "definition": 'Description: Represents the HL7 V3 publishing sub-section that holds specifications related to query/response activities within the Infrastructure Management (IM) section.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.\r\n\n                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.',
            "display": "query",
        }
    )
    """
    query

    Description: Represents the HL7 V3 publishing sub-section that holds specifications related to query/response activities within the Infrastructure Management (IM) section.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.

                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.
    """

    rc = CodeSystemConcept(
        {
            "code": "RC",
            "definition": 'Description: Represents the HL7 V3 publishing sub-section that holds specifications related to the definition and communication of records of clinical care within the Health and Clinical Management (HM) section.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.\r\n\n                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.',
            "display": "records",
        }
    )
    """
    records

    Description: Represents the HL7 V3 publishing sub-section that holds specifications related to the definition and communication of records of clinical care within the Health and Clinical Management (HM) section.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.

                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.
    """

    re = CodeSystemConcept(
        {
            "code": "RE",
            "definition": 'Description: Represents the HL7 V3 publishing sub-section that holds specifications related to the definition and communication of reasoning (knowledge) within the Health and Clinical Management (HM) section.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.\r\n\n                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.',
            "display": "reasoning",
        }
    )
    """
    reasoning

    Description: Represents the HL7 V3 publishing sub-section that holds specifications related to the definition and communication of reasoning (knowledge) within the Health and Clinical Management (HM) section.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.

                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.
    """

    uu = CodeSystemConcept(
        {
            "code": "UU",
            "definition": 'Description: Represents the HL7 V3 publishing sub-section that holds specifications that are unassigned - that have not yet been assigned to one of the formal publishing sections.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.\r\n\n                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.',
            "display": "unknown",
        }
    )
    """
    unknown

    Description: Represents the HL7 V3 publishing sub-section that holds specifications that are unassigned - that have not yet been assigned to one of the formal publishing sections.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.

                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.
    """

    class Meta:
        resource = _resource
