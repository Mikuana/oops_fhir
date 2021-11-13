"""This value set includes codes from
[BCP-47](http://tools.ietf.org/html/bcp47). This value set matches the
ONC 2015 Edition LanguageCommunication data element value set within
C-CDA to use a 2 character language code if one exists,   and a 3
character code if a 2 character code does not exist. It points back to
[RFC 5646](https://tools.ietf.org/html/rfc5646), however only the
language codes are required, all other elements are optional."""

_resource_type_ = "ValueSet"
_id_ = "simple-language"
_url_ = "http://hl7.org/fhir/us/core/ValueSet/simple-language"
_identifier_ = None
_version_ = "4.0.0"
_name_ = "LanguageCodesWithLanguageAndOptionallyARegionModifier"
_title_ = "Language codes with language and optionally a region modifier"
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
_copyright_ = """ISO Maintains the copyright on the country codes and controls it's use carefully. For
further details, see the [ISO 3166 Home Page](http://www.iso.org/iso/country_codes.htm)"""
