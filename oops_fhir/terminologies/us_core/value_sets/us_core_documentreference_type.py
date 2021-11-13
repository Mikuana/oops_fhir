"""The US Core DocumentReference Type Value Set includes all LOINC  values
whose SCALE is DOC in the LOINC database and the HL7 v3 Code System
NullFlavor concept 'unknown'"""

_resource_type_ = "ValueSet"
_id_ = "us-core-documentreference-type"
_url_ = "http://hl7.org/fhir/us/core/ValueSet/us-core-documentreference-type"
_identifier_ = None
_version_ = "4.0.0"
_name_ = "USCoreDocumentReferenceType"
_title_ = "US Core DocumentReference Type"
_status_ = "active"
_date_ = "2019-05-21"
_publisher_ = "HL7 International - US Realm Steering Committee"
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
_copyright_ = """This material contains content from LOINC (http://loinc.org). LOINC is copyright ©
1995-2020, Regenstrief Institute, Inc. and the Logical Observation Identifiers Names and
Codes (LOINC) Committee and is available at no cost under the license at
http://loinc.org/license. LOINC® is a registered United States trademark of Regenstrief
Institute, Inc"""

unknown = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/us-core-documentreference-type",
    "valueCoding": {
        "system": "http://terminology.hl7.org/CodeSystem/v3-NullFlavor",
        "code": "UNK",
        "display": "unknown",
    },
}
""" unknown """
