"""The US Core Condition Category Codes support the separate concepts of
problems and health concerns in Condition.category in order for API
consumers to be able to separate health concerns and problems. However
this is not mandatory for 2015 certification"""


__all__ = ["health_concern", "death_diagnosis"]

_resource_type_ = "ValueSet"
_id_ = "us-core-condition-category"
_url_ = "http://hl7.org/fhir/us/core/ValueSet/us-core-condition-category"
_version_ = "4.0.0"
_name_ = "USCoreConditionCategoryCodes"
_title_ = "US Core Condition Category Codes"
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
_copyright_ = """This value set includes content from SNOMED CT, which is copyright © 2002+ International
Health Terminology Standards Development Organisation (IHTSDO), and distributed by
agreement between IHTSDO and HL7. Implementer use of SNOMED CT is not covered by this
agreement"""

health_concern = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/us-core-condition-category",
    "valueCoding": {
        "system": "http://hl7.org/fhir/us/core/CodeSystem/condition-category",
        "code": "health-concern",
        "display": "Health Concern",
    },
}
""" Health Concern """

death_diagnosis = {
    "url": "http://hl7.org/fhir/us/core/ValueSet/us-core-condition-category",
    "valueCoding": {
        "system": "http://snomed.info/sct",
        "code": "16100001",
        "display": "Death diagnosis",
    },
}
""" Death diagnosis """
