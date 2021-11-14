"""The type of encounter: a specific code indicating type of service
provided. This value set includes codes from SNOMED CT decending from
the concept 308335008 (Patient encounter procedure (procedure)) and
codes from the Current Procedure and Terminology (CPT) found in the
following CPT sections:   - 99201-99499 E/M  - 99500-99600 home health
(mainly nonphysician, such as newborn care in home)  - 99605-99607
medication management  - 98966-98968 non physician telephone services
(subscription to AMA Required)"""


__all__ = []

_resource_type_ = "ValueSet"
_id_ = "us-core-encounter-type"
_url_ = "http://hl7.org/fhir/us/core/ValueSet/us-core-encounter-type"
_version_ = "4.0.0"
_name_ = "USCoreEncounterType"
_title_ = "US Core Encounter Type"
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
_copyright_ = """This value set includes content from:  1. SNOMED CT, which is copyright © 2002+
International Health Terminology Standards Development Organisation (IHTSDO), and
distributed by agreement between IHTSDO and HL7. Implementer use of SNOMED CT is not
covered by this agreement.   2. CPT © Copyright 2020 American Medical Association. All
rights reserved. AMA and CPT are registered trademarks of the American Medical
Association."""