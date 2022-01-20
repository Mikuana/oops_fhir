from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ActUSPrivacyLaw"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ActUSPrivacyLaw:
    """
    v3 Code System ActUSPrivacyLaw

     A jurisdictional mandate in the US relating to privacy.   Deprecation
Comment:  Content moved to ActCode under _ActPrivacyLaw; use that
instead.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ActUSPrivacyLaw
    """

    underscore_act_usprivacy_law = CodeSystemConcept(
        {
            "code": "_ActUSPrivacyLaw",
            "concept": [
                {
                    "code": "42CFRPart2",
                    "definition": "42 CFR Part 2 stipulates the right of an individual who has applied for or been given diagnosis or treatment for alcohol or drug abuse at a federally assisted program.\r\n\n                        \n                           Definition: Non-disclosure of health information relating to health care paid for by a federally assisted substance abuse program without patient consent.\r\n\n                        \n                           Usage Note: May be associated with an Act or a Role to indicate the legal provision to which the assignment of an Act.confidentialityCode or Role.confidentialityCode complies.",
                    "display": "42 CFR Part2",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2016-03-12"},
                    ],
                },
                {
                    "code": "CommonRule",
                    "definition": "U.S. Federal regulations governing the protection of human subjects in research (codified at Subpart A of 45 CFR part 46) that has been adopted by 15 U.S. Federal departments and agencies in an effort to promote uniformity, understanding, and compliance with human subject protections. Existing regulations governing the protection of human subjects in Food and Drug Administration (FDA)-regulated research (21 CFR parts 50, 56, 312, and 812) are separate from the Common Rule but include similar requirements.\r\n\n                        \n                           Definition: U.S. federal laws governing research-related privacy policies.\r\n\n                        \n                           Usage Note: May be associated with an Act or a Role to indicate the legal provision to which the assignment of an Act.confidentialityCode or Role.confidentialtyCode complies.",
                    "display": "Common Rule",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2016-03-12"},
                    ],
                },
                {
                    "code": "HIPAANOPP",
                    "definition": "The U.S. Public Law 104-191 Health Insurance Portability and Accountability Act (HIPAA) Privacy Rule (45 CFR Part 164 Subpart E) permits access, use and disclosure of certain personal health information (PHI as defined under the law) for purposes of Treatment, Payment, and Operations, and requires that the provider ask that patients acknowledge the Provider's Notice of Privacy Practices as permitted conduct under the law.\r\n\n                        \n                           Definition: Notification of HIPAA Privacy Practices.\r\n\n                        \n                           Usage Note: May be associated with an Act or a Role to indicate the legal provision to which the assignment of an Act.confidentialityCode or Role.confidentialtyCode complies.",
                    "display": "HIPAA notice of privacy practices",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2016-03-12"},
                    ],
                },
                {
                    "code": "HIPAAPsyNotes",
                    "definition": "The U.S. Public Law 104-191 Health Insurance Portability and Accountability Act (HIPAA) Privacy Rule (45 CFR Part 164 Section 164.508) requires authorization for certain uses and disclosure of psychotherapy notes.\r\n\n                        \n                           Definition: Authorization that must be obtained for disclosure of psychotherapy notes.\r\n\n                        \n                           Usage Note: May be associated with an Act or a Role to indicate the legal provision to which the assignment of an Act.confidentialityCode or Role.confidentialityCode complies.",
                    "display": "HIPAA psychotherapy notes",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2016-03-12"},
                    ],
                },
                {
                    "code": "HIPAASelfPay",
                    "definition": "Section 13405(a) of the Health Information Technology for Economic and Clinical Health Act (HITECH) stipulates the right of an individual to have disclosures regarding certain health care items or services for which the individual pays out of pocket in full restricted from a health plan.\r\n\n                        \n                           Definition: Non-disclosure of health information to a health plan relating to health care items or services for which an individual pays out of pocket in full.\r\n\n                        \n                           Usage Note: May be associated with an Act or a Role to indicate the legal provision to which the assignment of an Act.confidentialityCode or Role.confidentialityCode complies.",
                    "display": "HIPAA self-pay",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2016-03-12"},
                    ],
                },
                {
                    "code": "Title38Section7332",
                    "definition": "Title 38 Part 1-protected information may only be disclosed to a third party with the special written consent of the patient except where expressly authorized by 38 USC 7332. VA may disclose this information for specific purposes to: VA employees on a need to know basis - more restrictive than Privacy Act need to know; contractors who need the information in order to perform or fulfill the duties of the contract; and researchers who provide assurances that the information will not be identified in any report.  This information may also be disclosed without consent where patient lacks decision-making capacity; in a medical emergency for the purpose of treating a condition which poses an immediate threat to the health of any individual and which requires immediate medical intervention; for eye, tissue, or organ donation purposes; and disclosure of HIV information for public health purposes.\r\n\n                        \n                           Definition: Title 38 Part 1 - Â§1.462 Confidentiality restrictions.\r\n\n                        \n(a) General. The patient records to which Â§Â§1.460 through 1.499 of this part apply may be disclosed or used only as permitted by these regulations and may not otherwise be disclosed or used in any civil, criminal, administrative, or legislative proceedings conducted by any Federal, State, or local authority. Any disclosure made under these regulations must be limited to that information which is necessary to carry out the purpose of the disclosure. SUBCHAPTER III--PROTECTION OF PATIENT RIGHTS Sec. 7332. Confidentiality of certain medical records (a)(1) Records of the identity, diagnosis, prognosis, or treatment of any patient or subject which are maintained in connection with the performance of any program or activity (including education, training, treatment, rehabilitation, or research) relating to drug abuse, alcoholism or alcohol abuse, infection with the human immunodeficiency virus, or sickle cell anemia which is carried out by or for the Department under this title shall, except as provided in subsections (e) and (f), be confidential, and (section 5701 of this title to the contrary notwithstanding) such records may be disclosed only for the purposes and under the circumstances expressly authorized under subsection (b).\r\n\n                        \n                           Usage Note: May be associated with an Act or a Role to indicate the legal provision to which the assignment of an Act.confidentialityCode or Role.confidentialityCode complies.",
                    "display": "Title 38 Section 7332",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2016-03-12"},
                    ],
                },
            ],
            "definition": "Definition: A jurisdictional mandate in the U.S. relating to privacy.\r\n\n                        \n                           Usage Note: ActPrivacyLaw codes may be associated with an Act or a Role to indicate the legal provision to which the assignment of an Act.confidentialityCode or Role.confidentialtyCode complies.  May be used to further specify rationale for assignment of other ActPrivacyPolicy codes in the US realm, e.g., ETH and 42CFRPart2 can be differentiated from ETH and Title38Part1.",
            "display": "ActUSPrivacyLaw",
            "property": [
                {"code": "status", "valueCode": "deprecated"},
                {"code": "deprecationDate", "valueDateTime": "2016-03-12"},
            ],
        }
    )
    """
    ActUSPrivacyLaw

    Definition: A jurisdictional mandate in the U.S. relating to privacy.

                        
                           Usage Note: ActPrivacyLaw codes may be associated with an Act or a Role to indicate the legal provision to which the assignment of an Act.confidentialityCode or Role.confidentialtyCode complies.  May be used to further specify rationale for assignment of other ActPrivacyPolicy codes in the US realm, e.g., ETH and 42CFRPart2 can be differentiated from ETH and Title38Part1.
    """

    class Meta:
        resource = _resource
