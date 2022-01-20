from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3hl7PublishingSection"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7PublishingSection:
    """
    v3 Code System hl7PublishingSection

      Description:  Codes for HL7 publishing sections (major business
categories)

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-hl7PublishingSection
    """

    am = CodeSystemConcept(
        {
            "code": "AM",
            "definition": 'Description: Represents the HL7 V3 publishing section that deals with the administration and management of health care activities and organizations.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.\r\n\n                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.',
            "display": "administrative management",
        }
    )
    """
    administrative management

    Description: Represents the HL7 V3 publishing section that deals with the administration and management of health care activities and organizations.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.

                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.
    """

    hm = CodeSystemConcept(
        {
            "code": "HM",
            "definition": 'Description: Represents the HL7 V3 publishing section that deals with the health care provision and clinical management.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.\r\n\n                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.',
            "display": "health and clinical management",
        }
    )
    """
    health and clinical management

    Description: Represents the HL7 V3 publishing section that deals with the health care provision and clinical management.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.

                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.
    """

    im = CodeSystemConcept(
        {
            "code": "IM",
            "definition": 'Description: Represents the HL7 V3 publishing section that deals with the definition and management of the computing and communication infrastructure necessary to support health care.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.\r\n\n                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.',
            "display": "infrastructure management",
        }
    )
    """
    infrastructure management

    Description: Represents the HL7 V3 publishing section that deals with the definition and management of the computing and communication infrastructure necessary to support health care.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.

                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.
    """

    uu = CodeSystemConcept(
        {
            "code": "UU",
            "definition": 'Description: Represents the HL7 V3 publishing section that holds specifications that are unassigned - that have not yet been assigned to one of the formal publishing sections.\r\n\n                        \n                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.\r\n\n                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.',
            "display": "unknown",
        }
    )
    """
    unknown

    Description: Represents the HL7 V3 publishing section that holds specifications that are unassigned - that have not yet been assigned to one of the formal publishing sections.

                        
                           UsageNote: V3 Specifications are published in a set of "domains", which contain interactions and related specifications for a single area of health care within which can be supported by a single, coherent set of interoperability specifications.

                        For publishing purposes, these domains are aggregated into sub-sections of related health care areas and these sub-sections are further aggregated into three major sets.
    """

    class Meta:
        resource = _resource
