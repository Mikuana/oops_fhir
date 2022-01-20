from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["EndpointConnectionType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class EndpointConnectionType:
    """
    Endpoint Connection Type

    This is an example value set defined by the FHIR project, that could be
used to represent possible connection type profile values.

    Status: draft - Version: 4.0.1

    Copyright Some content from IHE® Copyright © 2015 IHE International, Inc.    This content is from the IHE Technical Frameworks and Supplements,    available for free download and use at http://www.ihe.net/Technical_Frameworks/

    http://terminology.hl7.org/CodeSystem/endpoint-connection-type
    """

    ihe_xcpd = CodeSystemConcept(
        {
            "code": "ihe-xcpd",
            "definition": "IHE Cross Community Patient Discovery Profile (XCPD) - http://wiki.ihe.net/index.php/Cross-Community_Patient_Discovery",
            "display": "IHE XCPD",
        }
    )
    """
    IHE XCPD

    IHE Cross Community Patient Discovery Profile (XCPD) - http://wiki.ihe.net/index.php/Cross-Community_Patient_Discovery
    """

    ihe_xca = CodeSystemConcept(
        {
            "code": "ihe-xca",
            "definition": "IHE Cross Community Access Profile (XCA) - http://wiki.ihe.net/index.php/Cross-Community_Access",
            "display": "IHE XCA",
        }
    )
    """
    IHE XCA

    IHE Cross Community Access Profile (XCA) - http://wiki.ihe.net/index.php/Cross-Community_Access
    """

    ihe_xdr = CodeSystemConcept(
        {
            "code": "ihe-xdr",
            "definition": "IHE Cross-Enterprise Document Reliable Exchange (XDR) - http://wiki.ihe.net/index.php/Cross-enterprise_Document_Reliable_Interchange",
            "display": "IHE XDR",
        }
    )
    """
    IHE XDR

    IHE Cross-Enterprise Document Reliable Exchange (XDR) - http://wiki.ihe.net/index.php/Cross-enterprise_Document_Reliable_Interchange
    """

    ihe_xds = CodeSystemConcept(
        {
            "code": "ihe-xds",
            "definition": "IHE Cross-Enterprise Document Sharing (XDS) - http://wiki.ihe.net/index.php/Cross-Enterprise_Document_Sharing",
            "display": "IHE XDS",
        }
    )
    """
    IHE XDS

    IHE Cross-Enterprise Document Sharing (XDS) - http://wiki.ihe.net/index.php/Cross-Enterprise_Document_Sharing
    """

    ihe_iid = CodeSystemConcept(
        {
            "code": "ihe-iid",
            "definition": "IHE Invoke Image Display (IID) - http://wiki.ihe.net/index.php/Invoke_Image_Display",
            "display": "IHE IID",
        }
    )
    """
    IHE IID

    IHE Invoke Image Display (IID) - http://wiki.ihe.net/index.php/Invoke_Image_Display
    """

    dicom_wado_rs = CodeSystemConcept(
        {
            "code": "dicom-wado-rs",
            "definition": "DICOMweb RESTful Image Retrieve - http://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_6.5.html",
            "display": "DICOM WADO-RS",
        }
    )
    """
    DICOM WADO-RS

    DICOMweb RESTful Image Retrieve - http://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_6.5.html
    """

    dicom_qido_rs = CodeSystemConcept(
        {
            "code": "dicom-qido-rs",
            "definition": "DICOMweb RESTful Image query - http://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_6.7.html",
            "display": "DICOM QIDO-RS",
        }
    )
    """
    DICOM QIDO-RS

    DICOMweb RESTful Image query - http://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_6.7.html
    """

    dicom_stow_rs = CodeSystemConcept(
        {
            "code": "dicom-stow-rs",
            "definition": "DICOMweb RESTful image sending and storage - http://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_6.6.html",
            "display": "DICOM STOW-RS",
        }
    )
    """
    DICOM STOW-RS

    DICOMweb RESTful image sending and storage - http://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_6.6.html
    """

    dicom_wado_uri = CodeSystemConcept(
        {
            "code": "dicom-wado-uri",
            "definition": "DICOMweb Image Retrieve - http://dicom.nema.org/dicom/2013/output/chtml/part18/sect_6.3.html",
            "display": "DICOM WADO-URI",
        }
    )
    """
    DICOM WADO-URI

    DICOMweb Image Retrieve - http://dicom.nema.org/dicom/2013/output/chtml/part18/sect_6.3.html
    """

    hl7_fhir_rest = CodeSystemConcept(
        {
            "code": "hl7-fhir-rest",
            "definition": "Interact with the server interface using FHIR's RESTful interface. For details on its version/capabilities you should connect the value in Endpoint.address and retrieve the FHIR CapabilityStatement.",
            "display": "HL7 FHIR",
        }
    )
    """
    HL7 FHIR

    Interact with the server interface using FHIR's RESTful interface. For details on its version/capabilities you should connect the value in Endpoint.address and retrieve the FHIR CapabilityStatement.
    """

    hl7_fhir_msg = CodeSystemConcept(
        {
            "code": "hl7-fhir-msg",
            "definition": "Use the servers FHIR Messaging interface. Details can be found on the messaging.html page in the FHIR Specification. The FHIR server's base address is specified in the Endpoint.address property.",
            "display": "HL7 FHIR Messaging",
        }
    )
    """
    HL7 FHIR Messaging

    Use the servers FHIR Messaging interface. Details can be found on the messaging.html page in the FHIR Specification. The FHIR server's base address is specified in the Endpoint.address property.
    """

    hl7v2_mllp = CodeSystemConcept(
        {
            "code": "hl7v2-mllp",
            "definition": "HL7v2 messages over an LLP TCP connection",
            "display": "HL7 v2 MLLP",
        }
    )
    """
    HL7 v2 MLLP

    HL7v2 messages over an LLP TCP connection
    """

    secure_email = CodeSystemConcept(
        {
            "code": "secure-email",
            "definition": "Email delivery using a digital certificate to encrypt the content using the public key, receiver must have the private key to decrypt the content",
            "display": "Secure email",
        }
    )
    """
    Secure email

    Email delivery using a digital certificate to encrypt the content using the public key, receiver must have the private key to decrypt the content
    """

    direct_project = CodeSystemConcept(
        {
            "code": "direct-project",
            "definition": "Direct Project information - http://wiki.directproject.org/",
            "display": "Direct Project",
        }
    )
    """
    Direct Project

    Direct Project information - http://wiki.directproject.org/
    """

    class Meta:
        resource = _resource
