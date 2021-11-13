"""This describes the problem. Diagnosis/Problem List is broadly defined as
a series of brief statements that catalog a patient's medical, nursing,
dental, social, preventative and psychiatric events and issues that are
relevant to that patient's healthcare (e.g., signs, symptoms, and
defined conditions).   ICD-10 is appropriate for Diagnosis information,
and ICD-9 for historical information."""

_resource_type_ = """ValueSet"""
_id_ = """us-core-condition-code"""
_url_ = """http://hl7.org/fhir/us/core/ValueSet/us-core-condition-code"""
_identifier_ = None
_version_ = """4.0.0"""
_name_ = """USCoreConditionCode"""
_title_ = """US Core Condition Code"""
_status_ = """active"""
_date_ = """2019-05-21"""
_publisher_ = """HL7 International - US Realm Steering Committee"""
_contact_ = [
    {
        "name": "HL7 International - US Realm Steering Committee",
        "telecom": [
            {
                "system": "url",
                "value": "http://www.hl7.org/Special/committees/usrealm/index.cfm",
            }
        ],
    }
]
_jurisdiction_ = [{"coding": [{"system": "urn:iso:std:iso:3166", "code": "US"}]}]
_copyright_ = """This value set includes content from:
  1. SNOMED CT, which is copyright © 2002+ International Health Terminology Standards Development Organisation (IHTSDO), and distributed by agreement between IHTSDO and HL7. Implementer use of SNOMED CT is not covered by this agreement.
  2. ICD-9 and ICD-10 are copyrighted by the World Health Organization (WHO) which owns and publishes the classification. See https://www.who.int/classifications/icd/en. WHO has authorized the development of an adaptation of ICD-9 and ICD-10 to ICD-9-CM to ICD-10-CM for use in the United States for U.S. government purposes.
"""

x160245001 = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/us-core-condition-code",
    "valueCoding": {"system": "http://snomed.info/sct", "code": "160245001"},
}
""" 160245001 """
