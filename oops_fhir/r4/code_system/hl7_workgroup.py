from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["HL7Workgroup"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class HL7Workgroup:
    """
    HL7Workgroup

    An HL7 administrative unit that owns artifacts in the FHIR
specification.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/hl7-work-group
    """

    cbcc = CodeSystemConcept(
        {
            "code": "cbcc",
            "definition": "Community Based Collaborative Care (http://www.hl7.org/Special/committees/cbcc/index.cfm).",
            "display": "Community Based Collaborative Care",
        }
    )
    """
    Community Based Collaborative Care

    Community Based Collaborative Care (http://www.hl7.org/Special/committees/cbcc/index.cfm).
    """

    cds = CodeSystemConcept(
        {
            "code": "cds",
            "definition": "Clinical Decision Support (http://www.hl7.org/Special/committees/dss/index.cfm).",
            "display": "Clinical Decision Support",
        }
    )
    """
    Clinical Decision Support

    Clinical Decision Support (http://www.hl7.org/Special/committees/dss/index.cfm).
    """

    cqi = CodeSystemConcept(
        {
            "code": "cqi",
            "definition": "Clinical Quality Information (http://www.hl7.org/Special/committees/cqi/index.cfm).",
            "display": "Clinical Quality Information",
        }
    )
    """
    Clinical Quality Information

    Clinical Quality Information (http://www.hl7.org/Special/committees/cqi/index.cfm).
    """

    cg = CodeSystemConcept(
        {
            "code": "cg",
            "definition": "Clinical Genomics (http://www.hl7.org/Special/committees/clingenomics/index.cfm).",
            "display": "Clinical Genomics",
        }
    )
    """
    Clinical Genomics

    Clinical Genomics (http://www.hl7.org/Special/committees/clingenomics/index.cfm).
    """

    dev = CodeSystemConcept(
        {
            "code": "dev",
            "definition": "Health Care Devices (http://www.hl7.org/Special/committees/healthcaredevices/index.cfm).",
            "display": "Health Care Devices",
        }
    )
    """
    Health Care Devices

    Health Care Devices (http://www.hl7.org/Special/committees/healthcaredevices/index.cfm).
    """

    ehr = CodeSystemConcept(
        {
            "code": "ehr",
            "definition": "Electronic Health Records (http://www.hl7.org/special/committees/ehr/index.cfm).",
            "display": "Electronic Health Records",
        }
    )
    """
    Electronic Health Records

    Electronic Health Records (http://www.hl7.org/special/committees/ehr/index.cfm).
    """

    fhir = CodeSystemConcept(
        {
            "code": "fhir",
            "definition": "FHIR Infrastructure (http://www.hl7.org/Special/committees/fiwg/index.cfm).",
            "display": "FHIR Infrastructure",
        }
    )
    """
    FHIR Infrastructure

    FHIR Infrastructure (http://www.hl7.org/Special/committees/fiwg/index.cfm).
    """

    fm = CodeSystemConcept(
        {
            "code": "fm",
            "definition": "Financial Management (http://www.hl7.org/Special/committees/fm/index.cfm).",
            "display": "Financial Management",
        }
    )
    """
    Financial Management

    Financial Management (http://www.hl7.org/Special/committees/fm/index.cfm).
    """

    hsi = CodeSystemConcept(
        {
            "code": "hsi",
            "definition": "Health Standards Integration (http://www.hl7.org/Special/committees/hsi/index.cfm).",
            "display": "Health Standards Integration",
        }
    )
    """
    Health Standards Integration

    Health Standards Integration (http://www.hl7.org/Special/committees/hsi/index.cfm).
    """

    ii = CodeSystemConcept(
        {
            "code": "ii",
            "definition": "Imaging Integration (http://www.hl7.org/Special/committees/imagemgt/index.cfm).",
            "display": "Imaging Integration",
        }
    )
    """
    Imaging Integration

    Imaging Integration (http://www.hl7.org/Special/committees/imagemgt/index.cfm).
    """

    inm = CodeSystemConcept(
        {
            "code": "inm",
            "definition": "Infrastructure And Messaging (http://www.hl7.org/special/committees/inm/index.cfm).",
            "display": "Infrastructure And Messaging",
        }
    )
    """
    Infrastructure And Messaging

    Infrastructure And Messaging (http://www.hl7.org/special/committees/inm/index.cfm).
    """

    its = CodeSystemConcept(
        {
            "code": "its",
            "definition": "Implementable Technology Specifications (http://www.hl7.org/special/committees/xml/index.cfm).",
            "display": "Implementable Technology Specifications",
        }
    )
    """
    Implementable Technology Specifications

    Implementable Technology Specifications (http://www.hl7.org/special/committees/xml/index.cfm).
    """

    mnm = CodeSystemConcept(
        {
            "code": "mnm",
            "definition": "Modeling and Methodology (http://www.hl7.org/Special/committees/mnm/index.cfm).",
            "display": "Modeling and Methodology",
        }
    )
    """
    Modeling and Methodology

    Modeling and Methodology (http://www.hl7.org/Special/committees/mnm/index.cfm).
    """

    oo = CodeSystemConcept(
        {
            "code": "oo",
            "definition": "Orders and Observations (http://www.hl7.org/Special/committees/orders/index.cfm).",
            "display": "Orders and Observations",
        }
    )
    """
    Orders and Observations

    Orders and Observations (http://www.hl7.org/Special/committees/orders/index.cfm).
    """

    pa = CodeSystemConcept(
        {
            "code": "pa",
            "definition": "Patient Administration (http://www.hl7.org/Special/committees/pafm/index.cfm).",
            "display": "Patient Administration",
        }
    )
    """
    Patient Administration

    Patient Administration (http://www.hl7.org/Special/committees/pafm/index.cfm).
    """

    pc = CodeSystemConcept(
        {
            "code": "pc",
            "definition": "Patient Care (http://www.hl7.org/Special/committees/patientcare/index.cfm).",
            "display": "Patient Care",
        }
    )
    """
    Patient Care

    Patient Care (http://www.hl7.org/Special/committees/patientcare/index.cfm).
    """

    pher = CodeSystemConcept(
        {
            "code": "pher",
            "definition": "Public Health and Emergency Response (http://www.hl7.org/Special/committees/pher/index.cfm).",
            "display": "Public Health and Emergency Response",
        }
    )
    """
    Public Health and Emergency Response

    Public Health and Emergency Response (http://www.hl7.org/Special/committees/pher/index.cfm).
    """

    phx = CodeSystemConcept(
        {
            "code": "phx",
            "definition": "Pharmacy (http://www.hl7.org/Special/committees/medication/index.cfm).",
            "display": "Pharmacy",
        }
    )
    """
    Pharmacy

    Pharmacy (http://www.hl7.org/Special/committees/medication/index.cfm).
    """

    brr = CodeSystemConcept(
        {
            "code": "brr",
            "definition": "Biomedical Research and Regulation (http://www.hl7.org/Special/committees/rcrim/index.cfm).",
            "display": "Biomedical Research and Regulation",
        }
    )
    """
    Biomedical Research and Regulation

    Biomedical Research and Regulation (http://www.hl7.org/Special/committees/rcrim/index.cfm).
    """

    sd = CodeSystemConcept(
        {
            "code": "sd",
            "definition": "Structured Documents (http://www.hl7.org/Special/committees/structure/index.cfm).",
            "display": "Structured Documents",
        }
    )
    """
    Structured Documents

    Structured Documents (http://www.hl7.org/Special/committees/structure/index.cfm).
    """

    sec = CodeSystemConcept(
        {
            "code": "sec",
            "definition": "Security (http://www.hl7.org/Special/committees/secure/index.cfm).",
            "display": "Security",
        }
    )
    """
    Security

    Security (http://www.hl7.org/Special/committees/secure/index.cfm).
    """

    us = CodeSystemConcept(
        {
            "code": "us",
            "definition": "US Realm Taskforce (http://www.hl7.org/Special/committees/usrealm/index.cfm).",
            "display": "US Realm Taskforce",
        }
    )
    """
    US Realm Taskforce

    US Realm Taskforce (http://www.hl7.org/Special/committees/usrealm/index.cfm).
    """

    vocab = CodeSystemConcept(
        {
            "code": "vocab",
            "definition": "Vocabulary (http://www.hl7.org/Special/committees/Vocab/index.cfm).",
            "display": "Vocabulary",
        }
    )
    """
    Vocabulary

    Vocabulary (http://www.hl7.org/Special/committees/Vocab/index.cfm).
    """

    aid = CodeSystemConcept(
        {
            "code": "aid",
            "definition": "Application Implementation and Design (http://www.hl7.org/Special/committees/java/index.cfm).",
            "display": "Application Implementation and Design",
        }
    )
    """
    Application Implementation and Design

    Application Implementation and Design (http://www.hl7.org/Special/committees/java/index.cfm).
    """

    class Meta:
        resource = _resource
