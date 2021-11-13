"""The codes for the concepts 'Unknown' and  'Asked but no answer' and the
the codes for the five race categories - 'American Indian' or 'Alaska
Native', 'Asian', 'Black or African American', 'Native Hawaiian or Other
Pacific Islander', and 'White' - as defined by the [OMB Standards for
Maintaining, Collecting, and Presenting Federal Data on Race and
Ethnicity, Statistical Policy Directive No. 15, as revised, October 30, 
1997](https://www.govinfo.gov/content/pkg/FR-1997-10-30/pdf/97-28653.pdf
) ."""

_resource_type_ = "ValueSet"
_id_ = "omb-race-category"
_url_ = "http://hl7.org/fhir/us/core/ValueSet/omb-race-category"
_identifier_ = [
    {"system": "urn:ietf:rfc:3986", "value": "urn:oid:2.16.840.1.113883.4.642.2.575"}
]
_version_ = "4.0.0"
_name_ = "OmbRaceCategories"
_title_ = "OMB Race Categories"
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

american_indian_or_alaska_native = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/omb-race-category",
    "valueCoding": {
        "system": "urn:oid:2.16.840.1.113883.6.238",
        "code": "1002-5",
        "display": "American Indian or Alaska Native",
    },
}
""" American Indian or Alaska Native """

asian = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/omb-race-category",
    "valueCoding": {
        "system": "urn:oid:2.16.840.1.113883.6.238",
        "code": "2028-9",
        "display": "Asian",
    },
}
""" Asian """

black_or_african_american = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/omb-race-category",
    "valueCoding": {
        "system": "urn:oid:2.16.840.1.113883.6.238",
        "code": "2054-5",
        "display": "Black or African American",
    },
}
""" Black or African American """

native_hawaiian_or_other_pacific_islander = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/omb-race-category",
    "valueCoding": {
        "system": "urn:oid:2.16.840.1.113883.6.238",
        "code": "2076-8",
        "display": "Native Hawaiian or Other Pacific Islander",
    },
}
""" Native Hawaiian or Other Pacific Islander """

white = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/omb-race-category",
    "valueCoding": {
        "system": "urn:oid:2.16.840.1.113883.6.238",
        "code": "2106-3",
        "display": "White",
    },
}
""" White """

unknown = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/omb-race-category",
    "valueCoding": {
        "system": "http://terminology.hl7.org/CodeSystem/v3-NullFlavor",
        "code": "UNK",
        "display": "Unknown",
    },
}
""" Unknown """

asked_but_no_answer = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/omb-race-category",
    "valueCoding": {
        "system": "http://terminology.hl7.org/CodeSystem/v3-NullFlavor",
        "code": "ASKU",
        "display": "Asked but no answer",
    },
}
""" Asked but no answer """
