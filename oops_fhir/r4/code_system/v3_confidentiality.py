from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3Confidentiality"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3Confidentiality:
    """
    v3 Code System Confidentiality

     A set of codes specifying the security classification of acts and roles
in accordance with the definition for concept domain "Confidentiality".

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-Confidentiality
    """

    underscore_confidentiality = CodeSystemConcept(
        {
            "code": "_Confidentiality",
            "concept": [
                {
                    "code": "L",
                    "definition": "Definition: Privacy metadata indicating that the information has been de-identified, and there are mitigating circumstances that prevent re-identification, which minimize risk of harm from unauthorized disclosure.  The information requires protection to maintain low sensitivity.\r\n\n                        \n                           Examples: Includes anonymized, pseudonymized, or non-personally identifiable information such as HIPAA limited data sets.\r\n\n                        \n                           Map: No clear map to ISO 13606-4 Sensitivity Level (1) Care Management:   RECORD_COMPONENTs that might need to be accessed by a wide range of administrative staff to manage the subject of care's access to health services.\r\n\n                        \n                           Usage Note: This metadata indicates the receiver may have an obligation to comply with a data use agreement.",
                    "display": "low",
                },
                {
                    "code": "M",
                    "definition": "Definition: Privacy metadata indicating moderately sensitive information, which presents moderate risk of harm if disclosed without authorization.\r\n\n                        \n                           Examples: Includes allergies of non-sensitive nature used inform food service; health information a patient authorizes to be used for marketing, released to a bank for a health credit card or savings account; or information in personal health record systems that are not governed under health privacy laws.\r\n\n                        \n                           Map: Partial Map to ISO 13606-4 Sensitivity Level (2) Clinical Management:  Less sensitive RECORD_COMPONENTs that might need to be accessed by a wider range of personnel not all of whom are actively caring for the patient (e.g. radiology staff).\r\n\n                        \n                           Usage Note: This metadata indicates that the receiver may be obligated to comply with the receiver's terms of use or privacy policies.",
                    "display": "moderate",
                },
                {
                    "code": "N",
                    "definition": "Definition: Privacy metadata indicating that the information is typical, non-stigmatizing health information, which presents typical risk of harm if disclosed without authorization.\r\n\n                        \n                           Examples: In the US, this includes what HIPAA identifies as the minimum necessary protected health information (PHI) given a covered purpose of use (treatment, payment, or operations).  Includes typical, non-stigmatizing health information disclosed in an application for health, workers compensation, disability, or life insurance.\r\n\n                        \n                           Map: Partial Map to ISO 13606-4 Sensitivity Level (3) Clinical Care:   Default for normal clinical care access (i.e. most clinical staff directly caring for the patient should be able to access nearly all of the EHR).   Maps to normal confidentiality for treatment information but not to ancillary care, payment and operations.\r\n\n                        \n                           Usage Note: This metadata indicates that the receiver may be obligated to comply with applicable jurisdictional privacy law or disclosure authorization.",
                    "display": "normal",
                },
                {
                    "code": "R",
                    "definition": "Privacy metadata indicating highly sensitive, potentially stigmatizing information, which presents a high risk to the information subject if disclosed without authorization. May be pre-empted by jurisdictional law, e.g., for public health reporting or emergency treatment.\r\n\n                        \n                           Examples: Includes information that is additionally protected such as sensitive conditions mental health, HIV, substance abuse, domestic violence, child abuse, genetic disease, and reproductive health; or sensitive demographic information such as a patient's standing as an employee or a celebrity. May be used to indicate proprietary or classified information that is not related to an individual, e.g., secret ingredients in a therapeutic substance; or the name of a manufacturer.\r\n\n                        \n                           Map: Partial Map to ISO 13606-4 Sensitivity Level (3) Clinical Care: Default for normal clinical care access (i.e. most clinical staff directly caring for the patient should be able to access nearly all of the EHR). Maps to normal confidentiality for treatment information but not to ancillary care, payment and operations..\r\n\n                        \n                           Usage Note: This metadata indicates that the receiver may be obligated to comply with applicable, prevailing (default) jurisdictional privacy law or disclosure authorization..",
                    "display": "restricted",
                },
                {
                    "code": "U",
                    "definition": 'Definition: Privacy metadata indicating that the information is not classified as sensitive.\r\n\n                        \n                           Examples: Includes publicly available information, e.g., business name, phone, email or physical address.\r\n\n                        \n                           Usage Note: This metadata indicates that the receiver has no obligation to consider additional policies when making access control decisions.   Note that in some jurisdictions, personally identifiable information must be protected as confidential, so it would not be appropriate to assign a confidentiality code of "unrestricted"  to that information even if it is publicly available.',
                    "display": "unrestricted",
                },
                {
                    "code": "V",
                    "definition": ". Privacy metadata indicating that the information is extremely sensitive and likely stigmatizing health information that presents a very high risk if disclosed without authorization.  This information must be kept in the highest confidence.  \r\n\n                        \n                           Examples:  Includes information about a victim of abuse, patient requested information sensitivity, and taboo subjects relating to health status that must be discussed with the patient by an attending provider before sharing with the patient.  May also include information held under ???????legal lock?????? or attorney-client privilege\r\n\n                        \n                           Map:  This metadata indicates that the receiver may not disclose this information except as directed by the information custodian, who may be the information subject.\r\n\n                        \n                           Usage Note:  This metadata indicates that the receiver may not disclose this information except as directed by the information custodian, who may be the information subject.",
                    "display": "very restricted",
                },
            ],
            "definition": 'A specializable code and its leaf codes used in Confidentiality value sets to value the Act.Confidentiality and Role.Confidentiality attribute in accordance with the definition for concept domain "Confidentiality".',
            "display": "Confidentiality",
        }
    )
    """
    Confidentiality

    A specializable code and its leaf codes used in Confidentiality value sets to value the Act.Confidentiality and Role.Confidentiality attribute in accordance with the definition for concept domain "Confidentiality".
    """

    underscore_confidentiality_by_access_kind = CodeSystemConcept(
        {
            "code": "_ConfidentialityByAccessKind",
            "concept": [
                {
                    "code": "B",
                    "definition": "Description: Since the service class can represent knowledge factory that may be considered a trade or business secret, there is sometimes (though rarely) the need to flag those items as of business level confidentiality.  However, no patient related information may ever be of this confidentiality level.\r\n\n                        \n                           Deprecation Comment: Replced by ActCode.B",
                    "display": "business",
                    "property": [
                        {"code": "status", "valueCode": "retired"},
                        {"code": "deprecationDate", "valueDateTime": "2011-12-14"},
                    ],
                },
                {
                    "code": "D",
                    "definition": "Description: Only clinicians may see this item, billing and administration persons can not access this item without special permission.\r\n\n                        \n                           Deprecation Comment:Deprecated due to updated confidentiality codes under ActCode",
                    "display": "clinician",
                    "property": [
                        {"code": "status", "valueCode": "retired"},
                        {"code": "deprecationDate", "valueDateTime": "2011-12-14"},
                    ],
                },
                {
                    "code": "I",
                    "definition": "Description: Access only to individual persons who are mentioned explicitly as actors of this service and whose actor type warrants that access (cf. to actor type code).\r\n\n                        \n                           Deprecation Comment:Deprecated due to updated confidentiality codes under ActCode",
                    "display": "individual",
                    "property": [
                        {"code": "status", "valueCode": "retired"},
                        {"code": "deprecationDate", "valueDateTime": "2011-12-14"},
                    ],
                },
            ],
            "definition": "Description: By accessing subject / role and relationship based  rights  (These concepts are mutually exclusive, one and only one is required for a valid confidentiality coding.)\r\n\n                        \n                           Deprecation Comment:Deprecated due to updated confidentiality codes under ActCode",
            "display": "ConfidentialityByAccessKind",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "status", "valueCode": "retired"},
                {"code": "deprecationDate", "valueDateTime": "2011-12-14"},
            ],
        }
    )
    """
    ConfidentialityByAccessKind

    Description: By accessing subject / role and relationship based  rights  (These concepts are mutually exclusive, one and only one is required for a valid confidentiality coding.)


                           Deprecation Comment:Deprecated due to updated confidentiality codes under ActCode
    """

    underscore_confidentiality_by_info_type = CodeSystemConcept(
        {
            "code": "_ConfidentialityByInfoType",
            "concept": [
                {
                    "code": "ETH",
                    "definition": "Description: Alcohol/drug-abuse related item\r\n\n                        \n                           Deprecation Comment:Replced by ActCode.ETH",
                    "display": "substance abuse related",
                    "property": [
                        {"code": "status", "valueCode": "retired"},
                        {"code": "deprecationDate", "valueDateTime": "2011-12-14"},
                    ],
                },
                {
                    "code": "HIV",
                    "definition": "Description: HIV and AIDS related item\r\n\n                        \n                           Deprecation Comment:Replced by ActCode.HIV",
                    "display": "HIV related",
                    "property": [
                        {"code": "status", "valueCode": "retired"},
                        {"code": "deprecationDate", "valueDateTime": "2011-12-14"},
                    ],
                },
                {
                    "code": "PSY",
                    "definition": "Description: Psychiatry related item\r\n\n                        \n                           Deprecation Comment:Replced by ActCode.PSY",
                    "display": "psychiatry relate",
                    "property": [
                        {"code": "status", "valueCode": "retired"},
                        {"code": "deprecationDate", "valueDateTime": "2011-12-14"},
                    ],
                },
                {
                    "code": "SDV",
                    "definition": "Description: Sexual assault / domestic violence related item\r\n\n                        \n                           Deprecation Comment:Replced by ActCode.SDV",
                    "display": "sexual and domestic violence related",
                    "property": [
                        {"code": "status", "valueCode": "retired"},
                        {"code": "deprecationDate", "valueDateTime": "2011-12-14"},
                    ],
                },
            ],
            "definition": "Description: By information type, only for service catalog entries (multiples allowed). Not to be used with actual patient data!\r\n\n                        \n                           Deprecation Comment:Deprecated due to updated confidentiality codes under ActCode",
            "display": "ConfidentialityByInfoType",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "status", "valueCode": "retired"},
                {"code": "deprecationDate", "valueDateTime": "2011-12-14"},
            ],
        }
    )
    """
    ConfidentialityByInfoType

    Description: By information type, only for service catalog entries (multiples allowed). Not to be used with actual patient data!


                           Deprecation Comment:Deprecated due to updated confidentiality codes under ActCode
    """

    underscore_confidentiality_modifiers = CodeSystemConcept(
        {
            "code": "_ConfidentialityModifiers",
            "concept": [
                {
                    "code": "C",
                    "definition": "Description: Celebrities are people of public interest (VIP) including employees, whose information require special protection.\r\n\n                        \n                           Deprecation Comment:Replced by ActCode.CEL",
                    "display": "celebrity",
                    "property": [
                        {"code": "status", "valueCode": "retired"},
                        {"code": "deprecationDate", "valueDateTime": "2011-12-14"},
                    ],
                },
                {
                    "code": "S",
                    "definition": "Description: \n                        \r\nInformation for which the patient seeks heightened confidentiality. Sensitive information is not to be shared with family members.  Information reported by the patient about family members is sensitive by default. Flag can be set or cleared on patient's request.\n                           Deprecation Comment:Deprecated due to updated confidentiality codes under ActCode",
                    "display": "sensitive",
                    "property": [
                        {"code": "status", "valueCode": "retired"},
                        {"code": "deprecationDate", "valueDateTime": "2011-12-14"},
                    ],
                },
                {
                    "code": "T",
                    "definition": "Description: Information not to be disclosed or discussed with patient except through physician assigned to patient in this case.  This is usually a temporary constraint only, example use is a new fatal diagnosis or finding, such as malignancy or HIV.\r\n\n                        \n                           Deprecation Note:Replced by ActCode.TBOO",
                    "display": "taboo",
                    "property": [
                        {"code": "status", "valueCode": "retired"},
                        {"code": "deprecationDate", "valueDateTime": "2011-12-14"},
                    ],
                },
            ],
            "definition": "Description: Modifiers of role based access rights  (multiple allowed)\r\n\n                        \n                           Deprecation Comment:Deprecated due to updated confidentiality codes under ActCode",
            "display": "ConfidentialityModifiers",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "status", "valueCode": "retired"},
                {"code": "deprecationDate", "valueDateTime": "2011-12-14"},
            ],
        }
    )
    """
    ConfidentialityModifiers

    Description: Modifiers of role based access rights  (multiple allowed)


                           Deprecation Comment:Deprecated due to updated confidentiality codes under ActCode
    """

    class Meta:
        resource = _resource
