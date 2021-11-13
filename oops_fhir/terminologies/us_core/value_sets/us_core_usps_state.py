"""This value set defines two letter USPS alphabetic codes."""

_resource_type_ = """ValueSet"""
_id_ = """us-core-usps-state"""
_url_ = """http://hl7.org/fhir/us/core/ValueSet/us-core-usps-state"""
_identifier_ = [
    {"system": "urn:ietf:rfc:3986", "value": "urn:oid:2.16.840.1.113883.4.642.3.40"}
]
_version_ = """4.0.0"""
_name_ = """UspsTwoLetterAlphabeticCodes"""
_title_ = """USPS Two Letter Alphabetic Codes"""
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
_copyright_ = """On July 1, 1963, the Post Office Department implemented the five-digit ZIP Code, which was placed after the state name in the last line of an address. To provide room for the ZIP Code, the Department issued two-letter abbreviations for all states and territories. Publication 59, Abbreviations for Use with ZIP Code, issued by the Department in October 1963. There is no copyright restriction on this value set."""
