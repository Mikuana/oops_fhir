"""The codes for the ethnicity categories - 'Hispanic or Latino' and 'Non
Hispanic or Latino' - as defined by the [OMB Standards for Maintaining,
Collecting, and Presenting Federal Data on Race and Ethnicity,
Statistical Policy Directive No. 15, as revised, October 30, 1997](https
://www.govinfo.gov/content/pkg/FR-1997-10-30/pdf/97-28653.pdf)."""


__all__ = ["hispanic_or_latino", "non_hispanic_or_latino"]

_resource_type_ = "ValueSet"
_id_ = "omb-ethnicity-category"
_url_ = "http://hl7.org/fhir/us/core/ValueSet/omb-ethnicity-category"
_version_ = "4.0.0"
_name_ = "OmbEthnicityCategories"
_title_ = "OMB Ethnicity Categories"
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

hispanic_or_latino = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/omb-ethnicity-category",
    "valueString": "Hispanic or Latino",
}
""" Hispanic or Latino """

non_hispanic_or_latino = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/omb-ethnicity-category",
    "valueString": "Non Hispanic or Latino",
}
""" Non Hispanic or Latino """
