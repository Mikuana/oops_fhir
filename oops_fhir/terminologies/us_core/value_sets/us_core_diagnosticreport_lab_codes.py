"""The Document Type value set includes all LOINC  values whose CLASSTYPE
is LABORATORY in the LOINC database"""

_resource_type_ = "ValueSet"
_id_ = "us-core-diagnosticreport-lab-codes"
_url_ = "http://hl7.org/fhir/us/core/ValueSet/us-core-diagnosticreport-lab-codes"
_identifier_ = None
_version_ = "4.0.0"
_name_ = "USCoreDiagnosticReportLabCodes"
_title_ = "US Core Diagnostic Report Laboratory Codes"
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
