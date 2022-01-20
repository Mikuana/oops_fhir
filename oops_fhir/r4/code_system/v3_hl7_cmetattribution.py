from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3hl7CMETAttribution"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7CMETAttribution:
    """
    v3 Code System hl7CMETAttribution

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-hl7CMETAttribution
    """

    contact = CodeSystemConcept(
        {
            "code": "contact",
            "definition": "Description: Provides sufficient information to allow the object identified to be contacted. This is likely to have the content of identified and confirmable plus telephone number.",
            "display": "contact",
        }
    )
    """
    contact

    Description: Provides sufficient information to allow the object identified to be contacted. This is likely to have the content of identified and confirmable plus telephone number.
    """

    identified = CodeSystemConcept(
        {
            "code": "identified",
            "definition": "Description: This variant is a proper subset of universal and is intended to provide sufficient information to identify the object(s) modeled by the CMET. This variant is only suitable for use within TIGHTLY COUPLED SYSTEMS ONLY. This variant provides ONLY the ID (and code where applicable) and Name. Other variants may not be substituted at runtime.",
            "display": "identified",
        }
    )
    """
    identified

    Description: This variant is a proper subset of universal and is intended to provide sufficient information to identify the object(s) modeled by the CMET. This variant is only suitable for use within TIGHTLY COUPLED SYSTEMS ONLY. This variant provides ONLY the ID (and code where applicable) and Name. Other variants may not be substituted at runtime.
    """

    identified_confirmable = CodeSystemConcept(
        {
            "code": "identified-confirmable",
            "definition": "Description: This extends the identified variant by adding just sufficient additional information to allow the identity of object modeled to be confirmed by a number of corroborating items of data; for instance a patient's date of birth and current address. However, specific contact information, such as telephone number, are not viewed as confirming information.",
            "display": "identified-confirmable",
        }
    )
    """
    identified-confirmable

    Description: This extends the identified variant by adding just sufficient additional information to allow the identity of object modeled to be confirmed by a number of corroborating items of data; for instance a patient's date of birth and current address. However, specific contact information, such as telephone number, are not viewed as confirming information.
    """

    identified_informational = CodeSystemConcept(
        {
            "code": "identified-informational",
            "definition": 'Description: Generally the same information content as "contactable" but using new "informational" CMETs as dependant CMETs. This flavor allows expression of the CMET when non-focal class information is not known.',
            "display": "identified-informational",
        }
    )
    """
    identified-informational

    Description: Generally the same information content as "contactable" but using new "informational" CMETs as dependant CMETs. This flavor allows expression of the CMET when non-focal class information is not known.
    """

    informational = CodeSystemConcept(
        {
            "code": "informational",
            "definition": 'Description: Generally the same information content as "contactable", but with required (not mandatory) ids on entry point class. This flavor allows expression of the CMET even when mandatory information is not known.',
            "display": "informational",
        }
    )
    """
    informational

    Description: Generally the same information content as "contactable", but with required (not mandatory) ids on entry point class. This flavor allows expression of the CMET even when mandatory information is not known.
    """

    minimal = CodeSystemConcept(
        {
            "code": "minimal",
            "definition": "Description: Provides more than identified, but not as much as universal. There are not expected to be many of these.",
            "display": "minimal",
        }
    )
    """
    minimal

    Description: Provides more than identified, but not as much as universal. There are not expected to be many of these.
    """

    universal = CodeSystemConcept(
        {
            "code": "universal",
            "definition": "Description: This variant includes all attributes and associations present in the R-MIM. Any of non-mandatory and non-required attributes and/or associations may be present or absent, as permitted in the cardinality constraints.",
            "display": "universal",
        }
    )
    """
    universal

    Description: This variant includes all attributes and associations present in the R-MIM. Any of non-mandatory and non-required attributes and/or associations may be present or absent, as permitted in the cardinality constraints.
    """

    class Meta:
        resource = _resource
