""" Codes providing the status of an observation for smoking status. Constrained to `final`and `entered-in-error`. """

_resource_type_ = """ValueSet"""
_id_ = """us-core-observation-smoking-status-status"""
_url_ = (
    """http://hl7.org/fhir/us/core/ValueSet/us-core-observation-smoking-status-status"""
)
_identifier_ = None
_version_ = """4.0.0"""
_name_ = """USCoreObservationSmokingStatusStatus"""
_title_ = """US Core Status for Smoking Status Observation"""
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
_copyright_ = """Used by permission of HL7 International, all rights reserved Creative Commons License"""

final = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/us-core-observation-smoking-status-status",
    "valueCode": "final",
}
""" final """

entered_in_error = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/us-core-observation-smoking-status-status",
    "valueCode": "entered-in-error",
}
""" entered-in-error """
