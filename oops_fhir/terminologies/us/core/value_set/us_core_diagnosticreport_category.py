"""The US Core Diagnostic Report Category Value Set is a 'starter set' of
categories supported for fetching and Diagnostic Reports and notes."""


__all__ = ["radiology", "cardiology", "pathology"]

_resource_type_ = "ValueSet"
_id_ = "us-core-diagnosticreport-category"
_url_ = "http://hl7.org/fhir/us/core/ValueSet/us-core-diagnosticreport-category"
_version_ = "4.0.0"
_name_ = "USCoreDiagnosticReportCategory"
_title_ = "US Core DiagnosticReport Category"
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

radiology = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/us-core-diagnosticreport-category",
    "valueString": "Radiology",
}
""" Radiology """

cardiology = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/us-core-diagnosticreport-category",
    "valueString": "Cardiology",
}
""" Cardiology """

pathology = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/us-core-diagnosticreport-category",
    "valueString": "Pathology",
}
""" Pathology """