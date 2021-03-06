from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SignatureTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SignatureTypeCodes:
    """
    Signature Type Codes

    The Digital Signature Purposes, an indication of the reason an entity
signs a document. This is included in the signed information and can be
used when determining accountability for various actions concerning the
document. Examples include: author, transcriptionist/recorder, and
witness.

    Status: draft - Version: 4.0.1

    Copyright These codes are excerpted from ASTM Standard, E1762-95(2013) - Standard Guide for Electronic Authentication of Health Care Information, Copyright by ASTM International, 100 Barr Harbor Drive, West Conshohocken, PA 19428. Copies of this standard are available through the ASTM Web Site at www.astm.org.

    urn:iso-astm:E1762-95:2013
    """

    one_2_840_10065_1_12_1_1 = CodeSystemConcept(
        {
            "code": "1.2.840.10065.1.12.1.1",
            "definition": "the signature of the primary or sole author of a health information document. There can be only one primary author of a health information document.",
            "display": "Author's Signature",
        }
    )
    """
    Author's Signature

    the signature of the primary or sole author of a health information document. There can be only one primary author of a health information document.
    """

    one_2_840_10065_1_12_1_2 = CodeSystemConcept(
        {
            "code": "1.2.840.10065.1.12.1.2",
            "definition": "the signature of a health information document coauthor. There can be multiple coauthors of a health information document.",
            "display": "Coauthor's Signature",
        }
    )
    """
    Coauthor's Signature

    the signature of a health information document coauthor. There can be multiple coauthors of a health information document.
    """

    one_2_840_10065_1_12_1_3 = CodeSystemConcept(
        {
            "code": "1.2.840.10065.1.12.1.3",
            "definition": "the signature of an individual who is a participant in the health information document but is not an author or coauthor. (Example a surgeon who is required by institutional, regulatory, or legal rules to sign an operative report, but who was not involved in the authorship of that report.)",
            "display": "Co-participant's Signature",
        }
    )
    """
    Co-participant's Signature

    the signature of an individual who is a participant in the health information document but is not an author or coauthor. (Example a surgeon who is required by institutional, regulatory, or legal rules to sign an operative report, but who was not involved in the authorship of that report.)
    """

    one_2_840_10065_1_12_1_4 = CodeSystemConcept(
        {
            "code": "1.2.840.10065.1.12.1.4",
            "definition": "the signature of an individual who has transcribed a dictated document or recorded written text into a digital machine readable format.",
            "display": "Transcriptionist/Recorder Signature",
        }
    )
    """
    Transcriptionist/Recorder Signature

    the signature of an individual who has transcribed a dictated document or recorded written text into a digital machine readable format.
    """

    one_2_840_10065_1_12_1_5 = CodeSystemConcept(
        {
            "code": "1.2.840.10065.1.12.1.5",
            "definition": "a signature verifying the information contained in a document. (Example a physician is required to countersign a verbal order that has previously been recorded in the medical record by a registered nurse who has carried out the verbal order.)",
            "display": "Verification Signature",
        }
    )
    """
    Verification Signature

    a signature verifying the information contained in a document. (Example a physician is required to countersign a verbal order that has previously been recorded in the medical record by a registered nurse who has carried out the verbal order.)
    """

    one_2_840_10065_1_12_1_6 = CodeSystemConcept(
        {
            "code": "1.2.840.10065.1.12.1.6",
            "definition": "a signature validating a health information document for inclusion in the patient record. (Example a medical student or resident is credentialed to perform history or physical examinations and to write progress notes. The attending physician signs the history and physical examination to validate the entry for inclusion in the patient's medical record.)",
            "display": "Validation Signature",
        }
    )
    """
    Validation Signature

    a signature validating a health information document for inclusion in the patient record. (Example a medical student or resident is credentialed to perform history or physical examinations and to write progress notes. The attending physician signs the history and physical examination to validate the entry for inclusion in the patient's medical record.)
    """

    one_2_840_10065_1_12_1_7 = CodeSystemConcept(
        {
            "code": "1.2.840.10065.1.12.1.7",
            "definition": "the signature of an individual consenting to what is described in a health information document.",
            "display": "Consent Signature",
        }
    )
    """
    Consent Signature

    the signature of an individual consenting to what is described in a health information document.
    """

    one_2_840_10065_1_12_1_8 = CodeSystemConcept(
        {
            "code": "1.2.840.10065.1.12.1.8",
            "definition": "the signature of a witness to any other signature.",
            "display": "Signature Witness Signature",
        }
    )
    """
    Signature Witness Signature

    the signature of a witness to any other signature.
    """

    one_2_840_10065_1_12_1_9 = CodeSystemConcept(
        {
            "code": "1.2.840.10065.1.12.1.9",
            "definition": "the signature of a witness to an event. (Example the witness has observed a procedure and is attesting to this fact.)",
            "display": "Event Witness Signature",
        }
    )
    """
    Event Witness Signature

    the signature of a witness to an event. (Example the witness has observed a procedure and is attesting to this fact.)
    """

    one_2_840_10065_1_12_1_10 = CodeSystemConcept(
        {
            "code": "1.2.840.10065.1.12.1.10",
            "definition": "the signature of an individual who has witnessed another individual who is known to them signing a document. (Example the identity witness is a notary public.)",
            "display": "Identity Witness Signature",
        }
    )
    """
    Identity Witness Signature

    the signature of an individual who has witnessed another individual who is known to them signing a document. (Example the identity witness is a notary public.)
    """

    one_2_840_10065_1_12_1_11 = CodeSystemConcept(
        {
            "code": "1.2.840.10065.1.12.1.11",
            "definition": "the signature of an individual who has witnessed the health care provider counselling a patient.",
            "display": "Consent Witness Signature",
        }
    )
    """
    Consent Witness Signature

    the signature of an individual who has witnessed the health care provider counselling a patient.
    """

    one_2_840_10065_1_12_1_12 = CodeSystemConcept(
        {
            "code": "1.2.840.10065.1.12.1.12",
            "definition": "the signature of an individual who has translated health care information during an event or the obtaining of consent to a treatment.",
            "display": "Interpreter Signature",
        }
    )
    """
    Interpreter Signature

    the signature of an individual who has translated health care information during an event or the obtaining of consent to a treatment.
    """

    one_2_840_10065_1_12_1_13 = CodeSystemConcept(
        {
            "code": "1.2.840.10065.1.12.1.13",
            "definition": "the signature of a person, device, or algorithm that has reviewed or filtered data for inclusion into the patient record. ( Examples: (1) a medical records clerk who scans a document for inclusion in the medical record, enters header information, or catalogues and classifies the data, or a combination thereof; (2) a gateway that receives data from another computer system and interprets that data or changes its format, or both, before entering it into the patient record.)",
            "display": "Review Signature",
        }
    )
    """
    Review Signature

    the signature of a person, device, or algorithm that has reviewed or filtered data for inclusion into the patient record. ( Examples: (1) a medical records clerk who scans a document for inclusion in the medical record, enters header information, or catalogues and classifies the data, or a combination thereof; (2) a gateway that receives data from another computer system and interprets that data or changes its format, or both, before entering it into the patient record.)
    """

    one_2_840_10065_1_12_1_14 = CodeSystemConcept(
        {
            "code": "1.2.840.10065.1.12.1.14",
            "definition": "the signature of an automated data source. (Examples: (1) the signature for an image that is generated by a device for inclusion in the patient record; (2) the signature for an ECG derived by an ECG system for inclusion in the patient record; (3) the data from a biomedical monitoring device or system that is for inclusion in the patient record.)",
            "display": "Source Signature",
        }
    )
    """
    Source Signature

    the signature of an automated data source. (Examples: (1) the signature for an image that is generated by a device for inclusion in the patient record; (2) the signature for an ECG derived by an ECG system for inclusion in the patient record; (3) the data from a biomedical monitoring device or system that is for inclusion in the patient record.)
    """

    one_2_840_10065_1_12_1_15 = CodeSystemConcept(
        {
            "code": "1.2.840.10065.1.12.1.15",
            "definition": "the signature on a new amended document of an individual who has corrected, edited, or amended an original health information document. An addendum signature can either be a signature type or a signature sub-type (see 8.1). Any document with an addendum signature shall have a companion document that is the original document with its original, unaltered content, and original signatures. The original document shall be referenced via an attribute in the new document, which contains, for example, the digest of the old document. Whether the original, unaltered, document is always displayed with the addended document is a local matter, but the original, unaltered, document must remain as part of the patient record and be retrievable on demand.",
            "display": "Addendum Signature",
        }
    )
    """
    Addendum Signature

    the signature on a new amended document of an individual who has corrected, edited, or amended an original health information document. An addendum signature can either be a signature type or a signature sub-type (see 8.1). Any document with an addendum signature shall have a companion document that is the original document with its original, unaltered content, and original signatures. The original document shall be referenced via an attribute in the new document, which contains, for example, the digest of the old document. Whether the original, unaltered, document is always displayed with the addended document is a local matter, but the original, unaltered, document must remain as part of the patient record and be retrievable on demand.
    """

    one_2_840_10065_1_12_1_16 = CodeSystemConcept(
        {
            "code": "1.2.840.10065.1.12.1.16",
            "definition": "the signature on an original document of an individual who has generated a new amended document. This (original) document shall reference the new document via an additional signature purpose. This is the inverse of an addendum signature and provides a pointer from the original to the amended document.",
            "display": "Modification Signature",
        }
    )
    """
    Modification Signature

    the signature on an original document of an individual who has generated a new amended document. This (original) document shall reference the new document via an additional signature purpose. This is the inverse of an addendum signature and provides a pointer from the original to the amended document.
    """

    one_2_840_10065_1_12_1_17 = CodeSystemConcept(
        {
            "code": "1.2.840.10065.1.12.1.17",
            "definition": "the signature of an individual who is certifying that the document is invalidated by an error(s), or is placed in the wrong chart. An administrative (error/edit) signature must include an addendum to the document and therefore shall have an addendum signature sub-type (see 8.1). This signature is reserved for the highest health information system administrative classification, since it is a statement that the entire document is invalidated by the error and that the document should no longer be used for patient care, although for legal reasons the document must remain part of the permanent patient record.",
            "display": "Administrative (Error/Edit) Signature",
        }
    )
    """
    Administrative (Error/Edit) Signature

    the signature of an individual who is certifying that the document is invalidated by an error(s), or is placed in the wrong chart. An administrative (error/edit) signature must include an addendum to the document and therefore shall have an addendum signature sub-type (see 8.1). This signature is reserved for the highest health information system administrative classification, since it is a statement that the entire document is invalidated by the error and that the document should no longer be used for patient care, although for legal reasons the document must remain part of the permanent patient record.
    """

    one_2_840_10065_1_12_1_18 = CodeSystemConcept(
        {
            "code": "1.2.840.10065.1.12.1.18",
            "definition": "the signature by an entity or device trusted to provide accurate timestamps. This timestamp might be provided, for example, in the signature time attribute.",
            "display": "Timestamp Signature",
        }
    )
    """
    Timestamp Signature

    the signature by an entity or device trusted to provide accurate timestamps. This timestamp might be provided, for example, in the signature time attribute.
    """

    class Meta:
        resource = _resource
