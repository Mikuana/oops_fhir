"""Codes for assigning sex at birth as specified by the [Office of the
National Coordinator for Health IT
(ONC)](https://www.healthit.gov/newsroom/about-onc)"""

_resource_type_ = "ValueSet"
_id_ = "birthsex"
_url_ = "http://hl7.org/fhir/us/core/ValueSet/birthsex"
_identifier_ = [
    {"system": "urn:ietf:rfc:3986", "value": "urn:oid:2.16.840.1.113762.1.4.1021.24"}
]
_version_ = "4.0.0"
_name_ = "BirthSex"
_title_ = "Birth Sex"
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
_copyright_ = "Used by permission of HL7 International, all rights reserved Creative Commons License"

female = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/birthsex",
    "valueCoding": {
        "system": "http://terminology.hl7.org/CodeSystem/v3-AdministrativeGender",
        "code": "F",
        "display": "Female",
    },
}
""" Female """

male = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/birthsex",
    "valueCoding": {
        "system": "http://terminology.hl7.org/CodeSystem/v3-AdministrativeGender",
        "code": "M",
        "display": "Male",
    },
}
""" Male """

unknown = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/birthsex",
    "valueCoding": {
        "system": "http://terminology.hl7.org/CodeSystem/v3-NullFlavor",
        "code": "UNK",
        "display": "Unknown",
    },
}
""" Unknown """
